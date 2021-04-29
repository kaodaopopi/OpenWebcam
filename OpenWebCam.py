import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # color to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display image
    cv2.imshow('frame', frame)
    # Press the q key to leave the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera device
cap.release()
cv2.destroyAllWindows()