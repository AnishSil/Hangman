import random
words='Play'
score=0
print("Guess the anime title!!!")
names=['tokyo ghoul', 'your lie in april','guilty crown', 'pokemon','grand blue', 'my hero academia',
'sword art online', 'attack on titan', 'death note', 'vinland saga']
while len(names)!=0:
    play=input(f"{words}?(Y/N)")
    if play.lower()=='y':
        num2,num1=1,0
        orig_word=[]
        num1=random.randint(0,len(names)-1)
        orig_word=list(names[num1])
        words=names[num1]
        names.remove(words)
        chr='_'*len(orig_word)
        words="Continue"
        num3=0
        while num1==num2 or num2==num3 or num1==num3: #3 unique random character
            num1=random.randint(1,len(orig_word)-1)
            num2=random.randint(1,len(orig_word)-1)
            num3=random.randint(1,len(orig_word)-1)
        in_game_word=list(chr)
        for i in range(0,len(orig_word)):#loop for blanks
            if i==num1 or i==num2 or i==num3 or orig_word[i]==' ':
                in_game_word[i]=orig_word[i]
            if len(orig_word)>=10 and i>=7: #additional random characters if word has more than 8 characters
                num2=random.randint(0,len(orig_word)-1)
                in_game_word[num2]=orig_word[num2]
        num2=0
        chr=""
        print(f"Your word is: {chr.join(in_game_word)}")
        while in_game_word!=orig_word:
            player_input=input(">>> ")
            num1,num4,num3=0,0,0
            if list(player_input)==orig_word:
                print("You guessed correct!, You win")
                score+=1
                break
            for i in range(0,len(orig_word)):#loop for comparing
                if player_input.lower()==in_game_word[i]:
                    num4+=1
                elif player_input.lower()==orig_word[i]:
                    in_game_word[i]=orig_word[i]
                    num1=-1
                    num3+=1
            print(chr.join(in_game_word))
            if num3==0 and num4>=1:
                print("This letter already exists!")
            elif num2==3:
                print(f"Correct word was: {chr.join(orig_word)}")
                print("All guesses used, You lose!")
                break
            elif num1!=-1 and num4==0:
                print(f"Wrong Guess!! {3-num2} chance(s) remaining")
                num2+=1
            elif in_game_word==orig_word:
                print("You win!")
                score+=1
    elif play.lower()=='n':
        print(f"Final score: {score}")
        print("Bye!") 
        break
    else:
        print("select a correct option")
if len(names)==0:
    print("You finished all levels!")
    print(f"Final score: {score}")

