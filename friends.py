# Coder: Gil
# Roblox Friend Api Online Checker

import requests
import json

class Friends:
    def __init__(self, userid):
        self.userid = userid
    
    def getfriendlist(self):
        response = requests.get('https://friends.roblox.com/v1/users/' + self.userid + '/friends?userSort=Alphabetical')
        json_data = json.loads(response.text)
        myfriends = json_data
        list_ofriends = []
        for i in range(len(myfriends['data'])):
            if myfriends['data'][i]['isOnline']:
                list_ofriends.append(myfriends['data'][i]['name'] + " => " + "is Online")
            else:
                list_ofriends.append(myfriends['data'][i]['name'] + " => " + "is Offline")
        else:
            return list_ofriends

if __name__ == '__main__':
    prompt = input("Enter your Roblox user-id: ")
    user = Friends(prompt)
    mfl = user.getfriendlist()
    for i in mfl:
        print(i)