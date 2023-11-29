#import delle librerie
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

#dichiarazione delle immagini
persona1 = 'database/img1.jpg'
persona2 = 'database/img4.jpg'

#funzione che legge e verifica se le immagini raffigurano la stessa persona
def verify(img1_path,img2_path):
    #legge le immagini
    img1= cv2.imread(img1_path)
    img2= cv2.imread(img2_path)

    #le converte in spazio colore RGB per una corretta visualizzazione
    img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    #crea un subplot per le immagini
    _, axes = plt.subplots(1, 2)  # 1 riga, 2 colonne per due immagini

    #mostra la prima immagine
    axes[0].imshow(img1_rgb)
    axes[0].set_title('Immagine 1')

    #mostra la seconda immagine
    axes[1].imshow(img2_rgb)
    axes[1].set_title('Immagine 2')

    #nasconde gli assi
    for ax in axes:
        ax.axis('off')

    #utilizza la funzione DeepFace.verify per confrontare le immagini
    output = DeepFace.verify(img1_path,img2_path)
    verification = output['verified']

    if verification:
       plt.figtext(0.5, 0.01, 'È la stessa persona', ha='center', va='bottom', fontsize=12)
    else:
       plt.figtext(0.5, 0.01, 'Non è la stessa persona', ha='center', va='bottom', fontsize=12)

    #mostra a video il confronto tra le immagini
    plt.tight_layout()  # Per garantire che le immagini non si sovrappongano
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2)# Per garantire che le immagini non si sovrappongano con il testo
    plt.show()

#chiamata della funzione
verify(persona1,persona2)