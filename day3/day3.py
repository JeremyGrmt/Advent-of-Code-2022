alph = 'abcdefghijklmnopqrstuvwxyz'
for i in len(alph):
    

ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def function1():
    with open('day3input.txt', 'r') as data_file:
        for line in data_file:
            half1 = line[:len(line)//2]
            half2 = line[len(line)//2:]


            print(half1)
            print(half2 + "\n")
    return half1
    
        
def finditem(string1, string2):

