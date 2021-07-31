# Coder: Gil
# Roblox Api online
import os
import requests
import json
import time

class User():
    def __init__(self, userid):
        self.userid = userid

    def onlineStatus(self):
        response = requests.get(os.getenv('URL'))
        json_data = json.loads(response.text)
        usr = json_data
        t = (usr['VisitorId'], usr['IsOnline'], usr['LastLocation'], usr['LastOnline'], usr['LocationType'], usr['PresenceType'], usr['PlaceId'], usr['UniverseId'])
        return """
        VisitorId   : {}
        IsOnline    : {}
        LastLocation: {}
        LastOnline  : {}
        LocationType: {}
        PresenceType: {}
        PlaceId     : {}
        UniverseId  : {}
        """.format(*t)

class Friends(User):
    def __init__(self, userid):
        super().__init__(userid)
    
    def getfriendlist(self):
        response = requests.get(os.getenv('URL'))
        json_data = json.loads(response.text)
        myfriends = json_data
        key = list(myfriends.keys())
        if key[0] == 'data' and myfriends[key[0]] == []:
            return "Empty Friends"
        elif key[0] == 'errors':
            return "{} {}".format(myfriends[key[0]][0]['message'], myfriends[key[0]][0]['userFacingMessage'])
        list_ofriends = [myfriends['data'][i]['name'] + " => " + "is Online" if myfriends['data'][i]['isOnline'] else myfriends['data'][i]['name'] + " => " + "is Offline" for i in range(len(myfriends['data']))]
        return list_ofriends

if __name__ == '__main__':
    prompt = int(input("Enter userId: "))
    while True:
        try:
            user = User(prompt)
            print(user.onlineStatus())
            time.sleep(10)
        except ValueError:
            print('UserId must be an Integer/number')

