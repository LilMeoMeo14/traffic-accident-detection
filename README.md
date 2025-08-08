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
    ├── data/                         # Dữ liệu video test
    │   └── input_video.mp4
    ├── outputs/                      # Kết quả xuất ra
    │   ├── video_out.mp4
    │   └── accident_log.txt
    ├── models/                       # Trọng số YOLO
    │   └── yolov8n.pt
    ├── src/
    │   ├── main.py                   # Entry chính: gọi toàn bộ pipeline
    │   ├── detector.py               # Sử dụng YOLO để phát hiện object
    │   ├── tracker.py                # Theo dõi đối tượng
    │   ├── analyzer.py               # Phân tích sự kiện tai nạn
    │   ├── visualizer.py             # Vẽ kết quả, highlight tai nạn
    │   ├── logger.py                 # Ghi log + báo cáo sự kiện
    │   └── utils.py                  # Hàm hỗ trợ (ví dụ: đo khoảng cách)
    ├── notebooks/
    │   └── model_testing.ipynb       # Test YOLOv8 trước khi tích hợp
    ├── requirements.txt
    └── README.md