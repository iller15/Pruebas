import cv2

# Initializing webcam
cap = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    print(ret)
    ##frame = cv2.resize(frame,(720,1280))

    # Display the resulting frame
    cv2.imshow('Webcam', frame)

    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()