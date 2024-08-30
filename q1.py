###         IEEE Backend task 1           ###
### by Kaustubh Verma, EEE, 2024A3PS0645P ###

def are_strings_complementary(s1, s2):
    check_s1_in_s2 = ""
    check_s2_in_s1 = ""
    check_s1_in_s2 = [i for i in s1 if i in s2]
    # print(f"debug: {check_s1_in_s2}") #debug
    check_s2_in_s1 = [i for i in s2 if i in s1]
    # print(f"debug: {check_s2_in_s1}") #debug

    if (not check_s1_in_s2 and not check_s2_in_s1):
        return True

    return False

def main ():
    s1 = input()
    s2 = input()

    if (not s1 or not s2):
        print("Invalid Input!")
        raise RuntimeError

    if (are_strings_complementary(s1, s2)):
        print(f"{s1} and {s2} are complementary")
    else:
        print(f"{s1} and {s2} are not complementary")

if __name__ == "__main__":
    main()