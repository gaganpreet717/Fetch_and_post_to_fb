import random
import PIL as Pillow
from PIL import Image   
from PIL import ImageDraw
from PIL import ImageFont
import codecs
import sys
import facebook

# the text file is created with collection of quotes and list(lines) is created
#containing all the quotes through which any quote is accessed randomly when script runs

lines = []
in_file = open("quotess.txt", "rt") # open file lorem.txt for reading text data
contents = in_file.read()         # read the entire file into a string variable
lines = [] #Declare an empty list named "lines"
with codecs.open ('quotess.txt',encoding='utf-8',errors="surrogateescape") as in_file:  # UnicodeDecodeError is handled using surrogateescape
    for line in in_file:
        lines.append(line)
     
n = len(lines)
in_file.close()
rand_number = random.randrange(0,n,1)


quote = lines[rand_number]
# Now creating image of the quote accessed using Pillow
img = Image.new('RGB', (3000, 1000))
font = ImageFont.truetype("arial.ttf",50)
d = ImageDraw.Draw(img)
d.text((150,200),quote,font=font,fill=(255,0,0))
img.save("newpic.jpg")



#now posting the image created on facebook
# This requires access token which can be generated through graphApiExplorer after creating the facebook page from facebook for developers site. The access
#... token should be modified to one which never expires as the access token we get intially is short-lived only.

graph = facebook.GraphAPI(access_token='EAABuD3ezhXABAHctBEtbxLUEawBhOexklrJj06Acfy1ygLBPvYY5qYMJVeeMkuDFIt6WyI88rx4ZBvVBAIjWEBQ63uiiXyh4z6FmYdZCC7ZAYuD2hui1ZCmDH2ZBcxShGmVHdRUikYqGtJhOPuP1O0wUkUq4ibVMDlwkwSNGcHarPdtcz08ZCn', version='2.7')
graph.put_photo(image=open("newpic.jpg", 'rb'), album_path='110555099552820'+ "/photos")  



#.....end......
