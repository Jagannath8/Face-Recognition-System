#from PIL import Image

#im=Image.open("img/Debi.jpg")

#r=360
#o=im.rotate(r, expand=True)
#o.save('name.jpg')
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
from PIL import Image,ImageTk

imgg=[]
ang=StringVar()

class Test():

    def __init__(self, root):
        self.root=root
        self.root.geometry("600x600+0+0")
        self.root.title("Image Rotation")
        imgPath=r"C:\Users\DELL\Desktop\Face_Recognization2\img"

        

        down_frame=Frame(self.root,bd=2,bg="white")
        down_frame.place(x=20,y=500,width=570,height=100)

        

        ad_b1=Button(down_frame,text="Import Image",cursor="hand2",command=self.show_image,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        ad_b1.place(x=0,y=20,width=120,height=60)

        # Angle
        #Angle_label=Label(down_frame,text="Angle:",font=("times new roman",13,"bold"),bg="white")
        #Angle_label.grid(padx=10,pady=5,sticky=W)
        self.var_angle=StringVar()

        Angle_combo=ttk.Combobox(down_frame,font=("times new roman",15,"bold"),textvariable=self.var_angle,state="readonly",width=13)
        Angle_combo["values"]=("Select Angle","90","180","270","360")
        Angle_combo.current(0)
        Angle_combo.grid(padx=130,pady=20,sticky=W)
        ang=self.var_angle


        # Rotate
        ad_b3=Button(down_frame,text="Rotate",cursor="hand2",command=self.rotate,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        ad_b3.place(x=300,y=20,width=120,height=60)

        # Exit
        ad_b4=Button(down_frame,text="Exit",cursor="hand2",command=lambda: exit(),font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        ad_b4.place(x=430,y=20,width=125,height=60)

    def show_image(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
        img=Image.open(fln)
        img.thumbnail((350,350))
        img=ImageTk.PhotoImage(img)
        imgg.append(img)
        lbl=Label(root)
        lbl.configure(image=img)
        lbl.image=img
        lbl.pack()

    def rotate(self):
        if ang!="Select Angle":
            pass

        

if __name__=="__main__":
    root=Tk()
    obj=Test(root)
    root.mainloop()


