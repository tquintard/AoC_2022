import time
import re
import sys
from abc import ABC, abstractclassmethod
from collections
from contextlib
from dataclasses
from functools
from heapq
from itertools
from typing
start = time.perf_counter()
sys.setrecursionlimit(3000)

class Valve:
    def __init__(self, line):
        pattern = re.compile(r"([A-Z]{2})")
        self.name = [match.group(1) for match in pattern.finditer(line)][0]
        self.connected_valves = []
        pattern = re.compile(r"(\d+)")
        self.flowrate = [int(match.group(1)) for match in pattern.finditer(line)][0]
        self.state = 'Closed'

def open_valve(valve):
    pass

with open(r'AoC_2022\Day_16\example.txt', "r") as f:
    inputs = f.read().splitlines()
    valves = dict()
    #create all the valve object without their connected_valves attribute 
    for line in inputs:
        valve = Valve(line)
        valves[valve.name] = valve
    #for each valve fill the connected valves and sort them
    pattern = re.compile(r"([A-Z]{2})")
    for i, valve in enumerate(valves):
        valves_connected = [match.group(1) for match in pattern.finditer(inputs[i])][1:]
        for valve_connected in valves_connected:
            valves[valve].connected_valves.append([valve_connected, False])
    minute = 0
    pressure_released = 0
    current_valve = valves[list(valves.keys())[0]]
    previous_valve = ''
    while minute <= 30:
        minute += 1
        #determne the next valve to visit
        if len(current_valve.connected_valves) == 1:
            next_valve = valves[current_valve.connected_valves[0][0]]
            current_valve.connected_valves[0][1] = True
        else:
            for i, valve in enumerate(current_valve.connected_valves):
                next_valve_not_previous = valves[valve[0]].name != previous_valve
                next_valve_closed = valves[valve[0]].state == 'Closed'
                next_valve_not_visited = valve[1] == False
                if next_valve_not_previous and next_valve_closed and next_valve_not_visited:
                    next_valve = valves[valve[0]]
                    valve[1] = True
                    break
        if next_valve == current_valve:
            next_valve = valves[current_valve.connected_valves[0][0]]
        #open the valve if required and go to next valve
        if current_valve.flowrate > next_valve.flowrate and current_valve.state == 'Closed':
            current_valve.state = 'Open'
            pressure_released += current_valve.flowrate * (30 - minute)
            print(sep='\n', *[f'== Minute {minute} ==',f'You open valve {current_valve.name}'],end='\n')
            minute += 1
        previous_valve = current_valve.name
        current_valve = next_valve
        print(sep='\n', *[f'== Minute {minute} ==',f'You move to valve {current_valve.name}'],end='\n')
                               
    print()



