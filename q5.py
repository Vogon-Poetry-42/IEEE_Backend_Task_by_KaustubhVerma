###         IEEE Backend task 5           ###
### by Kaustubh Verma, EEE, 2024A8PS0645P ###

def recommend (interactions):
    length = len(interactions)
    length_list = [len(interactions[i]) for i in range(length)]
    recommended = [[0 for i in range(length_list[j])] for j in range(length)]
    #print(recommended) #debug
    items_views = {}

    for i in interactions:
        for j in i:
            if (j in items_views):
                recommended[interactions.index(i)][i.index(j)] = j
                items_views[j] += 1
            else:
                items_views[j] = 1

            
    return recommended
        
    



def main():
    
    customers = int(input("No of customers: "))
    interactions = []
    for i in range(customers):
        print("Enter the items viewed by the customer separated by a ' '")
        customer_list_inp = input().split(" ")
        customer_list = [int(i) for i in customer_list_inp]
        interactions.append(customer_list)

    recommended = recommend(interactions)

    print(recommended)

if __name__ == "__main__":
    main()