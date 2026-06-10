import re

email = 'siddharthnm07@gmail.com'
name = 'NM Siddharth'
Mobile = 9611849572
passw = "Siddharth@5069"

pattern = r'^[A-Z]+\s[A-Za-z]+$'
if re.match(pattern, name):
    print(name)
else:
    print("invalid")
    
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+{}|:"<>?~`\-]).{8,25}$'
if re.match(pattern, passw):
    print(passw)
else:
    print("invalid")    
    
name = 27.423423
len_name = len(str(name).replace('.',''))
print(len_name)    