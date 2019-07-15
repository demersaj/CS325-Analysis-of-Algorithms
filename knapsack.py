import sys

# reads input file and determines variables
def loop_file():
    with open('shopping.txt') as infile:
        numTestCases = int(infile.readline())
        sys.stdout = open('results.txt', 'w')

        # loop through file and for each test case
        for k in range(numTestCases):
            print('Test Case ', k + 1, '\nMember Items:')
            price, weight, items = [], [], []  # reset variables
            numItems = int(infile.readline())

            # loop through and get each item and weight
            for i in range(numItems):
                line = infile.readline().split()
                price.append(int(line[0]))
                weight.append(int(line[1]))
                items.append(int(line[1]))
            maxPrice = 0
            numFamilyMembers = int(infile.readline())

            # loop through each family member and calculate the max price
            for j in range(numFamilyMembers):
                familyMem = j + 1
                capacity = int(infile.readline())
                maxPrice = maxPrice + knapsack(weight, price, numItems, capacity, items, familyMem)

            print('Total Price ', maxPrice, '\n')


def knapsack(W, P, N, M, items, familyMem):
    K = [[0 for m in range(M + 1)] for n in range(N + 1)]     # create array of [N + 1] x [M + 1]
    for i in range(N + 1):      # loop through each item
        for w in range(M + 1):  # loop through each weight of family member
            if i == 0 or w == 0:
                K[i][w] = 0
            elif W[i - 1] <= w:
                K[i][w] = max(P[i - 1] + K[i - 1][w - W[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    res = K[N][M]

    chosen = []     # create array to store chose item info in

    # work back through table to determine items that were chosen
    w = M
    for i in range(N, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            for j in range(len(items)):
                if items[j] == W[i - 1]:
                    if j + 1 not in chosen:
                        chosen.append(j + 1)
                        break
            res = res - P[i - 1]
            w = w - W[i - 1]
    print(familyMem, ':', ' '.join(str(k) for k in chosen))
    return K[N][M]


if __name__ == '__main__':
    loop_file()
