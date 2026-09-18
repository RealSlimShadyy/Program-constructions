def fahrenheit_to_celsius(f):
    return round((f - 32) * 5 / 9, 1)


if __name__ == "__main__":
    while True:
        f = int(input("Enter temperature in F: "))
        c = fahrenheit_to_celsius(f)
        print(f"Temperature in C: {c}")

        answer = input("Want to proceed? y/n: ")
        if answer.lower() != "y":
            break
