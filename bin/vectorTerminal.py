import bin.graphics
import time
import os
g=bin.graphics

p = ['x','y','z','w','v']



def openCache(type='r'):
    loco = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    loco = loco.replace("/bin", "") + "/cache/vectorCache.txt"
    cacheFile = open(loco, type)
    return cacheFile

def varCache():
    s = []
    cache = openCache()
    lines = cache.readlines()
    # for line in lines:
    #     cache.readline(line)
    return s


def reset():
    cache = openCache(type='w')
    cache.write("")
    cache.close()
    print("\nvector cache cleared\n")

def printCache():
    cache = openCache()
    print(cache.read())
    cache.close()

functions = {
    "reset" : reset,
    "print" : printCache,
}

def load():
    pass

class vector:
    name = str
    d = int
    coords = {}
    def __init__(self, n):
        self.name = n
    def append(self):
        cache_w = openCache('w')
        cache_w.writelines([self.name + "->" + str(self.coords) + "\n"])
        cache_w.close()
        


def newVector(name):
    print("\nhow many dimensions:")
    v = vector(name)

    def askForD():
        i = input()
        if not i.isdigit():
            print("\nwhat you submitted was not a valid int. please try again:")
            askForD()
        v.d = int(i)
    askForD()
   
    def askForCoord(c):
        print("")
        print(c + "=")
        i = input()
        if not i.isdigit():
            print("\nthat is not a valid float. try again")
            askForCoord(c)
        v.coords[c] = i

    for i in range(v.d):
        askForCoord(p[i])
    v.append()




#this should be a method      
class vectorTerminal():
    def __init__(self, var):
        if var in functions:
            functions[var]()
        elif var in varCache():
            print("you found me in cache!")
        else:
            print("\nopening vector operations panel\n")
            load()
            #this means its meant to set a varible as a vector
            newVector(var)
 
    def reload():
        pass
