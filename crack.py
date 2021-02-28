import zipfile
import itertools
from tqdm import tqdm

found = False
file_name = input("Enter the name of the file to be cracked : ")
file_inside = file_name + '.txt'
file_name = file_name + '.zip'
z = zipfile.ZipFile(file_name)

print("Choose The Type of Attack : ")
print("1 : Brute Force Passwords of Length <= 5")
print("2 : Run through famous Password Dictionaries")
print("3 : Personalized Attack.")


type_of_attack = input("Enter the type of attack : ")

if type_of_attack == '1' : 

    print("Preparing Brute Force Attack")
    x = input("The list consists of all the lower case alphabets, would you like to extend the list? y/n : ")
    CharList = 'abcdefghijklmnopqrstuvwxyz'
    
    if x == 'y' or x=='Y' :
        num = int( input("Enter the number of characters : ") )
        for i in range(num):
            entry = input(f"Enter {i+1}th character : ")
            CharList+=entry
    print(f"the final character list is : {CharList}")
    complete = []
    for current in range(4) :
            a = [i for i in CharList]
            for x in range(current) :
                a = [y + i for i in CharList for y in a]
            complete =  complete + a
# print(len(complete))
# print(len(CharList))


    print("New WordList has been created")
    print(f"size of WordList : {len(complete)}")
    print("Trying WordList on the encrypted file...")


    for i in tqdm(complete):
        try:
            z.setpassword(i.encode('ascii'))
            z.extract('f1.txt')
            print(f"Password is : {i}")
            found = True
            break
        except:
            pass
if found == True:
    exit()


if type_of_attack == '2':

    print("Preparing Dictinary Attack!")

    print("Running on Dictionary : Cain and Abel")
    WordList = open('cain.txt','r').read()
    WordList = WordList.splitlines()
    print(f"Length of Cain and Abel : {len(WordList)} ")

    for word in tqdm(WordList):
        try:
            z.setpassword(word.encode('ascii'))
            z.extract('f1.txt')
            # p=True
            print(f' Password is {word}!')
            found = True
            break
        except:
            pass
    if found == True:
        exit()

    print("Running on Dictionary : John The Ripper ")
    WordList = open('john.txt','r').read()
    WordList = WordList.splitlines()
    print(f"Length of John The Ripper : {len(WordList)} ")

    for word in WordList:
        try:
            z.setpassword(word.encode('ascii'))
            z.extract('f1.txt')
            # p=True
            print(f'Password is {word}!')
            found = True
            break
        except:
            pass

    if found == True :
        exit()
        

if type_of_attack == '3' : 
    print("Preparing Personalized Attack")
    keywords = []
    print("User has to enter potential keywords that could have been used in password ")
    n = int(input("Enter the number of input keywords : "))
    for i in range(n):
        key = input(f"Enter {i}th Keyword : ")
        keywords.append(key)
    print("creating passwords from keywords ")
    
    codes=[]
    for i in range(3):
        permutations = itertools.permutations(keywords,i+1)
        # print(permutations)
        for p in permutations:
            word=""
            for i in p:
                word = word + i
            codes.append(word)

    print(f"{len(codes)} passwords have been created")
    print("Attack is in progress")
    for word in codes:
        try:
            z.setpassword(word.encode('ascii'))
            z.extract(file_inside)
            # p=True
            print(f'Password is {word}!')
            found = True
            break
        except:
            pass

    if found == True :
        exit()
    print("Password Not Found")

    



