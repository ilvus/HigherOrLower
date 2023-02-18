
from game_data import data
import art
import random as rd
import os 


#Print out the logo

#Create 2 characters 

account_a = rd.choice(data)
account_b = rd.choice(data)
if account_a == account_b:
    account_b = rd.choice(data)

def formating(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"

def followers(account):
    follower_count = account["follower_count"]
    return follower_count


def compare(account_a, account_b):
    scores = 0

    restart = False
    while not restart:
        print(art.logo)
        print(formating(account_a))

        print(art.vs)

        print(formating(account_b))
        users_answer = input("Choose 'A' or 'B': ").lower()
        
        if users_answer == "a" and followers(account_a) > followers(account_b):
            print("You are right!")
            scores += 1
        elif users_answer == "b" and followers(account_b) > followers(account_a):
            print("You are right!")
            scores += 1
        else: 
            print("You lose")
            restart = True

        os.system("cls")

        account_a = account_b
        account_b = rd.choice(data)
        if account_a == account_b:
            account_b = rd.choice(data)
    return f"Your score is: {scores}"

print(compare(account_a, account_b))        



