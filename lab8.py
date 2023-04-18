s = input('Vvedite stroku \n')
flag=1
string=''
for i in range(len(s)):
    if s[i]!='':
        string+=s[i]
print(string)
for i in range(len(s)//2):
    if string[i]!=string[-i-1]:
        flag=0
        break
if flag: print('Palindrom')
else: print('Ne palindrom')

#team work
print("Hi Aiym!")
print("How are you doing?")
