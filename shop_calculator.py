#shop calculator
sum=0
item_list=[]
while('True'):
    user_input=input("enter the price or press q to exit:")
    if user_input!='q':
        
        
        item_list.append(user_input)
        sum=sum + int(user_input)
        print("order total so far:",sum)
    else:
        print("total bill is:",sum)
        print("summary of bill is:")
        for x in item_list:
            print(x)
        break
