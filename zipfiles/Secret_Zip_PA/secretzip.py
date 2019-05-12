# Challenge 1
# See the content of the password protected files


# import zipfile
# z = zipfile.ZipFile('secret.zip')
# z.printdir()
# z.close()



# Challenge 2
# Create a Dict file where a passwords will be generated

# import itertools
# alphabets = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']
# f = open("dict.txt", "w")
# for passlen in [6]:
#     combinations = itertools.product(alphabets, repeat = passlen)
#     for combination in combinations:
#         f.write(''.join(combination)+"\n")



# Challenge 2
# Crack the zip file

import zipfile
cracked = False
z = zipfile.ZipFile("secret.zip")
with open("dict.txt") as f:
    lines = f.readlines()
for password in lines:
    password = password.replace('\n','')
    try:
        z.extractall(pwd=password)
        correct_password = 'Correct password: %s' % password
        cracked = True
        break
    except:
        pass

if cracked:
    print correct_password
else:
    print "Password not found"
