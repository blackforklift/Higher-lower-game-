from game_data import data
from art import logo, vs
from replit import clear
import random

winning =True
score=0
def print_account(person):
  return(f"{data[person]['name']} , a {data[person]['description']}, from  {data[person]['country']}")
  

def compare(followers_a,followers_b):
  if followers_a >= followers_b:  
    
    return f"You're right! Current score: {score} "
  elif followers_a<followers_b:  
    global winning
    winning=False
    clear()
    return f"Sorry, that's wrong. Final score: : {score-1}"
    

def get_account():
  return random.randint(0,49)

def Game():
  print(logo)
  
  personA=get_account()
  personB=get_account()
  
  followers_A=data[personA]['follower_count']
  followers_B=data[personB]['follower_count']
  
  
  
  print("Compare A : ", print_account(personA),"\n")

  print(vs)
  
  print("Against B : ", print_account(personB),"\n")
  
  guess=input("Who has more followers type A or B:  ").upper()
  
  
  if guess=="A":
    print(compare(followers_A,followers_B))
  elif guess=="B":
    print(compare(followers_B,followers_A))
  

while winning:
  clear()
  score+=1
  Game()
  
