#! /usr/bin/env python

def find(number):
    
    i = 999
    j = 999
    cords=[]
    for i in range(999,100,-1):
        for j in range(i,100,-1):
            a = i*j
            #print i,' * ',j,'=',a
            b = str(a)
            if b[:int(len(b)/2)] == b[int(len(b)/2):][::-1]:
                print i,j
                cords.append(i*j)
    print max(cords)                
           
        
    
number = 997799
find (number)

