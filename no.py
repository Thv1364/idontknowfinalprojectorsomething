#Defs
words=["chicken", "pie", "jonathanyoon", "jaydencheng", "topology", "lights", "rudolph", "september", "never", "gonna", "give", "you", "up", "wish", "were", "here", "marestaing"]
import random
word=random.choice(words)
leng=len(word)
splitword=list(word)
Letters=[]
Lettersasked=0
solved=0
resul=0
fails=0


#Setup word code
def setup():
    unknown=[]
    i=0
    while i<leng:
        unknown.append("_")
        i=i+1
    return unknown    
uknown = setup()



#Initial thing to tell person how many letters
combi=  ' '.join(uknown)
print("Here is your solved word so far: " + combi)



#Setup fails code
def setupfails():
    r=input("How many fails are you allowing? \n")
    return r
allowedfails=setupfails()


#Letter checker
def checkletter(lette):#check if letter is solved
    k=0
    woo=0
    while k<leng:
        if str(lette)==str(splitword[k]):
            uknown[k]=lette

            woo=1
        k=k+1
    if woo==0:
        return 1
    else:
        return 0


#Set up returner
def returner(result):
    if result==0:
        return 1
    else:
        return 0#word not sp;ved


#Checks to see if the whole word is solved
def checkall():#check if whole word is solved
    j=0
    result=0
    while j<leng:
        if uknown[j]==splitword[j]:
            result=result+0
        else:
            result=1

        j=j+1  
    return returner(result)
    
#Initial Divider
print("_______________________________________________ \n")

########################################################################################################

while resul==0: #main while loop
    
    if fails<=int(allowedfails):

        if checkall()==0:
            newletter = input("What is your letter? \n")
            Letters.append(newletter)
            print(int(checkletter(newletter)))
            fails=int(fails) + int(checkletter(newletter))

            combiword= ' '.join(uknown)
            combilet=', '.join(Letters)
            print("\nHere are the letters you have used: " + combilet)
            print("Here is your solved word so far: " + combiword)
            print("You have " + str(fails) + " fails out of " + str(allowedfails) + " allowed.")

        else:#word is solved
            print("Yay! You solved it!")
            resul=1
    else:
        resul=2
        print("loser")
    print("_______________________________________________ \n")
    Lettersasked=Lettersasked+1