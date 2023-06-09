## @author Nathan Morris
## Last updated 6/8/2023
## Description: Game that encourages users to enchance there knowledge of worldwide Trivia!

#counter that counts the user's score after each answer
count = 0

#introduction
print("Welcome to my Trivia Game, Test your knowledge of science, movies, math, pop culture, and more!!!")

#user vefication prompt
attempt = input("\n" + "Do you want to attempt the quiz? ")

if (attempt == "yes" or attempt == "Yes"):
    print("\n" + "Time to begin!")
else:
    print ("Feel free to come back anytime. Have a nice day!")
    quit()


#easy difficulty
question1 = input("\n" + "Question number 1: How many days are in a year? (Please note that answers are case sensitive) ") 
if question1 == ("365"):
    print("\n" + "That is Correct!")
    count = count + 1

else:
    print("\n" + "That is Incorrect!")
    count = count - 1

#easy difficulty
question2 = input("\n" + "Question number 2: Which continent is the United States located in? (Please note that answers are case sensitive) ") 
if question2 == ("North America"):
    print("\n" + "That is Correct!")
    count = count + 1
else:
    print("\n" + "That is Incorrect!")
    count = count - 1

#easy difficulty
question3 = input("\n" + "Question number 3: What is the superhero who's name is Peter Parker? (Please note that answers are case sensitive) ") 
if question3 == ("Spiderman"):
    print("\n" + "That is Correct!")
    count = count + 1
else:
    print("\n" + "That is Incorrect!")
    count = count - 1

#if the user's score is less than or equal 0 keep the score at 0
if count <= 0:
    count = 0

#display the user's final score and exit the program
score = count 
print("\n" + "Thank you for playing! Your final score was " + str(score) + "/3")
quit()
