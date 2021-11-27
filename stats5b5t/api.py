import requests

def checkvalid(apicall):
    if apicall.get("success") != None:
        return True

class Statistics:

    def request(self, user):
        try:
            req = requests.get(f"https://api.2b2tlarp.org/user/stats/{(user)}").json()
            return req
        except:
            print("""
-----------------------
Critical Library error.
Err: Module API; class Statistics in function 'request'
An error occurred in the Library.
This is not a bug in your code.
Please open an issue on the github repository.
Sorry for the inconvenience.
-----------------------

""")
            return None

    def raw(self, apicall):
        return apicall

    def uuid(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["uuid"]
            return data
        else:
            return None

    def ratio(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["ratio"]
            return data
        else:
            return None

    def kills(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["kills"]
            return data
        else:
            return None

    def deaths(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["deaths"]
            return data
        else:
            return None

    def joindate(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["joindate"]
            return data
        else:
            return None

    def lastplayed(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["lastPlayed"]
            return data
        else:
            return None

    def leaves(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["leaves"]
            return data
        else:
            return None

    def enderpearls(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["enderPearls"]
            return data
        else:
            return None

    def crystal(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["crystal"]
            return data
        else:
            return None
    
    def damage(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["damage"]
            return data
        else:
            return None

    def damagetaken(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["damageTaken"]
            return data
        else:
            return None

    def mobkills(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["mobkills"]
            return data
        else:
            return None

    def jumps(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["jumps"]
            return data
        else:
            return None

    def timesincedeath(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["timeSinceDeath"]
            return data
        else:
            return None

    def score(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["score"]
            return data
        else:
            return None

    def health(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["health"]
            return data
        else:
            return None

    def playtime(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["playTime"]
            return data
        else:
            return None

    def recordtime(self, apicall):
        if checkvalid(apicall):
            data = apicall["success"]["lastUpdated"]
            return data
        else:
            return None


