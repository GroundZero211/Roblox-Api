# Coder: Gil
# Roblox Api online

class User():
    def __init__(self, userid):
        self.userid = userid

    def userStatus(self):
        response = requests.get('https://api.roblox.com/users/'+ str(self.userid) + '/onlinestatus/')
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
        response = requests.get('https://friends.roblox.com/v1/users/' + str(self.userid) + '/friends?userSort=Alphabetical')
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
    import requests
    import json

    try:
        prompt = int(input('Enter your user-id: '))
        user = Friends(prompt)
        print(user.userStatus())
    except ValueError:
        print('Userid must be an Integer/number')
