print("welcome to my python quiz!")
playing = input("do you want to play with me? ")
if playing != "yes":
    quit()
print("okay! let's play :) ")
score = 0
wrong = 0

answer = input("Who developed Python Programming Language? ")
if answer == "Guido van Rossum":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    wrong += 1

answer = input("Is Python case sensitive when dealing with identifiers? ")
if answer == "Yes":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    wrong += 1
    
answer = input("extension of the Python file? ")
if answer == ".py":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    wrong += 1
    
answer = input("Is Python code compiled or interpreted? ")
if answer == "Both":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    wrong += 1

answer = input("Which is used to define a block of code in Python language? ")
if answer == "Indentation":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    wrong += 1
    
answer = input("Which keyword is used for function in Python language? ")
if answer == "def":
    print("correct!")
    score +=1
else:
    print("incorrect!")
    wrong += 1
   
print("you got " + str(score) + " correct answers")
print("you got " + str(wrong) + " incorrect answers")


val = round(((score / 6) * 100),2)


print("you got " + str(val) + "%" )










