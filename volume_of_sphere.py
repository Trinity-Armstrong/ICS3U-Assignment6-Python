#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: November 2019
# This program calculates the volume of a sphere

import math


def calculate(radius):
    # This function calculates the volume of a sphere

    # Process
    volume = 4/3*math.pi*radius**3

    return volume


def main():
    # This function gets the radius then outputs the answer

    # Input
    while True:
        print("")
        user_radius = input("Enter the radius of your sphere here (cm): ")

        try:
            user_radius = int(user_radius)
            volume = calculate(radius=user_radius)
            if user_radius == int(user_radius):
                # Output
                print("The volume of your sphere is {}cm³.".format(volume))
                break
            else:
                print("")
                print("Error! Try again.")
        except Exception:
            print("")
            print("Error! Try again.")


if __name__ == "__main__":
    main()
