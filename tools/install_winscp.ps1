<#
Downloads the portable WinSCP ZIP and installs it into tools\winscp (no admin required).
Usage: powershell -ExecutionPolicy Bypass -File tools\install_winscp.ps1
#>
param(
    [switch]$Force
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$dest = Join-Path $scriptDir 'winscp'
if (-not (Test-Path $dest)) { New-Item -ItemType Directory -Path $dest -Force | Out-Null }

$zipUrl = 'https://winscp.net/download/winscp.zip'
$zipPath = Join-Path $env:TEMP 'winscp_portable.zip'

Write-Host "Downloading WinSCP portable from $zipUrl..." -ForegroundColor Cyan
try {
    Invoke-WebRequest -Uri $zipUrl -OutFile $zipPath -UseBasicParsing -ErrorAction Stop
} catch {
    Write-Error "Download failed: $_"
    exit 1
}

Write-Host "Extracting archive to $dest..." -ForegroundColor Cyan
try {
    Expand-Archive -LiteralPath $zipPath -DestinationPath $dest -Force
} catch {
    Write-Error "Extraction failed: $_"
    exit 1
}

# Locate winscp.com inside extracted files and ensure it's at the root of $dest
$winscpCom = Get-ChildItem -Path $dest -Recurse -Filter 'winscp.com' -ErrorAction SilentlyContinue | Select-Object -First 1
if ($winscpCom) {
    $targetPath = Join-Path $dest 'winscp.com'
    if ($winscpCom.FullName -ne $targetPath) {
        Copy-Item -Path $winscpCom.FullName -Destination $targetPath -Force
    }
    Write-Host "WinSCP installed to: $dest" -ForegroundColor Green
    Write-Host "Executable: $targetPath" -ForegroundColor Green
    Write-Host "Run: .\upload_db.bat (it prefers tools\\winscp\\winscp.com if present)"
    Remove-Item $zipPath -Force -ErrorAction SilentlyContinue
    exit 0
} else {
    Write-Error "winscp.com not found in the downloaded archive."
    exit 1
}