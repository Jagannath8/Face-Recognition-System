from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        imgPath=r"C:\Users\DELL\Desktop\Face_Recognization2\img"

        title=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red")
        title.place(x=0,y=0,width=1530,height=45)

        # left Image
        img_left=Image.open(imgPath+"/face_detector1.jpg")
        img_left=img_left.resize((650,700),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        lab1=Label(self.root,image=self.photoimg_left)
        lab1.place(x=0,y=55,width=650,height=700)

        # right Image
        img_right=Image.open(imgPath+"/face.jpg")
        img_right=img_right.resize((950,700),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        lab1=Label(self.root,image=self.photoimg_right)
        lab1.place(x=650,y=55,width=950,height=700)

        # Button
        ad_b1=Button(lab1,text="Face Recognition",cursor="hand2",command=self.face_rec,font=("times new roman",15,"bold"),bg="red",fg="white")
        ad_b1.place(x=365,y=620,width=200,height=40)
    
    #======================================= Attendance ======================================================
    def mark_attendance(self,id,roll,name,dep):
        with open("sambit.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for lines in myDataList:
                entry=lines.split(",")
                name_list.append(entry[0])
            if((id not in name_list) and (roll not in name_list) and (name not in name_list) and (dep not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{id},{roll},{name},{dep},{dtString},{d1},Present")

        

        


    # ======================================= face recognition ===============================================
    def face_rec(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y), (x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int(100*(1-predict/300))


                conn=mysql.connector.connect(host="localhost",username="root",password="Sambit",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                name=my_cursor.fetchone()
                name="+".join(name)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                roll=my_cursor.fetchone()
                roll="+".join(roll)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                dep=my_cursor.fetchone()
                dep="+".join(dep)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                id=my_cursor.fetchone()
                id="+".join(id)

                
                



                if confidence>77:
                    cv2.putText(img, f"ID: {id}", (x,y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                    cv2.putText(img, f"Roll: {roll}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                    cv2.putText(img, f"Name: {name}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                    cv2.putText(img, f"Department: {dep}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)
                    self.mark_attendance(id, roll, name, dep)
                else:
                    cv2.rectangle(img,(x,y), (x+w,y+h),(0,0,255),3)
                    cv2.putText(img, "Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3)

                coord=[x,y,w,y]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img


        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face Recognition", img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__=="__main__":
	root=Tk()
	obj=Face_Recognition(root)
	root.mainloop()