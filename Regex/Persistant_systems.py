'''
username, emailid, age, gender, addr, geolocation, passw

username = all alpha
email = @ 
age = number min >20 and max<55
addr= aphanumeric
location =Two 8 digits with floating number ,
passw = special character , uppercase, lowercase,8 min digits and max = 25 digits
'''

import re

class Credentials:
    def __init__(self, username, email, age, address, password, lat_location,long_location):
        self.username = username
        self.email = email
        self.age = age
        self.address = address
        self.password = password
        self.lat_location = lat_location
        self.long_location = long_location
        
    def check_username(self):
        if self.username.isalpha():
            return self.username
        else:
            return "Invalid username"
    
    def check_email(self):
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, self.email):
            return self.email
        return "Invalid emailid"
        
    def check_age(self):
        if isinstance(self.age, int) and 20<self.age<55:
            return self.age
        else:
            return "Invalid age"
        
    def check_addr(self):
        if self.address.isalnum():
            return self.address
        return "Invalid address"
        
    def check_location(self):
        if isinstance(self.lat_location, float) and isinstance(self.long_location, float):
            lat_len = len(str(self.lat_location).replace(".",''))
            long_len = len(str(self.long_location).replace(".",''))
            
            if lat_len == 8 and long_len==8:
                return f"{self.lat_location},{self.long_location}"
        else:
            return "Invalid Latitude and longitude"
        
    def check_passw(self):
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+{}|:"<>?~`\-]).{8,25}$'
        if re.match(pattern, self.password):
            return self.password
        else:
            return "Invalid password"
            
#obj = Credentials("Sid",'sid@gmail.com', 34, 'Bengaluru5600','sid@sda123',28.502412, 77.034564)

def get_input():
    username = input("enter username")
    email = input("enter email")
    age = int(input("Enter age"))
    addr = input("enter addr")
    lat_location = float(input("Enter location"))
    long_location = float(input("Enter location")) 
    passw = input("Enter passw")
    
    return Credentials(username,email,age,addr,lat_location,long_location,passw)

def display(obj):          
    print(obj.check_username())
    print(obj.check_email())       
    print(obj.check_age())       
    print(obj.check_addr())       
    print(obj.check_location())       
    print(obj.check_passw())       
    
       
       
obj = get_input()
display(obj)