#install tkinter
from tkinter import *
from tkinter import ttk
#install PyPl ->  pip install Pillow
import tkinter
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from time import strftime 
from datetime import datetime
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help



class Face_recognition:
	
	def __init__(self, root):
		#super(Face_recognition, self).__init__()
		self.root = root
		self.root.geometry("1530x710+0+0")
		self.root.title("Face Recognition System")
		imgPath=r"C:\Users\DELL\Desktop\Face_Recognization2\img"


		# bg image

		img3=Image.open(imgPath+"/bg.png")

		img3=img3.resize((1530,710),Image.ANTIALIAS)
		self.photoimg3=ImageTk.PhotoImage(img3)

		bg_lab=Label(self.root,image=self.photoimg3)
		bg_lab.place(x=0,y=0,width=1530,height=710)

		# title

		title_lab=Label(bg_lab,text="FACE  RECOGNITION  SOFTWARE",font=("times new roman",45,"bold"),bg="white",fg="red")
		title_lab.place(x=0,y=0,width=1530,height=75)

		#==================== time==================
		def time():
			string=strftime('%H:%M:%S %p')
			lbl.config(text=string)
			lbl.after(1000, time)

		lbl=Label(title_lab,font=("times new roman ",14, "bold"),background="white",foreground="green")
		lbl.place(x=10,y=0,width=150,height=50)
		time()


		# Student Button

		img4=Image.open(imgPath+"/admin.jpg")
		img4=img4.resize((220,220),Image.ANTIALIAS)
		self.photoimg4=ImageTk.PhotoImage(img4)

		ad_b1=Button(bg_lab,image=self.photoimg4,command=self.student_Detail,cursor="hand2")
		ad_b1.place(x=200,y=100,width=220,height=220)

		ad_b1=Button(bg_lab,text="Student Detail",command=self.student_Detail,cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white")
		ad_b1.place(x=200,y=300,width=220,height=40)


		# Detect face Button

		img5=Image.open(imgPath+"/fd.jpg")
		img5=img5.resize((220,210),Image.ANTIALIAS)
		self.photoimg5=ImageTk.PhotoImage(img5)

		ad_b1=Button(bg_lab,image=self.photoimg5,cursor="hand2",command=self.face_data)
		ad_b1.place(x=500,y=100,width=220,height=220)

		ad_b1=Button(bg_lab,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="orange",fg="white")
		ad_b1.place(x=500,y=300,width=220,height=40)


		# Attend face Button

		img6=Image.open(imgPath+"/status.png")
		img6=img6.resize((220,200),Image.ANTIALIAS)
		self.photoimg6=ImageTk.PhotoImage(img6)

		ad_b1=Button(bg_lab,image=self.photoimg6,cursor="hand2",command=self.attendancE)
		ad_b1.place(x=800,y=100,width=220,height=220)

		ad_b1=Button(bg_lab,text="Check Status",cursor="hand2",command=self.attendancE,font=("times new roman",15,"bold"),bg="orange",fg="white")
		ad_b1.place(x=800,y=300,width=220,height=40)

		# Help Button

		img7=Image.open(imgPath+"/help.png")
		img7=img7.resize((200,180),Image.ANTIALIAS)
		self.photoimg7=ImageTk.PhotoImage(img7)

		ad_b1=Button(bg_lab,image=self.photoimg7,cursor="hand2",command=self.helper)
		ad_b1.place(x=1100,y=100,width=220,height=220)

		ad_b1=Button(bg_lab,text="Help",cursor="hand2",command=self.helper,font=("times new roman",15,"bold"),bg="orange",fg="white")
		ad_b1.place(x=1100,y=300,width=220,height=40)

		# Face Train Button

		img8=Image.open(imgPath+"/train.jpg")
		img8=img8.resize((250,200),Image.ANTIALIAS)
		self.photoimg8=ImageTk.PhotoImage(img8)

		ad_b1=Button(bg_lab,image=self.photoimg8,cursor="hand2",command=self.train_data)
		ad_b1.place(x=200,y=380,width=220,height=220)

		ad_b1=Button(bg_lab,text="Trainning",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="orange",fg="white")
		ad_b1.place(x=200,y=580,width=220,height=40)

		# photo Button

		img9=Image.open(imgPath+"/photo.png")
		img9=img9.resize((200,180),Image.ANTIALIAS)
		self.photoimg9=ImageTk.PhotoImage(img9)

		ad_b1=Button(bg_lab,image=self.photoimg9,cursor="hand2",command=self.open_img)
		ad_b1.place(x=500,y=380,width=220,height=220)

		ad_b1=Button(bg_lab,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="orange",fg="white")
		ad_b1.place(x=500,y=580,width=220,height=40)

		# Developer Button

		imgg=Image.open(imgPath+"/developer.jpg")
		imgg=imgg.resize((220,220),Image.ANTIALIAS)
		self.photoimgg=ImageTk.PhotoImage(imgg)

		ad_b1=Button(bg_lab,image=self.photoimgg,cursor="hand2",command=self.developer_open)
		ad_b1.place(x=800,y=380,width=220,height=220)

		ad_b1=Button(bg_lab,text="Developer",cursor="hand2",command=self.developer_open,font=("times new roman",15,"bold"),bg="orange",fg="white")
		ad_b1.place(x=800,y=580,width=220,height=40)

		# Exit Button

		imgg1=Image.open(imgPath+"/exit1.jpg")
		imgg1=imgg1.resize((220,220),Image.ANTIALIAS)
		self.photoimgg1=ImageTk.PhotoImage(imgg1)

		ad_b1=Button(bg_lab,image=self.photoimgg1,cursor="hand2",command=self.iExit)
		ad_b1.place(x=1100,y=380,width=220,height=220)

		ad_b1=Button(bg_lab,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="orange",fg="white")
		ad_b1.place(x=1100,y=580,width=220,height=40)

	def open_img(self):
		os.startfile("data")

	def iExit(self):
		self.iExit=tkinter.messagebox.askyesno("Face Recognization","Are you sure to exit this project",parent=self.root)
		if self.iExit>0:
			self.root.destroy()
		else:
			return
	# ================================ Function Buttton =================================

	def student_Detail(self):
		self.newWindow=Toplevel(self.root)
		self.app=Student(self.newWindow)

	def train_data(self):
		self.newWindow=Toplevel(self.root)
		self.app=Train(self.newWindow)

	def face_data(self):
		self.newWindow=Toplevel(self.root)
		self.app=Face_Recognition(self.newWindow)

	def attendancE(self):
		self.newWindow=Toplevel(self.root)
		self.app=Attendance(self.newWindow)

	def developer_open(self):
		self.newWindow=Toplevel(self.root)
		self.app=Developer(self.newWindow)

	def helper(self):
		self.newWindow=Toplevel(self.root)
		self.app=Help(self.newWindow)
		
			
		

		






if __name__=="__main__":
	root=Tk()
	obj=Face_recognition(root)
	root.mainloop()
