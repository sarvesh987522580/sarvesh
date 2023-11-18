import random
import time
TOTAL_QUESTIONS=5
MAX_INT=5
MIN_INT=1
OPERATOR=["+" , "-" , "*"]

def questio_genrator():
    left=random.randint(MIN_INT,MAX_INT)
    right=random.randint(MIN_INT,MAX_INT)
    middle=random.choice(OPERATOR)
    exper= str(left) + middle + str(right)
    answer=eval(exper)
    return exper,answer

start_time=time.time()
for i in range(TOTAL_QUESTIONS):
    exper,answer=questio_genrator()
    while True:
        print(f"question number {i+1} :{exper} ")
        user_answer=input()
        if user_answer==str(answer):
            break

end_time=time.time()   
print(f"you complete the challange in {round(end_time -start_time,2)} sec")