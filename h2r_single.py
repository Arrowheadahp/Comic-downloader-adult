import urllib.request
from PIL import Image
import time

def getpic(picurl):
    picreq = urllib.request.urlopen(picurl)
    
    img = Image.open(picreq)
    print ('.', end='')
    time.sleep(2)

    return img.convert('RGB')


def dwnldr(url, playlist=''):
    piclist = []
    murl = url[:-7]
    t = 2
    i = 1
    while t:
        try:
            picurl = murl+str(i).zfill(3)+'.jpg'
            piclist.append(getpic(picurl))
              
            
            t=2
            i+=1
            if i>1000:
                break
        except:
            time.sleep(2)
            t-=1
    piclist[0].save('doujinshi/'+ playlist+'h2r_' + murl.split('/')[-3]+'-'+murl.split('/')[-2] + '.pdf',
                    save_all = True,
                    append_images = piclist)
    print ()


url = 'https://static.hentaicdn.com/hentai/14392/1/hcdn0009.jpg'


if '__name__'=='__main__':
    dwnldr(input('Enter url of any page: '))



















