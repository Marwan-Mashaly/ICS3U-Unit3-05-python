#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on September 2019
# This program tells user the month afte typing the number


def main():
    # This function tells user the month afte typing the number

    # input
    month_number = int(input("Enter a number of a month: "))
    print("")

    # process
    if month_number == 1:
        # output
        print("January")
    elif month_number == 2:
        # output
        print("February ")
    elif month_number == 3:
        # output
        print("March ")
    elif month_number == 4:
        # output
        print("April ")
    elif month_number == 5:
        # output
        print("May ")
    elif month_number == 6:
        # output
        print("June ")
    elif month_number == 7:
        # output
        print("July ")
    elif month_number == 8:
        # output
        print("August ")
    elif month_number == 9:
        # output
        print("September ")
    elif month_number == 10:
        # output
        print("October ")
    elif month_number == 11:
        # output
        print("November ")
    elif month_number == 12:
        # output
        print("December ")

    else:
        # output
        print("invalid month ")


if __name__ == '__main__':
    main()
