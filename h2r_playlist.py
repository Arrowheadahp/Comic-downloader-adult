import urllib.request
from urllib.request import Request, urlopen
from PIL import Image
import time
import re
from os import mkdir

from h2r_single import dwnldr

inp = 'https://hentai2read.com/oideyo_mizuryu_kei_land/8/'
out = 'https://static.hentaicdn.com/hentai/10959/8b/ccdn0001.jpg'

def dwnld_frm_main(url, name):
    html = urlopen(url).read()

    imglink = re.findall('src="https://static.hentaicdn.com/hentai/.*001.jpg" alt=', str(html))
    imglink = imglink[0].split('"')[1]
    
    print (url)
    dwnldr(imglink, name)
    

inp = 'https://hentai2read.com/oideyo_mizuryu_kei_land/'
out = 'https://hentai2read.com/oideyo_mizuryu_kei_land/9/'

def download_playlist(url):
    name = url.split('/')[-2]
    print (name)

    html = urlopen(url).read()
    L = re.findall('https://hentai2read.com/'+name+'/\d.{0,2}/', str(html))
    L = list(set(L))
    print (f'There are {len(L)} comics in the playlist')
    if len(L) > 1:
        mkdir('doujinshi/'+name)
        name = name + '/'
    else:
        name = name + '_'
    for c in L:
        dwnld_frm_main(c, name)

##download_playlist(inp)

while True:
    try:
        download_playlist(input('Enter playlist url: '))
    except:
        continue
    else:
        break


