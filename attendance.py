from tkinter import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")
        imgPath=r"C:\Users\DELL\Desktop\Face_Recognization2\img"

        #================================== variable ==================================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        
        # bg image
        img3=Image.open(imgPath+"/bg.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_lab=Label(self.root,image=self.photoimg3)
        bg_lab.place(x=0,y=0,width=1530,height=710)

        # title
        title=Label(bg_lab,text="FACE RECOGNITION MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title.place(x=0,y=0,width=1530,height=45)

        # main frame
        main_frame=Frame(bg_lab,bd=2)
        main_frame.place(x=20,y=55,width=1480,height=600)

        # left frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        
        # left label frame image
        img_left=Image.open(imgPath+"/girl.jpeg")
        img_left=img_left.resize((720,150),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        lab2=Label(left_frame,image=self.photoimg_left)
        lab2.place(x=5,y=0,width=720,height=150)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=400)

        # lable and entry
        # attendance id
        attendanceId_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",13,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,sticky=W)

        # Roll
        rollId_label=Label(left_inside_frame,text="Roll:",font=("times new roman",13,"bold"),bg="white")
        rollId_label.grid(row=0,column=2,padx=30,pady=8)

        rollID_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        rollID_entry.grid(row=0,column=3,pady=8)

        # Name
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        name_label.grid(row=1,column=0)

        name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=22,font=("times new roman",13,"bold"))
        name_entry.grid(row=1,column=1,pady=8)

        # Department
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=1,column=2)

        dep_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=22,font=("times new roman",13,"bold"))
        dep_entry.grid(row=1,column=3,pady=8)

        # Time
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        time_label.grid(row=2,column=0)

        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=22,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,pady=8)

        # Date
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        date_label.grid(row=2,column=2)

        date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=22,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,pady=8)

        # Attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status",bg="white",font=("times new roman",11,"bold"))
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,width=22,font=("times new roman",11,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)

        save_btn=Button(btn_frame,text="Import csv",command=self.impoerCSV,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCSV,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)





        # right frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        # ============================== scroll bar table ==============================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
		
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # ========================= fetch data ===============================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #================================ import csv =================================
    def impoerCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #================================ export csv =================================
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found.",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="")as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" sucessfully")
        except Exception as ex:
            messagebox.showerror("Error",f"Due to :{str(ex)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_focus=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_focus)
        data=content["values"]

        self.var_atten_id.set(data[0])
        self.var_atten_roll.set(data[1])
        self.var_atten_name.set(data[2])
        self.var_atten_dep.set(data[3])
        self.var_atten_time.set(data[4])
        self.var_atten_date.set(data[5])
        self.var_atten_attendance.set(data[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")

            
		

		



if __name__=="__main__":
	root=Tk()
	obj=Attendance(root)
	root.mainloop()