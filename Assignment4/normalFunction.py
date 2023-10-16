import numpy as np
import matplotlib.pyplot as plt
import timeit

class normGenerator:
    def __init__(self, mean : float, sigma : float):
        self.mean = mean
        self.sigma = sigma
    
    def fromUniform(self, n: int):
        randList = {}
        for i in range(n):
            rand = np.random.uniform(low = -1, high = 1, size = (1, 12))
            total = self.mean+np.sqrt(self.sigma)*round((np.sum(rand)/2),2)
            if total not in randList:
                randList[total] = 1
            else:
                randList[total]+=1
        plt.bar(list(randList.keys()), list(randList.values()), width = 0.05)
        #plt.show()

    @staticmethod
    def normal(mean:float, sigma:float, x:float):
        return (1/(np.sqrt(2*np.pi*(sigma)))*np.exp(-(x-mean)**2/(2*(sigma))))

    def fromRejection(self, n:int):
        randList = {}
        for i in range(n):
            x = round(np.random.uniform(low=(self.mean-10*(self.sigma)), high=(self.mean+10*(self.sigma))),2)
            y = np.random.uniform(low=0, high=10)
            if (self.normal(mean=self.mean, sigma=self.sigma, x=x) > y):
                randList[x] = y
        plt.scatter(list(randList.keys()), list(randList.values()))
        #plt.show()
    
    def boxMuller(self, n:int):
        randList = {}
        for i in range(n):
            u1 = np.random.uniform(low = 0, high = 1)
            u2 = np.random.uniform(low = 0, high = 1)
            x = self.mean+self.sigma*(round(np.cos(2*np.pi*u1)*np.sqrt(-2*np.log(u2)), 2))
            if x not in randList:
                randList[x] = 1
            else:
                randList[x]+=1
        plt.bar(list(randList.keys()), list(randList.values()), width=0.05)
        #plt.show()


def main():
    print(timeit.timeit(stmt="mean = float(input(\"Enter mean :\"));sigma = float(input(\"Enter sigma:\"));norm = normGenerator(mean, sigma);norm.boxMuller(100000)", setup = "from __main__ import normGenerator", number=1))
    print(timeit.timeit(stmt="mean = float(input(\"Enter mean :\"));sigma = float(input(\"Enter sigma:\"));norm = normGenerator(mean, sigma);norm.fromRejection(100000)", setup = "from __main__ import normGenerator", number=1))
    print(timeit.timeit(stmt="mean = float(input(\"Enter mean :\"));sigma = float(input(\"Enter sigma:\"));norm = normGenerator(mean, sigma);norm.fromUniform(100000)", setup = "from __main__ import normGenerator", number=1))
if __name__ == "__main__":
    main()
        

