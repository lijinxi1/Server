#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2
import shutil
from .video import video_set


class FaceProcess(object):
    """
    为每个学生训练单独的模型
    """
    # 路径必须这样写
    data_folder = './DataSet/PICS'
    model_folder = './DataSet/MODELS'

    face_cascade = None

    def __init__(self, _class, stu_id, update=False):
        """
        班级,学号,是否更新数据
        :param _class:
        :param stu_id:
        :param update:
        """
        self._class = _class  # 班级
        self.stu_id = stu_id  # 学号
        self.data_folder = os.path.join(self.data_folder, _class, stu_id)  # 班级学生图片目录
        self.model_folder = os.path.join(self.model_folder, _class)  # 班级模型目录
        self.update = update

    @staticmethod
    def change_cv2_draw(image, str_, local, sizes, colour):
        """
        给图片添加文字
        :param image: 输入的图像,已读取
        :param str_: 添加的字符
        :param local: 位置
        :param sizes: 字体大小,单位px
        :param colour: 颜色RGB
        :return image:添加文字的图像
        """
        cv2img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(cv2img)
        draw = ImageDraw.Draw(pil_img)  # 图片上打印
        font = ImageFont.truetype('fzqgjt.ttf', sizes, encoding="utf-8")  # 加载字体
        draw.text(local, str_, colour, font=font)
        image = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
        return image

    def prepare_train_data(self):
        """
        准备训练数据
        :return:
        """
        faces = []
        labels = []
        # 判断是否为视频
        if len(os.listdir(self.data_folder))==1:
            for stu_video in os.listdir(self.data_folder):
                frames=video_set(os.path.join(self.data_folder, stu_video))
                os.remove(os.path.join(self.data_folder, stu_video))
                break
            for frame in frames:
                face, gray = self.detect_face(frame)
                if face:
                    gray = cv2.resize(gray, (200, 200))
                    # cv2.imwrite('save.jpg',img)
                    gray = np.array(gray, 'uint8')
                    faces.append(gray)
                    labels.append(int(self.stu_id))
        else:
            for stu_img in os.listdir(self.data_folder):
                # 中文路径
                img = cv2.imdecode(np.fromfile(os.path.join(self.data_folder, stu_img), dtype=np.uint8), cv2.IMREAD_COLOR)
                face, gray = self.detect_face(img)
                if face:
                    gray = cv2.resize(gray, (200, 200))
                    # cv2.imwrite('save.jpg',img)
                    gray = np.array(gray, 'uint8')
                    faces.append(gray)
                    labels.append(int(self.stu_id))
                os.remove(os.path.join(self.data_folder, stu_img))
        print(faces,labels)
        return faces, labels

    def train(self):
        """
        训练人脸数据
        :return:
        """
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        faces, labels = self.prepare_train_data()
        face_recognizer.train(faces, np.array(labels))
        if os.path.exists(os.path.join(self.model_folder, self.stu_id + '.yml')):
            os.remove(os.path.join(self.model_folder,self.stu_id+'.yml'))
        if not os.path.exists(self.model_folder):
            os.makedirs(self.model_folder)
        face_recognizer.save(self.stu_id + '.yml')  # 当前路径下生成
        shutil.move(self.stu_id + '.yml', os.path.join(self.model_folder, self.stu_id + '.yml'))

    def detect_face(self, img):
        """
        检测人脸
        :param img:
        :return:
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # gray = cv2.equalizeHist(gray)
        # 路径必须这样写
        self.face_cascade = cv2.CascadeClassifier('./ImageProcess/haarcascades/haarcascade_frontalface_default.xml')
        faces = self.face_cascade.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5, minSize=(90, 90))
        if len(faces) == 0:
            return None, None
        if len(faces) > 1:
            return None,None
        (x, y, w, h) = faces[0]
        return (x, y, w, h), gray[y :y + h , x :x + w]

    def face_recognition(self):
        """
        人脸识别,输出相应信息
        :return:
        """
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        shutil.move(os.path.join(self.model_folder, self.stu_id + '.yml'), self.stu_id + '.yml')
        recognizer.read(self.stu_id + '.yml')
        shutil.move(self.stu_id + '.yml', os.path.join(self.model_folder, self.stu_id + '.yml'), )  # 放回去
        for stu_img in os.listdir(self.data_folder):
            # 中文路径
            print(os.path.join(self.data_folder, stu_img))
            img = cv2.imdecode(np.fromfile(os.path.join(self.data_folder, stu_img), dtype=np.uint8), cv2.IMREAD_COLOR)
            os.remove(os.path.join(self.data_folder,stu_img))
            face, gray = self.detect_face(img)
            if face:
                recognized=None
                gray = cv2.resize(gray, (200, 200))
                (x, y, w, h) = face
                cv2.rectangle(img, (x, y), (x + w, y + h), (232, 138, 30), 1)
                gray = np.array(gray, 'uint8')
                face_id, confidence = recognizer.predict(gray)
                if confidence < 30:
                    recognized=False
                else:
                    img = self.change_cv2_draw(img, 'stu_id:' + str(face_id), (x + w + 5, y), 20, (0, 0, 255))
                    recognized=True
                cv2.imwrite('result.jpg', img)
                return recognized


if __name__ == '__main__':
    # fp=FaceProcess('通信1602','20164767')
    # fp.train()
    #fp = FaceProcess('计算机1601', '20164767')
    # fp.train()
    fp=FaceProcess('通信1603','20164797')
    fp.train()
    #fp.face_recognition()
