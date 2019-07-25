import cv2


def video_set(fileanme):
    cap = cv2.VideoCapture(fileanme)  # 打开相机
    frames=[]
    while (True):
        ret, frame = cap.read()  # 捕获一帧图像
        if ret:
            frames.append(frame)
        else:
            break
    cap.release()  # 关闭相机
    return frames
