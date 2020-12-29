from PIL import Image


img = Image.open("ascii-pineapple.jpg")

#https://en.wikibooks.org/wiki/Python_Imaging_Library/Editing_Pixels
# pixel_array = []
# for i in range(img.size[0]): #for every column
#     for j in range(img.size[1]): #for every row
#         pixel_array.append(img[i][j])

pixels = list(img.getdata())
pixel_matrix = [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]

print(pixel_matrix)