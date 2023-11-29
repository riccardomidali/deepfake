#import delle librerie
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

#inserire qui il percorso dell'immagine da analizzare
img_path = 'database/img3.jpg'

#apre l'immagine
img = cv2.imread(img_path)

#la converte in spazio colore RGB per una corretta visualizzazione
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#analizza le caratteristiche utilizzanto "Deepface.analyze"
obj = DeepFace.analyze(img_path, actions = ['age', 'gender', 'race', 'emotion'])
output = "age: "+str(obj[0]["age"])+" years old\nrace: "+str(obj[0]["dominant_race"])+"\nemotion: "+str(obj[0]["dominant_emotion"])+"\ngender: "+str(obj[0]["dominant_gender"])

#mostra a video l'immagine e le caratteristiche
plt.imshow(img_rgb)
plt.figtext(0.5, 0.01, output, ha='center', va='bottom', fontsize=12)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)
plt.axis('off')
plt.show()