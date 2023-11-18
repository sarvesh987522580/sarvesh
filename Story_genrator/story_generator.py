with open("story.txt" , "r") as file:
    content=file.read()

start_of_word=-1
target_start="<"
target_end=">"
for i in content:
    print(i)