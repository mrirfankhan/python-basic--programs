from PIL import Image
import stepic

# encode masseg in image
image1=Image.open("new2.png")
encod1=stepic.encode(image1,b"hello irfan khan")
encod1.save("new2.png")

# decode secret masseg
image2=stepic.decode(image1)
print(image2)
