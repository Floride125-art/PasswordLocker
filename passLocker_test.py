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
        self.user = User('Floride','fofo123')
    def test_init(self):
        '''
        to check if user is correctly created
        '''
        self.assertEqual(self.user.username,'Floride')
        self.assertEqual(self.user.password,'fofo123')
