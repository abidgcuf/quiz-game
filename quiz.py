print("Welcome to Computer Quiz")

playing = input("Do You Want To play ? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let,s Play the game ")
score = 0

answer = input("What does CPU Mean? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    print("the coreect answer is central processing unit ")
answer = input("What does GPU Mean? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    print("the coreect answer is graphics processing unit ")

answer = input("What does Ram Mean? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    print("the coreect answer is Random access memory ")

answer = input("What does PSU Mean? ")
if answer.lower() == "power supply unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    print("the coreect answer is power supply unit ")
answer = input("Key board is ----- device? ")
if answer.lower() == "input":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    print("the coreect answer is input ")

print("You Got " +  str(score)  +  " Question correct!")
print("You Got " +  str((score/5)* 100)  + "% marks")

