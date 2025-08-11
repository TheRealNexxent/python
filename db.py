class Database:
    "Simulates a basic user database"
    def __init__(self):
        self.data = {} #In memory Database
    
    def add_user(self, userid, name):
        if userid in self.data:
            raise ValueError("Already exists")
        self.data[userid] = name
    
    def get_user(self, userid):
        return self.data.get(userid, None)
    
    def delete_user(self, userid):
        if userid in self.data:
            del self.data[userid]
    