def part1(lines):
    total = 0
    for line in lines:
        x, y = map(str.split, line.split('|'))
        matches = set(x) & set(y)
        total += 2 ** (len(matches) - 1) if matches else 0
    return total

def part2(lines):
    cards = [1] * len(lines)
    #print(cards)
    for i, line in enumerate(lines):
        x, y = map(str.split, line.split('|'))
        n = len(set(x) & set(y))
        for j in range(i + 1, min(i + 1 + n, len(lines))):
            cards[j] += cards[i]
        #print(cards)
    return sum(cards)

#print(part1(), part2())

def count_matches(tuple) -> int:
    winners = tuple[0]
    numbers = tuple[1]
    matches = 0

    for winner in winners:
        if winner in numbers:
            matches = matches + 1
    return matches

def calculate_points(int):
    if int > 0:
        return 2**(int-1)
    return 0

def extend_scratchcards(list, matches, current_index):
    #cards = [1] * len(lines)


    return True



def calculate_full_game(list) -> int:
    game_points = 0
    for entry in list:
        matches = count_matches(entry)
        points = calculate_points(matches)
        game_points = game_points + points
    return game_points

def run():
    ## read stuff
    list = open('days/data/four').read().splitlines()
    new_list = [item.split(": ")[1] for item in list]
    data = [(entry.split(" | ")[0].split(),entry.split(" | ")[1].split()) for entry in new_list ]


    lines = open('days/data/four', 'r').readlines()
    print("Day one puzzle 1a is:")
    print(calculate_full_game(data))

