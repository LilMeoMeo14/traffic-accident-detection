import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture('road.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    # Vẽ bounding boxes
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # Lấy tọa độ (x1, y1, x2, y2)
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]  # độ tin cậy
            cls = int(box.cls[0])  # ID lớp
            label = model.names[cls]
            
            # Vẽ khung và nhãn
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, f"{label} {conf:.2f}",
                        (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 255), 2)

    
    # Hiển thị kết quả
    cv2.imshow('Car Detection',frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()