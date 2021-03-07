import unittest
from passLocker import User, Credential
class User_Test(unittest.TestCase):
    '''
    class to test an user class
    '''
    def setUp(self):
        '''
        function that runs before
        '''
        self.user = User('Floride','Tuyisenge')