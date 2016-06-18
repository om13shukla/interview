from sys import argv
import re
from os.path import exists

script, from_file, to_file = argv

#print ("Copying from %s to %s" % from_file, to_file>> after the processing..!)


with open(from_file) as f:
    lines=f.read().splitlines()

lines.sort()
words=[]

print ("Processing.... ",'\n')

a=len(lines)
lt3=[]

#print('len= ',a)
#print('\n')

            #Read file into a list

for i in range(len(lines)):
    lt3.append(re.findall(r"\A\d+", lines[i]))

print('lt3= ',lt3)
print('\n')

            #optimize the list
for i in range(len(lt3)):
    if not lt3[i]:
        a=a-1
print('len of alphanums = ',a,'\n')

       
            #Seperating nums and words into a list
for i in range(len(lines)):
    words.append(re.findall(r"[^\W\d_]+|\d+", lines[i])) 

            # Part 1 of 2: Alpabetically sorting    
words.sort()

print('words= ',len(words),' =',words)

print('\n')
l1=(len(lines)+(a-len(lines)-1))
print('l1= ',l1)
lt1=[]
for i in range(l1):
    lt1.append(int(words[i][0]))

lt1.sort()

            #Part 2 of 2: Numerical sorting: unique List of nums from input
lt1=list(set(lt1))
lt1.sort()
print('lt1= ',lt1)

            #debug Purpose
for i in range(len(words)):
    print(words[i][0],end=', ')
print('\n')

lt2=[]



            #Combine for result: it All happens here
for i in range(len(lt1)):
    for j in range(l1):
        if(str(lt1[i]) in words[j]):
            lt2.append(' '.join(words[j]))
            print(' ',lt1[i],words[j][0])


print('\n')
l2=(a-len(lines))
print('l2',l2,'\n')


for i in range(l2,0):
    lt2.append(' '.join(words[i]))
    print(' ',words[i])




out_file = open(to_file, 'w')
for i in range(len(lt2)):
    out_file.write(lt2[i])
    out_file.write('\n')

print ("Alright, all done.")

out_file.close()
f.close()

