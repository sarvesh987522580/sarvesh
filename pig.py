import random
max_score=10
mon_score=0
player_score=list()
print("welcome to pig game")

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

while True:
    no_of_player=input("enter no of player between 2-4: ") 
    if no_of_player.isdigit():
        no_of_player=int(no_of_player)
        if 2<=no_of_player<=4:
            break
        else:
            print("please enter a valid number of player ")
    else:
        print("please enter a valid input: ")


player_score = [0 for _ in range(no_of_player)]    
print(f"current score : {player_score}")

current_score=0
while max(player_score)<max_score:
    for i in range(no_of_player):
        if(max(player_score)>max_score):
            break
        print(f"player{1+i} turn.")
        while True:
            dice_choise=input("Do you want to roll the dice press y to roll the dice or any other key to over the turn:")
            if dice_choise.lower()!="y":
                print(f"\n\n player {1+i} turn is over \n\n")
                break
            else:
                current_score=player_score[i]
                value=roll()
                print(f"you roll the {value}")
                current_score=current_score+value
                player_score[i]=current_score
                print(player_score)
                if(max(player_score)>=max_score):
                    break
                if value==1:
                    current_score=0
                    player_score[i]=current_score
                    print("your all score become 0")
                    print(f"\n\n player {1+i} turn is over \n\n")
                    break
                
                player_score[i]=current_score
wining_player=player_score.index(max(player_score)) + 1        
print(f"player {wining_player} wins the game.")



    









# Chosse_no_of_player()
# roll()
# check_score()
