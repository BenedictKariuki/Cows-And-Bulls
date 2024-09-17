"""
Author: BENEDICT KARIUKI
Date: Sep 17, 2024
Version: 1.0
Description: This program implements the cows and bulls game using python programming language
"""
import random
# get the digits as a list
def get_digits(num: str) -> list:
    return [int(i) for i in num]

# check for duplicates
def contains_duplicates(num: str) -> bool:
    digits_list = get_digits(num)
    new_list = []
    for i in digits_list:
        if i not in new_list:
            new_list.append(i)
        else:
            return True
    return False
# generate the number and make sure it doesn't contain duplicates
def generate_num():
    # loop until the number has no duplicates
    while True:
        num = str(random.randint(1000, 10000))
        if not contains_duplicates(num):
            return num

# return the number of cows and bulls
def bulls_and_cows(number: list, guess: str) -> tuple:
    guess_ = get_digits(guess)
    # make a copy of the number_ variable that we can modify
    number_copy = number[:]
    cows_ = 0
    bulls_ = 0
    # find bulls
    for i in range(len(guess_)):
        if guess[i] == number[i]:
            bulls_ += 1
            # mark the digit not to use it in bulls
            number_copy[i] = None
    # find bulls
    for i in range(len(guess)):
        if guess[i] in number_copy and guess[i] != number[i]:
            cows_ += 1
            # mark the digit as used
            number_copy[number_copy.index(guess[i])] = None
    return cows_, bulls_


# validating the number of tries entered by the user
def validate_tries() -> int:
    # if no number is entered
    while True:
        try:
            num_tries = int(input("Enter the number of tries: "))
            if num_tries < 0:
                print("Number of tries should be positive")
            else:
                return num_tries
        except ValueError:
            print("Invalid input!!")

if __name__ == "__main__":
    number_ = list(generate_num())
    tries = validate_tries()

    while int(tries) > 0:
        guess = input("Enter your guess: ")
        # if the guess is not a 4-digit number, move to the next iteration
        if not 1000 <= int(guess) <= 9999:
            print("Enter a 4-digit number")
            continue
        # if the guess contains duplicates
        if contains_duplicates(guess):
            print("Your guess should not have duplicates. Please try again")
            continue
        cows, bulls = bulls_and_cows(number_, guess)
        print(f"{bulls} bulls {cows} cows")
        # check win
        if bulls == 4:
            print("\033[92mYou guessed right!\033[0m")
            break
        tries -= 1
    else:
        print("You ran out of tries!!")