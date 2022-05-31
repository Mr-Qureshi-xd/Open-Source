def main_apv():
    os.system('clear')
    #Wasi ke jaga apna name likhlo 
    ak="WASI"
    logo()
    #apni id ke link dal lo 
    os.system('xdg-open https://www.Facebook.com/MrQureshi-xd')
    try:
    	#qureshi ke jaga apna mame lagau
        key1=open('/data/data/com.termux/files/usr/bin/.qureshi-cov', 'r').read()
    except IOError:
        os.system("clear")
        logo()
        print ("[*]--------------------------------------------------------------")
        print ("  Your Token Is Not Approved Already")
        print ("[*]--------------------------------------------------------------")
        print ("           THIS TOOL IS PAID RS 150")
        print ("           THIS IS YOUR KEY BRO")
        print ("[*]--------------------------------------------------------------")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid)
        print ("[*]--------------------------------------------------------------")
        #qureshi ke jaga apna name or kch ni cherna
        kok=open('/data/data/com.termux/files/usr/bin/.qureshi-cov', 'w')
        kok.close()
        print ("")
        print ("")
        print ("     Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print ("[*]--------------------------------------------------------------")
        time.sleep(6)
        #nichy number ki hata k apna numbr dal lo 
        os.system("xdg-open https://wa.me/+923118933642")
        #nichy  link hata k apni github ke link lagau
    r1=requests.get("https://pastebin.com/raw/GUgkVAWC").text
    if key1 in r1:
    	#R ke jaga apne main jahan sy script started krna chahty wo lagao 
        R()
    else:
        os.system("clear")
        os.system('xdg-open https://youtube.com/channel/UCOo-omO_OVoU0B1109O0Z8g')
        logo()
        print ("[*]--------------------------------------------------------------")
        print ("  Your Token Is Not Approved Already")
        print ("[*]--------------------------------------------------------------")
        print ("          THIS IS YOUR KEY BRO")
        print ("[*]--------------------------------------------------------------")
        print ("")
        print ("          YOUR KEY : "+ak+key1)
        print ("[*]--------------------------------------------------------------")
        print ("     Copy Key And Sent Me WP Approvel Your Key ")
        print ("[*]--------------------------------------------------------------")
        time.sleep(3.5)
        #Numbr chnge krlyna
        os.system("xdg-open https://wa.me/+923118933642")