import random
import string


code_set=['A','D','F','G','V','X']
character_set="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
character_set=list(character_set)
# print(character_set,len(character_set))

cipher_matrix={}

def best_random():
    while character_set:
        index = random.randrange(len(character_set))
        elem = character_set[index]
        # direct deletion, no search needed
        del character_set[index] 
        return elem

for first in code_set:
    for second in code_set:
        cipher_matrix[best_random()]=first+second

print(cipher_matrix,len(cipher_matrix))
# test=list(cipher_matrix.values())
# print(sorted(test),len(test))

file=open("sample.txt","r+")
cipher=open("encrypted.txt","w")
cipher_len=0

with file as f:
    for char in f.read():
        if (char.isalpha() or char.isdigit()):
            char=char.upper()
            cipher.write(cipher_matrix[char])
            cipher_len+=2
        else:
            # cipher_len+=1
            continue
         


key=input("Enter the character key\nThe key should contain only alphabets of length<100\n")
if key.isalpha()==False:
    print("Invalid key!\nTry Again")
    exit(0)    

key_len=len(key)
key=list(key)
sort_key=sorted(key)
column_size=cipher_len//key_len
print(column_size)
cipher.close()
encrypted=open("encrypted.txt","r+")

with encrypted as f:
    while i in range(column_size):

