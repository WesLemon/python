def main():

    a = float(input("Enter the first decimal value: "))
    b = float(input("Enter the second decimal value: "))
    c = float(input("Enter the third decimal value: "))
    d = float(input("Enter the fourth decimal value: "))

    mean_float = (a + b + c + d) / 4
    mean_int = int((a + b + c + d) / 4)

    print(f"The float mean of the four values entered is: {mean_float}")
    print(f"The int mean of the four values entered is: {mean_int}")

if __name__ == "__main__":
    main()