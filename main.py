import time,httpx,re,json,random,websocket
from random import randint as r
from faker import Faker
from hcapbypass import bypass
from threading import Thread

fake = Faker()
Xsuper = '4D042846D708CA694E202DE23AB2EFBD60518747C9888E1134A1C8FC914E3CE56F48AFA0F6ADD111A3F8D543AD07FA03E8875E0E81A3AA99E447A9616A0ECA64EE7B7C6AAB699D09549CBF6B480B72E9BA332D9FFCB0FC5346C58EA32A9B813C37A64A177F6CB0E864DDE3DFB347DE57292BF979BEFAC04ED151C6D8E2303ECB2723044ABB561F24EF3C6520EFFFFA7A66EC716ED08AB7454CFB5CDDF600EED5B22A390040E3359288EB767709CE4BBD79BC791B02C6D3B10A6FDF6E10BFACE2B2D60BB4D692DDDDD1F9F12A4CAABDF9F92C67EC89EF75D10843256D3877F5E3DA5F71641C548BDD7C9C4AD9EF6FE0EE3F3CBE20B9EB3621383FAEC510EF0AFD0F21CA5D5D3320B9725A45A7C2D362861DD4A22C9B3970C6B271D9B14157218ABA63AB7D5ADE34E171FAE6059549B5EB16B50FB23D7F23AC49F14B4C4171171C8F403BB3F26686156983BAF7370526F4A6345D83D8C1CAD8086759BABA0110780DAE6A569EBD7503D504D23B5F7D56ED933507135C2EE93D348C691AB4BC3393CAA526638A119E51844BFB5DAC956D6498BEE540A4DD7A51A64761225B5AE479BCEC59536C89489D5FA64BA56A1C0569FF8D05CBB8A29C0B88D13B385CF23B252CBFE34364547909215E7E2F7478CD3F4F050E0755953F6BCFF7BF2885EDB39E6C310DD7E1C59F127EB01A03A233EE1AC02BD1EA8D6D9D0E0635CEDCD9A4F75C5BC6498F41D81012D990077032AD7BB40CF4C78FB15B6EBFE6691C5DB27820D734A2DE28C3C1B368DB8BA8F40F71F630238FC932D42C5DF2288E099BBE964BD47F1F9729AFF11B03AEA0D8607784BF396FCB6108DDB49D51FF5A4179CE29CE9FF853A645'




class gen():
	def __init__(self):
		pass

	





	def register(x,y,fingerprint,username,email,captchakey,proxy,id):
		


		headers={
			"Host": "discord.com",
			"Connection": "keep-alive",
			"sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
			"X-Super-Properties": Xsuper,
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
			"Cookie": f"__dcfduid={x}; __sdcfduid={y}",

		}

		body={
			'fingerprint':fingerprint,
			'username':username,
			'email':email,
			'password':'PassTh1s!',
			'consent':'true',
			'date_of_birth':'2003-04-13',
			"gift_code_sku_id": "",
			"captcha_key": captchakey

		}

		tries = 0

		


		while True:

			try:
				r = httpx.post("https://discord.com/api/v9/auth/register",headers=headers,json=body,timeout=30,proxies=proxy)
				token = r.json()['token']
				
			except KeyError:
				return('err')

				time.sleep(60)
				register(x,y,fingerprint,username,email,captchakey,proxy,id)
				
			else:
				return token
		
		




	def captcha(proxy,id):
		print(f'{[id]} Attempting to Bypass Captcha')
		key = bypass("4c672d35-0701-42b2-88c3-78380b0db560", "discord.com", proxy)
		return key



	def fingerprint(proxy,id):
		print(f'{[id]} Generating Fingerprint...')
		
		r = httpx.get("https://discord.com/api/v9/experiments", timeout=10,proxies=proxy)

		if r.text == "":
			print(f'{[id]}Failed to get fingerprint')
			raise Exception
		else:
			print(f'{[id]} Got Fingerprint')
			fingerprint = r.json()['fingerprint']
			
			return fingerprint


	def cookies(proxy):
		headers={
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
			"Accept-Language": "en-us,en;q=0.9"
		}

		r = httpx.get("https://discord.com/register", headers=headers,proxies=proxy).headers['set-cookie']
		

		x = re.findall(r'__dcfduid=(\w+);', r)[0]
		y = re.findall(r'sdcfduid=(\w+);', r)[0]

		if x and y:
			return x,y

	
	def proxy():
		x = open('proxies.txt','r')
		f = random.choice(x.readlines()).strip()
		ip,port,user,passw = f.split(':')
		fproxy = f'http://{user}:{passw}@{ip}:{port}'
		proxy = {
            "http://":fproxy
		}
		return proxy		
	





class run:
	def __init__(self):
		pass
	

	def start(id):
		
		proxy = gen.proxy()
		username = fake.first_name() + str(r(10,99))
		email = username + '@idklol.com'
		x,y = gen.cookies(proxy)
		fingerprint = gen.fingerprint(proxy,id)
		
		
		captchakey = gen.captcha(proxy,id)
		if captchakey:
			print(f'{[id]} Bypassed Captcha!')
		else:
			print(f'{[id]} Failed to pass captcha')

		unverified = gen.register(x,y,fingerprint,username,email,captchakey,proxy,id)
		if unverified:
			while True:
				if unverified == 'err':
					print(f'{[id]} Rate Limited! Retrying in 1min')
					time.sleep(60)
					unverified = gen.register(x,y,fingerprint,username,email,captchakey,proxy,id)
				else:
					print(f'{[id]} Token: {unverified}')
					break




			
		

		




if __name__ == "__main__":
	amt = int(input('Tasks: '))
	amt += 1
	for i in range(amt):
		run.start(i)

	
