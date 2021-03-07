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
    def test_save_user(self):
        '''
        to test if user is saved
        '''
        self.user.save_user()
        self.assertEqual(len(User.users),1)
class Credential_Test(unittest.TestCase):
    '''
    class to test a credential class
    '''
    def setUp(self):
        '''
        function that runs before
        '''
        self.credential = Credential('Twitter','Floride','fofo123')

    def test_init(self):
        """
        test to check if a new Credentials has been created correctly
        """
        self.assertEqual(self.credential.account_name,'Twitter')
        self.assertEqual(self.credential.user_name,'Floride')
        self.assertEqual(self.credential.account_password,'fofo123')   

    def save_credential_test(self):
        """
        test if the credential  is saved .
        """
        self.credential.save_credential()
        self.assertEqual(len(Credential.credentials),1) 


    def tearDown(self):
        '''
        method that clean after each test runned.
        '''
        Credential.credentials = []

