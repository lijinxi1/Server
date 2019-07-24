#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2
import shutil


class FaceProcess(object):
    """
    为每个学生训练单独的模型
    """
    data_folder = '../DataSet/PICS'
    model_folder = '../DataSet/MODELS'

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
        for stu_img in os.listdir(self.data_folder):
            # 中文路径
            img = cv2.imdecode(np.fromfile(os.path.join(self.data_folder, stu_img), dtype=np.uint8), cv2.IMREAD_COLOR)
            face, img = self.detect_face(img)
            if face:
                img = cv2.resize(img, (200, 200))
                # cv2.imwrite('save.jpg',img)
                img = np.array(img, 'uint8')
                faces.append(img)
                labels.append(int(self.stu_id))
            os.remove(os.path.join(self.data_folder, stu_img))
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
            os.remove(self.model_folder)
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
        gray = cv2.equalizeHist(gray)
        self.face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(90, 90))
        if len(faces) == 0:
            return None, None
        if len(faces) > 1:
            return None
        (x, y, w, h) = faces[0]
        return (x, y, w, h), gray[y - 10:y + h + 10, x - 10:x + w + 10]

    def face_recognition(self, img_file):
        """
        人脸识别,输出相应信息
        :param img_file:
        :return:
        """
        img = cv2.imread(img_file)
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        shutil.move(os.path.join(self.model_folder, self.stu_id + '.yml'), self.stu_id + '.yml')
        recognizer.read(self.stu_id + '.yml')
        shutil.move(self.stu_id + '.yml', os.path.join(self.model_folder, self.stu_id + '.yml'), )  # 删除
        face, gray = self.detect_face(img)
        if face:
            gray = cv2.resize(gray, (200, 200))
            (x, y, w, h) = face
            cv2.rectangle(gray, (x, y), (x + w, y + h), (232, 138, 30), 1)
            gray = np.array(gray, 'uint8')
            face_id, confidence = recognizer.predict(gray)
            if confidence < 50:
                print("unknown")
            else:
                img = self.change_cv2_draw(img, 'stu_id:' + str(face_id), (x + w + 5, y), 20, (0, 0, 255))
            cv2.namedWindow('hello')
            cv2.imshow('hello', img)
            cv2.imwrite('result.jpg', img)
            cv2.waitKey(0)


if __name__ == '__main__':
    # fp=FaceProcess('通信1602','20164767')
    # fp.train()
    fp = FaceProcess('计算机1601', '20164767')
    # fp.train()
    fp.face_recognition('test.jpg')
