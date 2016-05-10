import sys

def findPeak(arr):
    if len(arr)%2==0:
        nhalf=len(arr)/2
    else:
        nhalf=(len(arr)-1)/2
    if arr[nhalf]<=arr[nhalf+1]:
        findPeak(arr[nhalf:])
    elif arr[nhalf]<=arr[nhalf-1]:
        findpeak(arr[:nhalf])
    else:
        print "peak is ",arr[nhalf]
        
n=int(raw_input())
arr=map(int,raw_input().split())

findPeak(arr)
#end
