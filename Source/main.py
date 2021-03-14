import requests
import colorama
from colorama import Fore
colorama.init(autoreset=True)
logo = """
 _                _    
| |              | |   
| |     ___  __ _| | __
| |    / _ \/ _` | |/ /
| |___|  __/ (_| |   < 
\_____/\___|\__,_|_|\_\\
"""
logoo = """
 _____                 _ 
/  ___|               | |
\ `--.  ___  _   _  __| |
 `--. \/ _ \| | | |/ _` |
/\__/ / (_) | |_| | (_| |
\____/ \___/ \__,_|\__,_|
"""
print(Fore.GREEN+f"{logo}\n{logoo}")
print(Fore.GREEN+"\t\t[Leak Soud]\nCheck If Your Email Is Breached or Leaked\n\t\tCredit: _agf - Soud#0737")
head = {
	"Host": "identityprotection.avast.com",
	"Vaar-Header-App-Product-Name": "hackcheck-web-avast",
	"Accept": "application/json, text/plain, */*",
	"Vaar-Version": 0,
	"Vaar-Header-App-Product": "hackcheck-web-avast",
	"Accept-Language": "en-us",
	"Accept-Encoding": "gzip, deflate, br",
	"Content-Type": "application/json;charset=utf-8",
	"Origin": "https://www.avast.com",
	"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
	"Vaar-Header-App-Build-Version": "1.0.0",
	"Referer": "https://www.avast.com/hackcheck",
	"Connection": "keep-alive"
	}
	
url = "https://identityprotection.avast.com/v1/web/query/site-breaches/unauthorized-data"

email = input("Enter Your Email: ")

data = {
	"emailAddresses" : [
		email
		]
}

req = requests.post(url, json=data, headers=head)
if '{"breaches":{"' and '"data":{"' in req.text:
	print(Fore.RED+f"Leaked Email: {email}")
	
elif '{"breaches":{},"data":{},' in req.text:
	print(Fore.GREEN+f"[+] No Breach Found: {email}")

else:
	print(Fore.YELLOW+"Something Went Wrong!")
	print(f"Response: [~~ {req.text} ~~]")
	print(Fore.YELLOW+"\nTry Again Later.")

# Soud Was Here 
