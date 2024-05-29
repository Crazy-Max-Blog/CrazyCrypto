class Data:
    bd={
        "users":{},
        "chats":{},
    }
    
    def userIsExists(self, name):
        if name in self.bd["users"].keys():
            return True
        return False
        
    def userIsValid(self, nick, key):
        if not self.userIsExists(nick):
            return False
        if self.bd["users"][nick]["key"]==key:
            return True
        return False
    
    def createUser(self, nick, key):
        if self.userIsExists(nick):
            return "User already exists"
        self.bd["users"][nick]={}
        self.bd["users"][nick]["key"]=key
    
    def chatIsExists(self, name):
        if name in self.bd["chats"].keys():
            return True
        return False
        
    def chatIsValid(self, nick, key):
        if not self.chatIsExists(nick):
            return False
        if self.bd["chats"][nick]["key"]==key:
            return True
        return False
    
    def createChat(self, nick, key, name, ckey, save=False):
        if not self.userIsValid(nick, key):
            return 'Admin not valid'
        if self.chatIsValid(name, ckey):
            return 'Chat is valid'
        self.bd["chats"][name]={"creator":nick, "key":ckey, "users":{}, "msgs":[]}
        if save:
            self.bd["users"][nick]["chats"].append([name])
        self.addedToChat(nick, key, name, ckey)
        self.modUser(nick, key, name, ckey, nick, 'rw')
            
    def getUsers(self, nick, key, name, ckey):
        if not self.userIsValid(nick, key):
            return 'Admin not valid'
        if not self.chatIsValid(name, ckey):
            return 'Chat not valid'
        return self.bd["chats"][name]["users"]
        
    def modUser(self, nick, key, name, ckey, user, mod):
        if not self.userIsValid(nick, key):
            return 'Admin not valid'
        if not self.chatIsValid(name, ckey):
            return 'Chat not valid'
        if not self.userIsExists(user):
            return 'User not exists'
        self.bd["chats"][name]["users"][user]=mod
        
    def userInChat(self, nick, key, name, ckey):
        if not self.userIsValid(nick, key):
            return 'User not valid'
        if not self.chatIsValid(name, ckey):
            return 'Chat not valid'
        if nick in self.bd["chats"][name]["users"]:
            return True
        return False
        
        
    def addedToChat(self, nick, key, name, ckey):
        if self.userInChat(nick, key, name, ckey):
            return 'User already in chat'
        if not self.userIsValid(nick, key):
            return 'User not valid'
        if not self.chatIsValid(name, ckey):
            return 'Chat not valid'
        self.bd["chats"][name]["users"][nick]=''
        
    def addMsg(self, nick, key, name, ckey, msg):
        if not self.userIsValid(nick, key):
            return 'User not valid'
        if not self.chatIsValid(name, ckey):
            return 'Chat not valid'
        if not self.userInChat(nick, key, name, ckey):
            return 'User not in chat'
        if not 'w' in self.bd["chats"][name]["users"][nick]:
            return 'User not allowed to send msgs'
        self.bd["chats"][name]["msgs"].append({"user":nick, "msg":msg})
        
    def getMsgsNum(self, nick, key, name, ckey):
        if not self.userIsValid(nick, key):
            return 'User not valid'
        if not self.chatIsValid(name, ckey):
            return 'Chat not valid'
        if not self.userInChat(nick, key, name, ckey):
            return 'User not in chat'
        if not 'r' in self.bd["chats"][name]["users"][nick]:
            return 'User not allowed to get msgs'
        return len(self.bd["chats"][name]["msgs"])
        
    def getMsg(self, nick, key, name, ckey, id):
        if not self.userIsValid(nick, key):
            return 'User not valid'
        if not self.chatIsValid(name, ckey):
            return 'Chat not valid'
        if not self.userInChat(nick, key, name, ckey):
            return 'User not in chat'
        if not 'r' in self.bd["chats"][name]["users"][nick]:
            return 'User not allowed to get msgs'
        if id not in range(0, len(self.bd["chats"][name]["msgs"])):
            return 'Msg not exists'
        return self.bd["chats"][name]["msgs"][id]
        
    
        
d=Data()
d.createUser('admin', 'nimda')
d.createChat('admin', 'nimda', 'adminchat', 'tahcnimda')

d.createUser('admin1', '1nimda')
d.addedToChat('admin1', '1nimda', 'adminchat', 'tahcnimda')
d.modUser('admin', 'nimda', 'adminchat', 'tahcnimda', 'admin1', 'rw')
d.addMsg('admin1', '1nimda', 'adminchat', 'tahcnimda', '123')

#>>> d.createUser('admin1', '1nimda')
#>>> d.addedToChat('admin1', '1nimda', 'adminchat', 'tahcnimda')
#>>> d.getUsers('admin', 'nimda', 'adminchat', 'tahcnimda')
#{'admin1': ''}
#>>> d.modUser('admin', 'nimda', 'adminchat', 'tahcnimda', 'admin1', 'rw')
#>>> d.getUsers('admin', 'nimda', 'adminchat', 'tahcnimda')
#{'admin1': 'rw'}
#>>> d.getMsgs('admin1', '1nimda', 'adminchat', 'tahcnimda')
#{}
#>>> d.addMsg('admin1', '1nimda', 'adminchat', 'tahcnimda', '123')
#>>> d.getMsgs('admin1', '1nimda', 'adminchat', 'tahcnimda')
#{'0': {'user': 'adminchat', 'msg': '123'}}

d.addMsg('admin1', '1nimda', 'adminchat', 'tahcnimda', '456')
d.addMsg('admin', 'nimda', 'adminchat', 'tahcnimda', 'CrazyTest')

def r(url):
    return url.split("?")[1].replace("=", "='").replace("&", "', ")+"'"
    
def c(u):
    s=u.split('?')[0]
    return s#[(max(s.rindex('/'), s.rindex(chr(92)))):]

def dcmd(u):
    print(f"d.{c(u)}({r(u)})")
    #try:
    #    print(f"d.{c(u)}({r(u)})")
    #except:
    #    pass

