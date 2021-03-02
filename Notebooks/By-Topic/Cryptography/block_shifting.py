

# ------- msg block shifting ------- #

s1="abc"
key=0
i=0
for l in s1:
    current_msgblock=s1
    print (csr(current_msgblock,key))
    key+=1
# ------- msg block shifting ------- #



def csr(m,k):
    i=0
    RL=[]
    for l in m:
        RL.append(m[(i+k)%len(m)])
        i+=1
    return RL


abc="abcdefghijklmnopqrstuvwxyz"
abcrev=abc[::-1] # reverse abc
csr(abcrev[:5:],3),csr(abcrev[::5],3)
# (['w', 'v', 'z', 'y', 'x'], ['k', 'f', 'a', 'z', 'u', 'p'])
# csr(abcrev[:5:],20) # ['z', 'y', 'x', 'w', 'v']
# csr(abc[:5:],3) # ['d', 'e', 'a', 'b', 'c']

# ------- output ------- #

# ['a', 'b', 'c']
# ['b', 'c', 'a']
# ['c', 'a', 'b']
# 
# (['w', 'v', 'z', 'y', 'x'], ['k', 'f', 'a', 'z', 'u', 'p'])


# 
