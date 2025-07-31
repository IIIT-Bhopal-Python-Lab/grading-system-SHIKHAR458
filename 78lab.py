while True:
    # Taking input from user
    user_input = input("Enter marks obtained or type 'exit' to quit program: ")

    # Condition to exit the program
    if user_input.lower() == "exit":
        print("Program exited.")
        break

    try:
        # Convert input to integer
        marks = int(user_input)

        # Check if marks are in valid range
        if 0 <= marks <= 100:
            # Grade assignment based on mark ranges
            if 90 <= marks <= 100:
                print("Obtained grade is A")
            elif 75 <= marks <= 89:
                print("Obtained grade is B")
            elif 60 <= marks <= 74:
                print("Obtained grade is C")
            elif 40 <= marks <= 59:
                print("Obtained grade is D")
            else:
                print("Obtained grade is F")
        else:
            # Marks out of valid range
            print("Error: Marks should be between 0 and 100.")
    
    except ValueError:
        # Error if input is not a number
        print("Invalid input: Please enter a number.")






