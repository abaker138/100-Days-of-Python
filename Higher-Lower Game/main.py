import game_data
import art
import random

choices  = []
score = 0
playing = True

def find_celebrity():
  return random.choice(game_data.data)

def print_choice(list, index):
  choice = list[index]
  letter = ""
  if index == 0:
    letter = "A"
  else: 
    letter = "B"
  print(f"Compare {letter}: {choice['name']}, a {choice['description']}, " f"from {choice['country']}, has " f"{choice['follower_count']}")

def compare(list, answer):
  first = list[0]
  second = list[1]
  if first['follower_count'] > second['follower_count'] and answer == 'a':
    print("You are right, it's A")
    return next_question(list, find_celebrity())
  elif first['follower_count'] < second['follower_count'] and answer == 'b':
    print("You are right, it's B")
    return next_question(list, find_celebrity())
  else:
    print("You lose")
    return lose_and_restart(list)

def next_question(list, new_celeb):
  global score
  score += 1
  list.pop(0)
  list.append(new_celeb)
  return list

def lose_and_restart(list):
  answer = input("Do you want to play again? y or no?").lower()
  if answer =="y":
    global score
    score = 0
    list = []
    list.append(find_celebrity())
    list.append(find_celebrity())
    return list
    
choices.append(find_celebrity())
choices.append(find_celebrity())

while playing:
  print(art.logo)
  if choices[0]["name"] == choices[1]["name"]:
    choices[1] = find_celebrity()
  if score > 0:
    print(f"Your score is {score}")
  print_choice(choices,0)
  print(art.vs)
  print_choice(choices, 1)
  answer = input("\nA or B?  ").lower()
  choices = compare(choices, answer)

  

  