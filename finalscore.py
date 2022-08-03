final_score = 0  # Variable for users final score
name = intro()  # runs intro def and returns name so don't have to code again, name defined in intro and def transfered onto the bottom
score, retry = questions(name)  # runs questions def and returns score and retry
if final_score <= score:
    final_score = score  # Updates the final score