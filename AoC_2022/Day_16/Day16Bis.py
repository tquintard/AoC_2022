

import re
from collections import deque
from contextlib import suppress
from dataclasses import dataclass
from functools import cached_property
from itertools import permutations
from typing import Final, Iterator, NamedTuple, Self


LINE: Final[re.Pattern[str]] = re.compile(
    r"^Valve (?P<name>[A-Z]{2}) has flow rate=(?P<rate>\d+); "
    r"(?:tunnels lead to valves|tunnel leads to valve) (?P<valves>[A-Z, ]*)$"
)


class Valve(NamedTuple):
    name: str
    rate: int
    valves: frozenset[str]

    @classmethod
    def from_line(cls, line: str) -> Self:
        match = LINE.match(line)
        # assert match is not None
        rate = int(match["rate"])
        valves = frozenset(v.strip() for v in match["valves"].split(","))
        return cls(match["name"], rate, valves)


@dataclass
class TunnelStep:
    valve: Valve
    time_left: int = 30
    total_released: int = 0
    visited: frozenset[Valve] = frozenset()

    def traverse(self, graph: "Graph") -> Iterator[Self]:
        for valve, steps in graph.distances[self.valve].items():
            if valve in self.visited or not valve.rate:
                # either we already opened the valve here, or it is not worth
                # stopping here as the effect would be 0.
                continue
            if (time_left := self.time_left - steps - 1) <= 0:
                # no point in going here, the result would be 0.
                continue
            yield __class__(
                valve,
                time_left,
                self.total_released + valve.rate * time_left,
                self.visited | {valve},
            )


class Graph:
    def __init__(self, nodes: dict[str, Valve]):
        self.nodes = nodes

    @classmethod
    def from_text(cls, text: str) -> Self:
        return cls({(v := Valve.from_line(line)).name: v for line in text.splitlines()})

    @cached_property
    def distances(self) -> dict[Valve, dict[Valve, int]]:
        """Minimal distances to move from one valve to another
        
        Uses the Floyd-Warshall algorithm to find the minimum distances from
        any node in the graph to any other node.
        """
        graph = self.nodes
        dist: dict[Valve, dict[Valve, int]] = {v: {graph[n]: 1 for n in v.valves} for v in graph.values()}
        max = len(graph)
        for k, i, j in permutations(graph.values(), r=3):
            with suppress(KeyError):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i].get(j, max))
        return dist

    def max_pressure_reliefs(self, remaining: int = 30) -> dict[frozenset[Valve], int]:
        max_relief: dict[frozenset[Valve], int] = {}
        queue = deque([TunnelStep(self.nodes["AA"], remaining)])
        while queue:
            node = queue.popleft()
            for new in node.traverse(self):
                max_relief[new.visited] = max(max_relief.get(new.visited, 0), new.total_released)
                queue.append(new)
        return max_relief

    def optimise_pressure_relief(self) -> int:
        return max(self.max_pressure_reliefs().values())


example = Graph.from_text(
    """\
Valve OQ has flow rate=17; tunnels lead to valves NB, AK, KL
Valve HP has flow rate=0; tunnels lead to valves ZX, KQ
Valve GO has flow rate=0; tunnels lead to valves HR, GW
Valve PD has flow rate=9; tunnels lead to valves XN, EV, QE, MW
Valve NQ has flow rate=0; tunnels lead to valves HX, ZX
Valve DW has flow rate=0; tunnels lead to valves IR, WE
Valve TN has flow rate=24; tunnels lead to valves KL, EI
Valve JJ has flow rate=0; tunnels lead to valves EV, HR
Valve KH has flow rate=0; tunnels lead to valves ZQ, AA
Valve PH has flow rate=0; tunnels lead to valves FN, QE
Valve FD has flow rate=0; tunnels lead to valves SM, HX
Valve SM has flow rate=7; tunnels lead to valves WW, RZ, FD, HO, KQ
Valve PU has flow rate=0; tunnels lead to valves VL, IR
Valve OM has flow rate=0; tunnels lead to valves CM, AA
Valve KX has flow rate=20; tunnel leads to valve PC
Valve IR has flow rate=3; tunnels lead to valves PU, CM, WW, DW, AF
Valve XG has flow rate=0; tunnels lead to valves RX, OF
Valve QE has flow rate=0; tunnels lead to valves PH, PD
Valve GW has flow rate=0; tunnels lead to valves JQ, GO
Valve HO has flow rate=0; tunnels lead to valves SM, TY
Valve WU has flow rate=0; tunnels lead to valves SG, RZ
Valve MS has flow rate=0; tunnels lead to valves UE, OF
Valve JS has flow rate=0; tunnels lead to valves DO, ZX
Valve YQ has flow rate=0; tunnels lead to valves BC, SG
Valve EJ has flow rate=0; tunnels lead to valves AA, LR
Valve EI has flow rate=0; tunnels lead to valves BV, TN
Valve NC has flow rate=0; tunnels lead to valves TS, BC
Valve AF has flow rate=0; tunnels lead to valves IR, HX
Valve OX has flow rate=0; tunnels lead to valves HR, BV
Valve BF has flow rate=0; tunnels lead to valves JQ, SY
Valve CA has flow rate=0; tunnels lead to valves YD, HX
Valve KQ has flow rate=0; tunnels lead to valves HP, SM
Valve NB has flow rate=0; tunnels lead to valves OQ, OF
Valve SY has flow rate=0; tunnels lead to valves BF, BV
Valve AA has flow rate=0; tunnels lead to valves KH, EJ, OM, TY, DO
Valve BC has flow rate=11; tunnels lead to valves WE, RX, YQ, LR, NC
Valve HR has flow rate=14; tunnels lead to valves OX, GO, JJ
Valve WE has flow rate=0; tunnels lead to valves DW, BC
Valve MW has flow rate=0; tunnels lead to valves JQ, PD
Valve DO has flow rate=0; tunnels lead to valves JS, AA
Valve PC has flow rate=0; tunnels lead to valves AK, KX
Valve YD has flow rate=0; tunnels lead to valves CA, OF
Valve RX has flow rate=0; tunnels lead to valves XG, BC
Valve CM has flow rate=0; tunnels lead to valves IR, OM
Valve HX has flow rate=6; tunnels lead to valves ZQ, NQ, AF, FD, CA
Valve ZQ has flow rate=0; tunnels lead to valves KH, HX
Valve BV has flow rate=21; tunnels lead to valves SY, OX, EI
Valve AK has flow rate=0; tunnels lead to valves PC, OQ
Valve UE has flow rate=0; tunnels lead to valves MS, JQ
Valve LR has flow rate=0; tunnels lead to valves BC, EJ
Valve JQ has flow rate=8; tunnels lead to valves MW, UE, BF, GW
Valve VL has flow rate=0; tunnels lead to valves PU, ZX
Valve EV has flow rate=0; tunnels lead to valves JJ, PD
Valve TS has flow rate=0; tunnels lead to valves NC, ZX
Valve RZ has flow rate=0; tunnels lead to valves SM, WU
Valve OF has flow rate=13; tunnels lead to valves XG, YD, NB, MS, XN
Valve WW has flow rate=0; tunnels lead to valves SM, IR
Valve TY has flow rate=0; tunnels lead to valves HO, AA
Valve XN has flow rate=0; tunnels lead to valves OF, PD
Valve SG has flow rate=15; tunnels lead to valves WU, YQ
Valve FN has flow rate=25; tunnel leads to valve PH
Valve KL has flow rate=0; tunnels lead to valves TN, OQ
Valve ZX has flow rate=5; tunnels lead to valves JS, HP, VL, NQ, TS
"""
)

print(example.optimise_pressure_relief())

