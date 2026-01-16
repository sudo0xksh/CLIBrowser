import sys
import requests

print("=========================================")
print("Welcome to Cli Browser")

if(len(sys.argv) < 2):
    print("Usage: python cli_browser.py https://target")
    sys.exit()

target = sys.argv[1]

response = requests.get(target)

print("Target: ", target)
print("Status Code: ", response.status_code)
print(response.text)

print("=========================================")
print("Thanks for using cli browser")
print("Developed by sudo_0xksh")
exit()