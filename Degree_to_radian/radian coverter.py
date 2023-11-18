user_choise=int(input("""enter your choise:
press 1 for degree to radian
press 2 for radian to degree"""))
angle_radian=0
angle_degree=0
def conv():
            angle_radian=angle_degree*22/180*7
            print(f"{angle_radian}")

def convd():
            angle_degree=angle_radian*180*7/22
            print(f"{angle_degree}degree")
match user_choise:
    case 1:
        angle_degree=int(input("Enter your angel in degree:"))
        conv()
    case 2:
        angle_radian=int(input("Enter your angle in radian"))
        convd()



