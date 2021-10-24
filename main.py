import cv2
from lbp import LocalBinaryPatterns as LBP
from to_gray import toGray

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

database_name = "COVID-19_Radiography_Dataset"
radius = 1
n_points = 8*radius

# Número máximo de imagens possível 3616
# vai ser treinado números iguais de imagens de COVID e NORMAL
qtd_max_imgs = 3616   

lbp = LBP(n_points, radius)
gray = toGray()

imgs_covid_lbp = []
imgs_normal_lbp = []
descriptor = []
data = []
label = []

for i in range(1,qtd_max_imgs+1):
    id = str(i)

    path_covid = "./database/"+database_name+"/COVID/COVID-"+id+".png"
    path_normal = "./database/"+database_name+"/Normal/Normal-"+id+".png"

    img_covid = cv2.imread(path_covid)
    img_covid = gray.image_to_gray(img_covid)

    img_normal = cv2.imread(path_normal)
    img_normal = gray.image_to_gray(img_normal)


    descriptor.append({"feature" : lbp.describe(img_covid), "label" : "COVID" })
    descriptor.append({"feature" : lbp.describe(img_normal), "label" : "NORMAL" })
    
    data.append(lbp.describe(img_covid))
    label.append("COVID")
    data.append(lbp.describe(img_normal))
    label.append("NORMAL")

x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.20)

clf = MLPClassifier( hidden_layer_sizes = ( 10, 10, 10), max_iter=500, activation = 'relu', solver = 'adam', random_state=0)

clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

print (accuracy_score(y_test, y_pred))
print (confusion_matrix(y_test, y_pred))
# Curva de aprendizado (olhar no keras)

    

# activation = 'identity', solver = 'sgd' 0.915 de accuracy


# cv2.imshow("imagem", imgs[0])
# cv2.waitKey(0)
# cv2.destroyAllWindows()