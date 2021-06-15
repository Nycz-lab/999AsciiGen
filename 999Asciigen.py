from PIL import Image, ImageDraw, ImageFont
import random
import sys




def main():

    filename = sys.argv[1]




def converter(filename, block=99, char = '9', char_size_mult=1.5):
    img = Image.open(filename)
    img = img.convert("RGBA")
    pix = img.load()

    print(img.size)


    block_size_x = int(img.size[0] / block)
    block_size_y = int(img.size[1] / block)

    new_img = Image.new(mode = "RGBA", size=img.size, color=(0,0,0,0))


    d1 = ImageDraw.Draw(new_img)
    font = ImageFont.truetype(font="glitch.otf", size=int(block_size_x*char_size_mult), index=0, encoding="unic")
    img.show()


    for x in range(0, img.size[0], block_size_x):
        for y in range(0, img.size[1], block_size_y):

            R = pix[x,y][0]
            G = pix[x,y][1]
            B = pix[x,y][2]
            A = pix[x,y][3]

            if A > 0:
                d1.text((x, y), char, fill =(R, G, B, A),font=font)
            #print(x,"/",img.size[0], y,"/",img.size[1])


    new_img.save(filename + ".ascii.png")
    new_img.show()

if __name__ == "__main__":
    if(len(sys.argv) > 4):
        filename = sys.argv[1]
        converter(filename, int(sys.argv[2]), sys.argv[3], float(sys.argv[4]))
    elif(len(sys.argv) > 1):
        filename = sys.argv[1]
        converter(filename)
    else:
        print("Error wrong format")
        print("usage: ", sys.argv[0], "[input_file: String] [block_size: int] [char: char/String] [char_size_mult: float/int]")
