from colarama import Fore, Back, Style, init
import cmd
import socket
import requests
from bs import BeautifulSoup
import mechanicalsoup
from urlib.parse import urljoin
init()
#####################################################
##-------------TOOLS --- FUNCTIONS-----------------##
#####################################################


#####################################################
##--------------sherlock -- Holmes ----------------##
#####################################################
def sherlock_logo():
  
   print(r""" 
   ,'' 'V''-.
  /          \                  -                  --
  |.   _..--'-.,               / SHERLOCK HOLMES:
  >,  /(     |\                    A WAY TO GO DETECTIVE FOR INVESTIGATION.
      `)____ /-.
       |-- \    \ J /
          
   """) 
    
def xss_scan(url, headers):
  payload = "<script>alert<1);</script>;
  browser = mechanicalsoup.Browser();
  page = browser.get(url,headers=headers);
  html = page.soup;
  form = html.select("form")[0];
  for inputs in form.select("input") or form.select("textarea"):
    inputs["value"] = payload;
    xss = browser.submit(form, page.url);
  if payload in xss.content.decode():
    print(f"[*] XSS Detected on {url}");
  else:
    try:
      xss = browser.get(url+"?"+form.select("select")[0]["name"]+"="+payload);
    except:
      print("This tool can't detect DOM yet, it's in it's early form at best.);
            

def lfi_scan(url, headers):
    browser = mechanicalsoup.Browser();
    page = browser.get(url+"../../etc/passwd",headers=headers);
    html = page.soup;
    if "root:" in html.content.decode():
        print(f"[*] LFI Detected on {url}");
#######################################################################################################################  
#                Page 1
####################################################################################################################### 
def menu():
    print(Fore.GREEN+""" 
[m]===========================================
[+] dexter.py --enumeration/forensic
[+] sherlock.h --info gather/vulnscan
[+] cheat.c --exploit/payload
[+] atom_net --reverse assembly / binary vuln
[m]===========================================
    """+Style.RESET_ALL)

print(Fore.BLUE+r"""
        /--------
         \\m@shell\
          \\_______\
          /-}}-}}-/
            // //
        Welcome to Microshell
    Dedicated to David Linus Lieberman From
            The Punisher.
"""+Style.RESET_ALL)

class shell(cmd.Cmd):
    prompt = '$:'
    #########################################################
    #-----Dexter.py----------------#                        #
    #=Enumerations and Forensics.  #                        #
    #########################################################
    def do_dexter(self, line):                              #
        args = line.split('-');                             #
        for arg in args:                                    #
            print(arg);                                     #
    #########################################################################################
    #-----Sherlock.H----------------#                                                       #
    #=tools for info gather that in-#                                                       #
    #includes a person. also a vuln-#                                                       #
    #scan mostly OWASP.             #                                                       #
    #########################################################################################
    def do_sherlock(self,line):                                                             #
        sherlock_logo();                                                                    #
        args = line.split();                                                                #
        for arg in args:                                                                    #
            if "vuln_scan:": in arg:                                                        #
                comment = args[args.index("vuln_scan:")+1];                                 #
                headers = None; dicts = {};                                                 #
                try:                                                                        #
                  headers = arg[args.index(comment)+1];                                     #
                  headers = headers.split(",");                                             #
                                                                                            #
                  for i in headers:                                                         #
                    i = i.replace("{", ""); i = i.replace("}", "");                         #
                    i = i.replace("'", ""); i = i.replace("'", "");                         #
                    i = i.split(":");                                                       #
                    dicts = [i[0]] = i[1];                                                  #
                except:                                                                     #
                    print("Found no headers sir.");                                           #
                if headers != None:                                                         #
                   arg = arg.replace("vuln_scan:", "");                                     #
                   xss_scan(comment);                                                       #
    #########################################################################################
            #--Port Scanning                   #
            #################################################################################
                if "port:" in arg:                                                          #
                    comment = args[args.index("port:")+1];                                  #
                    arg = arg.replace('port:', "");                                         #
                    for port in range(1, 10):                                               #
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);           #
                        result = sock.connect_ex((comment, port));                          #
                        if result == 0:                                                     #
                            print("port:"+str(port)+"STATUS: ONLINE");                      #
                        else:                                                               #
                            print("port"+str(port)+"STATUS: OFFLINE");                      #
    #########################################################################################
    def emptyline(self):                        ####
        pass;                                   ####
####################################################
shell().cmdloop();
