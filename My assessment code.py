"""
   May 11th 2026, Cruz Newton.
   This program is a quiz to guess the first as well as sir names of 
   new zealand actors who have had a role inside marvel movies: 
"""

# Variable Section
# Converting dict's into something that I can iterate through with next() function:
questionsandanswersdict= {
   "Who played Odin actor in Thor Ragnarok? Was it? Sam Neill, Karl Urban, Or Hannah Gray": "Sam Neill", 
   "Who plays Korg in Avengers End Game? Was it? Chadwick Boseman, Taika Waititi, Or Jimmy Drake": "Taika Waititi", 
   "Who played Skurge in Thor Ragnarok? Was it? Karl Urban, Park Sanchez, Or Rachel House": "Karl Urban", 
   "Who played Fire fist in Deadpool 2? Was it? Ryan Reynolds, Tony Hawk, Or Julian Dennison": "Julian Dennison", 
   "Who played Topaz in Thor Ragnarok? Was it? Emily Farce, Rachel House, Or Chris Hemsworth": "Rachel House", 
   "Who played Ashley Kafka in Spiderman 2? Was it? Rosemary Harris, Kirsten Dunst, Or Marton Csokas": "Marton Csokas", 
   "Who played Rouge in X-Men: Days of Future Past? Was it? Anna Paquin, Jennifer Lawrence, Or Morgan Lily": "Anna Paquin", 
   "And finally, who played the Maori Princess in Thor: Love and Thunder? Was it? Chayla Korewha, Melissa McCarthy, Or Pom Klementieff": "Chayla Korewha"
   }
wronganswers = {
    "Karl Urban": "Hannah Gray", 
    "Chadwick Boseman": "Jimmy Drake", 
    "Park Sanchez": "Rachel House", 
    "Ryan Reynolds": "Tony Hawk", 
    "Emily Farce": "Chris Hemsworth", 
    "Rosemary Harris": "Kirsten Dunst", 
    "Jennifer Lawrence": "Morgan Lily", 
    "Melissa McCarthy": "Pom Klementieff"
}
#The iterates: Can use next() to cycle through one variable at a time..
questioniterator = iter(questionsandanswersdict.keys())
answeriterator = iter(questionsandanswersdict.values())
firstwrongansweriterator = iter(wronganswers.keys())
secondwrongansweriterator = iter(wronganswers.values())
# To keep score of how many answers are right: Score is 0 by default
score = 0
#Import difference library for checking a 80% match to answers 
import difflib

# Quiz Loop: Each question in the dict will be asked here and users will be able to input their answer through this filter until all of them are done. 
while True:
    # This will print out the questions for people to see and will stop the quiz loop if there is nothing left to iterate
    try:
       question = next(questioniterator)
    except StopIteration:
      break
    print(question)

    # Will ask for user to type an answer and if their input is anything but the names it will ask to try again.
    rightanswer = next(answeriterator)
    wronganswer = next(firstwrongansweriterator)
    wronganswer2 = next(secondwrongansweriterator)
    while True:
      userinput = input("Name: ")
      #If your answer is wrong: Print right answer if difflib says it's close enough, Break loop to get next question
      if difflib.SequenceMatcher(None, wronganswer, userinput.title()).ratio() > 0.8 or difflib.SequenceMatcher(None, wronganswer2, userinput.title()).ratio() > 0.8:
         print(f"That answer is wrong, the answer is {rightanswer}")
         break
      #If your answer is right: Give score if difflib says it's close enough, Print some congrats, Break loop to get next question
      elif difflib.SequenceMatcher(None, rightanswer, userinput.title()).ratio() > 0.8:
         print("That answer is right!")
         score = score + 1
         break
      print("Please enter one of the three names correctly:")
      print(question)

# Score ratings: Each number of questions correct will print out a win message, it uses "lesser than" specific numbers to cover all possible scores.
if score < 2:
   print(f"You only got a score of {score}, thats means you're an actual normal person and not a marvel geek.")
elif score < 4:
   print(f"You got a score of {score}, thats pretty impressive not gonna lie. But you can do better.")
elif score < 6:
   print(f"You got a score of {score}, that must mean you really know alot about marvel. Impressive indeed.")
elif score < 8:
   print(f"You got a score of {score}, this score is really impressive if you can actually remember some of those obscure ones.")
elif score < 10:
   print(f"You got a score of {score}, congrats on cheating to get here but if you didn't then you're just marvels biggest geek.")