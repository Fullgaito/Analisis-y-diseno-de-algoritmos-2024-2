import time
time_start = time.perf_counter()
def isSubsetSum(set, n, sum):
    # The value of subset[i][j] will be
    # true if there is a
    # subset of set[0..j-1] with sum equal to i
    subset = ([[False for i in range(sum + 1)]
               for i in range(n + 1)])

    # If sum is 0, then answer is true
    for i in range(n + 1):
        subset[i][0] = True

    # then answer is false
    for i in range(1, sum + 1):
        subset[0][i] = False

    # Fill the subset table in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < set[i - 1]:
                subset[i][j] = subset[i - 1][j]
            if j >= set[i - 1]:
                subset[i][j] = (subset[i - 1][j] or subset[i - 1][j - set[i - 1]])

    for i in range(1, n + 1):
        for j in range(1, n+ 1):
            if set[i-1] + set[j-1] == sum:
                print(set[i-1] , set[j-1])
            if set[i-1] == sum:
                print(set[i - 1])
            if set[j-1] == sum:
                print(set[j - 1])

    print(subset[n][sum])
    return subset[n][sum]


# Driver code
if __name__ == '__main__':
    set = [2,4,8,6,10]
    sum = 10
    n = len(set)
    if (isSubsetSum(set, n, sum) == True):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")

    time_elapsed = (time.perf_counter() - time_start)
    print(time_elapsed)