p = ['x','y','z','w','v']
operationsList = ["divde by scaler (ds)", "multiply by scaler (ms)", "multiply by vector (m)", "add another vector (a)", "subtract another vector (s)"]

# def setUpProp(self):
#     d = len(self.v)
#     for i in range(d):
#         while True:
#             try:
#                 print("\nvector." + p[i] + " = ?")
#                 num = input()
#                 self.v[p[i]] = float(num)
#                 break
#             except TypeError:
#                 print("numbers only")
                


def setUpProp(self):
    c = False
    d = len(self.v)
    for i in range(d):
            if c == True: return
            print("\nvector." + p[i] + " = ?")
            num = input()
            self.v[p[i]] = eval(num)
            # if num.isnumeric(): 
            #     self.v[p[i]] = num
            # else:
            #     print("numbers only")
            #     c = True
            #     setUpProp(self)

class vector:
    def __init__(self, d):
        self.v = {}
        for i in range(d):
            self.v.update({p[i] : 0})
        setUpProp(self)

def s(a):
    print("\nVector B is now being created. please list the cords")
    d = len(a.v)
    b = vector(d)
    n = []
    for i in range(d):
        cord = p[i]
        n.append(float(a.v[cord]) - float(b.v[cord]))
    print("\nanswer:")
    print(str(n) + '\n')
     
def ds(a):
    print("\nThe scaler you would like to divide the vector by:")
    d = len(a.v)
    b = input()
    n = []
    for i in range(d):
        cord = p[i]
        n.append(float(a.v[cord]) / float(b))
    print("\nanswer:")
    print(str(n) + '\n')

vectorOperations = {
     "s" : s,
     "ds" : ds
}