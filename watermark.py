from PIL import Image,ImageFont,ImageDraw
img=Image.open(r"C:\Users\azeaz\Pictures\Camera Roll\20251222143612_52_2.jpg")
font=ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc",size=36)
draw=ImageDraw.Draw(img)
draw.text(xy=(360,420),text="Zelia",fill="blue",font=font)
img.show()
img.save(r"C:\Users\azeaz\Pictures\shuiying.jpg")