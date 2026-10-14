$ErrorActionPreference = "Stop"

Write-Host "Windows infrastructure baseline"
Get-Service WinRM | Select-Object Name, Status
Get-CimInstance Win32_OperatingSystem |
    Select-Object Caption, Version, LastBootUpTime
Get-NetFirewallProfile |
    Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
