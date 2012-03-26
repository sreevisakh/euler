#! /usr/bin/env/ python
sum1 = 0
sum2 = 0
result = 0
for s in range(1,101,1):
    
    sum1 += s*s
    sum2 += s

print sum1,sum2*sum2
result = sum1 - (sum2*sum2)
print result

