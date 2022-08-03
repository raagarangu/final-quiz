def intro():
    name = ""
    print("====****Introduction****=======")
    print("Hey there!\n")
    while len(name) < 1 or len(name) > 10:  # Asks the user for their name and limits inputs to no less than 1 and no more than 10
        name = input("Please enter a name with no more than 10 characters to continue: ")  # This will ask for the end users name
    print("Hey!" + name + "!\n")
    print("Welcome to my Education Quiz" + "\n")  # Welcoming the end user, and introduction to the quiz and gives the user a rundown of the quiz
    time.sleep(1)  # Stops time for 1 second
    print("In this quiz you will be quizzed on 20 random questions about education")
    time.sleep(1)
    print("You will receive your results and final score at the end.")
    time.sleep(1)
    print("Enjoy the quiz!")
    print("")
    return name  # Returns name

def questions(a):  # Definition for main part of code which is the questions
    count = 1  # Variables for count, score, and retry
    score = 0
    retry = ""
    for key, value in question_dic.items():  # prints the questions out to the user and asks for an input
        print(count, ".", key)  # key= question, value= answer
        for items in range(4):  # amount of options for answers available
            print(value[items])  # e.g A.answer
        count = count + 1
        ans = ""  # Variable for answer
        while ans not in valid:  # checks if the answer is valid
            ans = input("-----Please enter A, B, C, D to answer-----\nWhat is your answer? ")
            print("")
        if ans.upper() == value[4]:  # checks if the answer is correct and prints this statement
            print("Congrats, you are correct!")
            score = score + 1
            print("Your score is", score)
            print("")
        else:  # checks if the answer is incorrect and prints this statement
            print("Sorry, your answer was incorrect!")
            print("Your score is", score)
            print("")
    print("Congrats,", a, "you completed the education quiz!")  # Prints if user gets 5 or below
    print("You got a score of", score, "/ 15")
    if score <= 5:  # The program determines how well the user did and prints their name and score out to them
        print("Better luck next time!")
    elif score <= 10:
        print("Good job you did well!")
    elif score < 15:
        print("Great work you actually did really well!")
    elif score == 20:
        print("You got a perfect score!\nExcellent work!")
    print("")

    while retry not in retry_ans:  # Asks the user if they want to try again
        retry = input("Would you like to try the quiz again to get a better score?\nPlease enter yes or no: ")  # Input for retry
        print("")
        retry = retry.upper()  # Makes the retry answer uppercase
    return score, retry  # Returns score= makes variable global so access to different def and retry

def main():  # Definition for the main part of the code
    final_score = 0  # Variable for users final score
    name = intro()  # runs intro def and returns name so don't have to code again, name defined in intro and def transfered onto the bottom
    score, retry = questions(name)  # runs questions def and returns score and retry
    if final_score <= score:
        final_score = score  # Updates the final score
    while retry == "YES":  # Asks the user if they want to retry the quiz and if they do it restarts it
        retry = ""
        score, retry = questions(name)
        if final_score <= score:
            final_score = score
    if retry == "NO":  # If the user does not want to retry the quiz it ends the quiz
        print("Congrats,", name, "your final score was", final_score, "!")  # Final statement
        print("Thanks for playing the Education quiz")
        print("Goodbye...")
        exit()
