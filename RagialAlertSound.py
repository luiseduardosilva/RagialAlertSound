# Python 3.x
# Github: 
#	- github.com/luiseduardosilva
import requests, re, time, os
# Install requests
# python -m pip install requests

# URL Item
# Strawberry(Morango) -> http://ragi.al/item/iRO-Classic/QgI
url = "http://ragi.al/item/iRO-Classic/QgI"

# Requesição | Request
req = requests.get(url)

vending_now = re.search(r'asd Now', req.text)

while True:
	if req.status_code == 200:
		try:
			print(vending_now.group())

			# Diretório do Audio | Audio Directory
			os.system("start C:\\ragial\\ragial.mp3")
			# 10 seconds delay
			time.sleep(10)
		except:
			time.sleep(10)
			pass
	else:
		print("Erro 404!")
