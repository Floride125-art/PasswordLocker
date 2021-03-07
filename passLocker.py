import random
class User:
    '''
    create a user class
    '''
    users = []
    def __init__(self,username,password):
            '''
            generate new instance of a class user
            '''

            self.username = username
            self.password = password
    def save_user(self):
            '''
            function to save a user credentials
            '''
            User.users.append(self)
    @classmethod #This means you can use the class and its properties inside that method rather than a particular instance.
    def list_users(cls):
            '''
            method to display all credentials
            '''
            return cls.users
    def delete(self):
        '''
        delete credential
        '''
        User.users.remove(self)