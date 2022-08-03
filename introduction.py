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
