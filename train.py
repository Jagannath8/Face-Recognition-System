from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        imgPath=r"C:\Users\DELL\Desktop\Face_Recognization2\img"
        

        title=Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),bg="white",fg="green")
        title.place(x=0,y=0,width=1530,height=45)

        # Top Image
        img_top=Image.open(imgPath+"/facialrecognition.png")
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        lab1=Label(self.root,image=self.photoimg_top)
        lab1.place(x=0,y=55,width=1530,height=325)

        # Button
        b1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1.place(x=0,y=380,width=1530,height=60)

    

        # Bottom Image
        img_bottom=Image.open(imgPath+"/clg.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        lab2=Label(self.root,image=self.photoimg_bottom)
        lab2.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # Gray Scale Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Trainning", imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #============================= Train the classifier and save ========================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destoryAllWindows()
        messagebox.showinfo("Result","Trainning DataSet Completed")

        





if __name__=="__main__":
	root=Tk()
	obj=Train(root)
	root.mainloop()