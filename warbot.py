#utf_8 *lineX [prankBots Creator]

"""
all of this data is copied from creator production PrankBots
don't forget to always support the prabkbots channel
SUBSCRABE HERE https://bit.ly/2xbVxlh
MY ID LINE :: http://line.me/ti/p/~Adiputra.95
Copy Righ :: http://github.com/Aprank
Country :: INDONESIA.
Response by acil


MENERIMA PEMESANAN SCRIPT
BOT PROTECT
BOT WAR
SELFBOT
BOT OFFICIAL TEMPLATE

PEMBUATAN BOT BEBAS REQUEST COMMANT, MODE BACKUP DLL.
JIKA KAMU MINAT CHAT KE ID LINE
line.me/ti/p/~Adiputra.95
[TIDAK MENERIMA CALL ATAU UNDANGAN GRUP [AUTO REJECET AKTIF]]

BIASAKAN CHAT DENGAN SOPAN WALAWPUN MENGGUNAKAN BAHAS FORMAL (LO,GW)
SELENGEAN ANE GAK RESPON.
YANG MAU KEPOIN GW JUGA BOLEH WKWKWK

"""
from Rank.lineX import *
from Rank.service.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from threading import Thread
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
_session = requests.session()
botStart = time.time()
settingsOpen = codecs.open("PrankBots.json","r","utf-8")
PrankBots = json.load(settingsOpen)
settingsOpen = codecs.open("Abouts.json","r","utf-8")
Abouts = json.load(settingsOpen)
# MASUKIN TOKEN DISINI GUYS
selfbot = "TOKEN"
kicker1 = "TOKEN"
kicker2 = "TOKEN"
kicker3 = "TOKEN"
kicker4 = "TOKEN"
pending = "TOKEN"
"""
PPPPPPPPPPPPPPPPP                                                           kkkkkkkk           BBBBBBBBBBBBBBBBB                             tttt                           
P::::::::::::::::P                                                          k::::::k           B::::::::::::::::B                         ttt:::t                           
P::::::PPPPPP:::::P                                                         k::::::k           B::::::BBBBBB:::::B                        t:::::t                           
PP:::::P     P:::::P                                                        k::::::k           BB:::::B     B:::::B                       t:::::t                           
  P::::P     P:::::Prrrrr   rrrrrrrrr     aaaaaaaaaaaaa   nnnn  nnnnnnnn     k:::::k    kkkkkkk  B::::B     B:::::B   ooooooooooo   ttttttt:::::ttttttt        ssssssssss   
  P::::P     P:::::Pr::::rrr:::::::::r    a::::::::::::a  n:::nn::::::::nn   k:::::k   k:::::k   B::::B     B:::::B oo:::::::::::oo t:::::::::::::::::t      ss::::::::::s  
  P::::PPPPPP:::::P r:::::::::::::::::r   aaaaaaaaa:::::a n::::::::::::::nn  k:::::k  k:::::k    B::::BBBBBB:::::B o:::::::::::::::ot:::::::::::::::::t    ss:::::::::::::s 
  P:::::::::::::PP  rr::::::rrrrr::::::r           a::::a nn:::::::::::::::n k:::::k k:::::k     B:::::::::::::BB  o:::::ooooo:::::otttttt:::::::tttttt    s::::::ssss:::::s
  P::::PPPPPPPPP     r:::::r     r:::::r    aaaaaaa:::::a   n:::::nnnn:::::n k::::::k:::::k      B::::BBBBBB:::::B o::::o     o::::o      t:::::t           s:::::s  ssssss 
  P::::P             r:::::r     rrrrrrr  aa::::::::::::a   n::::n    n::::n k:::::::::::k       B::::B     B:::::Bo::::o     o::::o      t:::::t             s::::::s      
  P::::P             r:::::r             a::::aaaa::::::a   n::::n    n::::n k:::::::::::k       B::::B     B:::::Bo::::o     o::::o      t:::::t                s::::::s   
  P::::P             r:::::r            a::::a    a:::::a   n::::n    n::::n k::::::k:::::k      B::::B     B:::::Bo::::o     o::::o      t:::::t    ttttttssssss   s:::::s 
PP::::::PP           r:::::r            a::::a    a:::::a   n::::n    n::::nk::::::k k:::::k   BB:::::BBBBBB::::::Bo:::::ooooo:::::o      t::::::tttt:::::ts:::::ssss::::::s
P::::::::P           r:::::r            a:::::aaaa::::::a   n::::n    n::::nk::::::k  k:::::k  B:::::::::::::::::B o:::::::::::::::o      tt::::::::::::::ts::::::::::::::s 
P::::::::P           r:::::r             a::::::::::aa:::a  n::::n    n::::nk::::::k   k:::::k B::::::::::::::::B   oo:::::::::::oo         tt:::::::::::tt s:::::::::::ss  
PPPPPPPPPP           rrrrrrr              aaaaaaaaaa  aaaa  nnnnnn    nnnnnnkkkkkkkk    kkkkkkkBBBBBBBBBBBBBBBBB      ooooooooooo             ttttttttttt    sssssssssss    

"""
#__________________________
kk1 = LINE(kicker1)
kk2 = LINE(kicker2)
kk3 = LINE(kicker3)
kk4 = LINE(kicker4)
jss = LINE(pending)
runnerResponse = "\n\nPPPPPPPPPPPPPPPPP\nP::::::::::::::::P\nP::::::PPPPPP:::::P\nPP:::::P     P:::::P\n  P::::P     P:::::P\n  P::::P     P:::::P\n  P::::PPPPPP:::::P\n  P:::::::::::::PP\n  P::::PPPPPPPPP\n  P::::P\n  P::::P\n  P::::P\nPP::::::PP\nP::::::::P\nP::::::::P\nPPPPPPPPPP\n\n\nrrrrr   rrrrrrrrr\nr::::rrr:::::::::r\nr:::::::::::::::::r\nrr::::::rrrrr::::::r\n r:::::r     r:::::r\n r:::::r     rrrrrrr\n r:::::r\n r:::::r\n r:::::r\n r:::::r\n r:::::r\n rrrrrrr\n\n\n  aaaaaaaaaaaaa\n  a::::::::::::a\n  aaaaaaaaa:::::a\n           a::::a\n    aaaaaaa:::::a\n  aa::::::::::::a\n a::::aaaa::::::a\na::::a    a:::::a\na::::a    a:::::a\na:::::aaaa::::::a\n a::::::::::aa:::a\n  aaaaaaaaaa  aaaa\n\n\nnnnn  nnnnnnnnn\nn:::nn::::::::nn\nn::::::::::::::nn\nnn:::::::::::::::n\n  n:::::nnnn:::::n\n  n::::n    n::::n\n  n::::n    n::::n\n  n::::n    n::::n\n  n::::n    n::::n\n  n::::n    n::::n\n  n::::n    n::::n\n  nnnnnn    nnnnnn\n\n\nkkkkkkkk\nk::::::k\nk::::::k\nk::::::k\n k:::::k    kkkkkkk\n k:::::k   k:::::k\n k:::::k  k:::::k\n k:::::k k:::::k\n k::::::k:::::k\n k:::::::::::k\n k:::::::::::k\n k::::::k:::::k\nk::::::k k:::::k\nk::::::k  k:::::k\nk::::::k   k:::::k\nkkkkkkkk    kkkkkkk\n\n\nBBBBBBBBBBBBBBBBB\nB::::::::::::::::B\nB::::::BBBBBB:::::B\nBB:::::B     B:::::B\n  B::::B     B:::::B\n  B::::B     B:::::B\n  B::::BBBBBB:::::B\n  B:::::::::::::BB\n  B::::BBBBBB:::::B\n  B::::B     B:::::B\n  B::::B     B:::::B\n  B::::B     B:::::B\nBB:::::BBBBBB::::::B\nB:::::::::::::::::B\nB::::::::::::::::B\nBBBBBBBBBBBBBBBBB\n\n\n   ooooooooooo\n oo:::::::::::oo\no:::::::::::::::o\no:::::ooooo:::::o\no::::o     o::::o\no::::o     o::::o\no::::o     o::::o\no::::o     o::::o\no:::::ooooo:::::o\no:::::::::::::::o\n oo:::::::::::oo\n   ooooooooooo\n\n\n         tttt\n      ttt:::t\n      t:::::t\n      t:::::t\nttttttt:::::ttttttt\nt:::::::::::::::::t\nt:::::::::::::::::t\ntttttt:::::::tttttt\n      t:::::t\n      t:::::t\n      t:::::t\n      t:::::t    tttttt\n      t::::::tttt:::::t\n      tt::::::::::::::t\n        tt:::::::::::tt\n          ttttttttttt\n\n\n    ssssssssss\n  ss::::::::::s\nss:::::::::::::s\ns::::::ssss:::::s\n s:::::s  ssssss\n   s::::::s\n     s::::::s\n        s:::::s\nssssss   s:::::s\ns:::::ssss::::::s\ns::::::::::::::s\n s:::::::::::ss\n  sssssssssss"
me = LINE(selfbot)
me.log(runnerResponse)
meProfile = me.getProfile()
meSettings = me.getSettings()
kk1Profile = kk1.getProfile()
kk2Profile = kk2.getProfile()
kk3Profile = kk3.getProfile()
kk4Profile = kk4.getProfile()
jssProfile = jss.getProfile()
meM = meProfile.mid
kk1Rank = kk1Profile.mid
kk2Rank = kk2Profile.mid
kk3Rank = kk3Profile.mid
kk4Rank = kk4Profile.mid
jssRank = jssProfile.mid
oepoll = OEPoll(me)
Owner = PrankBots["owner"]
Stiles = "│○"
BotWar = [meM,kk1Rank,kk2Rank,kk3Rank,kk4Rank,jssRank]
allrepositories = [me,kk1,kk2,kk3,kk4,jss]
respontags = {
    "Auto_text": "\nYes I'am Here"
}
Sid={
    "Tar":{},
    "Red":{},
    "Reason":{}
}
mid = me.getProfile().mid
PrankBots["myProfile"]["displayName"] = meProfile.displayName
PrankBots["myProfile"]["statusMessage"] = meProfile.statusMessage
cont = me.getContact(meM)
PrankBots["myProfile"]["pictureStatus"] = meProfile.pictureStatus
coverId = me.getProfileDetail()["result"]["objectId"]
apikey_com = "u0ac948397fbc732bd3bc5ca273faa698"
coverId = me.getProfileDetail()["result"]["objectId"]
PrankBots["myProfile"]["coverId"] = coverId
Extr = me.getContact(apikey_com).displayName
all_Square = ["ub0842532a31b9d99856cf2590b17d33f","udfaf52176415b46cb445ae2757ec85f3","u17a086ccff618e754588a1108335867f","uc8dc5352066b6a344bde3c07b0fe04ea","ub9c30fd47257ec4337ee777657b4df66"]
for busht in allrepositories:
    for anding in all_Square:
        try:
            busht.findAndAddContactsByMid(anding)
        except:pass
    for botKickers in BotWar:
        try:
            busht.findAndAddContactsByMid(botKickers)
        except:pass
def backupData():
    try:
        backup = PrankBots
        f = codecs.open('PrankBots.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = Abouts
        f = codecs.open('Abouts.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        ErrorX(error)
        return False
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@PrankBots "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    me.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def Run_Xp():
    print ("RESTART")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
Devert = "My name is "+cont.displayName+"\nMy git your bots"
def Run_Xx():
    print ("BOT KEMBALI AKTIF")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
mulai = time.time()
def Musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+me.getContact(meM).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': me.getContact(meM).statusMessage if me.getContact(meM).statusMessage != '' else 'creator By meMots |ID LINE|\nadiputra.95', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': me.getContact(meM).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  me.getContact(meM).displayName,}
    return me.sendMessage(to, me.getContact(meM).displayName, contentMetadata, 19)
def ErrorX(text):
    me.log("data: " + str(text))
    time_ = datetime.now()
    with open("Data.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@PrankBots "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    me.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ErrorX(error)
        me.sendMessage(to, "Error\n\n" + str(error))
extras = Stiles+"Creator:by "+Extr+"\n"
def RunTheRun(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,7,25)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = me.getAllContactIds()
        gid = me.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        h = me.getContact(meM)
        me.reissueUserTicket()
        My_Id = "http://line.me/ti/p/"+me.getUserTicket().id
        text += mention+"WAKTU : "+datetime.strftime(timeNow,'%H:%M:%S')+" INDONESIA\n\nMY GROUP : "+str(len(gid))+"\n\nMY FRIEND: "+str(len(teman))+"\n\nTIME VPS : In "+hari+"\n\nᴄʀᴇᴀᴛᴏʀ ʙʏ : ᴘʀᴀɴᴋʙᴏᴛs. ʟɪɴᴇ ᴠᴇʀ.8.14.2\n\nTANGGAL : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n\nTIME RUN : \n • "+bot+"\n\nMY TOKEN : "+str(me.authToken)+"\n\nMY MID : "+h.mid+"\n\nMY ID LINE : "+My_Id
        me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        me.sendMessage(to, "Error :\n" + str(error))
warKey = """_________warbot__________
1. warbot
2. warban
3. warclearban
4. warespon
5. warspeed
6. warstay
7. warout
8. warkick @
9. warkey
______prankBots creator______
"""
def SqL_R(text):
    R_SQL = text.lower()
    if PrankBots["key"] == True:
        if R_SQL.startswith(PrankBots["text"]):
            PrankBotsData = R_SQL.replace(PrankBots["text"],"")
        else:
            PrankBotsData = "Undefined command"
    else:
        PrankBotsData = text.lower()
    return PrankBotsData
def serviceX(rank):
    global groupParam
    opps1 = rank.param1
    opps2 = rank.param2
    opps3 = rank.param3
    try:
        if rank.type == 0:
            return
        if rank.type == 19 or rank.type == 32:
            if meM in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    PrankBots["blacklist"] = True
                    try:
                        kk1.inviteIntoGroup(opps1,[opps3])
                        kk1.kickoutFromGroup(opps1,[opps2])
                        me.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk2.inviteIntoGroup(opps1,[opps3])
                            kk2.kickoutFromGroup(opps1,[opps2])
                            me.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk3.inviteIntoGroup(opps1,[opps3])
                                kk3.kickoutFromGroup(opps1,[opps2])
                                me.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    kk4.inviteIntoGroup(opps1,[opps3])
                                    kk4.kickoutFromGroup(opps1,[opps2])
                                    me.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        jss.acceptGroupInvitation(opps1)
                                        grup = jss.getGroup(opps1)
                                        grup.preventedJoinByTicket = False
                                        jss.updateGroup(grup)
                                        Ti = reissueGroupTicket(opps1)
                                        for all in allrepositories:
                                            all.acceptGroupInvitationByTicket(opps1, Ti)
                                        jss.leaveGroup(opps1)
                                        kk1.inviteIntoGroup(opps1,[opps3])
                                    except:pass
            if kk1Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    PrankBots["blacklist"] = True
                    try:
                        kk2.inviteIntoGroup(opps1,[opps3])
                        kk2.kickoutFromGroup(opps1,[opps2])
                        kk1.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk3.inviteIntoGroup(opps1,[opps3])
                            kk3.kickoutFromGroup(opps1,[opps2])
                            kk1.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk4.inviteIntoGroup(opps1,[opps3])
                                kk4.kickoutFromGroup(opps1,[opps2])
                                kk1.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    me.inviteIntoGroup(opps1,[opps3])
                                    me.kickoutFromGroup(opps1,[opps2])
                                    kk1.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        jss.acceptGroupInvitation(opps1)
                                        grup = jss.getGroup(opps1)
                                        grup.preventedJoinByTicket = False
                                        jss.updateGroup(grup)
                                        Ti = reissueGroupTicket(opps1)
                                        for all in allrepositories:
                                            all.acceptGroupInvitationByTicket(opps1, Ti)
                                        jss.leaveGroup(opps1)
                                        kk2.inviteIntoGroup(opps1,[opps3])
                                    except:pass
            if kk2Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    PrankBots["blacklist"] = True
                    try:
                        kk3.inviteIntoGroup(opps1,[opps3])
                        kk3.kickoutFromGroup(opps1,[opps2])
                        kk2.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk4.inviteIntoGroup(opps1,[opps3])
                            kk4.kickoutFromGroup(opps1,[opps2])
                            kk2.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk1.inviteIntoGroup(opps1,[opps3])
                                kk1.kickoutFromGroup(opps1,[opps2])
                                kk2.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    me.inviteIntoGroup(opps1,[opps3])
                                    me.kickoutFromGroup(opps1,[opps2])
                                    kk2.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        jss.acceptGroupInvitation(opps1)
                                        grup = jss.getGroup(opps1)
                                        grup.preventedJoinByTicket = False
                                        jss.updateGroup(grup)
                                        Ti = reissueGroupTicket(opps1)
                                        for all in allrepositories:
                                            all.acceptGroupInvitationByTicket(opps1, Ti)
                                        jss.leaveGroup(opps1)
                                        kk3.inviteIntoGroup(opps1,[opps3])
                                    except:pass
            if kk3Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    PrankBots["blacklist"] = True
                    try:
                        kk4.inviteIntoGroup(opps1,[opps3])
                        kk4.kickoutFromGroup(opps1,[opps2])
                        kk3.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk1.inviteIntoGroup(opps1,[opps3])
                            kk1.kickoutFromGroup(opps1,[opps2])
                            kk3.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk2.inviteIntoGroup(opps1,[opps3])
                                kk2.kickoutFromGroup(opps1,[opps2])
                                kk3.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    me.inviteIntoGroup(opps1,[opps3])
                                    me.kickoutFromGroup(opps1,[opps2])
                                    kk3.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        jss.acceptGroupInvitation(opps1)
                                        grup = jss.getGroup(opps1)
                                        grup.preventedJoinByTicket = False
                                        jss.updateGroup(grup)
                                        Ti = reissueGroupTicket(opps1)
                                        for all in allrepositories:
                                            all.acceptGroupInvitationByTicket(opps1, Ti)
                                        jss.leaveGroup(opps1)
                                        kk4.inviteIntoGroup(opps1,[opps3])
                                    except:pass
            if kk4Rank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    PrankBots["blacklist"] = True
                    try:
                        kk2.inviteIntoGroup(opps1,[opps3])
                        kk1.kickoutFromGroup(opps1,[opps2])
                        kk4.acceptGroupInvitation(opps1)
                    except:
                        try:
                            kk3.inviteIntoGroup(opps1,[opps3])
                            kk2.kickoutFromGroup(opps1,[opps2])
                            kk4.acceptGroupInvitation(opps1)
                        except:
                            try:
                                kk1.inviteIntoGroup(opps1,[opps3])
                                kk3.kickoutFromGroup(opps1,[opps2])
                                kk4.acceptGroupInvitation(opps1)
                            except:
                                try:
                                    me.inviteIntoGroup(opps1,[opps3])
                                    me.kickoutFromGroup(opps1,[opps2])
                                    kk4.acceptGroupInvitation(opps1)
                                except:
                                    try:
                                        jss.acceptGroupInvitation(opps1)
                                        grup = jss.getGroup(opps1)
                                        grup.preventedJoinByTicket = False
                                        jss.updateGroup(grup)
                                        Ti = reissueGroupTicket(opps1)
                                        for all in allrepositories:
                                            all.acceptGroupInvitationByTicket(opps1, Ti)
                                        jss.leaveGroup(opps1)
                                        me.inviteIntoGroup(opps1,[opps3])
                                    except:pass
            if jssRank in opps3:
                if opps2 in BotWar:
                    pass
                else:
                    PrankBots["blacklist"] = True
                    try:
                        kk1.inviteIntoGroup(opps1,[opps3])
                        kk1.kickoutFromGroup(opps1,[opps2])
                    except:
                        try:
                            kk2.inviteIntoGroup(opps1,[opps3])
                            kk2.kickoutFromGroup(opps1,[opps2])
                        except:
                            try:
                                kk3.inviteIntoGroup(opps1,[opps3])
                                kk3.kickoutFromGroup(opps1,[opps2])
                            except:
                                try:
                                    kk4.inviteIntoGroup(opps1,[opps3])
                                    kk4.kickoutFromGroup(opps1,[opps2])
                                except:
                                    try:
                                        me.inviteIntoGroup(opps1,[opps3])
                                        me.kickoutFromGroup(opps1,[opps2])
                                    except:pass
        if rank.type == 17:
            if opps2 in PrankBots["blacklist"]:
                try:
                    kk1.kickoutFromGroup(opps1,[opps2])
                except:
                    try:
                        kk2.kickoutFromGroup(opps1,[opps2])
                    except:
                        try:
                            kk3.kickoutFromGroup(opps1,[opps2])
                        except:
                            try:
                                kk4.kickoutFromGroup(opps1,[opps2])
                            except:pass
            else:pass
        if rank.type == 13:
            if opp3 in PrankBots["blacklist"]:
                try:
                    kk4.cancelGroupInvitation(opps1,[opps3])
                except:
                    try:
                        kk3.cancelGroupInvitation(opps1,[opps3])
                    except:
                        try:
                            kk2.cancelGroupInvitation(opps1,[opps3])
                        except:
                            try:
                                kk1.cancelGroupInvitation(opps1,[opps3])
                            except:pass
            else:pass
        if rank.type == 26 or rank.type == 25:
            msg = rank.message
            Id = msg.id
            R = msg.to
            D = msg._from
            Proses_message = msg.text
            if Proses_message == "Active" or Proses_message == "active":
                if D in Owner or D in meM:
                    PrankBots["bot"] = True
                    me.sendMessage(R,"Bot active")
                    me.sendMessage(R,"Already Ok "+me.getContact(D).displayName)
                    PrankBots["Conection"] = R
                    Run_Xx()
                    
            if Proses_message == "Non active" or Proses_message == "non active":
                print ("NOTIF BOT NON ACTIVE")
                if D in Owner or D in meM:
                    PrankBots["bot"] = False
                    me.sendMessage(R,"Bot Non Active")
                    me.sendMessage(R,"Ok I'am Turn down "+me.getContact(D).displayName)
                
        if rank.type == 25 or rank.type == 26:
          if PrankBots["bot"] == True:
            msg = rank.message
            text = msg.text
            Id = msg.id
            R = msg.to
            D = msg._from
            Gr = opps1
            OperPrankBotsData = PrankBots["text"].title()
            if PrankBots["key"] == False:
                 OperPrankBotsData = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if D != me.profile.mid:
                        to = D
                    else:
                        to = R
                elif msg.toType == 1:
                    to = R
                elif msg.toType == 2:
                    to = R
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        PrankBotsData = SqL_R(text)
                        if PrankBotsData == Abouts["1"]:
                          if D in Owner or D in meM:
                            Res= extras+Stiles+Abouts["0"]+"\n"
                            Res+= Stiles+"1. "+OperPrankBotsData+Abouts["1"]+"\n"
                            Res+= Stiles+"2. "+OperPrankBotsData+Abouts["2"]+"\n"
                            Res+= Stiles+"3. "+OperPrankBotsData+Abouts["3"]+"\n"
                            Res+= Stiles+"4. "+OperPrankBotsData+Abouts["4"]+"\n"
                            Res+= Stiles+"5. "+OperPrankBotsData+Abouts["5"]+"\n"
                            Res+= Stiles+"6. "+OperPrankBotsData+Abouts["6"]+"\n"
                            Res+= Stiles+"7. "+OperPrankBotsData+Abouts["7"]+"\n"
                            Res+= Stiles+"8. "+OperPrankBotsData+Abouts["8"]+" *porn\n"
                            Res+= Stiles+"9. "+OperPrankBotsData+Abouts["9"]+" *judul\n"
                            Res+= Stiles+"10. "+OperPrankBotsData+Abouts["10"]+" *tags\n"
                            Res+= Stiles+"11. "+OperPrankBotsData+Abouts["11"]+"\n"
                            Res+= Stiles+"12. "+OperPrankBotsData+Abouts["12"]+" *txt/txt/txt\n"
                            Res+= Stiles+"13. "+OperPrankBotsData+Abouts["13"]+" *text\n"
                            Res+= Stiles+"14. "+OperPrankBotsData+Abouts["14"]+"\n"
                            Res+= Stiles+"15. "+OperPrankBotsData+Abouts["15"]+"\n"
                            Res+= Stiles+"16. "+OperPrankBotsData+Abouts["16"]+"\n"
                            Res+= Stiles+"17. "+OperPrankBotsData+Abouts["17"]+"\n"
                            Res+= Stiles+"18. "+OperPrankBotsData+Abouts["18"]+"\n"
                            Res+= Stiles+"19. "+OperPrankBotsData+Abouts["19"]+" *tags\n"
                            Res+= Stiles+"20. "+OperPrankBotsData+Abouts["20"]+" *tags\n"
                            Res+= Stiles+"21. "+OperPrankBotsData+Abouts["21"]+" *tags\n"
                            Res+= Stiles+"22. "+OperPrankBotsData+Abouts["22"]+" *tags\n"
                            Res+= Stiles+"23. "+OperPrankBotsData+Abouts["23"]+" *tags\n"
                            Res+= Stiles+"24. "+OperPrankBotsData+Abouts["24"]+" *tags\n"
                            Res+= Stiles+"25. "+OperPrankBotsData+Abouts["25"]+" *text\n"
                            Res+= Stiles+"26. "+OperPrankBotsData+Abouts["26"]+" *01-02-1995\n"
                            Res+= Stiles+"27. "+OperPrankBotsData+Abouts["27"]+" *id ig\n"
                            Res+= Stiles+"28. "+OperPrankBotsData+Abouts["28"]+" *id smule\n"
                            Res+= Stiles+"29. "+OperPrankBotsData+Abouts["29"]+"\n"
                            Res+= Stiles+"30. "+OperPrankBotsData+Abouts["30"]+" *text\n"
                            Res+= Stiles+"31. "+OperPrankBotsData+Abouts["31"]+" *text\n"
                            Res+= Stiles+"32. "+OperPrankBotsData+Abouts["32"]+"\n"
                            Res+= Stiles+"33. "+OperPrankBotsData+Abouts["33"]+" *text\n"
                            Res+= Stiles+"34. "+OperPrankBotsData+Abouts["34"]+"\n"
                            Res+= Stiles+"35. "+OperPrankBotsData+Abouts["35"]+"\n"
                            Res+= Stiles+"36. "+OperPrankBotsData+Abouts["36"]+"\n"
                            Res+= Stiles+"37. "+OperPrankBotsData+Abouts["37"]+"\n"
                            Res+= Stiles+"38. "+OperPrankBotsData+Abouts["38"]+"\n"
                            Res+= Stiles+"39. "+OperPrankBotsData+Abouts["39"]+"\n"
                            Res+= Stiles+"40. "+OperPrankBotsData+Abouts["40"]+"\n"
                            Res+= Stiles+"41. "+OperPrankBotsData+Abouts["41"]+"\n"
                            Res+= Stiles+"42. "+OperPrankBotsData+Abouts["42"]+"\n"
                            Res+= Stiles+"43. "+OperPrankBotsData+Abouts["43"]+"\n"
                            Res+= Stiles+"44. "+OperPrankBotsData+Abouts["44"]+"\n"
                            Res+= Stiles+"45. "+OperPrankBotsData+Abouts["45"]+"\n"
                            Res+= Stiles+"46. "+OperPrankBotsData+Abouts["46"]+"\n"
                            Res+= Stiles+"47. "+OperPrankBotsData+Abouts["47"]+"\n"
                            Res+= Stiles+"48. "+OperPrankBotsData+Abouts["48"]+"\n"
                            Res+= Stiles+"49. "+OperPrankBotsData+Abouts["49"]+"\n"
                            Res+= Stiles+"50. "+OperPrankBotsData+Abouts["50"]+"\n"
                            Res+= Stiles+"51. "+OperPrankBotsData+Abouts["51"]+"\n"
                            Res+= Stiles+"52. "+OperPrankBotsData+Abouts["52"]+"\n"
                            Res+= Stiles+"53. "+OperPrankBotsData+Abouts["53"]+"\n"
                            Res+= Stiles+"54. "+OperPrankBotsData+Abouts["54"]+"\n"
                            Res+= Stiles+"55. "+OperPrankBotsData+Abouts["55"]+"\n"
                            Res+= Stiles+"56. "+OperPrankBotsData+Abouts["56"]+"\n"
                            Res+= Stiles+"57. "+OperPrankBotsData+Abouts["57"]+"\n"
                            Res+= Stiles+"58. "+OperPrankBotsData+Abouts["58"]+"\n"
                            Res+= Stiles+"59. "+OperPrankBotsData+Abouts["59"]+"\n"
                            Res+= Stiles+"60. "+OperPrankBotsData+Abouts["60"]+"\n"
                            Res+= Stiles+"61. "+OperPrankBotsData+Abouts["61"]+"\n"
                            Res+= Stiles+"62. "+OperPrankBotsData+Abouts["62"]+"\n"
                            Res+= Stiles+"63. "+OperPrankBotsData+Abouts["63"]+"\n"
                            Res+= Stiles+"64. "+OperPrankBotsData+Abouts["64"]+"\n"
                            Res+= Stiles+"65. "+OperPrankBotsData+Abouts["65"]+"\n"
                            Res+= Stiles+"66. "+OperPrankBotsData+Abouts["66"]+"\n"
                            Res+= Stiles+"_____CHECK BOT______\n"
                            if PrankBots["Add"] == True: Res+= Stiles+" autoadd->『on』\n"
                            else: Res+= Stiles+" autoadd->『off』\n"
                            if PrankBots["Shared"] == True: Res+= Stiles+" shared->『on』\n"
                            else: Res+= Stiles+" shared->『off』\n"
                            if PrankBots["Join"] == True: Res+= Stiles+" autojoin->『on』\n"
                            else: Res+= Stiles+" autojoin->『off』\n"
                            if PrankBots["Read"] == True: Res+= Stiles+" autoread->『on』\n"
                            else: Res+= Stiles+" autoread->『off』\n"
                            if PrankBots["Unsend"] == True: Res+= Stiles+" unsend->『on』\n"
                            else: Res+= Stiles+" unsend->『off』\n"
                            if PrankBots["Wc"] == True: Res+= Stiles+" welcome->『on』\n"
                            else: Res+= Stiles+" welcome->『off』\n"
                            if PrankBots["Respon"] == True: Res+= Stiles+" respon->『on』\n"
                            else: Res+= Stiles+" respon->『off』\n"
                            Res+= Stiles+"____________________\n"
                            Res+= Stiles+"______SelfName______\n"+Stiles+meProfile.displayName+"\n"
                            me.sendMessage(apikey_com,Devert)
                            me.sendMessage(R, str(Res)+Stiles+"Subcrabe my Channel\n"+Stiles+" https://bit.ly/2xbVxlh")
                        if PrankBotsData == Abouts["2"]:
                          if D in Owner or D in meM:
                            try:
                                me.findAndAddContactsByMid("ub0842532a31b9d99856cf2590b17d33f")
                                me.findAndAddContactsByMid("udfaf52176415b46cb445ae2757ec85f3")
                                me.findAndAddContactsByMid("u17a086ccff618e754588a1108335867f")
                                me.findAndAddContactsByMid("uc8dc5352066b6a344bde3c07b0fe04ea")
                                Musik(R)
                                RunTheRun(apikey_com, D, "_______RESULT______\n")
                            except:Musik(R)
                        if PrankBotsData == Abouts["3"]:
                          if D in Owner or D in meM:
                            me.reissueUserTicket()
                            My_Id = me.profile.displayName + "My id Line: http://line.me/ti/p/" + me.getUserTicket().id
                            me.sendMessage(R,My_Id)
                        if PrankBotsData == Abouts["4"]:
                          if D in Owner or D in meM:
                            me.leaveGroup(R)
                        if PrankBotsData == Abouts["5"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            cu = me.getProfileCoverURL(D)          
                            path = str(cu)
                            me.sendImageWithURL(R, path)
                        if PrankBotsData == Abouts["6"]:
                          if D in Owner or D in meM:
                            result = requests.get("http://jadwalnonton.com/")
                            data = BeautifulSoup(result.content, 'html5lib')
                            hasil = "_______CINEMA______\nType : Movie List Today\n"
                            no = 1
                            for dzin in data.findAll('div', attrs={'class':'col-xs-6 moside'}):
                                hasil += "\n\n{}. {}".format(str(no), str(dzin.find('h2').text))
                                hasil += "\n     Link : {}".format(str(dzin.find('a')['href']))
                                no = (no+1)
                            me.sendMessage(R, str(hasil))
                        if PrankBotsData == Abouts["7"]:
                          if D in Owner or D in meM:
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(PrankBots["userAgent"])
                                r = web.get('http://api-1cak.herokuapp.com/random')
                                data = r.text
                                data = json.loads(data)
                                img = data["img"]
                                me.sendMessage(R,"━═| Daftar cakcak |═━\n━═| Title: %s\n━═| Link: %s\n━═| Id: %s\n━═| Votes: %s\n━═| NSFW: %s\n━═| [ Finish ] |═━" %(str(data["title"].replace('FACEBOOK Comments', ' ')), str(data["url"]), str(data["id"]), str(data["votes"]), str(data["nsfw"])))
                        if PrankBotsData.startswith(Abouts["8"]):
                          if D in Owner or D in meM:
                            separate = text.split(" ")
                            kata = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(PrankBots["userAgent"])
                                try:
                                    r = web.get("https://api.redtube.com/?data=redtube.Videos.searchVideos&output=json&search={}".format(urllib.parse.quote(kata)))
                                    data = r.text
                                    data = json.loads(data)
                                    ret_ = "━═Bokep inimah"
                                    no = 1
                                    anu = data["videos"]
                                    if len(anu) >= 20:
                                        for s in range(20):
                                            hmm = anu[s]
                                            title = hmm['video']['title']
                                            duration = hmm['video']['duration']
                                            views = hmm['video']['views']
                                            link = hmm['video']['embed_url']
                                            ret_ += "\n━═ {}. \nTitle ━═ {}\nDurasi ━═ {}\nViews ━═ {}\nLink ━═ {}".format(str(no), str(title), str(duration), str(views), str(link))
                                            no += 1
                                    else:
                                        for s in anu:
                                            hmm = s
                                            title = hmm['video']['title']
                                            duration = hmm['video']['duration']
                                            views = hmm['video']['views']
                                            link = hmm['video']['embed_url']
                                            ret_ += "\n━═ {}. \nTitle ━═ {}\nDurasi ━═ {}\nViews ━═ {}\nLink ━═ {}".format(str(no), str(title), str(duration), str(views), str(link))
                                            no += 1
                                    me.sendMessage(R, str(ret_))
                                except:
                                    me.sendMessage(R, "Tidak ditemukan")
                        if PrankBotsData.startswith(Abouts["9"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            title = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(PrankBots["userAgent"])
                                r = web.get("http://www.omdbapi.com/?t="+title+"&y=&plot=full&apikey=4bdd1d70")
                                data=r.text
                                data=json.loads(data)
                                hasil = "╭━━═════[ Hasil pencarian film]"
                                hasil += "\nInformasi ━═| " +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                                hasil += "\nPlot ━═| " +str(data["Plot"])
                                hasil += "\nDirector ━═| " +str(data["Director"])
                                hasil += "\nActors ━═| " +str(data["Actors"])
                                hasil += "\nRelease ━═| " +str(data["Released"])
                                hasil += "\nGenre ━═| " +str(data["Genre"])
                                hasil += "\nTimer ━═| " +str(data["Runtime"])
                                img = data["Poster"]
                                me.sendImageWithURL(R,img)
                                me.sendMessage(R,hasil)
                        if PrankBotsData.startswith(Abouts["10"]):
                          if D in Owner or D in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]                
                            mmid = me.getContact(key1)
                            me.findAndAddContactsByMid(key1)
                            me.sendMessage(R, "teman di tambahkan")
                        if PrankBotsData == Abouts["11"]:
                          if D in Owner or D in meM:
                            me.sendMessage(R, "Selesai.!!")
                            PrankBots["Conection"] = R
                            Run_Xp()
                        if PrankBotsData.startswith(Abouts["12"]):
                          if D in Owner or D in meM:
                            separate = text.split(" ")
                            teks = text.replace(separate[0] + " ","")
                            txt = teks.split("/")
                            bag1 = txt[0]
                            bag2 = txt[1]
                            bag3 = txt[2]
                            angka = ["1","2","3","4","5"]
                            latar = random.choice(angka)
                            nomor = ["1","2","3","4"]
                            background = random.choice(nomor)
                            url = "https://ari-api.herokuapp.com/retro?bg="+latar+"&txt="+background+"&text1="+bag1+"&text2="+bag2+"&text3="+bag3
                            me.sendImageWithURL(R, url)
                        if PrankBotsData.startswith(Abouts["13"]):
                          if D in Owner or D in meM:
                            separate = text.split(" ")
                            teks = text.replace(separate[0] + " ","")
                            url = "https://ari-api.herokuapp.com/led?text="+teks+"&sign=PB"
                            me.sendImageWithURL(R, url)
                        if PrankBotsData == Abouts["14"]:
                          if D in Owner or D in meM:
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = format_timespan(runtime)
                            me.sendMessage(R, "━━━━━╦RUNTIME BOTS╦━━━━━\n ┣━╦[ {}".format(str(runtime)))
                        if PrankBotsData == Abouts["15"]:
                          if D in Owner or D in meM:
                            start = time.time()
                            me.sendMessage(R, "gooo...")
                            elapsed_time = time.time() - start
                            me.sendMessage(R,format(str(elapsed_time)))
                        if PrankBotsData == Abouts["16"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            me.sendMessage(R,h.mid)
                        if PrankBotsData == Abouts["17"]:
                          if D in Owner or D in meM:
                            contact = me.getContact(D)
                            cover = me.getProfileCoverURL(D)
                            result = "╔══[ Details Profile ]"
                            result += "\n╠ Display Name : {}".format(contact.displayName)
                            result += "\n╠ Mid : {}".format(contact.mid)
                            result += "\n╠ Status Message : {}".format(contact.statusMessage)
                            result += "\n╠ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            result += "\n╠ Cover : {}".format(str(cover))
                            result += "\n╚══[ Finish ]"
                            me.sendImageWithURL(R, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            me.sendImageWithURL(R, str(cover))
                            me.sendMessage(R, str(result))
                        if PrankBotsData == Abouts["18"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            me.sendVideoWithURL(R,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                        if PrankBotsData.startswith(Abouts["19"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = ""
                                for ls in lists:
                                    ret_ += "{}".format(str(ls))
                                me.sendMessage(R, str(ret_))
                        if PrankBotsData.startswith(Abouts["20"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.me.naver.jp/" + me.getContact(ls).pictureStatus
                                    me.sendImageWithURL(R, str(path))
                        if PrankBotsData.startswith(Abouts["21"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.me.naver.jp/" + me.getContact(ls).pictureStatus + "/vp"
                                    me.sendVideoWithURL(R, str(path))
                        if PrankBotsData.startswith(Abouts["22"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    me.sendMessage(R, "Namanya\n{}".format(str(contact.displayName)))
                        if PrankBotsData.startswith(Abouts["23"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    me.sendMessage(R, "Status kontak\n\n{}".format(str(contact.statusMessage)))
                        if PrankBotsData.startswith(Abouts["24"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    mi_d = contact.mid
                                    me.sendContact(R, mi_d)
                        if PrankBotsData.startswith(Abouts["25"]):
                          if D in Owner or D in meM:
                            me.sendMessage(R, "Waiting...")
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            params = {"search_query": search}
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(PrankBots["userAgent"])
                                r = web.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╭━━━━━[ Youtube link di tampilkan ]━"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n┣[ {} ]".format(str(data["title"]))
                                    ret_ += "\n┣━ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╰━━━━━━━━[ Total {} link]━━━━━".format(len(datas))
                                me.sendMessage(R, str(ret_))
                        if PrankBotsData.startswith(Abouts["26"]):
                          if D in Owner or D in meM:
                            try:
                                sep = msg.text.split(" ")
                                tanggal = msg.text.replace(sep[0] + " ","")
                                r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                ret_ = "╭━━━━════[Tanggal,Lahir]"
                                ret_ += "\n┣═Tanggal lahir : {}".format(str(data["data"]["lahir"]))
                                ret_ += "\n┣═Umur : {}".format(str(data["data"]["usia"]))
                                ret_ += "\n┣═Tanggal ultah : {}".format(str(data["data"]["ultah"]))
                                ret_ += "\n┣═Zodiak : {}".format(str(data["data"]["zodiak"]))
                                ret_ += "\n╰━━═════[CREATOR PRANKBOTS]"
                                me.sendMessage(R, str(ret_))
                            except Exception as error:
                                logError(error)
                        if PrankBotsData.startswith(Abouts["27"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            instagram = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(PrankBots["userAgent"])
                                html = web.get("https://www.instagram.com/" + instagram + "/")
                                soup = BeautifulSoup(html.text, 'html5lib')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://instagram.com/" + instagram
                                me.sendImageWithURL(R, text1[0])
                                me.sendMessage(R, user + user1 + followers + following + post + link)
                                print("[Notif] Search Instagram Sucess")
                        if PrankBotsData.startswith(Abouts["28"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            smule = "https://www.smule.com/"+ key
                            me.sendMessage(R, "ini id smulenya kak\n" + smule)
                        if PrankBotsData == Abouts["29"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                members = [mem.mid for mem in group.members]
                                me.acquireGroupCallRoute(R)
                                me.inviteIntoGroupCall(R, contactIds=members)
                                me.sendMessage(R, "Berhasil")
                        if PrankBotsData.startswith(Abouts["30"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            say = text.replace(sep[0] + " ","")
                            lang = 'id'
                            tts = gTTS(text=say, lang=lang)
                            tts.save("hasil.mp3")
                            me.sendAudio(R,"hasil.mp3")
                        if PrankBotsData.startswith(Abouts["31"]):
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                X = me.getGroup(R)
                                sep = msg.text.split(" ")
                                X.name = msg.text.replace(sep[0] + " ","")
                                me.updateGroup(X)
                        if PrankBotsData == Abouts["32"]:
                          if D in Owner or D in meM:
                            me.removeAllMessages(opps2)
                            me.sendMessage(R, "Chat deleted")
                        if PrankBotsData.startswith(Abouts["33"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            groups = me.groups
                            for group in groups:
                                sendMessageWithFooter(group, "╭━━━━━╦BroadCast by Self╦━━━━━╮\n{}".format(str(txt))+"\nDont forget to Subscrabe :D\nChannel : https://bit.ly/2xbVxlh")
                            me.sendMessage(R, "Berhasil broadcast ke {} group".format(str(len(groups))))
                        if PrankBotsData == Abouts["34"]:
                          if D in Owner or D in meM:
                            groups = me.groups
                            ret_ = "╭━━━━━══[ Group List ]══━━━━━╮"
                            no = 0 + 1
                            for gid in groups:
                                group = me.getGroup(gid)
                                ret_ += "\n┣═ {}. {} ┣═Member: {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "\n╰━━━━━══[ Total {} Groups ]════━━━━━".format(str(len(groups)))
                            me.sendMessage(R, str(ret_))
                        if PrankBotsData == Abouts["35"]:
                          if D in Owner or D in meM:
                            contactlist = me.getAllContactIds()
                            kontak = me.getContacts(contactlist)
                            num=1
                            msgs="╭━━━━━══[ Friend List ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Friend Result ]══━━━━━\nTotal : %i" % len(kontak)
                            me.sendMessage(R, msgs)
                        if PrankBotsData == Abouts["36"]:
                          if D in Owner or D in meM:
                            blockedlist = me.getBlockedContactIds()
                            kontak = me.getContacts(blockedlist)
                            num=1
                            msgs="╭━━━━━══[ Friend Block ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Block Result ]══━━━━━\nBlock Total : %i" % len(kontak)
                            me.sendMessage(R, msgs)
                        if PrankBotsData == Abouts["37"]:
                          if D in Owner or D in meM:
                            me.sendMessage(R, "━━━━══[Pembuat Grup]══━━━━")
                            group = me.getGroup(R)
                            GS = group.creator.mid
                            me.sendContact(R, GS)
                            me.sendMessage(R, "━━━━══━━╩━━══━━━━")
                        if PrankBotsData == Abouts["38"]:
                          if D in Owner or D in meM:
                            if D in meM:
                                if msg.toType == 2:
                                    group = me.getGroup(R)
                                    ret_ = "╭━━━══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n┣═ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╰━━━══[ Total {} member]".format(str(len(group.members)))
                                    me.sendMessage(R, str(ret_))
                        if PrankBotsData == Abouts["39"]:
                          if D in Owner or D in meM:
                            if D in meM:
                                if msg.toType == 2:
                                    group = me.getGroup(R)
                                    ret_ = "╭━━━══[ Pending List ]"
                                    no = 0 + 1
                                    if group.invitee is None or group.invitee == []:
                                        me.sendMessage(R, "Tidak ada pendingan")
                                        return
                                    else:
                                        for pen in group.invitee:
                                            ret_ += "\n┣═ {}. {}".format(str(no), str(pen.displayName))
                                            no += 1
                                        ret_ += "\n╰━━━══[ Total {} tertunda]".format(str(len(group.invitee)))
                                        me.sendMessage(R, str(ret_))
                        if PrankBotsData == Abouts["40"]:
                          if D in Owner or D in meM:
                            if D in meM:
                                group = me.getGroup(R)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Closed"
                                    gTicket = "Qr tidak tersedia karna di tutup"
                                else:
                                    gQr = "Open"
                                    gTicket = "https://me.me/R/ti/g/{}".format(str(me.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╭━━━━══[ Group Info ]"
                                ret_ += "\n┣═Nama Group : {}".format(str(group.name))
                                ret_ += "\n┣═ID Group : {}".format(group.id)
                                ret_ += "\n┣═Pembuat : {}".format(str(gCreator))
                                ret_ += "\n┣═Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n┣═Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┣═━━━Kode Qr/Link━━━═"
                                ret_ += "\n┣═Group Ticket : {}".format(gTicket)
                                ret_ += "\n┣═Group Qr : {}".format(gQr)
                                ret_ += "\n╰━━━━══[ CREATOR PRANKBOT]"
                                me.sendImageWithURL(R, path)
                                me.sendMessage(R, str(ret_))
                        if PrankBotsData == Abouts["41"]:
                          if D in Owner or D in meM:
                            group = me.getGroup(R)
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            me.sendImageWithURL(R, path)
                        if PrankBotsData == Abouts["42"]:
                          if D in Owner or D in meM:
                            gid = me.getGroup(R)
                            me.sendMessage(R, "Name group\n" + gid.name)
                        if PrankBotsData == Abouts["43"]:
                          if D in Owner or D in meM:
                            gid = me.getGroup(R)
                            me.sendMessage(R,gid.id)
                        if PrankBotsData == Abouts["44"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == False:
                                    ticket = me.reissueGroupTicket(R)
                                    me.sendMessage(R, "https://me.me/R/ti/g/{}".format(str(ticket)))
                                else:
                                    group.preventedJoinByTicket = False
                                    me.updateGroup(group)
                                    me.sendMessage(R, "https://me.me/R/ti/g/{}".format(str(ticket)))
                        if PrankBotsData == Abouts["45"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == False:
                                    me.sendMessage(R, "Sudah terbuka")
                                else:
                                    group.preventedJoinByTicket = False
                                    me.updateGroup(group)
                                    me.sendMessage(R, "Berhasil membuka Qr")
                        if PrankBotsData == Abouts["46"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == True:
                                    me.sendMessage(R, "Sudah tertutup")
                                else:
                                    group.preventedJoinByTicket = True
                                    me.updateGroup(group)
                                    me.sendMessage(R, "Berhasil menutup Qr")
                        if PrankBotsData == Abouts["47"]:
                          if D in Owner or D in meM:
                            PrankBots["Add"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["48"]:
                          if D in Owner or D in meM:
                            PrankBots["Add"] = False
                            me.sendMessage(R, "Already ff")
                        if PrankBotsData == Abouts["49"]:
                          if D in Owner or D in meM:
                            PrankBots["Join"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["50"]:
                          if D in Owner or D in meM:
                            PrankBots["Join"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["51"]:
                          if D in Owner or D in meM:
                            PrankBots["Read"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["52"]:
                          if D in Owner or D in meM:
                            PrankBots["Read"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["53"]:
                          if D in Owner or D in meM:
                            PrankBots["Unsend"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["54"]:
                          if D in Owner or D in meM:
                            PrankBots["Unsend"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["55"]:
                          if D in Owner or D in meM:
                            PrankBots["Wc"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["56"]:
                          if D in Owner or D in meM:
                            PrankBots["Wc"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["57"]:
                          if D in Owner or D in meM:
                            PrankBots["Shared"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["58"]:
                          if D in Owner or D in meM:
                            PrankBots["Shared"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["59"]:
                          if D in Owner or D in meM:
                            PrankBots["Respon"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["60"]:
                          if D in Owner or D in meM:
                            PrankBots["Respon"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["61"]:
                          if D in Owner or D in meM:
                                try:
                                    del Sid['Red'][R]
                                    del Sid['Reason'][R]
                                    del Sid['Tar'][R]
                                except:
                                    pass
                                Sid['Red'][R] = Id
                                Sid['Reason'][R] = ""
                                Sid['Tar'][R]=True
                                me.sendMessage(R, "di aktifkan untuk grup\n"+g.name)
                        if PrankBotsData == Abouts["62"]:
                          if D in Owner or D in meM:
                            if R in Sid['Red']:
                                Sid['Tar'][R]=False
                                me.sendMessage(R, "Daftar yang terlihat\n"+Sid['Reason'][msg.to])
                                me.sendMessage(R, "Already off")
                            else:
                                me.sendMessage(R, "aktifkan dulu beb")
                        if PrankBotsData == Abouts["63"]:
                         if D in Owner or D in meM:
                          group = me.getGroup(R)
                          Rmem = [contact.mid for contact in group.members]
                          Dmem = len(Rmem)//20
                          try:                          	
                              for mentionMembers in range(Dmem+1):
                                  no = 0
                                  ret_ = "\n╔════════════"
                                  dataMid = []
                                  for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n╠. @!".format(str(no))
                                  ret_ += "\n╚══════════════".format(str(len(dataMid)))
                                  sendMeention(R, ret_, dataMid)
                          except Exception as Ewe:
                              print(Ewe)
                        if PrankBotsData == Abouts["64"]:
                          if D in Owner or D in meM:
                            try:
                                PrankBots["Shared"] = True
                                PrankBots["Add"] = True
                                PrankBots["Join"] = True
                                PrankBots["Wc"] = True
                                PrankBots["Read"] = True
                                PrankBots["Unsend"] = True
                                me.findAndAddContactsByMid("ub0842532a31b9d99856cf2590b17d33f")
                                me.findAndAddContactsByMid("udfaf52176415b46cb445ae2757ec85f3")
                                me.findAndAddContactsByMid("u17a086ccff618e754588a1108335867f")
                                me.findAndAddContactsByMid("uc8dc5352066b6a344bde3c07b0fe04ea")
                                me.sendMessage(R,"SETTING ALL IN ONLINE")
                            except:me.sendMessage(R,"SETTING ALL IN ONLINE")
                        if PrankBotsData == Abouts["65"]:
                          if D in Owner or D in meM:
                            try:
                                PrankBots["Shared"] = False
                                PrankBots["Add"] = False
                                PrankBots["Join"] = False
                                PrankBots["Wc"] = False
                                PrankBots["Read"] = False
                                PrankBots["Unsend"] = False
                                me.findAndAddContactsByMid("ub0842532a31b9d99856cf2590b17d33f")
                                me.findAndAddContactsByMid("udfaf52176415b46cb445ae2757ec85f3")
                                me.findAndAddContactsByMid("u17a086ccff618e754588a1108335867f")
                                me.findAndAddContactsByMid("uc8dc5352066b6a344bde3c07b0fe04ea")
                                me.sendMessage(R,"SETTING ALL IN OFFLINE")
                            except:me.sendMessage(R,"SETTING ALL IN OFFLINE")
                        if PrankBotsData == Abouts["66"]:
                          if D in Owner or D in meM:
                            RunTheRun(R, D, "_______RESULT______\n")
                            """
                            BOT WAR
                            VERSION : PRANKBOTS
                            REVISION : OPPS
                            """
        if rank.type == 25:
          """
          BOT WAR
          VERSION : PRANKBOTS
          REVISION : OPPS
          """
          if PrankBots["bot"] == True:
            war = rank.message
            Warstart = war.text
            Id = war.id
            R = war.to
            D = war._from
            if Warstart == "Warkey" or Warstart == "warkey":
                me.sendMessage(R, str(warKey))
            if Warstart == "Warbot" or Warstart == "warbot":
                me.sendContact(to,kk1Rank)
                me.sendContact(to,kk2Rank)
                me.sendContact(to,kk3Rank)
                me.sendContact(to,kk4Rank)
                me.sendContact(to,jssRank)
            if Warstart == "Warban" or Warstart == "warban":
                if PrankBots["blacklist"] == {}:
                    me.sendMessage(R,"Tidak mempunyai kontak blacklist")
                else:
                    me.sendMessage(R,"═══════BLACKLIST═══════")
                    h = ""
                    for i in PrankBots["blacklist"]:
                      h = me.getContact(i)
                      me.sendContact(R,i)
                    me.sendMessage(R,"═══════WANTED═══════")
            if Warstart == "Warclearban" or Warstart == "warclearban":
                me.sendMessage(R, "Berhasil menghapus {} user blacklist".format(str(len(PrankBots["blacklist"]))))
                PrankBots["blacklist"] = {}
            if Warstart == "Warespon" or Warstart == "warespon":
                kk1.sendMessage(R, kk1Profile.displayName)
                kk2.sendMessage(R, kk2Profile.displayName)
                kk3.sendMessage(R, kk3Profile.displayName)
                kk4.sendMessage(R, kk4Profile.displayName)
            if Warstart == "Warspeed" or Warstart == "warspeed":
                start = time.time()
                me.sendMessage(R, "kecepatan...")
                tes = time.time() - start
                me.sendMessage(R, "{}".format(str(tes)))
                kk1.sendMessage(R, "{}".format(str(tes)))
                kk2.sendMessage(R, "{}".format(str(tes)))
                kk3.sendMessage(R, "{}".format(str(tes)))
                kk4.sendMessage(R, "{}".format(str(tes)))
            if Warstart == "Warstay" or Warstart == "warstay":
                try:
                    me.inviteIntoGroup(R, [kk1Rank,kk2Rank,kk3Rank,kk4Rank,jssRank])
                    kk1.acceptGroupInvitation(R)
                    kk2.acceptGroupInvitation(R)
                    kk3.acceptGroupInvitation(R)
                    kk4.acceptGroupInvitation(R)
                    kk1.sendMessage(R, "already..")
                    kk2.sendMessage(R, "already..")
                    kk3.sendMessage(R, "already..")
                    kk4.sendMessage(R, "already..")
                except:
                    try:
                        gg = me.getGroup(R)
                        gg.preventedJoinByTicket = False
                        me.updateGroup(gg)
                        grup = me.reissueGroupTicket(R)
                        kk1.acceptGroupInvitationByTicket(R, grup)
                        kk2.acceptGroupInvitationByTicket(R, grup)
                        kk3.acceptGroupInvitationByTicket(R, grup)
                        kk4.acceptGroupInvitationByTicket(R, grup)
                        jss.acceptGroupInvitationByTicket(R, grup)
                        gg.preventedJoinByTicket = True
                        jss.updateGroup(gg)
                        jss.leaveGroup(R)
                        kk4.inviteIntoGroup(R, [jssRank])
                    except:me.sendMessage(R, "BOT REVOKE")
            if Warstart == "Warout" or Warstart == "warout":
                try:
                    kk1.leaveGroup(R)
                    kk2.leaveGroup(R)
                    kk3.leaveGroup(R)
                    kk4.leaveGroup(R)
                    me.cancelGroupInvitation(R,[jssRank])
                except:
                    try:
                        me.cancelGroupInvitation(R,[jssRank])
                    except:me.sendMessage(R, "tidak ada bot di dalam grup")
            if Warstart.startswith("Warkick ") or Warstart.startswith("warkick "):
                tagTarget = eval(msg.contentMetadata["MENTION"])
                contact = tagTarget["MENTIONEES"][0]["M"]                
                allkicker = [kk1,kk2,kk3,kk4]
                forall = random.choice(allkicker)
                forall.kickoutFromGroup(contact)
        if rank.type == 26:
          if PrankBots["bot"] == True:
            msg = rank.message
            text = msg.text
            Id = msg.id
            R = msg.to
            D = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = D
                elif msg.toType == 2:
                    to = R
                if PrankBots["Read"] == True:
                    me.sendChatChecked(R, Id)
                if msg.contentType == 0:
                    if text is None:
                        return
                if msg.contentType == 16:
                        if PrankBots["Shared"] == True:
                            try:
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = me.getContact(D)
                                    auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://me.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠ Stiker : https://me.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚══[ Finish ]"
                                me.sendMessage(R, str(ret_))
                            except Exception as error:
                                logError(error)
                                traceback.print_tb(error.__traceback__)
                if msg.contentType == 0 and D not in meM and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if meM in mention["M"]:
                                if PrankBots["Respon"] == True:
                                    sendMention(R, D, "\n",respontags["Auto_text"])
                                    me.sendContact(R, D)
                                break
        if rank.type == 13:
            print ("NOTIFIED MEMBER OR SELF JOIN GROUP")
            Gr = opps1
            if PrankBots["Join"] == True:
                me.acceptGroupInvitation(Gr)
            else:
                pass
        if rank.type == 5:
            print ("NOTIFIED ADD CONTACT SELF")
            if PrankBots["Add"] == True:
                me.findAndAddContactsByMid(opps1)
            sendMention(opps1, opps1, "Thanks For add Me ","")
        if rank.type == 15:
            Gr = opps1
            Cj = opps2
            print ("NOTIFIED CONTACT MEMBER LEAVE TO GROUP")
            if PrankBots["Wc"] == True:
              if Cj in BotWar:
                pass
              else:
                Gc = me.getGroup(Gr)
                dia = me.getContact(Cj)
                ms = "Good bye : {}".format(dia.displayName)
                ms += "In group : {}".format(Gc.name)
                mt = "Why your leave in group {}".format(Gc.name)
                me.sendMessage(Gr,str(ms))
                me.sendMessage(dia,mt)
                me.sendContact(Gr,dia)
        if rank.type == 17:
            Gr = opps1
            Cj = opps2
            print ("NOTIFIED CONTACT MEMBER JOIN TO GROUP")
            if PrankBots["Wc"] == True:
              if Cj in BotWar:
                pass
              else:
                Gc = me.getGroup(Gr)
                dia = me.getContact(Cj)
                ms = "Welcome : {}".format(dia.displayName)+" In group : {}".format(Gc.name)
                me.sendMessage(Gr,str(ms))
                me.sendContact(Gr,dia)
        if rank.type == 65:
            print ("UNSEND MESSAGE UNSENDER FROM MY SELF")
            if PrankBots["Unsend"] == True:
                Geting = opps1
                Text_in_Destroy = opps2
                if Text_in_Destroy in msg_dict:
                    Timer = time.time()
                    Target_Text = me.getContact(msg_dict[Text_in_Destroy]["from"])
                    if "text" in msg_dict[Text_in_Destroy]:
                        StartTimer = Timer - msg_dict[Text_in_Destroy]["waktu"]
                        StartTimer = format_timespan(StartTimer)
                        rat_ = "Timer unsend: {} WIB".format(StartTimer)
                        rat_ += "Text Unsend\n{}".format(msg_dict[Text_in_Destroy]["text"])
                        sendMention(Geting, Target_Text.mid, "Sorry\nMy Resend your Message\n\n", str(rat_))
                        del msg_dict[Text_in_Destroy]
                else:
                    me.sendMessage(Geting,"Detected Unsend")
        if rank.type == 55:
            Gr = opps1
            try:
                if Sid['Tar'][Gr]==True:
                        if Gr in Sid['Red']:
                            Name = me.getContact(opps2).displayName
                            Np = me.getContact(opps2).pictureStatus
                            if Name in Sid['Reason'][Gr]:
                                pass
                            else:
                                Sid['Reason'][Gr] += "\n||[ " + Name + " ]||"
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        me.sendMessage(Gr, "Hallo.. " + " " + nick[0] + " " + "\nNah jangan ngintip mulu . . .\nGabung Chat yux ")
                                        me.sendImageWithURL(Gr, "http://dl.profile.line-cdn.net/" + Np)
                                    else:
                                        me.sendMessage(Gr, "Hallo.. " + " " + nick[1] + " " + "\nJangan ngintip.. . . .\nMasuk  ayox... ")
                                        me.sendImageWithURL(Gr, "http://dl.profile.line-cdn.net/" + Np)
                                else:
                                    me.sendMessage(Gr, "hallo.. " + " " + Name + " " + "\nJangan ngintip aja\nMasuk gabung chat ya... ")
                                    me.sendImageWithURL(Gr, "http://dl.profile.line-cdn.net/" + Np)
                        else:
                            pass
                else:
                    pass
            except:
                pass
        else:
            pass
    except Exception as error:
        ErrorX(error)
        if rank.type == 59:
            print(rank)
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for rank in ops: 
          serviceX(rank)
          oepoll.setRevision(rank.revision)
    except Exception as e:
        me.log("RESPONSE: " + str(e))
