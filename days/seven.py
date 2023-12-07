from functools import cmp_to_key
import json

def is_five_of_a_kind(hand):
    different_cards = len(list(set(hand)))
    if hand.count(hand[0]) == 5:
        return True
    if hand.count("J") >= 1 and different_cards == 2:
        return True
    else:
        return False
    
def is_four_of_a_kind(hand):
    for card in hand:
        if card != "J":
          if hand.count(card) == 4:
              return True
          if hand.count(card) == 3 and hand.count("J") == 1:
              return True
          if hand.count(card) == 2 and hand.count("J") == 2:
              return True
          if hand.count(card) == 1 and hand.count("J") == 3:
              return True
    return False

def is_three_of_a_kind(hand):
    for card in hand:
        if "J" in hand:
            if hand.count(card) == 2 and len(list(set(hand))) > 3:
                return True
        if hand.count(card) == 3 and len(list(set(hand))) > 2:
            return True
    return False

def is_full_house(hand):
    different_cards = len(list(set(hand)))
    if "J" in hand:
        if different_cards == 3:
            for card in hand:
              if hand.count(card) == 2:
                  return True

    if different_cards == 2:
        for card in hand:
            if hand.count(card) == 3:
                return True
    else:
        return False
    
def is_two_pair(hand):
    different_cards = len(list(set(hand)))
    if "J" not in hand:
      if different_cards == 3:
          cleared_hand = list(set(hand))
          if hand.count(cleared_hand[0]) == 2 and hand.count(cleared_hand[1]) == 2:
            return True
          if hand.count(cleared_hand[0]) == 2 and hand.count(cleared_hand[2]) == 2:
            return True
          if hand.count(cleared_hand[1]) == 2 and hand.count(cleared_hand[2]) == 2:
            return True
      else:
          return False
    else:
      return False

def is_one_pair(hand):
    different_cards = len(list(set(hand)))
    if "J" in hand:
      if different_cards == 5:
        return True

    if different_cards == 4:
        return True
    else:
        return False

def identify_hand(hand):
    if is_five_of_a_kind(hand):
        return "five_of_a_kind"
    if is_four_of_a_kind(hand):
        return "four_of_a_kind"
    if is_full_house(hand):
        return "full_house"
    if is_three_of_a_kind(hand):
        return "three_of_a_kind"
    if is_two_pair(hand):
        return "two_pair"
    if is_one_pair(hand):
        return "one_pair"
    else:
        return "high_card"
    
    

def get_ordered_hand(list):
    ordered_hand = {
      "five_of_a_kind": [],
      "four_of_a_kind": [],
      "full_house": [],
      "three_of_a_kind": [],
      "two_pair": [],
      "one_pair": [],
      "high_card": []
    }
    for hand in list:
        hand_type = identify_hand(hand[0])
        ordered_hand[hand_type].append(hand)

    return ordered_hand

def compare(tuple1,tuple2):
    order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    char1 = tuple1[0][0]
    char2 = tuple2[0][0]
    if order.index(char1) < order.index(char2):
        return -1
    elif order.index(char1) > order.index(char2):
        return 1
    else:
        return 0
    
def map_cards(hand_tuple):
    string = hand_tuple[0]
    tmp = string.replace("K", "B")
    tmp = tmp.replace("Q", "C")
    tmp = tmp.replace("J", "P")
    tmp = tmp.replace("T", "E")
    tmp = tmp.replace("9", "F")
    tmp = tmp.replace("8", "G")
    tmp = tmp.replace("7", "H")
    tmp = tmp.replace("6", "I")
    tmp = tmp.replace("5", "L")
    tmp = tmp.replace("4", "M")
    tmp = tmp.replace("3", "N")
    tmp = tmp.replace("2", "O")
    return (tmp,hand_tuple[1])

def reverse_map_cards(hand_tuple):
    string = hand_tuple[0]
    tmp = string.replace("B", "K")
    tmp = tmp.replace("C", "Q")
    tmp = tmp.replace("P", "J")
    tmp = tmp.replace("E", "T")
    tmp = tmp.replace("F", "9")
    tmp = tmp.replace("G", "8")
    tmp = tmp.replace("H", "7")
    tmp = tmp.replace("I", "6")
    tmp = tmp.replace("L", "5")
    tmp = tmp.replace("M", "4")
    tmp = tmp.replace("N", "3")
    tmp = tmp.replace("O", "2")
    return (tmp,hand_tuple[1])


def get_rank_hands(hands):
  mapped = []
  for hand in hands:
      new = map_cards(hand)
      mapped.append(new)
  sorted_hand = sorted(mapped, key=lambda x: x[0])

  new_mapped = []
  for hand in sorted_hand:
      new = reverse_map_cards(hand)
      new_mapped.append(new)

  return new_mapped


def get_ranked_game(dict):
    ordered_hand = {
      "five_of_a_kind": [],
      "four_of_a_kind": [],
      "full_house": [],
      "three_of_a_kind": [],
      "two_pair": [],
      "one_pair": [],
      "high_card": []
    }

    for hands in dict:
        handlist = dict[hands]
        if len(handlist) > 0:  
          ranked_hands = get_rank_hands(handlist)
          for hand in ranked_hands:
              ordered_hand[hands].append(hand)
    return ordered_hand

def count_hands(game):
  count = 0
  for hand_type in game:
    count = count + len(game[hand_type])
  return count

def calculate_winnings(game):
    max_rank = count_hands(game)
    winnings = 0
    for hand_type in game:
        for hand in game[hand_type]:
          winnings = winnings + (hand[1] * max_rank)
          max_rank = max_rank - 1
    return winnings

        
def run(list):
    ordered_hands = get_ordered_hand(list)
    ranked_games = get_ranked_game(ordered_hands)
    print(ranked_games)
    for game_type in ranked_games:
        for hand in ranked_games[game_type]:
            string = hand[0]

    winnings = calculate_winnings(ranked_games)
    print("Winnings are: ", winnings)