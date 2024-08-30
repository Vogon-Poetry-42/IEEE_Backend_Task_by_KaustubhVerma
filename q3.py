###         IEEE Backend task 3           ###
### by Kaustubh Verma, EEE, 2024A3PS0645P ###


def pairs(num_list, target):

    pairs_list = []

    for i in range(0, len(num_list)-2):
        for j in range(i+1, len(num_list)-1):
            if(num_list[i] + num_list[j] == target and (num_list[i], num_list[j]) not in pairs_list):
                pairs_list.append((num_list[i], num_list[j]))
    
    return pairs_list

def main():

    target = int(input()) # Give target value
    num_list_inp = input().split(" ") # Give inputs separated by space (eg 1 2 3 4 5 for inputting [1, 2, 3, 4, 5])
    num_list = [int(num) for num in num_list_inp]
    

    returned_pairs = pairs(num_list, target)

    print(returned_pairs)


if __name__ == "__main__":
    main()
