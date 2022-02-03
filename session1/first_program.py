"""
    Define main function of the program, this is a key structural element of simple 
    python script.
"""
def main():

    print("I just executed my first python program")

    # Comments in python start with hashtag

    """
        Multiline comments are normally written 
        inside triple quotes.
    """

    # variable a = 5, variable b = 7
    a = 5 
    b = 7 

    # add two numbers
    sum = a + b 

    print(f"The sum of {a} and {b} is {sum}")

"""
    When we run the file, python interpreter just memorizes the functions we define (in our case it is just one function
    called main) until it meets this if statement. Basically, it means if we are calling this script, execute the following
    functions it is called "main". When we write main() we call the function. Function does not have to be named "main"
    you can call it any how you like. 
"""
if __name__ == "__main__":
    main()
