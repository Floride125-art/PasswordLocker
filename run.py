#!/usr/bin/env python3.6
from passLocker import User, Credential
def create_user(username, password):
    '''
    function to create a user
    '''
    user = User(username,password)
    return user

def save_user(user):
    '''
    function to save a user
    '''
    user.save_user()

def list_users():
    '''
    function to display all users
    '''
    return User.list_users()
def user_checker(username,password):
    '''
    to check if user exist
    '''
    user_checker = Credential.user_checker(username,password)
    return user_checker

def create_credential(username,password,account_name):
    '''
    creating new account credential
    '''
    credential = Credential(username,password,account_name)
    return credential

def save_credential(credential):
    '''
    saving account credential
    '''
    credential.save_credential()

def delete_credential(credential):
    '''
    deleting an account credential
    '''
    credential.delete_credential()
def search_credential(credential):
    '''
    searching a certain account credential
    '''
    return Credential.search_credential(credential)

def view_all_credential():
    '''
    viewing all accounts credentials
    '''
    return Credential.view_all_credential()

def generate_password():
    '''
    generating a random password for a use
    '''
    password = generate_password()
    return password

def creadential_checker(credential):
    '''
    to check if credentials are true
    '''
    return Credential.creadential_checker(credential)
def main():
    print("Hey, welcome to password Locker!")  
    print('='*45)
    print("Please choose among the following in order to proceed:\n c ---------- Create an account \n s ---------- Signin for an existing account \n")
    print('='*45)
    abbreviation = input().lower()
    print('='*45)
    if abbreviation == 'c':
        print('='*45)
        print("Create an account in PASSWORD LOCKER")
        print('='*45)
       