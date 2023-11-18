user_input=input("enter your word:")
vowel=[]

def count_vowels(word):
    for i in word:
        if i=="a" or i=="e" or i=="i" or i=="o"or i=="u":
            vowel.append(i)
        else:
            continue
    print(f"number of vowels in your word is:{len(vowel)}")

count_vowels(user_input)