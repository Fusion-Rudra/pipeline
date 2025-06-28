import os

print("[+] Running Secrets scan using Gitleaks...")
os.system('gitleaks detect --source ./pygoat --report-format json --report-path gitleaks_report.json')
