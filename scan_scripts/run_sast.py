import os

print("[+] Running Semgrep scan...")
os.system('semgrep --config=p/ci ./pygoat')
