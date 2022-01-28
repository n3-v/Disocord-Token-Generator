import regex as re
import httpx,time


twocap = ''

def create():
	
	header1 = {
        "Host": "discord.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "Upgrade-Insecure-Requests": "1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-us,en;q=0.9",
    }
	cookies = httpx.get("https://discord.com/register", headers=header1).headers['set-cookie']

	x = re.findall(r'__dcfduid=(\w+);', cookies)[0]
	y = re.findall(r'sdcfduid=(\w+);', cookies)[0]


	res = httpx.get("https://discord.com/api/v9/experiments", timeout=15)
	if res.text == "":
		return True
		print()
	else:
		fingerprint = res.json()['fingerprint']
	print(fingerprint)

	solver = httpx.post(f'http://2captcha.com/in.php?key={twocap}&method=hcaptcha&sitekey=4c672d35-0701-42b2-88c3-78380b0db560&pageurl=discord.com&json=1')
	solverid = solver.json()['request']
	time.sleep(20)

	getcaptcha = httpx.get(f'http://2captcha.com/res.php?key={twocap}&action=get&id={solverid}')

	captchakey = getcaptcha.json()['request']
	print(captchakey)


'''
	
	headers2 = {

        "Host": "discord.com",
        "Connection": "keep-alive",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "X-Super-Properties": "eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85Mi4wLjQ1MTUuMTMxIFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiI5Mi4wLjQ1MTUuMTMxIiwib3NfdmVyc2lvbiI6IjEwLjE1LjciLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTI3OTIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9",
        "X-Fingerprint": fingerprint,
        "Accept-Language": "en-US",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Content-Type": "application/json",
        "Authorization": "undefined",
        "Accept": "*/*",
        "Origin": "https://discord.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://discord.com/register",
        "X-Debug-Options": "bugReporterEnabled",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": f"__dcfduid={x}; __sdcfduid={y}"

    }
    body = {
    	'fingerprint':fingerprint,
		'username':user,
		'password':'PassTh1s!',
		'consent':'true',
		'date_of_birth':'2003-04-13'
		"gift_code_sku_id": "",
		"captcha_key": captchakey,

	}
	req = httpx.post("https://discord.com/api/v9/auth/register",headers=headers2,json=body, timeout=10)

	token = req.json()['token']

	if req.response == 200:
		print(token)
	else:
		break

'''




create()
