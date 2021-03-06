import os

clear = lambda: os.system('cls')

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()

white = fg("white")
green = fg("green")
red = fg("red")
yellow = fg('yellow')

banner = white + """
   ____    ____        _  __     _                     __  
  / __ \  |___ \__   _(_)/ /_   | |__   ___ _ __ ___   \ \ 
 / / _` |   __) \ \ / / | '_ \  | '_ \ / _ \ '__/ _ \ (_) |
| | (_| |  / __/ \ V /| | (_) | | | | |  __/ | |  __/  _| |
 \ \__,_| |_____| \_/_/ |\___/  |_| |_|\___|_|  \___| (_) |
  \____/            |__/                               /_/ 

"""

print(banner + '             -  Shortlink By @2vj6 | inuts7#5742  !')

link = str(input("\n[" + red + 'x' + white + '] inter the link u wana Short : '))

name_link = str(input("[" + red + 'x' + white + '] inter the name u want : '))

url = 'https://v.ht/processreq.php'

headers = {
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8,he;q=0.7',
	'Connection': 'keep-alive',
	'Content-Length': '85',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Host': 'v.ht',
	'Origin': 'https://v.ht',
	'Referer': 'https://v.ht/',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-origin',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest'
}

data = {
	'txt_url': link,
	'txt_name': name_link
}
#bad = 'oops errormsg' , good = 'You can make sure, it's properly working by'
shr = requests.post(url=url, headers=headers, data=data)

if "You can make sure, it's properly working by" in shr.text:
    shortned_link = 'https://v.ht/' + name_link
    print("[" + red + 'x' + white + "] it's successfully shortned !")
    print("[" + red + 'x' + white + f'] your link is [' + red + f'{shortned_link}' + white + '] , Enjoy !')
    input("[" + red + 'x' + white + "] Prees Enter to exit !")
    exit()
elif 'oops errormsg' in shr.text:
    print("[" + red + 'x' + white + "] The Name u chosed is used , try another one please !")
    input("[" + red + 'x' + white + "] Prees Enter to exit !")
    exit()
else:
    print("[" + red + 'x' + white + "] Something went wrong , try again later !")
    input("[" + red + 'x' + white + "] Prees Enter to exit !")
    exit()