import playsound
import time

CLEAR="\033[2J"
CLEAR_AND_RETURN="\033[H"

#clearing the terminal for better view
print(CLEAR)

def alarm(minute,sec):

    #clearing the terminal after user gives input
    print(CLEAR)

    #changing string into integer
    minute=int(minute)
    sec=int(sec)

    #taking total time into sec
    total_sec= (minute * 60) + sec
    
    #actual timer
    while(total_sec>0):
                
        minute=total_sec//60 # like if 120 sec than 125 // 60 gives 2
        sec=total_sec%60
        time.sleep(1)
        total_sec -= 1
        print(f" {CLEAR_AND_RETURN} time left :  {minute:02d}:{sec:02d}")
        
    playsound.playsound("C:/Users/sarvi/Documents/Python learning/Alarm_clock/aa.mp3")


def user_input():
    check=True
    while check:
        time_input=input("please enter the time in format of minute:seconds. Example 01:30    :     ")
        time_input=time_input.split(":")

        #checking if user only use 1 : mark or not by checking elements
        if len(time_input)==2:
            
            #seprating list item into varible as string
            minute=time_input[0]
            seconds=time_input[1]
            check=False
        
        else:
            check=True
            continue

        #checking if user put integer or not
        for i in time_input:
            
            if i.isdigit():
                check=False
            else:
                print("Please enter a digit.")
                check=True
                break
    #calling the function
    alarm(minute,seconds)
            
    print("done")
        

# playsound.playsound("C:/Users/sarvi/Documents/Python learning/Alarm_clock/aa.mp3")
user_input()