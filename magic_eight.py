import random

def ask_for_question():
	question = input("What is your question? ")
	return question


def give_an_answer():
	return Answers[random.randint(0,19)]

Answers = [	
"It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]


q = ask_for_question()
while q != "quit":
	if q[-1] != "?":
		print("I’m sorry, I can only answer questions.")
	q = ask_for_question()
#print(give_an_answer())
