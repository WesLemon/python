def main():

    print("Enter the length of the rectangle: ")
    length = int(input())

    print("Enter the width of the rectangle: ")
    width = int(input())

    area = length * width
    perimeter = (2 * length) + (2 * width)

    print(f"The area of the rectangle is: {area}")
    print(f"The perimeter of the rectangle is: {perimeter}")

if __name__ == "__main__":
    main()
