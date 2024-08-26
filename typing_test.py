from time import *
import random as r

# Function for calculating accuracy
def errors(og, userinput, words):
    count = 0
    for i in range(min(len(og), len(userinput))):
        if og[i] != userinput[i]:
            count += 1
    
    count += abs(len(og) - len(userinput))

    correct = len(og) - count
    accuracy = (correct / len(og)) * 100
    return accuracy

# Function to calculate the typing speed in wpm 
def timetaken(start, end, userinput):
    duration = round((end-start), 3)/60
    word = userinput.split()
    timetaken = len(word)/duration
    return timetaken

while True :
    examples = ["Achieving a high level of typing proficiency involves a combination of regular practice, proper finger placement, and the gradual reduction of reliance on visual cues, all of which contribute to both speed and accuracy over time.", "To reach your typing goals, it's important to incorporate various exercises that challenge different aspects of your typing skills, such as typing long paragraphs, practicing with complex texts, and using typing tests to track your progress.", "Investing time in developing your typing technique can lead to significant improvements in your productivity, as faster and more accurate typing can streamline your work process and enhance overall efficiency in both professional and personal tasks."]
    test = r.choice(examples)

    print("Test your typing speed --\n")
    print(test + "\n\n")
    words = test.split()

    start = time()
    userinput=input("Type here : \n")
    end = time()

    netspeed = timetaken(start, end, userinput)
    accuracy = errors(test, userinput, words)

    print("Net speed : \n", round(netspeed, 3), "wpm")
    print("Accuracy : \n", round(accuracy, 2))

    num = int(input("Think you could do better?\nWell, you can always try again !\nPress 1 to continue."))
    if num==1:
        continue
    else:
        print("Thank you!\nSee you again!")
        break
