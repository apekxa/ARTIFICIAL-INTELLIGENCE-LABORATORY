print("Simple Question and Answering Program")
print("=====================================")
print(" You may ask any one of these questions")
print("Hi")
print("How are you?")
print("Are you studying?")
print("What is your name?")
print("what did you do yesterday?")
print("Quit")
while True:
    question = input("Enter one question from above list:")
    question = question.lower()
    if question in ['hi']:
        print("Hello")
    elif question in ['how are you?','how do you do?']:
        print("I am fine")
    elif question in ['are you studying?','are you doing any job?']:
        print("yes. I'am studying in VCET Puttur")
    elif question in ['what is your name?']:
        print("My name is Anu")
        name=input("Enter your name?")
        print("Nice name and Nice meeting you",name)
    elif question in ['what did you do yesterday?']:
        print("I saw Bahubali 5 times")
    elif question in ['quit']:
        break
    else:
        print("I don't understand what you said")