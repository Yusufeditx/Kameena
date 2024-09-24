
from urllib import response
import mechanize
import os
import datetime
import sys
from time import sleep
print(' JOIN TELEGRAM ')
os.system('xdg-open https://t.me/trickerxx7')
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [
    ('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)
url = 'https://m.facebook.com/login.php'

def clear():
    if os.name == 'nt':
        os.system('cls')
        return None
    None.system('clear')


def sp(stri):
    for letter in stri:
        print(letter, end = '')
        sys.stdout.flush()
        sleep(0.03)
        return None

logo = '              |$$  \  /$$/ $$ |  $$ |/$$$$$$  |$$ |  $$ |$$$$$$$$/ $$  \/$$/  $$ |  $$ |$$ \__$$/ $$ |  $$ |$$ |__    $$  $$/   $$ |  $$ |$$      \ $$ |  $$ |$$    |    $$$$/    $$ |  $$ | $$$$$$  |$$ |  $$ |$$$$$/        $$ |    $$ \__$$ |/  \__$$ |$$ \__$$ |$$ |      $$ |    $$ \__$$ |/  \__$$ |$$ \__$$ |$$ |      $$ |    $$    $$/ $$    $$/ $$    $$/ $$ |        $$/      $$$$$$/   $$$$$$/   $$$$$$/  $$/          [1;34;40m.     YUSUF BRAND HERE \n\x1b[1;34;40m     HATTER KI MAA KI XHUT\n\x1b[1;34;40m      YUSUF KIDZ OPEN SOURCE'

def menu():
    os.system('clear')
    print(logo)
    print('[1] Random Uid Crack')
    print('[2] Contact To Owner')
    print('[0] Exit')
    print('-----------------------------------------------')
    opt = input('[?] Choose : ')
    if opt == '1':
        md()
        return None
    if None == '2':
        Contact()
        return None
    if None == '0':
        exit()
        return None
    None('\n\x1b[1;31mChoose valid option\x1b[0;97m')
    menu()


def login():
    browser.open(url)
    browser.select_form(nr = 0)
    browser.form['email'] = USERNAME
    browser.form['pass'] = PASSWORD
    r = browser.submit()
    f = open('login.html', 'wb')
    f.write(r.read())
    f.close()


def findtextchat(curl):
    r = browser.open(curl)
    x = browser.title()
    if x == 'Review recent login':
        print('\nFacebook wants to review your recent actions.\nPlease fix that and then re run the program.')
        exit(1)
    if x == 'Login approval needed':
        print('\nYour account is stuck on verification\nPlease do it and then re run the program.')
        exit(1)
    if x == 'Epsilon':
        print('\nYour account got locked, recover it kindly and re run the script.')
        exit(1)
        return None


def sendtextconvo(comment):
    browser.select_form(nr = 1)
    if mechanize._mechanize.FormNotFoundError:
        print('Some error occured while finding text area, please check your account')
        exit(1)
    browser.form['body'] = comment
    if mechanize._form_controls.ControlNotFoundError:
        print('Some error occured while filling text, please check your account')
        exit(1)
    r = browser.submit()
    e = datetime.datetime.now()
    print('\x1b[1;35;40m', end = '')
    print(e.strftime('Ha Chla Gya Tera Msg :: Date - %d/%m/%Y  Time - %I:%M:%S %p'))
    print('>> Jake Soja Tatte Ki Maa Chudti Rhegi :: ', line, '\n')

print('\x1b[1;33;40m', end = '')
os.system('clear')
print(logo)
sp('\x1b[1m\x1b[36m[+] Login With Email/Number \n')
print('\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-')
USERNAME = str(input('[?] Enter Email/Number : '))
print('\x1b[1;33;40m', end = '')
print('\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-')
sp('\x1b[1m\x1b[36m[+] Enter Your Facebook Password\n')
print('\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-')
PASSWORD = str(input('[?] Enter your password : '))
login()
print('\x1b[1;34;40m', end = '')
print('\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-')
sp('\x1b[1m\x1b[36m[?] Enter Chat/inbox Link\n')
print('\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-')
cid = str(input('\x1b[1;37;1m[?] Enter Link : '))
curl = 'https://m.facebook.com/messages/t/' + str(cid)
print('\x1b[1;34;40m', end = '')
print('\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-')
sp('\x1b[1m\x1b[36m[?] Enter Notepad File Name\n')
print('\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-')
np = str(input('\x1b[1;37;1m[?] Enter File Name : '))
f = open(np, 'r')
lines = f.readlines()
f.close()
print('\x1b[1;33;40m', end = '')
print('\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-')
sp('\x1b[1m\x1b[36m[?] Enter The Time Delay In Seconds\n')
print('\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-\x1b[1;35;40m-')
t = int(input('\x1b[1;37;1m[?] Enter Time : '))
os.system('clear')
print(logo)
count = 0
for line in lines:
    if len(line) > 3:
        if count != 0:
            sleep(t)
        findtextchat(curl)
        sendtextconvo(line)
        count += 1
        if count % 10 == 0:
            sleep(1)
            clear()
            print('\x1b[0;37;41m\n')
