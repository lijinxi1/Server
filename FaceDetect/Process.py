import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2


class FaceProcess(object):
    """
    每个班级学生训练单独的数据,生成100张的图片数据,
    训练成功后删除人脸数据,保留人脸模型,增量训练
    """

    def __init__(self, _class,stu_id,increase=True):
        self._class=_class     # 班级
        self.stu_id=stu_id     # 学号
        self.data_folder=os.path.join('..','DataSet','PICS',_class)
        self.model=os.path.join('..','DataSet','MODELS',_class+'.yml')
        self.tmp_model=os.path.join('..','DataSet','MODELS','model.yml')     # 中文乱码问题
        self.face_cascade=None
        self.increase=increase        # 增量训练

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
        faces = []
        labels = []
        if not self.increase:
            for stu in os.listdir(self.data_folder):
                for img in os.listdir(os.path.join(self.data_folder,stu)):
                    image = Image.open(os.path.join(self.data_folder, stu,img)).convert('L')
                    image = np.array(image, 'uint8')
                    faces.append(image)
                    labels.append(int(stu))
            print(labels)
            return faces, labels
        else:
            for img in os.listdir(os.path.join(self.data_folder,self.stu_id)):
                image = Image.open(os.path.join(self.data_folder, self.stu_id, img)).convert('L')
                image = np.array(image, 'uint8')
                faces.append(image)
                labels.append(int(self.stu_id))
            print(labels)
            return faces, labels

    def train(self):
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        faces, labels = self.prepare_train_data()
        if self.increase:
            print('here')
            if os.path.exists(self.model):
                os.rename(self.model,self.tmp_model)
                face_recognizer.read(self.tmp_model)                        # 增量训练
                print('here 2')
        face_recognizer.train(faces, np.array(labels))
        print(self.model,self.tmp_model)
        if os.path.exists(self.tmp_model):
            os.remove(self.tmp_model)
        face_recognizer.save(self.tmp_model)  # 保存
        if os.path.exists(self.model):
            os.remove(self.model)
        os.rename(self.tmp_model,self.model)

    def detect_face(self,img):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray=cv2.equalizeHist(gray)
        self.face_cascade=cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_default.xml')
        faces=self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(90, 90))
        if len(faces)==0:
            return None,None
        if len(faces)>1:
            return None
        (x,y,w,h)=faces[0]
        return (x,y,w,h),gray[y:y+h,x:x+w]

    def face_recognition(self,img_file):
        img=cv2.imread(img_file)
        recognizer=cv2.face.LBPHFaceRecognizer_create()
        os.rename(self.model,self.tmp_model)
        recognizer.read(self.tmp_model)
        os.rename(self.tmp_model,self.model)
        face,gray=self.detect_face(img)
        if face:
            gray=cv2.resize(gray,(200,200))
            (x,y,w,h)=face
            cv2.rectangle(img, (x, y), (x + w, y + h), (232, 138, 30), 1)
            gray=np.array(gray,'uint8')
            face_id,confidence=recognizer.predict(gray)
            if confidence<50:
                print("unknown")
            else:
                img=self.change_cv2_draw(img,'stu_id'+str(face_id), (x + w + 5, y), 20, (0, 0, 255))
            cv2.namedWindow('hello')
            cv2.imshow('hello',img)
            print(self.data_folder,str(face_id))
            cv2.imwrite('result.jpg',img)
            cv2.waitKey(0)


if __name__ == '__main__':
<<<<<<< HEAD
    p=FaceProcess('通信1603',None,False)     # 20164859,20164797
=======
    p=FaceProcess('通信1603',20164897,False)     # 20164859,20164797
>>>>>>> dev
    p.train()
    # 增量训练
    #p=FaceProcess('通信1603','20164859',True)
    #p.train()
<<<<<<< HEAD
    p.face_recognition('test.jpg')
=======
    #p.face_recognition('test.jpg')
>>>>>>> dev
