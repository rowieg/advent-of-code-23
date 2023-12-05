class Game:
    boundary: {}
    game_data: {}

    def __init__(self, red, green, blue):
        self.boundary = {
            "red": red,
            "green": green,
            "blue": blue
        }

    def import_game_data(self, array):
        game_data = {}
        for game_index, line in enumerate(array):
            real_game_index = game_index + 1
            game_data[real_game_index] = {}
            all_game_data = line.split(":")
            single_games_data = all_game_data[1].split(";")
            for game_round_index, game in enumerate(single_games_data):
                real_game_round_index = game_round_index + 1
                red_index = 0
                green_index = 0
                blue_index = 0
                game_data[real_game_index][real_game_round_index]={}

                if "red" in game:
                    red_index = game.index("red")
                else:
                    red_index = 2

                if "green" in game:
                    green_index = game.index("green")
                else:
                    green_index = 2
                
                if "blue" in game:
                    blue_index = game.index("blue")
                else:
                    blue_index = 2

                if game[red_index-2].isdigit():
                    if game[red_index-2].isdigit() and game[red_index-3].isdigit():
                        game_data[real_game_index][real_game_round_index]["red"] = int(game[red_index-3] + game[red_index-2])
                    else:
                        game_data[real_game_index][real_game_round_index]["red"] = int(game[red_index-2])
                else:
                    game_data[real_game_index][real_game_round_index]["red"] = 0

                if game[green_index-2].isdigit():
                    if game[green_index-2].isdigit() and game[green_index-3].isdigit():
                        game_data[real_game_index][real_game_round_index]["green"] = int(game[green_index-3] + game[green_index-2])
                    else:
                        game_data[real_game_index][real_game_round_index]["green"] = int(game[green_index-2])
                else:
                    game_data[real_game_index][real_game_round_index]["green"] = 0

                if game[blue_index-2].isdigit():
                    if game[blue_index-2].isdigit() and game[blue_index-3].isdigit():
                        game_data[real_game_index][real_game_round_index]["blue"] = int(game[blue_index-3] + game[blue_index-2])
                    else:    
                        game_data[real_game_index][real_game_round_index]["blue"] = int(game[blue_index-2])
                else:
                    game_data[real_game_index][real_game_round_index]["blue"] = 0

        self.game_data = game_data

    def load_game_data(self):
        return self.game_data
    
    def get_possible_games(self):
        game_data = self.game_data
        boundary = self.boundary
        possible_games = []
        is_possible = True

        for game_key in game_data:
            is_possible = True

            for round_key in game_data[game_key]:
                if game_data[game_key][round_key]["red"] > boundary["red"]:
                    is_possible = False
                if game_data[game_key][round_key]["green"] > boundary["green"]:
                    is_possible = False
                if game_data[game_key][round_key]["blue"] > boundary["blue"]:
                    is_possible = False
                
            if is_possible:
                possible_games.append(game_key)
            
        return possible_games

    def get_min_number_of_cubes(self):
        game_data = self.game_data
        min_games = []

        for game_key in game_data:
            red = 0
            green = 0
            blue = 0
            for round_key in game_data[game_key]:
                if game_data[game_key][round_key]["red"] > red:
                    red = game_data[game_key][round_key]["red"]
                if game_data[game_key][round_key]["green"] > green:
                    green = game_data[game_key][round_key]["green"]
                if game_data[game_key][round_key]["blue"] > blue:
                    blue = game_data[game_key][round_key]["blue"]
            min_games.append(red * green * blue)
            
        return min_games
def run(data_input):
    print("Day two puzzle 1a is:")


    g1 = Game(12, 13, 14)

    g1.import_game_data(data_input)

    posible_games = g1.get_possible_games()
    min_games = g1.get_min_number_of_cubes()

    game_sum = 0
    min_game_sum = 0

    for game in posible_games:
        game_sum = game_sum + game

    for min in min_games:
        min_game_sum = min_game_sum + min

    print(game_sum)
    print(min_game_sum)
