import matplotlib.pyplot as plt
import random, time

class Array:


    def generateList(n:int):
        l = [random.randint(1,100) for i in range(n)]
        return l

    def generateObjective():
        o = random.randint(2,100)
        return o



    def checkSum(arr1:set, o:int):
        sumArr = {}
        key = 1
        for i in range(len(arr1)):
            for j in range(i+1, len(arr1)):
                if (arr1[i]+arr1[j]) == o:
                    sumArr.update({key:[arr1[i], arr1[j]]})
                    key+=1
        if sumArr:
            return sumArr
        else:
            return None

def test():
    objective = Array.generateObjective()
    steps = [[],[]]
    for i in range (2, 500, 1):
        tiempo = time.time()
        temp = Array.generateList(i)
        Array.checkSum(temp, objective)
        tiempo = time.time() - tiempo
        steps[0].append(i)
        steps[1].append(tiempo)
    return steps

def graphData(dataXY):
    plt.plot(dataXY[0], dataXY[1])
    plt.xlabel("data quantity in array")
    plt.ylabel("checking time in seconds")
    plt.grid()
    plt.title("Time complexity")
    plt.show()


def main():
    graphData(test())


    return 0


if __name__ == "__main__":
    main()