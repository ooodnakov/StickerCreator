from PIL import Image, ImageOps, ImageDraw
import os

images = []
num = 1

for file in os.listdir('input/'):
    if file[-3:] == ('jpg' or 'png' or 'peg'):
        images.append(file)
        print(file)
print(images)
for name in images:
    img = Image.open('input/'+name)

    basewidth = 512
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)

    bigsize = (img.size[0] * 3, img.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(img.size, Image.ANTIALIAS)
    img.putalpha(mask)

    output = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save('output/{}.png'.format(num))
    num += 1
    print(num, ' is done.')