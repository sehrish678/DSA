
n=10
m=4

class Solution(object):
    def differenceOfSums(self, n, m):
     num1=0
     num2=0
     for i in range(1,n+1):
        if(i%m!=0):
            num1=i+num1
        if(i%m==0):
            num2=i+num2
     return num1-num2
            
        