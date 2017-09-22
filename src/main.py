import random

TARGET_NUM = 42.0 #Goal

class cell():
    def __init__(self):
        self.ftion = ['x','x','x','x','x','x','x']
        self.fstring = "XXXXXXX"
        self.value = -0.000000
        self.egradient = TARGET_NUM - self.value
        self.mutated = False

    def getRandomN(self):
        return str(random.randint(1, 100))

    def getRandomO(self):
        x = random.randint(1, 4)
        if x == 1:
            return '+'
        if x == 2:
            return '-'
        if x == 3:
            return '*'
        if x == 4:
            return '/'

    def updateF(self):
        self.fstring = ''.join(self.ftion)
        self.value = eval(self.fstring)
        if (self.value < 1):
            self.egradient = TARGET_NUM + (-1 * self.value)
        else:
            self.egradient = TARGET_NUM - self.value
        if (self.egradient < 1):
            self.egradient *= -1

    def generateF(self):
        iters = 0
        while iters < 7:
            if(iters % 2 == 0):
                self.ftion[iters] = cell.getRandomN(None)
            elif(iters % 2 != 0):
                self.ftion[iters] = cell.getRandomO(None)
            iters+=1
        self.updateF()

def reproduce(cell1, cell2):
    newcell = cell()
    crossover = random.randint(2,5)
    #mutation crap
    mutation = random.randint(1, 1000)
    mutationN = random.randint(0,6)
    iters = 0
    while(iters < 7):
        if(iters <= crossover):
            newcell.ftion[iters] = cell1.ftion[iters]
        elif(iters>crossover and mutation <= 10 and iters == mutationN):
            if (iters % 2 == 0):
                newcell.ftion[iters] = cell.getRandomN(None)
                newcell.mutated = True
            elif (iters % 2 != 0):
                newcell.ftion[iters] = cell.getRandomO(None)
        elif (iters > crossover):
            newcell.ftion[iters] = cell2.ftion[iters]
        iters+=1
    newcell.updateF()
    return newcell

def bubosort(cell_list):
    swapped = False
    while(not swapped):
        swapped = True
        for x in range(1,20):
            if cell_list[x - 1].egradient > cell_list[x].egradient:

                tempcell = cell_list[x]
                cell_list[x] =

                swapped = False



celldad = cell()
celldad.generateF()
print("TARGET VALUE: ", TARGET_NUM, "\n Cell Dad:")
print(celldad.ftion, "=", celldad.value)
print("error gradient: ", celldad.egradient)
print("mutated? ", celldad.mutated)

cellmom = cell()
cellmom.generateF()
print("\n Cell Mom:\n",cellmom.ftion, "=", cellmom.value)
print("error gradient: ", cellmom.egradient)
print("mutated? ", celldad.mutated)

child = reproduce(celldad, cellmom)
print("\n Child:\n", child.ftion, "=", child.value)
print("error gradient: ", child.egradient)
print("mutated? ", celldad.mutated)

running = True

def main():
    generations = 0
    cellpool = []
    fitnesspool = []

    while(running == True and generations < 100):

        print("\n======[GENERATION ", generations + 1, "]======")
        if(generations == 0):
            for x in range(0, 20):
                placeholder = cell()
                placeholder.generateF()
                cellpool.append(placeholder);
        else:
            break
        generations+=1

        for x in range(0, 20):
            print(cellpool[x].ftion,"=" ,cellpool[x].value, " eG: ",cellpool[x].egradient)

if __name__ == '__main__':
    main()