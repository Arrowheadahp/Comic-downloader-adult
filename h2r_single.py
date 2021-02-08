import urllib.request
from PIL import Image
import time

def dwnldr(url, playlist=''):
    piclist = []
    murl = url[:-7]
    t = 10
    i = 1
    while t:
        try:
            picurl = murl+str(i).zfill(3)+'.jpg'
##            print (picurl,)
            picreq = urllib.request.urlopen(picurl)
             
            #open(str(i).zfill(4)+'.jpg', 'wb').write(picreq.content)
            img = Image.open(picreq)
            piclist.append(img.convert('RGB'))
              
            time.sleep(1)
            t=10
            i+=1
            if i>10000:
                break
        except:
            time.sleep(2)
            t-=1
    piclist[0].save('doujinshi/'+ playlist+'h2r_' + murl.split('/')[-3]+'-'+murl.split('/')[-2] + '.pdf',
                    save_all = True,
                    append_images = piclist)


url = 'https://static.hentaicdn.com/hentai/14392/1/hcdn0009.jpg'


if '__name__'=='__main__':
    dwnldr(input('Enter url of any page: '))



















