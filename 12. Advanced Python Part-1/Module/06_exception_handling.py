try:
    n = int(input("Enter a number: "))
    ans = 10 / n
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")

else:
    print(f"Answer is: {ans}")

finally:
    print("This will always run.")


# Exception handling is used to manage errors that occur during program execution. It prevents the program from crashing and allows you to handle errors gracefully.