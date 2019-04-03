# Sticker Creator.
Creats suitable round images for stickers in TG.

My friend asked me to crop some images for him.
At first I was doing it manually. But he saw my struggle and proposed to Python it.
And it is my result.
### Pre-Requirements.
1. Any basic Python IDE or Shell.
2. Not being dumb-ass.
3. Love dots.
## Manual.
1. Put your images in __input__ folder.
2. Run __main.py__.
3. Proceed in terminal.
```
We detected such images to crop:
name#1
name#2
...
Do you want to proceed(Y,N)?
Do you want to keep original names (Y/N)?
```
4. Get your stickers in __output__ folder.
```
name#1  is done.
name#2  is done.
...
```
5. You are brilliant! You are able to find your pngs in __output__ folder.

## How does it actually works?

You can just look to source code or read further:
1. Make a list of image names in __input__ folder.
2. After that we iterate through each name in a list
   1. Opening an __Image__.
   2. Cropping it to square which is centered.
   3. Resizing image to 512x512.
   4. Creating a round mask of suitable size.
   5. Putting alpha mask.
   6. Saving image with according filename.
3. Putting my sticker in __output__ folder so that everyone knows who done this amazing sticker pack!
