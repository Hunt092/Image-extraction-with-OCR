$Author Yash Chavan



import zipfile
from zipfile import ZipFile
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
name_list=[]
Text=[]
Page_data={}
# the rest is up to you!

with ZipFile(Zipfilename) as file:
    lst = file.infolist()
    for img in lst:
        Page_data[img.filename] = [Image.open(file.open(img.filename))]        
        name_list.append(img.filename)
for name in name_list:
    img = Page_data[name][0]               
    img = img.convert('L')
    text = pytesseract.image_to_string(img).replace(' \n',',')
    Page_data[name].append(text)        
    #print(Page_data[name][1])    

Page_data


#Word = input("Enter word to be searched:")
if Word in Page_data[name][1]:
    print("Result found on",name)
    try:
        faces = (face_cascade.detectMultiScale(np.array(img),1.35,4)).tolist()
        Page_data[name].append(faces)
        faces_in_each = []                               
        for x,y,w,h in Page_data[name][2]:                   
            faces_in_each.append(img.crop((x,y,x+w,y+h)))      
            display((img.crop((x,y,x+w,y+h))).resize((110,110)))                                
            contact_sheet = Image.new(img.mode, (550,110*int(np.ceil(len(faces_in_each)/5))))          
            x = 0               
            y = 0
        for face in faces_in_each:                   
                face.thumbnail((110,110))#                
                contact_sheet.paste(face, (x, y))                                      
                if x+110 == contact_sheet.width:                        
                    x=0                      
                    y=y+110                   
                else:                        
                    x=x+110                                       
                    display(contact_sheet)            
    except:               
        print('But there were no faces in that Page!')


