

def csr_Str(m,k):
    i=0
    RStr=""
    for l in m:
        RStr+=("\n".join(m[(i+k)%len(m)]))
        i+=1
    return RStr

AZ="abcdefghijklmnopqrstuvwxyz"
alphabets=[]
Wheel_1=0
Wheel_2=0
Wheel_3=0
Turner=0;II=0
for i in range(0,26):
        Wheel_1+=1
        if(Wheel_1 >= 26):
            for i in range(0,26):
                Wheel_2+=1
                for i in range(0,26):
                    if(Wheel_2 >= 26):
                        Wheel_3+=1
                        Turner = (Turner + Wheel_3) % len(AZ)
                        alphabets.append(csr_Str(AZ,Turner))
                        II+=1
                    III=II%3
# alphabets # outputs all enciphered alphabets, from bcde...yza, to nopq...klm (including, abcde..xyz)
# alphabets[0] # get specifically alphabet: bcdefghijklmnopqrstuvwxyza
#alphabets[0][0] # get the first letter of alphabet: bcdefghijklmnopqrstuvwxyza which is: b
csr_Str(alphabets[3],9)# enciphering the alphabet: klmnopqrstuvwxyzabcdefghij 
                   # with key 9 into:
                    # ['t',
                    #  'u',
                    #  'v',
                    #  'w',
                    #  'x',
                    #  'y',
                    #  'z',
                    #  'a',
                    #  'b',
                    #  'c',
                    #  'd',
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
                    #  's']
# Now, let's encrypt a message using one of these, many - many different enciphered alphabets.

# as always, we will define our  function for alphabetical substitution
def asub(m,Alphabet,
         SubAlphabet):
    
    res=""
    out = m.maketrans(Alphabet,SubAlphabet)
    result = m.translate(out)
    res+=result
    return(res) 
normal_alphabet="abcdefghijklmnopqrstuvwxyz"
reversed_alphabet=normal_alphabet[::-1]
# asub("hello world!",normal_alphabet,reversed_alphabet)# svool dliow!  ->| Dec "svool dliow!" into
# asub("svool dliow!",normal_alphabet,reversed_alphabet)# hello world!  <-| <-

# Okay,
MSG1="hello world!"
asub(MSG1,
     (csr_Str(alphabets[3],9)),
     (csr_Str(alphabets[9],20)))

# -> outputs -> 
# lipps asvph!

MSG1="lipps asvph!"
asub(MSG1,
     (csr_Str(alphabets[9],20)),
     (csr_Str(alphabets[3],9)))
     
# -> outputs -> 
# hello world!

text="hello"
ciphertext_1=asub(text,
     (csr_Str(alphabets[9],20)),
     (csr_Str(alphabets[3],9)))
ciphertext_2=csr_Str(asub(text,
     (csr_Str(alphabets[3],1)),
     (csr_Str(alphabets[8],2))),3)

#(ciphertext_2,ciphertext_1)[0]# ciphertext n. 1             # vyrov
#(ciphertext_2,ciphertext_1)[1]# ciphertext n. 2             # dahhk
#(ciphertext_2,ciphertext_1)    #both ciphertexts, 1 and 2.  # ('vyrov', 'dahhk')
BRUTE=0;IJ=0;JI=0
KEY=0

for i in range(0,len("abcdefghijklmnopqrstuvwxyz")):
    print(csr_Str(asub("basotpyrkazxw"[::-1]+"vuqnmljihgfedc",(csr_Str(alphabets[IJ],KEY)),(csr_Str(alphabets[JI],KEY%33)) ),BRUTE))
    BRUTE+=1;KEY+=1
    IJ+=1
    JI+=1

# output #
# 
# wxzakryptosabvuqnmljihgfedc
# xzakryptosabvuqnmljihgfedcw
# zakryptosabvuqnmljihgfedcwx
# akryptosabvuqnmljihgfedcwxz
# kryptosabvuqnmljihgfedcwxza
# ryptosabvuqnmljihgfedcwxzak
# yptosabvuqnmljihgfedcwxzakr
# ptosabvuqnmljihgfedcwxzakry
# tosabvuqnmljihgfedcwxzakryp
# osabvuqnmljihgfedcwxzakrypt
# sabvuqnmljihgfedcwxzakrypto
# abvuqnmljihgfedcwxzakryptos
# bvuqnmljihgfedcwxzakryptosa
# vuqnmljihgfedcwxzakryptosab
# uqnmljihgfedcwxzakryptosabv
# qnmljihgfedcwxzakryptosabvu
# nmljihgfedcwxzakryptosabvuq
# mljihgfedcwxzakryptosabvuqn
# ljihgfedcwxzakryptosabvuqnm
# jihgfedcwxzakryptosabvuqnml
# ihgfedcwxzakryptosabvuqnmlj
# hgfedcwxzakryptosabvuqnmlji
# gfedcwxzakryptosabvuqnmljih
# fedcwxzakryptosabvuqnmljihg
# edcwxzakryptosabvuqnmljihgf
# dcwxzakryptosabvuqnmljihgfe
