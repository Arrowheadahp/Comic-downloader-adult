import urllib.request
from urllib.request import Request, urlopen
from PIL import Image
import time


url = 'https://i3.nhentai.net/galleries/1564981/2.jpg'
nhserver = 'https://i3.nhentai.net/galleries/'


def getpic(picurl):
    print (picurl,)
##    picreq = urllib.request.urlopen(picurl)

    req = Request(picurl, headers={'User-Agent': 'Mozilla/5.0'})
    picreq = urlopen(req)
    
    img = Image.open(picreq)
    time.sleep(1)

    return img.convert('RGB')

def dwnldr4(sauce):
    galleryurl = nhserver + sauce + '/'
    piclist = []
    name = input('Enter name: ')

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

    piclist[0].save(r'D:\Media\doujinshi\\' + name + '.pdf', save_all = True,
                    append_images = piclist[1:])
            
        

##dwnldr4(input('Enter sauce: '))
dwnldr4(input('Enter sauce: '))

##getpic(url)
