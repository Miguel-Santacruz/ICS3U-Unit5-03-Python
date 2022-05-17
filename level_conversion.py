#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: May 2022
# This program coverts levels to percentages


def percentage(level):
    # convert from level to percentage

    # process
    if level == "4+":
        answer = "97%"
    elif level == "4":
        answer = "90%"
    elif level == "4-":
        answer = "83%"
    elif level == "3+":
        answer = "78%"
    elif level == "3":
        answer = "74%"
    elif level == "3-":
        answer = "71%"
    elif level == "2+":
        answer = "68%"
    elif level == "2":
        answer = "64%"
    elif level == "2-":
        answer = "61%"
    elif level == "1+":
        answer = "58%"
    elif level == "1":
        answer = "54%"
    elif level == "1-":
        answer = "51%"
    elif level == "R":
        answer = "25%"
    else:
        answer = -1

    return answer


def main():
    # This function gets the level
    level = input("Enter the level you want converted to a percentage: ")

    # call functions
    answer = percentage(level)

    print("Level {0} has a middle percentage of {1}.".format(level, answer))


if __name__ == "__main__":
    main()
