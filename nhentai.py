import urllib.request
from urllib.request import Request, urlopen
from PIL import Image
import time


url = 'https://cdn.dogehls.xyz/galleries/1803120/2.jpg'
nhserver = 'https://cdn.dogehls.xyz/galleries/'


def getpic(picurl):
    print (picurl,)
##    picreq = urllib.request.urlopen(picurl)

    req = Request(picurl, headers={'User-Agent': 'Mozilla/5.0'})
    picreq = urlopen(req)
    
    img = Image.open(picreq)
    time.sleep(2)

    return img.convert('RGB')

def dwnldr4(sauce):
    galleryurl = nhserver + sauce + '/'
    piclist = []

    i = 0
    while True:
        i+=1

        jpg = galleryurl + str(i) + '.jpg'
        png = galleryurl + str(i) + '.png'

        

        try:
            pic = getpic(jpg)
        except:
            try:
                pic = getpic(png)
            except:
                break

        piclist.append(pic)

    piclist[0].save('doujinshi/' + sauce + '.pdf', save_all = True,
                    append_images = piclist)
            
        

##dwnldr4(input('Enter sauce: '))
dwnldr4('1803120')

##getpic(url)








