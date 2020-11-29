import zipfile

CharList = 'abcdefghijklmnopqrstuvwxyz'
complete = []

for current in range(5):
        a = [i for i in CharList]
        for x in range(current):
             a = [y + i for i in CharList for y in a]
        complete =  complete + a
print(len(complete))
print(len(CharList))
    
z = zipfile.ZipFile('file.zip')
k=10


for password in complete:
    
    try:
        z.setpassword(password.encode('ascii'))
        z.extract('file.txt')
        print(f"Password is : {password}")
        break
    except:
        pass


