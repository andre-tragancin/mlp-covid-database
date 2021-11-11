import cv2
from to_gray import toGray

# Flip images in open cv:
# https://note.nkmk.me/en/python-opencv-numpy-rotate-flip/

database_name = "COVID-19_Radiography_Dataset"


qtd_max_imgs = 3616   
gray = toGray()

for i in range(1, qtd_max_imgs+1):
    id = str(i)

    path_covid = "./database/"+database_name+"/COVID/COVID-"+id+".png"

    img_covid = cv2.imread(path_covid)

    img_covid_flip = cv2.flip(img_covid, 1) # Flip horizontally 

    new_id = i+qtd_max_imgs
    new_id = str(new_id)

    path_covid_flip = "./database/"+database_name+"/COVID/COVID-"+new_id+".png"

    cv2.imwrite(path_covid_flip, img_covid_flip)

    


