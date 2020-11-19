from PIL import Image

mac = Image.open('example.jpg')
print(type(mac))
# image.show() will dispaly the image
# mac.show()

# the top left corner is the (0,0) coordinate
mac.crop((0,0,100,100))
pencils = Image.open('pencils.jpg')
# pencils.show()
print(pencils.size)

# BOTTOM PENCILS
# x = 0
# y = 1100

# w = 1950/3
# h = 1300
# pencils.crop((x,y,w,h)).show()

# halway = 1993/2
# x = halway - 200
# w = halway + 200

# y = 800
# h = 1257
# computer = mac.crop((x,y,w,h))
# mac.paste(im=computer,box=(0,0))
# mac.paste(im=computer,box=(796,0))
# mac.rotate(90).show()
# mac.show()

red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')
# blue.putalpha(255) # putalpha() 0 to 255 should change transparency
# blue.show()
blue.paste(im=red,box=(0,0),mask=red)
blue.show()