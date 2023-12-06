def calculate_distance(race_time, load_time):
    return (race_time-load_time)*load_time

def claculate_race_set(race_time):
    race_set = {}
    for time in range(0, race_time + 1):
        race_set[time] = (time,calculate_distance(race_time, time))
    return race_set

def calculate_winning_rounds(race_set, current_highscore):
    winner = []
    for race in range(len(race_set)):
        distance = race_set[race][1]
        if distance > current_highscore:
            winner.append(race)
    return winner

def number_of_wins(list):
    return len(list)

def run():
    print("Day 6 result 1 is:")
    result = 1

    input = [(47,400), (98,1213), (66,1011), (98,1540)]
    for race in input:
        time = race[0]
        highscore = race[1]

        race_set = claculate_race_set(time)
        winning_rounds = calculate_winning_rounds(race_set, highscore)
        result = result * number_of_wins(winning_rounds)
    
    print(result)

    print("Day 6 result 2 is:")
    result = 1

    input = [(47986698,400121310111540)]
    for race in input:
        time = race[0]
        highscore = race[1]

        race_set = claculate_race_set(time)
        winning_rounds = calculate_winning_rounds(race_set, highscore)
        result = result * number_of_wins(winning_rounds)
    
    print(result)