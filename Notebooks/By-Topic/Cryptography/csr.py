# conv. from jupyter notebook to python code #

# ------- caeser shift ------- #
def csr(m,k):
    i=0
    RL=[]
    for l in m:
        RL.append(m[(i+k)%len(m)])
        i+=1
    return RL
# ------- caeser shift ------- #


# Test

abc="abcdefghijklmnopqrstuvwxyz"
csr(abc,3)

# outputs 

# ['d',
#  'e',
#  'f',
#  'g',
#  'h',
#  'i',
#  'j',
#  'k',
#  'l',
#  'm',
#  'n',
#  'o',
#  'p',
#  'q',
#  'r',
#  's',
#  't',
#  'u',
#  'v',
#  'w',
#  'x',
#  'y',
#  'z',
#  'a',
#  'b',
#  'c']

