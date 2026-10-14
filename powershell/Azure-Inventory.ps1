$ErrorActionPreference = "Stop"

if (-not (Get-Command Get-AzResource -ErrorAction SilentlyContinue)) {
    throw "Az PowerShell module is required."
}

Get-AzResource |
    Select-Object Name, ResourceType, ResourceGroupName, Location |
    Sort-Object ResourceGroupName, ResourceType
