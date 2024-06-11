import cv2

import sys
#añadir esto para asegurar que el entorno considere todos los paquetes
mypath = "C:/Users/joaqu/AppData/Local/Programs/Python/Python312/Lib/site-packages" # TIP: This path is printed out in the terminal when installing this Python version with Homebrew
if mypath not in sys.path:
	sys.path = [mypath] + sys.path

import mediapipe as mp


cap = cv2.VideoCapture(0) #probar cual es tu camara xd


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.Hands(
    static_image_mode=False, #si se trata de un video donde varios frames son repetidos, poner false porq no conviene hacer el analisis cada frame por cuesqtion de recursos
    max_num_hands=2,
    min_detection_confidence=0.5) as hands: 
    
    while True:
        ret, frame = cap.read()
        if ret == False:
            
            break
          
        height, width, _ = frame.shape
        frame = cv2.flip(frame,1) #asi lo ve media pipe o lo quremos asi para verlo espejo jaja
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks is not None:
             for hand_landmarks in results.multi_hand_landmarks:
                  mp_drawing.draw_landmarks(
                       frame,hand_landmarks, mp_hands.HAND_CONNECTIONS
                  )

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xff == 27:
             break

cap.release()
cv2.destroyAllWindows()