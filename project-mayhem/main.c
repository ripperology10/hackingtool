#include <stdio.h>

struct HOST_INFO{
    char VERSION[100];
    char HARDWARE[100];
    char OS_RELEASE[100];
};

//DATABASE
// WINDOWS
int uac_MSchedExe(){

}
// LINUX & UNIX

//ANDROID

//APPLE

/* SANITY CHECK
    --WE NEED TO SCAN FOR OPERATING SYSTEM.
*/
int HOST_SCAN(){
    struct HOST_INFO HOST;
    //uname(&HOST);
    //OPERATING SYSTEM: SYSTEM_INFO = popen("systeminfo", "r");
    #ifdef _WIN32


        printf("WINDOWS 32");
    #elif _WIN64
        printf("WINDOWS 64");
    #elif __APPLE__
        #include "TargetConditionals.h"
        if TARGET_OS_IPHONE
            printf("Iphone");
    #elif __ANDROID__
        printf("ANDROID");
    #elif __unix__
        printf("UNIX");
    #elif __linux__
        printf("LINUX");
    #endif
}
//DATABASE

/*
 FIRST STAGE:
  Silent_Breakin(): < escalate privilege without notifiying antimalwares or-
  UAC.
  Siege(): < Turns off defenses(including firewall via siege tower) or UAC-
  via Battering Ram and tries to destroy anti-malware by checking if the
  application is vulnerable to a vulnerability, if not check the system host
  for possible vulnerability, if it exist. Deploy one and use it for System
  level Integrity.
*/


int SILENT_BREAKIN(){
    system("echo a");//"taskschd.msc");
}

//IGNORE THIS:
int main(){
    SILENT_BREAKIN();
    HOST_SCAN();
    printf("test");
    return 0;
}
