class Debugging:

    def isvalid(self, apicall):
        if apicall.get("success") != None:
            return True
        elif apicall.get("err") != None:
            return False

    def errmsg(self, apicall):
        if apicall.get("err") != None:
            return f'{apicall["err"]}'
        else:
            return "No error message provided. Json response is valid" 
