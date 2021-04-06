secret_number = 9
guess_count = 0
guess_limit = 30
while guess_count < guess_limit:
    user_input = input("Guess: ")
    converted_user_input = int(user_input)
    guess_count += 1
    if (converted_user_input == secret_number): b
        print("You won")
        break
    else:
        print("didn't match, please try again...")
        print("secret number is ",secret_number," and user input is ",user_input)
       