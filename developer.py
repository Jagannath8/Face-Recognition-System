#install tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train 
from face_recognition import Face_Recognition
from attendance import Attendance

class Developer:
	
	def __init__(self, root):
		self.root = root
		self.root.geometry("1530x790+0+0")
		self.root.title("Face Recognition System")


		title=Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
		title.place(x=0,y=0,width=1530,height=45)
		
		 # Top Image
		img_top=Image.open("img/dev.jpg")
		img_top=img_top.resize((1530,720),Image.ANTIALIAS)
		self.photoimg_top=ImageTk.PhotoImage(img_top)

		lab1=Label(self.root,image=self.photoimg_top)
		lab1.place(x=0,y=55,width=1530,height=720)

		# Left Frame
		main_frame=Frame(lab1,bd=2,bg="white")
		main_frame.place(x=15,y=50,width=450,height=600)

		info_lab=Label(main_frame,text="------------ Personal Info -----------",font=("times new roman",15,"bold"),bg="white",fg="red")
		info_lab.place(x=20,y=0,width=300,height=20)

		info1_lab=Label(main_frame,text="Name: Sambit Kumar Khandai",font=("times new roman",20,"bold"),bg="white",fg="blue")
		info1_lab.place(x=-85,y=30,width=600,height=20)

		info2_lab=Label(main_frame,text="Sex: Male",font=("times new roman",20,"bold"),bg="white",fg="blue")
		info2_lab.place(x=-60,y=60,width=300,height=20)

		info3_lab=Label(main_frame,text="Year: 2nd",font=("times new roman",20,"bold"),bg="white",fg="blue")
		info3_lab.place(x=-60,y=90,width=300,height=20)

		info4_lab=Label(main_frame,text="Branch: CSE",font=("times new roman",20,"bold"),bg="white",fg="blue")
		info4_lab.place(x=-40,y=120,width=300,height=20)

		img_main2=Image.open("img/sambit1.jpg")
		img_main2=img_main2.resize((450,450),Image.ANTIALIAS)
		self.photoimg_main2=ImageTk.PhotoImage(img_main2)

		img_main_lbl=Label(main_frame,image=self.photoimg_main2)
		img_main_lbl.place(x=0,y=200,width=450,height=450)
		
		# Right Frame
		main_frame=Frame(lab1,bd=2,bg="white")
		main_frame.place(x=1050,y=50,width=450,height=600)

		info_lab=Label(main_frame,text="------------ Personal Info -----------",font=("times new roman",15,"bold"),bg="white",fg="red")
		info_lab.place(x=20,y=0,width=300,height=20)

		info1_lab=Label(main_frame,text="Name: Debidatta Rout",font=("times new roman",20,"bold"),bg="white",fg="blue")
		info1_lab.place(x=35,y=30,width=300,height=20)

		info2_lab=Label(main_frame,text="Sex: Male",font=("times new roman",20,"bold"),bg="white",fg="blue")
		info2_lab.place(x=-40,y=60,width=300,height=20)

		info3_lab=Label(main_frame,text="Year: 2nd",font=("times new roman",20,"bold"),bg="white",fg="blue")
		info3_lab.place(x=-40,y=90,width=300,height=20)

		info4_lab=Label(main_frame,text="Branch: CSE",font=("times new roman",20,"bold"),bg="white",fg="blue")
		info4_lab.place(x=-20,y=120,width=300,height=20)

		img_main=Image.open("img/let1.jpg")
		img_main=img_main.resize((450,450),Image.ANTIALIAS)
		self.photoimg_main=ImageTk.PhotoImage(img_main)

		img_main_lbl=Label(main_frame,image=self.photoimg_main)
		img_main_lbl.place(x=0,y=200,width=450,height=450)

		# Middle Frame
		main_frame1=Frame(lab1,bd=2,bg="white")
		main_frame1.place(x=530,y=50,width=450,height=600)

		info_lab=Label(main_frame1,text="------------ Personal Info -----------",font=("times new roman",15,"bold"),bg="white",fg="red")
		info_lab.place(x=20,y=0,width=300,height=20)

		info1_lab=Label(main_frame1,text="Name: Jagannath Pal",font=("times new roman",20,"bold"),bg="white",fg="blue")
		info1_lab.place(x=30,y=20,width=300,height=40)

		info2_lab=Label(main_frame1,text="Sex: Male",font=("times new roman",20,"bold"),bg="white",fg="blue")
		info2_lab.place(x=-40,y=58,width=300,height=20)

		info3_lab=Label(main_frame1,text="Year: 2nd",font=("times new roman",20,"bold"),bg="white",fg="blue")
		info3_lab.place(x=-40,y=88,width=300,height=20)

		info4_lab=Label(main_frame1,text="Branch: CSE",font=("times new roman",20,"bold"),bg="white",fg="blue")
		info4_lab.place(x=-20,y=118,width=300,height=20)


		img_main1=Image.open("img/jaga1.jpeg")
		img_main1=img_main1.resize((450,450),Image.ANTIALIAS)
		self.photoimg_main1=ImageTk.PhotoImage(img_main1)

		img_main_lbl1=Label(main_frame1,image=self.photoimg_main1)
		img_main_lbl1.place(x=0,y=200,width=450,height=450)



if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()