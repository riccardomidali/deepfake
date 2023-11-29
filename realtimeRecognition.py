#import della libreria
from deepface import DeepFace

#esegue la funzione "stream"
DeepFace.stream("database")

#aprirà la webcam e mostrerà gli attributi del volto inquadrato
#inoltre lo confronta con quelli presenti nella cartella "database" e mostra se ci sono dei match

#!! per terminare l'esecuzione digitare crtl+c sul terminale !!