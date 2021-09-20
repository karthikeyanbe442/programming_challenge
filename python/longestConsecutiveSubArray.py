"""
Tag: Single Window Problem

Given two arrays find the longest consecutive sub array.
Eg:

findConsecutiveSubArray(a,b)

Sample Input:
a = [1,2,3,4,5]
b = [9,7,4,5,10]

Output
[4,5]
"""

a = [1,2,3,4,5]
b = [9,7,4,5,10]
c = []
d = [4,5,4,5,4,5]
e = [4,5]

def findConsecutiveSubArray(a,b):
    finalOutput = []
    tempOutput = []
    for i in range(0,len(a)):
        tempOutput = []
        for j in range(0,len(b)):
            # print(f"[{i},{j}] => [{a[i]},{b[j]}]")
            if(a[i] == b[j]):
                # print("append")
                tempOutput.append(a[i])
                i= i+1
            else:
                if(len(tempOutput) > len(finalOutput)):
                    finalOutput = tempOutput
                    tempOutput = []
            
            if(i >= len(a)):
                break
        if(i >= len(a)):
            break

    
    if(len(tempOutput) > 0 and len(tempOutput) > len(finalOutput)):
        finalOutput = tempOutput
    
    return finalOutput



print(f"a={a}, b={b}, output={findConsecutiveSubArray(a,b)}")
print(f"a={b}, b={a}, output={findConsecutiveSubArray(b,a)}")
print(f"a={a}, b={c}, output={findConsecutiveSubArray(a,c)}")
print(f"a={c}, b={a}, output={findConsecutiveSubArray(c,a)}")
print(f"a={a}, b={a}, output={findConsecutiveSubArray(a,a)}")
print(f"a={a}, b={d}, output={findConsecutiveSubArray(a,d)}")
print(f"a={d}, b={a}, output={findConsecutiveSubArray(d,a)}")
print(f"a={e}, b={d}, output={findConsecutiveSubArray(e,d)}")
print(f"a={d}, b={e}, output={findConsecutiveSubArray(d,e)}")