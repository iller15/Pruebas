import cv2
import sys
#añadir esto para asegurar que el entorno considere todos los paquetes
mypath = "C:/Users/joaqu/AppData/Local/Programs/Python/Python312/Lib/site-packages" # TIP: This path is printed out in the terminal when installing this Python version with Homebrew
if mypath not in sys.path:
	sys.path = [mypath] + sys.path


import mediapipe_static_image as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = 'hand_landmarker.task'

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(
    static_image_mode=True, #si se trata de un video donde varios frames son repetidos, poner false porq no conviene hacer el analisis cada frame por cuesqtion de recursos
    max_num_hands=2,
    min_detection_confidence=0.5) as hands: 
    
    image = cv2.imread("gracias.jpg")
    height, width, _ = image.shape
    image = cv2.flip(image, 1)

    # detecciones se hacen con imagnes en rgb

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    #Handedness
    #print("Handedness: ", results.multi_handedness)

    #Hand landmarks
    #print("Hand landmarks:", results.multi_hand_landmarks)

    if results.multi_hand_landmarks is not None:
        #---
        # Accedemos a los puntos en pixeles? de acuerdo a su nombre
        # coordenas aproximadas tho, pretty sure hay una mejor manera
        for hand_landmarks in results.multi_hand_landmarks:
            x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * width) #el x es para acceder a su coordenada en particular
            y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * height)
            print(x1)

            cv2.circle(image, (x1,y1), 3, (255,0,0),3)
        #----- 



    image = cv2.flip(image, 1)

cv2.imshow("Image", image)
cv2.waitKey(0) #hacer que espere terminar con un tecla random
cv2.destroyAllWindows()





#---
"""        #Dibujando los puntos y sus conexions con mediapipe
        for hand_landmarks in results.multi_hand_landmarks:
             #print(hand_landmarks)
             mp_drawing.draw_landmarks(image,hand_landmarks,mp_hands.HAND_CONNECTIONS, ##en que imagen, los 21 puntos a pinta?, para que se dibujen las coneciones,
                                       mp_drawing.DrawingSpec(color=(255,0,255), thickness=4, circle_radius=5), # spces de los puntos 
                                       mp_drawing.DrawingSpec(color=(25,134,255), thickness=4) #specs conexiones 
                                       )
        #----- """



#obtener puntas de los dedos mediante nombre
"""#---
        # Accedemos a los puntos en pixeles? de acuerdo a su nombre
        # coordenas aproximadas tho, pretty sure hay una mejor manera
        for hand_landmarks in results.multi_hand_landmarks:
            x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * width) #el x es para acceder a su coordenada en particular
            y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * height)
            print(x1)

            cv2.circle(image, (x1,y1), 3, (255,0,0),3)
        #----- """