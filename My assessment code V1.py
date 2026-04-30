#This program is a quiz on a new zealand actors who have had a role inside marvel movies
#Variable Section
questionsandanswersdict = {"Who played Odin in Thor Ragnarok?": "Sam Neill", "peace": "peace"}
iterator = iter(questionsandanswersdict)
#Converting dict into something that I can iterate through with next
score = 0
answeredquestions = 0


while True:
    try:
      print({next(iterator)})
    except StopIteration:
      break
