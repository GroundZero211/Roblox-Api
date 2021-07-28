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
        list_ofriends = [myfriends['data'][i]['name'] + " => " + "is Online" if myfriends['data'][i]['isOnline'] else myfriends['data'][i]['name'] + " => " + "is Offline" for i in range(len(myfriends['data']))]
        return list_ofriends

if __name__ == '__main__':
    prompt = input("Enter your Roblox user-id: ")
    user = Friends(prompt)
    mfl = user.getfriendlist()
    for i in mfl:
        print(i)
