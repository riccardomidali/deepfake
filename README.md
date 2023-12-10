# DeepFake utilizzando la libreria DeepFace

Link alla presentazione: https://www.canva.com/design/DAF2AYi_mxw/Zr2LEoWrNHFRFIuW-U0I9Q/edit?utm_content=DAF2AYi_mxw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

Questo progetto utilizza la libreria DeepFace per eseguire analisi e riconoscimento facciale su immagini.

## DeepFace
DeepFace è un efficiente framework per il riconoscimento facciale e l'analisi degli attributi progettato per Python. Questo strumento sfrutta modelli all'avanguardia come VGG-Face, Google FaceNet, OpenFace, Facebook DeepFace, DeepID, ArcFace, Dlib e SFace per riconoscere i volti e analizzare attributi come età, genere, emozioni ed etnia. Gli esperimenti dimostrano che mentre gli esseri umani raggiungono una precisione media del 97,53% nei compiti di riconoscimento facciale, i modelli racchiusi all'interno di DeepFace superano questo livello di precisione.

## Requisiti
Ogni modulo Python richiede le seguenti librerie installate e configurate correttamente:

- DeepFace: Per l'analisi facciale.
- Matplotlib: Utilizzato per la visualizzazione dei dati o delle immagini.
- OpenCV: Necessario per l'acquisizione e l'elaborazione delle immagini dalla webcam.

Puoi installarle utilizzando `pip install deepface`, `pip install matplotlib`, `pip install opencv-python` nel tuo terminale.

## Face Recognition
Il file `FaceRecognition.py` permette di valutare se due immagini in input raffigurano lo stesso volto. Utilizzando la libreria DeepFace, esegue un confronto tra le immagini per determinare la corrispondenza facciale.

## Face Attribute
Il modulo `FaceAttribute.py` accetta un'immagine contenente un volto e restituisce informazioni riguardanti età, genere, etnia e stato emotivo. Sfruttando le funzionalità di DeepFace, analizza i tratti facciali per fornire una descrizione.

## Real Time Recognition
Il file `RealTimeRecognition.py` offre le stesse funzionalità di `FaceAttribute`, ma funziona in tempo reale utilizzando la webcam. Riconosce e analizza i volti inquadrati dalla telecamera per fornire informazioni sul volto osservato.
