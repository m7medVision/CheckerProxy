import requests
from colorama import Fore
r = requests.Session()

def check(prox):
	link = 'http://instagram.com/'
	r.proxies = {
	'http':'http://{}'.format(prox),
	'https':'http://{}'.format(prox)
	}
	try:
		req = r.get(link,timeout=100)
		if req.status_code == 200:
			print(Fore.LIGHTGREEN_EX+"Proxy Work [{}]".format(prox))
			with open('working.txt','a') as wr:
				wr.write(prox+'\n')
		else:
				print(Fore.YELLOW +"blocked proxy [{}]".format(prox))
	except:
		print(Fore.LIGHTRED_EX+"Bad Proxy [{}]".format(prox))
proxies=open('proxies.txt', 'r').read().splitlines()
from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(13)
results = pool.map(check, proxies)
