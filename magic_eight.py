def ask_for_question():
	question = input("What is your question? ")
	return question

q = ask_for_question()
while q != "quit":
	if q[-1] != "?":
		print("I’m sorry, I can only answer questions.")
	q = ask_for_question()
