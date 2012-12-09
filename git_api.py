'''
Created on 09.12.2012

@author: Jury Golovan
'''
from __future__ import print_function
from libsaas.services import github

    
def get_auth(auth_login, auth_password):
    # use basic authentication to create a token for libsaas
    basic = github.GitHub(auth_login, auth_password)
    auth = basic.authorizations().create({'scopes': 'repo,gist',
                                      'note': 'libsaas example'})
    # use token authentication for the rest of the calls
    gh = github.GitHub(auth['token'])
    return gh

def get_following(gh):
    # i'm following for
    following_list = []
    print("i'm following for:")
    for following in gh.user().following():
        following_list.append(following['login'])
    return following_list

def get_followers(gh, usernames):
    for name in usernames:
        following_followers = []
        print(name + "  his followers:")
        for followers in gh.user(name).followers():
            following_followers.append(followers['login'])           
        for followers in following_followers:
            print('  ' + followers)            
        

get_followers(get_auth('login', 'password'), get_following(get_auth('login', 'password')))