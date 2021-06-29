from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train 
from face_recognition import Face_Recognition
from attendance import Attendance

class Help:
	
	def __init__(self, root):
		self.root = root
		self.root.geometry("1530x790+0+0")
		self.root.title("Face Recognition System")
		imgPath=r"C:\Users\DELL\Desktop\Face_Recognization2\img"

		title=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
		title.place(x=0,y=0,width=1530,height=45)
		
		 # Top Image
		img_top=Image.open(imgPath+"/help.jpeg")
		img_top=img_top.resize((1530,720),Image.ANTIALIAS)
		self.photoimg_top=ImageTk.PhotoImage(img_top)

		lab=Label(self.root,image=self.photoimg_top)
		lab.place(x=0,y=55,width=1530,height=720)

		infoLab=Label(self.root,text="Contact Email",font=("times new roman",30,"bold"),bg="white",fg="darkblue")
		infoLab.place(x=600,y=100)

		lab1=Label(self.root,text="Email: 19cse035.sambitkumarkhandai@giet.edu",font=("times new roman",25,"bold"),bg="white",fg="darkblue")
		lab1.place(x=450,y=290)

		lab2=Label(self.root,text="Email: 19cse032.debidattarout@giet.edu",font=("times new roman",25,"bold"),bg="white",fg="darkblue")
		lab2.place(x=450,y=230)

		lab3=Label(self.root,text="Email: 19cse091.jagannathpal@giet.edu",font=("times new roman",25,"bold"),bg="white",fg="darkblue")
		lab3.place(x=450,y=170)

		tuto_btn=Image.open(r"C:\Users\DELL\Desktop\Face_Recognization2\img\btn1.png")
		tuto_btn=tuto_btn.resize((20,20),Image.ANTIALIAS)
		self.tutorial_btn=ImageTk.PhotoImage(tuto_btn)

		toto_Button=Label(self.root,image=self.tutorial_btn)
		toto_Button.place(x=315,y=545)
        
        
		
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()