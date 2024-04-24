#Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a, 
#или Impossible, если операций потребуется более 1000.

s = input()
a = input() 
b = input()

n=0
result = 0
while (n<1000):
    if a == b and a in s:
        result = 'Impossible'
        n = 1000
    elif a == b and a not in s:
        result = 0
        n = 1000

    else:
        s = s.replace(a, b)
        result +=1
        n +=1
        if a not in s:
            n = 1000
            
print (result)           
        
            



