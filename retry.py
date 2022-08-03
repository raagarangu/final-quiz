while retry not in retry_ans:  # Asks the user if they want to try again
    retry = input(
        "Would you like to try the quiz again to get a better score?\nPlease enter yes or no: ")  # Input for retry
    print("")
    retry = retry.upper()  # Makes the retry answer uppercase

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