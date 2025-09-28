import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat 
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

''' To match the END string'''
# pattern = re.compile(r'T$')   # $ -> End of the string
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)
    
''' To match digits'''    
# pattern = re.compile(r"\d")
# matches1 = pattern.finditer(text_to_search)
# for match in matches1:
#     print(match)    

''' To match a Phone number'''
# pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
# pattern = re.compile(r'\d{3}\.\d{3}\.\d{4}')  # To match the dot ('.') we need to use \ before writing '.' 
# matches2 = pattern.finditer(text_to_search)

# for match in matches2:
#     print(match)    

''' To match a Phone number with - and . as a separator'''
# pattern = re.compile(r'\d{3}[-\.]\d{3}[-\.]\d{4}') 
# matches2 = pattern.finditer(text_to_search)

# for match in matches2:
#     print(match)  
    

''' To match a phone number starting with 800 & 900'''
# pattern = re.compile(r'[89]\d{2}[-.]\d{3}[-\.]\d{4}') 
# matches2 = pattern.finditer(text_to_search)

# for match in matches2:
#     print(match)  
    
 
''' To match all the words ending with 'at' but not 'bat' '''
# pattern = re.compile(r'[^b]at')
# matches2 = pattern.finditer(text_to_search)

# for match in matches2:
#     print(match)  


''' To match the names that starts with 'Mr' '''
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')  # Here ?( 0 or 1 occurences) is used to make '.' optional. '*' ( 0 or more occurences )
# matches2 = pattern.finditer(text_to_search)

# for match in matches2:
#     print(match)  


''' To match the names that starts with 'Mrs' or 'Ms' or 'Mr' '''
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')  
matches2 = pattern.finditer(text_to_search)

for match in matches2:
    print(match)  



''' Working with data.txt file'''
# with open('data.txt','r') as f:
#     contents = f.read()
    
#     pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
#     matches3 = pattern.finditer(contents)
    
#     for match in matches3:
#         print(match)    