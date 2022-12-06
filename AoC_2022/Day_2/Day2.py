import time
GAME_RESULT = [['A Z','B X','C Y'], ['A X','B Y','C Z'], ['A Y','B Z','C X'] ] #[LOST, DRAW, WIN]

def results(game, part = 1):
    my_result = results_points(game[2]) # to catch the value of X(Rock), Y(Paper), Z(Scissor)
    opponent_index = results_points(game[0],'A') - 1 # to catch the index of A(Rock), B(Paper), C(Scissor) in GAME_RESULT
    expected_play = results_points(GAME_RESULT[my_result-1][opponent_index][2])
    if part == 2:
        return expected_play + 3*(my_result-1)
    return [my_result + 3*final_result for final_result in range(len(GAME_RESULT)) if game in GAME_RESULT[final_result]][0]

def results_points(letter, ref_letter = 'X'):
    return ord(letter) - ord(ref_letter) + 1

with open('Day2.txt', "r") as f:
    games = f.read().splitlines()
    print (sum([results(game) for game in games]), sum([results(game,2) for game in games]))
 