from PIL import Image, ImageOps, ImageDraw
import os

images = []
num = 1

for file in os.listdir('input/'):           #search for images in 'input'
    if file[-3:] == 'jpg' or file[-3:] == 'png' or file[-4:] ==  'jpeg':
        images.append(file)

print('We detected such images to crop:')           #ask to proceed
for img in images:
    print(img)
if input('Do you want to proceed(Y,N)?').lower() != 'y':
    quit()

for name in images:         #resizes and crops
    img = Image.open('input/'+name)

    basewidth = 512                 #resizes image to 512x512
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)

    bigsize = (img.size[0] * 3, img.size[1] * 3)                #creats round mask
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(img.size, Image.ANTIALIAS)
    img.putalpha(mask)

    output = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))             #crops according to mask
    output.putalpha(mask)
    output.save('output/{}.png'.format(file[:-4]))

    print(file,' is done.')