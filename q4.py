###         IEEE Backend task 4           ###
### by Kaustubh Verma, EEE, 2024A3PS0645P ###

def gcd(a, b):
    if (b == 0):
        return a 
    else:
        return gcd(b, a%b)

def main():
    
    print("Enter 5 numbers separated by a space (Eg 1 2 3 4 5):")
    numbers_inp = input().split(" ")
    numbers = [int(num) for num in numbers_inp]

    gcd_of_all = gcd(numbers[0], gcd(numbers[1], gcd(numbers[2], gcd(numbers[3], numbers[4]))))

    print(gcd_of_all)

if __name__ == "__main__":
    main()