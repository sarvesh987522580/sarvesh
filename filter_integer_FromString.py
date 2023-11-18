user_input=input("entre a string with mixed postive integer")
filter_integer=[]
def get_integer(str):
    for i in str:
        if i=="0"or i=="1" or i=="2" or i=="3" or i=="4"or i=="5"or i=="6"or i=="7" or i=="8" or i=="9":
            filter_integer.append(i)
        else:
            continue
    print("filterd integer from string:",end=" ")
    for i in filter_integer:
        print(i,end=" ")
get_integer(user_input)