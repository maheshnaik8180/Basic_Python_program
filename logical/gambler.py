"""
date = '23/04/2021'
modified_date = '23/04/2021'
author = 'Mahesh Naik'
description = 'Simulates a gambler who start with $stake and place fair $1 bets until he/she goes broke
                (i.e. has no money) or reach $goal. Keeps track of the number of times he/she wins and the
                 number of bets he/she makes. Run the experiment N times, averages the results, and prints them out.'
"""
import random

while True:
    try:
        #given user Input Enter ammount stake and goal
        stake = int(input("Enter the amount you want to stake :"))
        goal = int(input("Enter your goal:"))
        #given User Input How many times play the user
        number_of_times = int(input("How many times you want to play:"))
        if stake>0 and goal>0 and number_of_times>0:
            break
        else:
            print("Invalid input!!")
    except:
        print("Invalid input!!")

def gambler(stake,goal,number_of_times):
    # initially win=0 and loose=0
    bets=0
    win=0
    # while loop till gambler stake=0 or stake =goal(200)
    while win!=goal and stake!=0:
        # random var for win or loose
        num=random.random()
        if num<0.5:
            # if gambler looses stake-1 and number of loose-1
            bets+=1
            win+=1
        else:
            # if wins stake++ and win++
            bets+=1
            stake-=1
    loss_percentage=((bets-win)/bets)*100
    win_percentage=(win/bets)*100
    # printing number of bets
    print(f"Total number of bets = {bets}")
    # printing number of wins
    print(f"Total win = {win}")
    # printing win percentage
    print(f"win percentage  ={win_percentage}")
    print(f"loss percentage ={loss_percentage}")

gambler(stake,goal,number_of_times)