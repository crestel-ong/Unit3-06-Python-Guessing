#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2020
# This is Guessing program, with error checking in python

import random


def main():
    # this function sees if you can guess the number

    # this is the where the random number is generated from
    computer_number = random.randint(0, 9)

    # input
    integer_as_string = input("Enter a number between 0 - 9: ")

    try:
        # convert string to integer
        integer_as_number = int(integer_as_string)

        # process and output
        if integer_as_number == computer_number:
            print("Correct!")
        elif integer_as_number != computer_number:
            print("Incorrect, the number was {0}.".format(computer_number))
    except Exception:
        print("{0} is not an integer.".format(integer_as_string))
    finally:
        print("Thanks for playing.")
    print("\nDone.")


if __name__ == "__main__":
    main()
