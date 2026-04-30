#This program is a quiz to guess the first as well as sir names of new zealand actors who have had a role inside marvel movies
#Variable Section (4 variables)
questionsandanswersdict = {"Who played Odin in Thor Ragnarok?": "Sam Neill", "Who plays Korg in Avengers end game?": "Taika Waititi", "Who played Skurge in Thor Ragnarok?": "Karl Urban", "Who played Fire fist in Deadpool 2?": "Julian Dennison", "Who played Topaz in Thor ragnarok?": "Rachel House", "Who played Ashley Kafka in Spiderman 2?": "Marton Csokas", "Who played Rouge in X-Men: Days of Future Past?": "Anna Paquin", "And finally, who played ghost in Ant-Man and the Wasp? (hint: last name is 2 words)": "Hannah John Kamen"}
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
if score < 2:
   print(f"You only got a score of {score}, thats means you're an actual normal person and not a marvel geek.")
elif score < 4:
   print(f"You got a score of {score}, thats pretty impressive not gonna lie. But you can do better.")
elif score < 6:
   print(f"You got a score of {score}, that must mean you really know alot about marvel. Impressive indeed.")
elif score < 8:
   print(f"You got a score of {score}, this score is really impressive if you can actually remember some of those obscure ones.")
elif score < 10:
   print(f"You got a score of {score}, either you got this score because some of your answers were ai sources from reddit or you're just a geek.")
elif score == 10:
   print(f"You got a score of {score}, congrats on cheating to get here but if you didn't then you're just marvels biggest geek.")