class Debugging:

    def isvalid(self, apicall):
        if apicall.get("success") != None:
            return True
        elif apicall.get("err") != None:
            return False

    def missmatch(self, apicall, user):
        if apicall.get("success") != None:
            if apicall["success"]["uuid"] == user:
                return False
            else:
                return True
        else:
            return None

    def errmsg(self, apicall):
        if apicall.get("err") != None:
            return f'{apicall["err"]}'
        else:
            return "No error message provided. JSON response is valid" 
