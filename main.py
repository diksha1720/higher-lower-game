import art
import game_data
import random
from replit import clear



def results(A,B,score):
  if A['follower_count']>B['follower_count']:
    score+=1
    print(f"\nYou're right! current score :{score}\n")
    return score
  else:
    print(f"\nSorry, that's wrong. Final score {score}\n")
    return -1


def play(score):
  
  print(art.logo) 
  A=random.choice(game_data.data)
  print(f"Compare A {A['name']}, a {A['description']}, from {A['country']}.")

  print(art.vs)

  B=random.choice(game_data.data)
  print(f"Compare B {B['name']}, a {B['description']}, from {B['country']}.")

  choice=input("Who has more followers? Type 'A' or 'B' :").lower()
  if choice=='a':
    score=results(A,B,score)
    if score!=-1:
      play(score)
  elif choice=='b':
    score=results(B,A,score)
    if score!=-1:
      play(score)
  else:
    print("Wrong choice")

score=0
play(score)


