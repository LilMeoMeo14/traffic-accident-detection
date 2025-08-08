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
