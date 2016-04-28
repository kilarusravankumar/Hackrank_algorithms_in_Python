import sys
global posCount
global negCount
global oCount

def integerTypes(arr):
    posCount=0
    negCount=0
    oCount=0
    for digit in arr:
        if digit>0:
            #print digit
            posCount+=1
            #print posCount
        elif digit<0:
            negCount+=1
        else:
            oCount+=1
            #print posCount,negCount
    return [posCount,negCount,oCount]
    
    
n=int(raw_input())
arr=map(int,raw_input().split())
#array_len=len(arr)
#print arr

posCount,negCount,oCount=integerTypes(arr)

print '{0:.6f}'.format(float(posCount)/n),
print '{0:.6f}'.format(float(negCount)/n),
print '{0:.6f}'.format(float(oCount)/n)