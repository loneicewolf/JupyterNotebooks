# csr but with lambda.

csr = lambda m,k:[ord(m[(i+k)%len(m)])for i in range(0,len(m))]
#m="llo world!he" # used for decrypt example.
m="hello world!" # used for encrypt example.

#print(csr(m,2))
#outputs #
# [108, 108, 111, 32, 119, 111, 114, 108, 100, 33, 104, 101]
ix=0
for i in range(0,len(m)):
    print( chr( csr(m,2)[ix]),end="")# encrypt: "hello world!" -> "llo world!he"
    #print( chr( csr(m,-2)[ix]),end="")# decrypt: "llo world!he" -> "hello world!"
    ix+=1
