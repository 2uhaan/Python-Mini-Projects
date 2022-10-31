print("-------------Movie Trivia Game-------------")

score = 0

question = input("1. What was the Facebook Biopic called : ")

if question.lower() == "social network":
    print("Correct!")
    score += 1
else :
    print("Incorrect")

question = input("2. Which MCU movie won an Oscar : ")

if question.lower() == "black panther":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

question = input("3. which is the only Horror Movie Shot on IMAX : ")

if question.lower() == "nope":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

question = input("4. what was the 5th Harry Potter Movie called : ")

if question.lower() == "order of pheonix":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

question = input("5. The Rock played which DC charecter : ")

if question.lower() == "black adam":
    print("Correct!")
    score += 1
else:
    print("Incorrect")


print("You Have Answered " + str(score) + " questions correct out of 5")
print("You Have Got " + str(((score)/5)*100) + "%")






