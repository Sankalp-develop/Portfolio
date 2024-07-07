import json
import os

def  validateuser(username ,password):
    current_directory = os.getcwd()
    print(current_directory)
    with open("static/styles/userconfig.json", 'r') as file:        
        data = json.load(file)
        for user in data['users']:
            if user['username'] == username and user['password'] == password:
                return True
    return False


def register_newuser(username,email,password):
    with open('userconfig.json', 'r+') as file:
        data = json.load(file)
        data['users'].append({"username": username, "password": password , "email" : email})
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
        return True;
    return False;