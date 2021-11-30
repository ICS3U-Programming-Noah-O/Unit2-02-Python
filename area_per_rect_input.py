#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Nov. 25, 2021
# This program calculates the area and perimeter of a rectangle
# with dimensions that 
# are inputted by the user.


def main():
    # This function asks for the length and width and then
    # calculates the area and    # perimeter.

    # Input
    length = int(input("Enter length of your rectangle: "))
    width = int(input("Enter width of your rectangle: "))
    units = (input("Enter the units that you're using: "))

    # Process
    area = length * width
    perimeter = 2 * (length + width)

    # Output
    print(" ")
    print("The area is {}".format(area) + "{}^2".format(units) +
          " and the perimeter is {}".format(perimeter) + "{}".format(units))


if __name__ == "__main__":
    main()
