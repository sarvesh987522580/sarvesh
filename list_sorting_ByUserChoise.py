user_list=[]

iter=int(input("how many number you want to store:"))
for i in range(iter):
    a=int(input("enter the number:"))
    user_list.append(a)
def sorting_list(list,order):
    match order:
        case 1:
            list.sort()
            print(list)
        case 2:
            a=[]
            a=list.reverse()
            print(a)
        case 3:
            print(list)
chosen_order=int(input("""Please chose your prefer order:
press 1 for asending 
press 2 for desending
press 3 for none"""))
sorting_list(user_list,chosen_order)