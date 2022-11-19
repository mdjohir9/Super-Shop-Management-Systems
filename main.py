from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime

class Billing_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Billing Software")

        #**********Variavle******#
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()

        #####Product Catagoris list
        self.Category=["Select options","Clothing","LifeStyle","Mobiles"]
        self.SubCatClothing=["Pant","T-Shirt","Shirt"]
        self.pant=["Levis","Mufti","Spykar"]
        self.price_leavis=5000
        self.price_mufti=7000
        self.price_spykar=8000

        self.t_shart=["polo","Roadstar","Jack&jones"]
        self.price_polo=1500
        self.price_Roadstar=1800
        self.price_Jackjons=1700

        self.Shart=["Peter England","louis phillipe","Park Avenue"]
        self.price_peter=2100
        self.price_Louis=2700
        self.price_Park=1700

        #LifeStyle

        self.SubCatLifeStyle = ["Bath Soap", "Face Creame", "Hair Oil"]
        self.Bath_soap=["Lifebuy","Lux","Santor","Pearl"]
        self.price_Life=float(25)
        self.price_lux=35
        self.price_santor=20
        self.price_pearl=30

        self.face_creame=["Fair&lovely","Ponds","olay","Garniar"]
        self.price_fair=120
        self.price_ponds=180
        self.price_olay=155
        self.price_garniar=80

        self.hair_oil=["DubberAmla","Belifull","Novaratno","juie"]
        self.price_dubr=130
        self.price_belifull=150
        self.price_Novaratno=120
        self.price_juie=90

        #mobiel sub contact

        self.SubCatmobiel = ["Iphone", "Sumsung", "Xiome","RealMe","Oneplus"]
        self.iphone=("Iphone_X","Iphone_11","Iphone_12")
        self.price_x=40000
        self.price_i11=60000
        self.price_i12=85000

        self.samsung=["SumsungM16","SumsungM12","SumsungM21"]
        self.price_sm16=16000
        self.price_sm12=12000
        self.price_sm21=18000

        ###Xiomi
        self.xiome=["Redme11","Redmi-12","RedmiPro"]
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000

        self.realMe=["RealMe12","RealMe13","RealMePro"]
        self.price_rel12=25000
        self.price_rel13=22000
        self.price_relpro=30000

        self.oneplus=["Oppo-F9","Oppo-12","oppo-f20"]
        self.price_op_f9=45000
        self.price_op_f12=60000
        self.price_op_f20=45800





        ###first Image
        img1 = Image.open('images/mall.jpg')
        img1 = img1.resize((517, 140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1)
        lblimg.place(x=0, y=0, width=517, height=140)

        img2 = Image.open('images/girls.jpg')
        img2 = img2.resize((517, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2)
        lblimg.place(x=516, y=0, width=517, height=140)

        img3 = Image.open('images/girl1.jpg')
        img3 = img3.resize((517, 140), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3)
        lblimg.place(x=1032, y=0, width=517, height=140)

        lbl_title = Label(self.root, text='BILLING SOFTWARE MANAGEMENT SYSTEM', font=('times new roman', 35, 'bold'),bg='white',fg='red')
        lbl_title.place(x=0, y=140, width=1550, height=35)

        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl=Label(lbl_title, font=("times new roman","20","bold"),background="white",foreground="blue")
        lbl.place(x=5,y=(-10),width=150,height=50)
        time()


        main_frame = Frame(self.root, bd=5, relief=GROOVE,bg="white")
        main_frame.place(x=0, y=180, width=1550, height=620)

        cust_frame = LabelFrame(main_frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        cust_frame.place(x=10, y=5, width=355, height=140)

        #customer Entry

        self.lbl_mobil = Label(cust_frame, font=("times new roman",12,"bold"),text="Mobil Number:", padx=2, pady=6,bg="white")
        self.lbl_mobil.grid(row=0, column=0, sticky=W)

        self.text_mobil = ttk.Entry(cust_frame,textvariable=self.c_phone,width=23, font=("arial", 12, "bold"))
        self.text_mobil.grid(row=0, column=1,padx=5,pady=6)

        self.lbl_cust_name=Label(cust_frame,font=("times new roman",12,"bold"),text="Customer Name:",padx=2,pady=6,bg="white")
        self.lbl_cust_name.grid(row=1,column=0,sticky=W)

        self.text_cust_name=ttk.Entry(cust_frame,textvariable=self.c_name,font=("arial",12,"bold"),width=23)
        self.text_cust_name.grid(row=1,column=1)

        self.lbl_cust_email=Label(cust_frame,font=("times new roman",12,"bold"),text="Email Adders:",padx=2,pady=6,bg="white")
        self.lbl_cust_email.grid(row=2,column=0,sticky=W)

        self.text_cust_email=ttk.Entry(cust_frame,textvariable=self.c_email,font=("arial",12,"bold"),width=23)
        self.text_cust_email.grid(row=2,column=1)

        #product label farame
        product_frame = LabelFrame(main_frame,text="Products",font=("times new roman",12,"bold"),bg="white",fg="red")
        product_frame.place(x=372, y=5, width=640, height=140)
        ##combobox
        self.lbl_cetagory = Label(product_frame, font=("times new roman",12,"bold"),text="Select Category:", padx=5, pady=2,bg="white")
        self.lbl_cetagory.grid(row=0, column=0, sticky=W)

        self.combo_category=ttk.Combobox(product_frame,value=self.Category,font=("arial",12,"bold"),width=23,state="readonly")
        self.combo_category.current(0)
        self.combo_category.grid(row=0,column=1,padx=5, pady=2,sticky=W)
        self.combo_category.bind("<<ComboboxSelected>>",self.Categories)

        #sub_catagoris
        self.lbl_sub_cetagory = Label(product_frame, font=("times new roman",12,"bold"),text="Sub Category:", padx=5, pady=2,bg="white")
        self.lbl_sub_cetagory.grid(row=1, column=0, sticky=W)

        self.combo_sub_category=ttk.Combobox(product_frame,value=[""],font=("arial",12,"bold"),width=23,state="readonly")
        self.combo_sub_category.grid(row=1,column=1,padx=5, pady=2,sticky=W)
        self.combo_sub_category.bind("<<ComboboxSelected>>", self.Product_add)

        # combo product name
        self.lbl_productname = Label(product_frame, font=("times new roman",12,"bold"),text="Product Name:", padx=5, pady=2,bg="white")
        self.lbl_productname.grid(row=2, column=0, sticky=W)

        self.combo_productname=ttk.Combobox(product_frame,textvariable=self.product,font=("arial",12,"bold"),width=23,state="readonly")
        self.combo_productname.grid(row=2,column=1,padx=5, pady=2,sticky=W)
        self.combo_productname.bind("<<ComboboxSelected>>", self.price)


        #pricy
        self.lbl_price = Label(product_frame, font=("times new roman",12,"bold"),text="Price:", padx=5, pady=2,bg="white")
        self.lbl_price.grid(row=0, column=2, sticky=W)

        self.combo_price=ttk.Combobox(product_frame, textvariable=self.prices, font=("arial",12,"bold"),width=20,state="readonly")
        self.combo_price.grid(row=0,column=3,padx=5, pady=2,sticky=W)
        ###qty
        self.lbl_qty = Label(product_frame, font=("times new roman",12,"bold"),text="Qty:", padx=5, pady=2,bg="white")
        self.lbl_qty.grid(row=1, column=2, sticky=W)

        self.qty_entry=ttk.Entry(product_frame,textvariable=self.qty,font=("arial",12,"bold"),width=22)
        self.qty_entry.grid(row=1,column=3,padx=5, pady=2,sticky=W)

        #Midel frame
        midel_frame=Frame(main_frame,bd=10)
        midel_frame.place(x=10,y=150,width=1000,height=340)


        img12 = Image.open('images/good.jpg')
        img12 = img12.resize((500, 340), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        lblimg = Label(midel_frame, image=self.photoimg12)
        lblimg.place(x=0, y=0, width=500, height=340)

        img13 = Image.open('images/mall.jpg')
        img13 = img13.resize((500, 340), Image.ANTIALIAS)
        self.photoimg13 = ImageTk.PhotoImage(img13)

        lblimg = Label(midel_frame, image=self.photoimg13)
        lblimg.place(x=499, y=0, width=500, height=340)


        ##Right fraame

        right_lavel_frame = LabelFrame(main_frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        right_lavel_frame.place(x=1030, y=45, width=480, height=440)

        #search frame
        serach_frame = Frame(main_frame,bg="white",bd="2")
        serach_frame.place(x=1030, y=10, width=480, height=40)

        self.lbl_bill = Label(serach_frame, font=("arial", 12, "bold"), text="Bill Number:", fg="white",bg="red")
        self.lbl_bill.grid(row=0, column=0,sticky=W, padx=5, pady=2)

        self.Entry_bill_number=ttk.Entry(serach_frame,textvariable=self.bill_no,font=("arial",12,"bold"),width=24)
        self.Entry_bill_number.grid(row=0,column=1,padx=2,sticky=W)

        self.btn_search=Button(serach_frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="orangered",fg="white",bd=2,width=15,height=1,cursor="hand1")
        self.btn_search.grid(row=0,column=2,padx=1,pady=2)


        scroll_y=Scrollbar(right_lavel_frame,orient=VERTICAL)
        self.textarea=Text(right_lavel_frame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Conuter lavel frame
        button_frame = LabelFrame(main_frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        button_frame.place(x=0, y=485, width=1520, height=125)

        self.lbl_sub_total = Label(button_frame, font=("times new roman",12,"bold"),text="Sub Total:", padx=5, pady=2,bg="white")
        self.lbl_sub_total.grid(row=0, column=0, sticky=W,padx=5,pady=2)

        self.Entry_sub_total=ttk.Entry(button_frame,textvariable=self.sub_total,font=("arial",12,"bold"),width=20)
        self.Entry_sub_total.grid(row=0,column=1,padx=5, pady=2,sticky=W)

        self.lbl_tex = Label(button_frame, font=("times new roman",12,"bold"),text="Gov Tex:", padx=5, pady=2,bg="white")
        self.lbl_tex.grid(row=1, column=0, sticky=W,padx=5,pady=2)

        self.text_tex=ttk.Entry(button_frame,textvariable=self.tax_input,font=("arial",12,"bold"),width=20)
        self.text_tex.grid(row=1,column=1,padx=5, pady=2,sticky=W)

        self.lbl_total_amount = Label(button_frame, font=("times new roman",12,"bold"),text="Total:", padx=5, pady=2,bg="white")
        self.lbl_total_amount.grid(row=2, column=0, sticky=W,padx=5,pady=2)

        self.text_total_amount=ttk.Entry(button_frame,textvariable=self.total,font=("arial",12,"bold"),width=20)
        self.text_total_amount.grid(row=2,column=1,padx=5, pady=2,sticky=W)

        ##button frame
        Btn_Frame=Frame(button_frame,bd=2,bg="White")
        Btn_Frame.place(x=325,y=0)


        self.btn_add_card=Button(Btn_Frame,command=self.AddItem,text="Add To Cart",font=("arial",15,"bold"),bg="orangered",fg="white",bd=2,width=15,height=2,cursor="hand1")
        self.btn_add_card.grid(row=0,column=0,padx=1)

        self.genaret_bill_btn=Button(Btn_Frame,command=self.gen_bill,text="Genaret Bill",font=("arial",15,"bold"),bg="orangered",fg="white",bd=2,width=15,height=2,cursor="hand1")
        self.genaret_bill_btn.grid(row=0,column=1,padx=1)

        self.save_btn=Button(Btn_Frame,command=self.save_bill,text="Save Bill",font=("arial",15,"bold"),bg="orangered",fg="white",bd=2,width=15,height=2,cursor="hand1")
        self.save_btn.grid(row=0,column=2,padx=1)

        self.print_btn=Button(Btn_Frame,command=self.iprint,text="Print",font=("arial",15,"bold"),bg="orangered",fg="white",bd=2,width=15,height=2,cursor="hand1")
        self.print_btn.grid(row=0,column=3,padx=1)

        self.clear_btn=Button(Btn_Frame,command=self.clear,text="Clear",font=("arial",15,"bold"),bg="orangered",fg="white",bd=2,width=15,height=2,cursor="hand1")
        self.clear_btn.grid(row=0,column=4,padx=1)

        self.exit_btn=Button(Btn_Frame,command=self.root.destroy,text="Exit",font=("arial",15,"bold"),bg="orangered",fg="white",bd=2,width=15,height=2,cursor="hand1")
        self.exit_btn.grid(row=0,column=5,padx=1)
        self.welcome()

        self.l=[]
    #******************Funcation Diclaretion******

    def welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\t\tWellcome To uor shoping mall")
        self.textarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END, f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END, "\n********************************************************")
        self.textarea.insert(END, f"\n Products\t\t\tQty\t\tPrice")
        self.textarea.insert(END, "\n********************************************************\n")

    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the product Name")
        else:
            self.textarea.insert(END,f"\n{self.product.get()}\t\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str("Rs.%.2f"%(sum(self.l))))
            self.tax_input.set(str("Rs.%.2f"%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str("Rs.%.2f"%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add to cart product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END, "\n********************************************************")
            self.textarea.insert(END, f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END, f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END, "\n********************************************************")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open("billes/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} Saved Successfully")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp(".txt")
        open(filename,"w").write(q)
        os.startfile(filename,"print")
    ##find function

    def find_bill(self):
        found="no"
        for i in os.listdir('billes/'):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'billes/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set("")
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()


    def Categories(self,event=""):
        if self.combo_category.get()=="Clothing":
            self.combo_sub_category.config(value=self.SubCatClothing)
            self.combo_sub_category.current(0)

        if self.combo_category.get() == "LifeStyle":
            self.combo_sub_category.config(value=self.SubCatLifeStyle)
            self.combo_sub_category.current(0)

        if self.combo_category.get() == "Mobiles":
            self.combo_sub_category.config(value=self.SubCatmobiel)
            self.combo_sub_category.current(0)

    def Product_add(self,event=""):
        if self.combo_sub_category.get()=="Pant":
            self.combo_productname.config(value=self.pant)
            self.combo_productname.current(0)

        if self.combo_sub_category.get()=="T-Shirt":
            self.combo_productname.config(value=self.t_shart)
            self.combo_productname.current(0)

        if self.combo_sub_category.get()=="Shirt":
            self.combo_productname.config(value=self.Shart)
            self.combo_productname.current(0)

        ##LifeStyle function
        if self.combo_sub_category.get()=="Bath Soap":
            self.combo_productname.config(value=self.Bath_soap)
            self.combo_productname.current(0)

        if self.combo_sub_category.get()=="Face Creame":
            self.combo_productname.config(value=self.face_creame)
            self.combo_productname.current(0)

        if self.combo_sub_category.get()=="Hair Oil":
            self.combo_productname.config(value=self.hair_oil)
            self.combo_productname.current(0)

        ####mobiel function

        if self.combo_sub_category.get()=="Iphone":
            self.combo_productname.config(value=self.iphone)
            self.combo_productname.current(0)

        if self.combo_sub_category.get()=="Sumsung":
            self.combo_productname.config(value=self.samsung)
            self.combo_productname.current(0)

        if self.combo_sub_category.get()=="Xiome":
            self.combo_productname.config(value=self.xiome)
            self.combo_productname.current(0)

        if self.combo_sub_category.get()=="RealMe":
            self.combo_productname.config(value=self.realMe)
            self.combo_productname.current(0)

        if self.combo_sub_category.get()=="Oneplus":
            self.combo_productname.config(value=self.oneplus)
            self.combo_productname.current(0)


    def price(self, event=""):
         ##Pant
        if self.combo_productname.get() == "Levis":
            self.combo_price.config(value=self.price_leavis)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Mufti":
            self.combo_price.config(value=self.price_mufti)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Spykar":
            self.combo_price.config(value=self.price_spykar)
            self.combo_price.current(0)
            self.qty.set(1)


        ###T_Shart
        if self.combo_productname.get() == "polo":
            self.combo_price.config(value=self.price_polo)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Roadstar":
            self.combo_price.config(value=self.price_Roadstar)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Jack&jones":
            self.combo_price.config(value=self.price_Jackjons)
            self.combo_price.current(0)
            self.qty.set(1)

        #Shirt

        if self.combo_productname.get() == "Peter England":
            self.combo_price.config(value=self.price_peter)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "louis phillipe":
            self.combo_price.config(value=self.price_Louis)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Park Avenue":
            self.combo_price.config(value=self.price_Park)
            self.combo_price.current(0)
            self.qty.set(1)
        ##life style
        if self.combo_productname.get() == "Lifebuy":
            self.combo_price.config(value=self.price_Life)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Lux":
            self.combo_price.config(value=self.price_lux)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Santor":
            self.combo_price.config(value=self.price_santor)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Pearl":
            self.combo_price.config(value=self.price_pearl)
            self.combo_price.current(0)
            self.qty.set(1)

        ############Face Creame
        if self.combo_productname.get() == "Fair&lovely":
            self.combo_price.config(value=self.price_fair)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Ponds":
            self.combo_price.config(value=self.price_ponds)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "olay":
            self.combo_price.config(value=self.price_olay)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Garniar":
            self.combo_price.config(value=self.price_garniar)
            self.combo_price.current(0)
            self.qty.set(1)
        #Heir oil
        if self.combo_productname.get() == "DubberAmla":
            self.combo_price.config(value=self.price_dubr)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Belifull":
            self.combo_price.config(value=self.price_belifull)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Novaratno":
            self.combo_price.config(value=self.price_Novaratno)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "juie":
            self.combo_price.config(value=self.price_juie)
            self.combo_price.current(0)
            self.qty.set(1)

    #Iphone
        if self.combo_productname.get() == "Iphone_X":
            self.combo_price.config(value=self.price_x)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Iphone_11":
            self.combo_price.config(value=self.price_i11)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Iphone_12":
            self.combo_price.config(value=self.price_i12)
            self.combo_price.current(0)
            self.qty.set(1)
    #Sumsung
        if self.combo_productname.get() == "SumsungM16":
            self.combo_price.config(value=self.price_sm16)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "SumsungM12":
            self.combo_price.config(value=self.price_sm12)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "SumsungM21":
            self.combo_price.config(value=self.price_sm21)
            self.combo_price.current(0)
            self.qty.set(1)

        #Xiomi
        if self.combo_productname.get() == "Redme11":
            self.combo_price.config(value=self.price_r11)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Redmi-12":
            self.combo_price.config(value=self.price_r12)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "RedmiPro":
            self.combo_price.config(value=self.price_rpro)
            self.combo_price.current(0)
            self.qty.set(1)

        #realme
        if self.combo_productname.get() == "RealMe12":
            self.combo_price.config(value=self.price_rel12)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "RealMe13":
            self.combo_price.config(value=self.price_rel13)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "RealMePro":
            self.combo_price.config(value=self.price_relpro)
            self.combo_price.current(0)
            self.qty.set(1)

        #Oppo
        if self.combo_productname.get() == "Oppo-F9":
            self.combo_price.config(value=self.price_op_f9)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "Oppo-12":
            self.combo_price.config(value=self.price_op_f12)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_productname.get() == "oppo-f20":
            self.combo_price.config(value=self.price_op_f20)
            self.combo_price.current(0)
            self.qty.set(1)




         #########title#####





if __name__== "__main__":
    root=Tk()
    obj=Billing_App(root)
    root.mainloop()
