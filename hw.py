from PIL import Image

matrix = Image.open('word_matrix.png') 
# 1015 x 559
mask = Image.open('mask.png')
# 505 x 251
mask.putalpha(100)
# mask.show()

matrix.paste(im=mask,box=(0,0),mask=mask)
matrix.save('hw.png')
goal = Image.open('hw.png')
goal.show()