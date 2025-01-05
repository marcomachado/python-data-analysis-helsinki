#!/usr/bin/env python3

import math


def main():
    response = input("Choose a shape (triangle, rectangle, circle):")
    while response != "":        
        if (response == "triangle"):
            base = float(input("Give base of the triangle:"))
            height = float(input("Give height of the triangle:"))
            print(f"The area is {base*height/2}")
        elif response == "rectangle":
            width = float(input("Give width of the rectangle:"))
            height = float(input("Give height of the rectangle:"))
            print(f"The area is {width*height}")
        elif response == "circle":
            radius = float(input("Give radius of the circle:"))
            print(f"The area is {math.pi*radius**2}")
        else:
            print("Unknown shape!")
        response = input("Choose a shape (triangle, rectangle, circle):")

if __name__ == "__main__":
    main()
