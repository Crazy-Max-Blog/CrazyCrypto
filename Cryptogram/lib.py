import random

class CrazyCrypto:
    key=''
    
    #def __init__(self):
    #    pass
    
    def __init__(self, nkey=''):
        self.key=nkey
    
    def setKey(self, nkey):
        self.key=nkey
        
    def crypt(self, val):
        return self._crypt(self.key, val)
                
    def decrypt(self, val):
        return self._decrypt(self.key, val)

    def _crypt(self, k, b):
        random.seed(k)
        s=b
        n=''
        u=[]
        while len(u)!=len(s):
            i=random.randint(0,len(s)-1)
            if i not in u:
                u.append(i)
                n+=s[i]
        #print(n)
        return n
    
    def _decrypt(self, s, b):
        random.seed(s)
        s=b
        n=[' ' for _ in s]
        u=[]
        k=0
        while k in range(len(s)):
            i=random.randint(0,len(s)-1)
            if i not in u:
                u.append(i)
                n[i]=s[k]
                k+=1
        r=''
        for i in n:
            r+=i
        #print(r)
        return r