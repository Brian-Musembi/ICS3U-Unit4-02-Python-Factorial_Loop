#!/usr/bin/env python3

# Created by Brian Musembi
# Created on May 2021
# This program calculates the factorial of a user input


def main():
    # this function will calculate the factorial of a user input

    print("This program calculates the factorial of the given user input.")

    # loop counter variable
    loop_counter = 1

    # sum of positive integers variable
    product_num = 1

    # input
    user_input = input("Enter a positive integer: ")
    print("")

    # process
    try:
        user_input_int = int(user_input)

        if user_input_int > 0:
            # loop statement
            while loop_counter <= user_input_int:
                # calculations
                product_num = product_num * loop_counter
                loop_counter = loop_counter + 1
            # output
            print("{0} factorial is {1}"
                  .format(user_input_int, product_num))
        elif user_input_int == 0:
            # output
            print("0 factorial is 1.")
        else:
            # output
            print("{} is not a positive integer!"
                  .format(user_input_int))
    except Exception:
        # output
        print("That's not a number! Try again.")
    finally:
        print("")
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
