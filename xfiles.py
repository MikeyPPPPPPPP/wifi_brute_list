import requests
from bs4 import BeautifulSoup
import json
#_____TODO_____
'''
fix th emiddle so it geets deeper files

try recurssion
'''
all_files = {}

extencions = {"ogm":"video","doc":"text","class":"code","js":"code","swift":"code","cc":"code","tga":"image","ape":"audio","woff2":"font","cab":"archiv","whl":"archiv","mpe":"video","rmvb":"video","srt":"video","pdf":"text","xz":"archiv","exe":"exec","m4a":"audio","crx":"exec","vob":"video","tif":"image","gz":"archiv","roq":"video","m4v":"video","gif":"image","rb":"code","3g2":"video","m4":"code","ar":"archiv","vb":"code","sid":"audio","ai":"image","wma":"audio","pea":"archiv","bmp":"image","py":"code","mp4":"video","m4p":"video","ods":"sheet","jpeg":"image","command":"exec","azw4":"book","otf":"font","ebook":"text","rtf":"text","ttf":"font","mobi":"book","ra":"audio","flv":"video","ogv":"video","mpg":"video","xls":"sheet","jpg":"image","mkv":"video","nsv":"video","mp3":"audio","kmz":"image","java":"code","lua":"code","m2v":"video","deb":"archiv","rst":"text","csv":"sheet","pls":"audio","pak":"archiv","egg":"archiv","tlz":"archiv","c":"code","cbz":"book","xcodeproj":"code","iso":"archiv","xm":"audio","azw":"book","webm":"video","3ds":"image","azw6":"book","azw3":"book","php":"code","kml":"image","woff":"font","log":"text","zipx":"archiv","3gp":"video","po":"code","mpa":"audio","mng":"video","wps":"text","wpd":"text","a":"archiv","s7z":"archiv","ics":"sheet","tex":"text","go":"code","ps":"image","org":"text","sh":"exec","msg":"text","xml":"code","cpio":"archiv","epub":"book","docx":"text","lha":"archiv","flac":"audio","odp":"slide","wmv":"video","vcxproj":"code","mar":"archiv","eot":"font","less":"web","asf":"video","apk":"archiv","css":"web","mp2":"video","odt":"text","patch":"code","wav":"audio","msi":"exec","rs":"code","gsm":"audio","ogg":"video","cbr":"book","azw1":"book","m":"code","dds":"image","h":"code","dmg":"archiv","mid":"audio","psd":"image","dwg":"image","aac":"audio","s3m":"audio","cs":"code","cpp":"code","au":"audio","aiff":"audio","diff":"code","avi":"video","bat":"exec","html":"code","pages":"text","bin":"exec","txt":"text","rpm":"archiv","m3u":"audio","max":"image","vcf":"sheet","svg":"image","ppt":"slide","clj":"code","png":"image","svi":"video","tiff":"image","tgz":"archiv","mxf":"video","7z":"archiv","drc":"video","yuv":"video","mov":"video","tbz2":"archiv","bz2":"archiv","gpx":"image","shar":"archiv","xcf":"image","dxf":"image","jar":"archiv","qt":"video","tar":"archiv","xpi":"archiv","zip":"archiv","thm":"image","cxx":"code","3dm":"image","rar":"archiv","md":"text","scss":"web","mpv":"video","webp":"image","war":"archiv","pl":"code","xlsx":"sheet","mpeg":"video","aaf":"video","avchd":"video","mod":"audio","rm":"video","it":"audio","wasm":"web","el":"code","eps":"image"}


class file_me_bitch:
    def __init__(self, url):
        self.url = url
        self.indexer = {}
        self.current_url = ''
        self.base = BeautifulSoup(requests.get(self.url).text, 'lxml')
    
    def is_file(self, file):
        filename = file.split('/')[-1]
        for x in extencions:
            if x in filename.split('.')[-1]:
                return file
            
    
    def is_dir(self, file):
        if file[-1] == '/':
            return file
        

    def get_urls_on_page(self, page):
        urls = []
        soup = BeautifulSoup(requests.get(page).text, 'lxml')
        for x in soup.find_all('a'):
            urls.append(x['href'])
        return urls



t = file_me_bitch('https://doc.lagout.org/')
for x in t.get_urls_on_page('https://doc.lagout.org/'):
    
    #if t.is_file(x):
    all_files[t.url] = []

    if t.is_dir(x) != None and t.is_dir(x) != 'https://www.lagout.org/dons/' and t.is_dir(x) != '../':#is_file(x):
        all_files[t.url+x] = []
        #all_files[t.url+x] = []
        #print(t.is_dir(t.url+x))
        for r in t.get_urls_on_page(t.url+x):
            
            if t.is_dir(r) != None and t.is_dir(r) != 'https://www.lagout.org/dons/' and t.is_dir(r) != '../':
                #print(t.is_dir(t.url+x+r))
                all_files[t.url+x+r] = []
                
                for s in t.get_urls_on_page(t.url+x+r):
                    if t.is_dir(s) != None and t.is_dir(s) != 'https://www.lagout.org/dons/' and t.is_dir(s) != '../':
                        #print(t.is_dir(t.url+x+r+s))
                        all_files[t.url+x+r+s] = []

                        for w in t.get_urls_on_page(t.url+x+r+s):
                            if t.is_dir(w) != None and t.is_dir(w) != 'https://www.lagout.org/dons/' and t.is_dir(w) != '../':
                                #print(t.url+x+r+s+w)
                                all_files[t.url+x+r+w] = []

                                for a in t.get_urls_on_page(t.url+x+r+s+w):
                                    if t.is_dir(a) != None and t.is_dir(a) != 'https://www.lagout.org/dons/' and t.is_dir(a) != '../':
                                        #print(t.url+x+r+s+w+a)
                                        all_files[t.url+x+r+w+a] = []

                                        for z in t.get_urls_on_page(t.url+x+r+s+w+a):
                                            if t.is_dir(z) != None and t.is_dir(z) != 'https://www.lagout.org/dons/' and t.is_dir(z) != '../':
                                                #print(t.url+x+r+s+w+a+z)
                                                all_files[t.url+x+r+w+a+z] = []

                                    elif t.is_file(t.url+x+r+s+w+a) != None:
                                        #all_files[t.url+x+r+s+w].append(t.is_file(t.url+x+r+s+w+a))
                                        #print(t.is_file(t.url+x+r+s+w+a))
                                        pass

                            elif t.is_file(t.url+x+r+s+w) != None:
                                all_files[t.url+x+r+s].append(t.is_file(t.url+x+r+s+w))
                                #print(t.is_file(t.url+x+r+s+w))

                                #keep going
                    elif t.is_file(t.url+x+r+s) != None:
                        all_files[t.url+x+r].append(t.is_file(t.url+x+r+s))
                        #print(t.is_file(t.url+x+r+s))
                
            elif t.is_file(t.url+x+r) != None:
                all_files[t.url+x].append(t.is_file(t.url+x+r))
                #print(t.is_file(t.url+x+r))
            
    elif t.is_file(t.url+x) != None:
        #all_files[t.url].append({t.url:t.is_file(t.url+x)})
        #print(t.is_file(t.url+x))
        pass
with open('data.json', 'w') as outfile:
    json.dump(all_files, outfile, indent=2)