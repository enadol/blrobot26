# blrobot26

## Tools
- Added `tools/install_winscp.ps1` — downloads portable WinSCP into `tools\winscp` (no admin required). Run:

  `powershell -ExecutionPolicy Bypass -File tools\install_winscp.ps1`

  `upload_db.bat` will prefer `tools\winscp\winscp.com` if present; otherwise it falls back to the Python uploader (`upload_db.py`).