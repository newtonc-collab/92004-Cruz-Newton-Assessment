#This program is a quiz to guess the first as well as sir names of new zealand actors who have had a role inside marvel movies
#Variable Section (4 variables)
questionsandanswersdict = {"Who played Odin in Thor Ragnarok?": "Sam Neill", "Who plays Korg in Avengers end game?": "Taika Waititi", "Who played Skurge in Thor Ragnarok?": "Karl-Hein"}
questioniterator = iter(questionsandanswersdict.keys())
answeriterator = iter(questionsandanswersdict.values())
#Converting dict into something that I can iterate through with next function (3-5)
score = 0
#To keep score of how many answers are right (7)
#Quiz loop e
while True:
    try:
      print({next(questioniterator.strip("[]'"))})
    except StopIteration:
      break
    #This will print out the question for people to see and will stop the quiz loop if there is nothing left to iterate it (11-14)
    while True:
      userinput = input("Name: ")
      if all(letter.isalpha() for letter in userinput.split()) and userinput.split() != "":
         break
      print("Please do not enter blank space, special characters, or numbers.")
    #Will ask for user to type an answer and if it contains nothing, special characters, or numbers it will ask again. (16-20)
    rightanswer = next(answeriterator.strip("[]'"))
    if userinput.capitalize == rightanswer:
       score = score + 1
    else:
       print(f"That answer is wrong, the answer is {rightanswer}")
    #Checks if their answer is right by checking if the input is the same as the answer. If answer is right it will add score but if not it will print out the right answer. (22-26)
print(score)