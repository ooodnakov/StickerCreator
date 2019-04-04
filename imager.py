from PIL import Image, ImageOps, ImageDraw
import os
import shutil


images = []
num = 1

for file in os.listdir('input/'):           #search for images in 'input'
    if file[-3:].lower() == 'jpg' or file[-3:].lower() == 'png' or file[-4:].lower() == 'jpeg':
        images.append(file)

print('We detected such images to crop:')           #ask to proceed
for img in images:
    print(img)
if input('Do you want to proceed (Y,N)?').lower() != 'y':
    quit()

if input('Do you want to keep original names (Y/N)?').lower() != 'y':
    orig = False
else:
    orig = True


for name in images:         #resizes and crops
    img = Image.open('input/'+name)

    width, height = img.size            #crop to square
    if width > height:
        margin = (width - height) / 2
        img = img.crop((margin, 0, width - margin, height))
    elif width < height:
        margin = (-width + height) / 2
        img = img.crop((0, margin, width, height - margin))

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

    try:                            #creats output folder if it doesn't exist
        os.mkdir('output')
    except FileExistsError:
        pass

    if orig:
        output.save('output/{}.png'.format(name[:-4]))
    else:
        output.save('output/{}.png'.format(images.index(name)))

    print(name, ' is done.')

if not os.path.isfile('output/CoolkaOS Sticker(EXAMPLE).png'):
    shutil.copy('CoolkaOS Sticker.png', 'output/CoolkaOS Sticker.png')