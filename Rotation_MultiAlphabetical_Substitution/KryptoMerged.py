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

# Okay, Let's try with a message hello world again, and encrypt it using 
# - a enciphered alphabet specified above, with a key shift.
MSG1="hello world!"
asub(MSG1,
     (csr_Str(alphabets[3],9)),
     (csr_Str(alphabets[9],20)))

# -> outputs -> 
# lipps asvph!

# And let's decrypt this...

MSG1="lipps asvph!"
asub(MSG1,
     (csr_Str(alphabets[9],20)),
     (csr_Str(alphabets[3],9)))
     
# -> outputs -> 
# hello world!

