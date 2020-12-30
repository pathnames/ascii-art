from PIL import Image


img = Image.open("ascii-pineapple.jpg")

#Convert image to a 2d-matrix:
pixels = list(img.getdata())
pixel_matrix = [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]

brightness_matrix = []
for x in range(len(pixel_matrix)):
    list = []
    for y in range(len(pixel_matrix)):
        list.append((pixel_matrix[x][y][0] + pixel_matrix[x][y][1] + pixel_matrix[x][y][2])/3)
    brightness_matrix.append(list)

def print_matrix(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            print(matrix[x][y])
        
print(len(brightness_matrix))
#print_matrix(brightness_matrix)




