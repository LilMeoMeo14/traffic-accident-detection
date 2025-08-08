# traffic-accident-detection
Dự án phát hiện tai nạn giao thông, thông qua computer vision. Nhận diện và gửi cảnh báo đến cho hệ thống để kịp xử lý 

Mục tiêu của dự án:
Xây dựng hệ thống phát hiện tai nạn giao thông qua video camera giám sát sử dụng YOLOv8 + OpenCV, có thể:

    Phát hiện các đối tượng: xe máy, ô tô, người.

    Theo dõi chuyển động để xác định va chạm/ngã xe/dừng bất thường.

    Xác định tai nạn dựa vào:

        Thay đổi vị trí bất thường

        Vật thể không di chuyển sau va chạm

        Người ngã ra đường

    Ghi log và cảnh báo

    Hiển thị video output có highlight sự kiện tai nạn

Cấu Trúc Dự Án:
traffic_accident_detection/
├── data/ # Input test video data
│ └── input_video.mp4
├── outputs/ # Exported video and accident logs
│ ├── video_out.mp4
│ └── accident_log.txt
├── models/ # YOLO model weights
│ └── yolov8n.pt
├── src/ # Main source code
│ ├── main.py # Main entry to run the full pipeline
│ ├── detector.py # Use YOLO to detect vehicles, people
│ ├── tracker.py # Track objects across frames
│ ├── analyzer.py # Analyze motion to detect accidents
│ ├── visualizer.py # Draw results, highlight accidents
│ ├── logger.py # Log detected accident events
│ └── utils.py # Helper functions (e.g., distance calculation)
├── notebooks/ # Jupyter notebooks for model testing
│ └── model_testing.ipynb
├── requirements.txt # Python dependencies
└── README.md # This file
