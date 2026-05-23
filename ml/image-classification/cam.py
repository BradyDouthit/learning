import cv2
from ultralytics import YOLO
from datetime import datetime

model = YOLO("yolo26n.pt")
cap = cv2.VideoCapture("/dev/video0", cv2.CAP_V4L2)

print("Feed running. Press 's' to save a snapshot, 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection on the frame
    results = model(frame, verbose=False)
    annotated = results[0].plot()  # draws boxes + labels onto the frame

    # Overlay instructions
    cv2.putText(annotated, "S: snapshot  Q: quit", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Camera", annotated)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        filename = f"test_images/snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, annotated)
        print(f"Saved {filename}")

cap.release()
cv2.destroyAllWindows()
