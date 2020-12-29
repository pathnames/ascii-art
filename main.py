from PIL import Image
img = Image.open("ascii-pineapple.jpg")

#https://en.wikibooks.org/wiki/Python_Imaging_Library/Editing_Pixels
# pixel_array = []
# for i in range(img.size[0]): #for every column
#     for j in range(img.size[1]): #for every row
#         pixel_array.append(img[i][j])

pixel_array = list(img.getdata())
pixel_matrix = []
for i in range(img.size[0]): #for every column
    for j in range(img.size[1]): #for every row
        pixel_matrix.append(pixel_array[i][j])

print(pixel_matrix)