import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
from BlurWindow.blurWindow import blur
from ctypes import windll
import random
import webbrowser 
import base64
from PIL import Image
from io import BytesIO
import os
import os
import cv2
import numpy as np
import shutil
import datetime
from tkinter import messagebox



p = ctk.CTk()
x_res = 500
y_res = 800
p.geometry(f"{x_res}x{y_res}")
p.title("ATM Machine")
p.config(bg = '#323335')
p.wm_attributes('-transparent' , '#323335' )
p.update()
bground = windll.user32.GetForegroundWindow()
blur(bground)


CARD_INFO = "None"
BANK_INFO = 'None'
CARD_NO = 0
USERNAME = 'None'
CVV = 0
PIN = 0
PIN_For_Checking = 0
REAL_USER_INDEX = 0
TEXTFILE_NO = 0
TRANSACTION_INDEX = 0


Balance_Of_Sender = 0
Balance_Of_Receiver = 0
Transaction_Amount = 0
Sender_Index = 0
Receiver_Index = 0
Transaction_Number = 0
date = datetime.datetime.now()
Table2 = None

#Blue theme
Blue_Background = "#0B2447"
Front_Blue_Color = "#362FD9"
Cyan_Blue_Color = "#64CCC5"

#orange theme
Orange_Background = "#20262E"
Medium_Orange_Color = "#F15412"
Light_Orange_Color = "#FF8C32"


Background = Blue_Background
Medium_Background = Front_Blue_Color
Front_Background = Cyan_Blue_Color

 
Verify_Username = 'None'
Verify_Account_ID = 'None'

def Card_Input_Page():
     global x_res
     global y_res
     x_res = 500
     y_res = 600
     p.minsize(x_res,y_res)
     p.maxsize(x_res,y_res)
     global Background
     global Medium_Background
     global Front_Background
     
     Main_Frame = ctk.CTkFrame(p,fg_color='#323335')
     Main_Frame.pack(expand = True,fill = 'both')
     bgimg = Image.open("grey.png")
     img = ctk.CTkImage(bgimg,size=(300,300))


     Main_label = ctk.CTkLabel(Main_Frame,text='',fg_color=Background,height = 600,width = 400,corner_radius=30,bg_color='#323335')
     Main_label.pack(padx = 60,pady = 30,anchor = 'center')

     label = ctk.CTkLabel(Main_Frame,
                          fg_color=Medium_Background,
                          corner_radius=25,
                          width = 300,
                          bg_color=Background,
                          height =300,
                          text = 'INSERT CARD',
                          font = ('ubuntu' , 27,'bold'))
     label.place(relx = 0.21,rely = 0.1)

     def going_ahead():
          Main_Frame.destroy()
          ATM_Login_page()
          p.minsize(x_res,y_res)
          p.maxsize(x_res,y_res)
          

     def admin():
          Main_Frame.destroy()
          Login_Page()

     Registeration = ctk.CTkButton(Main_Frame,
                        text = 'Are You Admin? Click Here to Login As Admin',
                        fg_color = Background,
                        bg_color=Background,
                        corner_radius=25,
                        hover_color=Background,
                        width=47,
                        height=20,command=admin,
                        text_color=Front_Background)
     Registeration.place(relx = 0.23,rely = 0.85)

     insert_button = ctk.CTkButton(Main_Frame,
                                   text = 'Insert Card',
                                   fg_color=Background,
                                   bg_color = Background,
                                   corner_radius=25,
                                   width = 50
                                   ,height = 50
                                   ,font = ('ubuntu' ,15,'bold') 
                                   ,border_width=1,
                                   border_color = Front_Background,
                                   command=going_ahead)

     insert_button.place(relx = 0.5,rely = 0.68)


     def value_teller():
          global Background
          global Medium_Background
          global Front_Background
          
          
          nonlocal value
          theme = value.get()
          if theme == 1:
               Background = "#0B2447"
               Medium_Background = "#362FD9"
               Front_Background = "#64CCC5"
          else:
               Background = "#20262E"
               Medium_Background = "#F15412"
               Front_Background = "#FF8C32"
          Main_Frame.destroy()
          Card_Input_Page()

     value= ctk.IntVar()
     Radio_of_Orange = ctk.CTkRadioButton(Main_Frame,bg_color = Background,text = 'Blue Theme',text_color=Front_Background,variable=value,command = value_teller,value = 1)
     Radio_of_Orange.place(relx = 0.2,rely = 0.68)
     Radio_of_Orange = ctk.CTkRadioButton(Main_Frame,bg_color = Background,text = 'Orange Theme',text_color=Front_Background,variable = value,command = value_teller,value = 2)
     Radio_of_Orange.place(relx = 0.2,rely = 0.75)

def Card_Detail_input_page():

     global CARD_INFO
     global BANK_INFO
     global CARD_NO
     global USERNAME
     global CVV
     global PIN
     global TEXTFILE_NO
     TEXTFILE_NO = 0
     global x_res
     global y_res
     x_res = 700
     y_res = 500
     p.minsize(x_res,y_res)
     p.maxsize(x_res,y_res)
    
     Main_Frame = ctk.CTkFrame(p,fg_color='#323335')
     Main_Frame.pack(expand = True,fill = 'both')
     
     Main_label = ctk.CTkLabel(Main_Frame,
                               text='',
                               fg_color=Background,
                               height = 550,
                               width = 620,
                               corner_radius=30
                               ,bg_color='#323335')
     Main_label.pack(padx = 20,pady = 15,anchor = 'center')

     
     
     def back():
          with open("index NO.txt","r") as file:
               x = file.read() 
          try:
               os.remove(f"text folder\\{x}.txt")
          except:
               pass
          Main_Frame.destroy()
          Card_Input_Page()
     
     back = ctk.CTkButton(Main_Frame,
                         command = back,
                         fg_color='#191919'
                         ,hover_color='black',
                         text = 'Back',
                         text_color='white',
                         font = ('ubuntu' , 13 , 'bold'),
                         corner_radius=15,
                         width=50,
                         bg_color=Background
                         )
     back.place(relx = 0.08,rely = 0.88)
     
     
     
     label2 = ctk.CTkLabel(Main_Frame,
                           text = ':--Enter Your Card Info--:',
                           font = ('ubuntu' , 25 , 'bold','underline'),
                           fg_color=Background,
                           text_color='white'
                           )
     label2.place(relx = 0.3,rely = 0.05)

     Card_Type_label = ctk.CTkLabel(Main_Frame,
                           text = 'Card Type ',
                           font = ( 'ariel',18 , 'bold'),
                           fg_color=Background
                           )
     Card_Type_label.place(relx = 0.10,rely = 0.32)
     
     def card(choice):
          if choice == 'Visa Card':
               card_type_saver.configure(text = 'Visa_Card')
          elif choice == 'Master Card':
               card_type_saver.configure(text = 'Master_Card')
          elif choice == 'Credit Card':
               card_type_saver.configure(text = 'Credit_Card')
          else:
               card_type_saver.configure(text = 'Debit_Card')
     
     
     types_of_cards = ctk.CTkOptionMenu(Main_Frame,corner_radius=15,values=('Visa Card','Master Card','Credit Card','Debit Card'),command = card,fg_color = Front_Background,
                                        bg_color = Background)
     types_of_cards.place(relx = 0.25,rely = 0.32)

     card_type_saver = ctk.CTkLabel(Main_Frame,text = '')
     
     Card_Type_label = ctk.CTkLabel(Main_Frame,
                           text = 'Username',
                           font = ( 'san serif',18 , 'bold'),
                           fg_color=Background
                           )
     Card_Type_label.place(relx = 0.52,rely = 0.32)

     username_str = ctk.StringVar()
     username_Entry = ctk.CTkEntry(Main_Frame,
                           textvariable=username_str,
                           corner_radius=15,
                           fg_color=Background,
                           border_width=2,
                           border_color = Front_Background,
                           width = 150,
                           bg_color = Background,
                           placeholder_text='Enter Username here',
                           placeholder_text_color='red')
     username_Entry.place(relx = 0.67,rely = 0.32)
     username_Entry.configure(placeholder_text = 'Enter')
     
     Card_no = ctk.CTkLabel(Main_Frame,
                           text = 'Card No',
                           font = ( 'san serif',18 , 'bold'),
                           fg_color=Background
                           )
     Card_no.place(relx = 0.10,rely = 0.47)

     First_number = ctk.StringVar()
     card_no_part_1 = ctk.CTkEntry(Main_Frame,
                           width = 42,
                           fg_color=Background,
                           border_width=2,
                           border_color = Front_Background,
                           placeholder_text='0000',
                           textvariable=First_number)
     card_no_part_1.place(relx = 0.21,rely = 0.47)

     dash = ctk.CTkLabel(Main_Frame,
                         text = '-',
                         bg_color=Background).place(relx = 0.27,rely = 0.47)
     Second_number = ctk.StringVar()
     card_no_part_2 = ctk.CTkEntry(Main_Frame,
                           width = 42,
                           fg_color=Background,
                           border_width=2,
                           border_color = Front_Background,
                           placeholder_text='0000',
                           textvariable=Second_number )
     card_no_part_2.place(relx = 0.28,rely = 0.47)

     dash = ctk.CTkLabel(Main_Frame,
                         text = '-',
                         bg_color=Background).place(relx = 0.34,rely = 0.47)
     Third_number = ctk.StringVar()
     card_no_part_3 = ctk.CTkEntry(Main_Frame,
                           width = 42,
                           placeholder_text='0000',
                           fg_color=Background,
                           border_width=2,
                           border_color = Front_Background,
                           textvariable=Third_number)
     card_no_part_3.place(relx = 0.35,rely = 0.47)

     dash = ctk.CTkLabel(Main_Frame,
                         text = '-',
                         bg_color=Background).place(relx = 0.41,rely = 0.47)
     Fourth_number = ctk.StringVar()
     card_no_part_4 = ctk.CTkEntry(Main_Frame,
                           width = 42,
                           fg_color=Background,
                           border_width=2,
                           border_color = Front_Background,
                           placeholder_text='0000',
                           textvariable=Fourth_number)
     card_no_part_4.place(relx = 0.42,rely = 0.47)


     
     Card_no = ctk.CTkLabel(Main_Frame,
                           text = 'CVV',
                           font = ( 'san serif',18 , 'bold'),
                           fg_color=Background
                           )
     Card_no.place(relx = 0.60,rely = 0.47)

     cvvVar =  ctk.StringVar()
     cvv_Entry = ctk.CTkEntry(Main_Frame,
                        textvariable=cvvVar,
                           width = 42,
                           fg_color=Background,
                           border_width=2,
                           border_color = Front_Background,
                           placeholder_text='000')
     cvv_Entry.place(relx = 0.67,rely = 0.47)


     Bank = ctk.CTkLabel(Main_Frame,
                           text = 'Select Your Bank',
                           font = ( 'san serif',18 , 'bold'),
                           fg_color=Background
                           )
     Bank.place(relx = 0.29,rely = 0.17)
     browser_checker=0
     post = 0
     num = 0
     def enroll():
          nonlocal browser_checker
          nonlocal post
          global TEXTFILE_NO
          nonlocal num
          def Again():
               nonlocal browser_checker
               nonlocal post
               nonlocal num  
               global TEXTFILE_NO
               ans = messagebox.askyesno("Alert",f"Do you want to add another Fingerprint? {num} Fingerprints Added for this registeration")
               if ans:
                    browser_checker=0
                    post = 0
                    enroll()
               else:
                    f_p.configure(text = "Fingerprint Registration Successful")
                    f_p.configure(text_color = 'green')
                    TEXTFILE_NO = 1
                    FingerPrint_Enrollment.destroy()
                    Fingerprint_Checkbox.destroy()
          if browser_checker == 0:
               webbrowser.open("project.html")
               f_p.configure(text = "Place your Finger on the reader Single Time")
               f_p.configure(text_color = 'white')
               FingerPrint_Enrollment.configure(text = "Done")
               browser_checker = 1
               post = 0
               
          if post > 0:
               with open("index NO.txt","r") as file:
                         x = file.read()
               if os.path.exists("C:\\Users\\DELL\\Downloads\\t.txt"):
                         shutil.move("C:\\Users\\DELL\\Downloads\\t.txt" , f"text folder\\{x}.{num}.txt")
                         num = num+1
                         Again()
               else:
                    f_p.configure(text = "Something Went Wrong")
                    FingerPrint_Enrollment.configure(text = "Try Again")
                    browser_checker = 0
          else:
               post = 1
     
     Fingerprint_Final = False
     def Fingerprint_checker():
          nonlocal Fingerprint_yes_or_no
          nonlocal Fingerprint_Final
          Fingerprint_Checkbox_Value = Fingerprint_yes_or_no.get()
          print(Fingerprint_Checkbox_Value)
          if Fingerprint_Checkbox_Value == "0": 
               FingerPrint_Enrollment.configure(state = "disabled")
               FingerPrint_Enrollment.configure(text = "Register Your FingerPrint")
               f_p.configure(text = '')
               Fingerprint_Final = False
          else:
               FingerPrint_Enrollment.configure(state = "normal")
               FingerPrint_Enrollment.configure(text = "Register Your FingerPrint")
               Fingerprint_Final = True
          return Fingerprint_Checkbox_Value

     Fingerprint_yes_or_no = ctk.StringVar()
     Fingerprint_Checkbox = ctk.CTkCheckBox(Main_Frame,text = "Do You Want To Add Fingerprint?",bg_color=Background,
                                            variable=Fingerprint_yes_or_no,command = Fingerprint_checker)
     Fingerprint_Checkbox.place(relx = 0.60,rely = 0.63)


     FingerPrint_Enrollment = ctk.CTkButton(Main_Frame,
                                            text = "Register Your FingerPrint",
                                            width = 130,
                                            fg_color=Background,
                                            corner_radius=16,
                                            border_width=2,
                                            border_color = Front_Background,
                                            height = 50,
                                            state = 'disabled',
                                            bg_color = Background,
                                            command = enroll)
     FingerPrint_Enrollment.place(relx = 0.64,rely = 0.7)

     f_p = ctk.CTkLabel(Main_Frame,
                           text = '',
                           font = ( 'san serif',12 , 'bold'),
                           fg_color=Background,
                           bg_color = Background
                           )
     f_p.place(relx = 0.45,rely = 0.8)



     pin_code_label = ctk.CTkLabel(Main_Frame,
                           text = 'Set Pin Code',
                           font = ( 'san serif',18 , 'bold'),
                           fg_color=Background
                           )
     pin_code_label.place(relx = 0.10,rely = 0.60)

     pinVar = ctk.StringVar()
     pin_entry = ctk.CTkEntry(Main_Frame,
                        textvariable=pinVar,
                        fg_color=Background,
                           border_width=2,
                           border_color = Front_Background,
                           width = 42,
                           placeholder_text='000')
     pin_entry.place(relx = 0.27,rely = 0.60)

     def bank(choice):
          if choice == 'HBL':
               bank_type_saver.configure(text = 'HBL')
          elif choice == 'UBL':
               bank_type_saver.configure(text = 'UBL')
          elif choice == 'National Bank':
               bank_type_saver.configure(text = 'National_Bank')
          elif choice == 'Meezan Bank':
               bank_type_saver.configure(text = 'Meezan_Bank')
          elif choice == 'Allied Bank':
               bank_type_saver.configure(text = 'Allied_Bank')
          elif choice == 'Alfla Bank':
               bank_type_saver.configure(text = 'Alfla_Bank')
          else:
               bank_type_saver.configure(text = 'Al_Habib')

     Type_of_bank = ctk.CTkOptionMenu(Main_Frame,corner_radius=15,
                                      bg_color = Background,values=('HBL','National Bank','Meezan Bank','UBL','Allied Bank','Alfla Bank','Al Habib'),command = bank,fg_color = Front_Background)
     Type_of_bank.place(relx = 0.53,rely = 0.17)

     bank_type_saver = ctk.CTkLabel(Main_Frame,text = '')

     Bank_type_warning = ctk.CTkLabel(Main_Frame,
                                      text = '',
                                      text_color='red',
                                      bg_color=Background)
     Bank_type_warning.place(relx = 0.75,rely = 0.17)

     cvv_warning = ctk.CTkLabel(Main_Frame,text = '',text_color='red',bg_color=Background)
     cvv_warning.place(relx = 0.67,rely = 0.53)

     username_warning = ctk.CTkLabel(Main_Frame,text = '',text_color='red',bg_color=Background)
     username_warning.place(relx = 0.58,rely = 0.38)

     Card_number_warning = ctk.CTkLabel(Main_Frame,text = '',text_color='red',bg_color=Background)
     Card_number_warning.place(relx = 0.33,rely = 0.53)

     card_type_warning = ctk.CTkLabel(Main_Frame,
                                      text = '',
                                      text_color='red',
                                      bg_color=Background)
     card_type_warning.place(relx = 0.27,rely =0.38 )

     pin_warning = ctk.CTkLabel(Main_Frame,
                                      text = '',
                                      text_color='red',
                                      bg_color=Background)
     pin_warning.place(relx = 0.14,rely =0.66)

     def submit():
          
          global CARD_INFO
          global BANK_INFO
          global CARD_NO
          global USERNAME
          global CVV
          global PIN
          
          def destroyer():
               Main_Frame.destroy()
               Data_Base()

          
          username = username_str.get()

          if len(username) < 3 or username.isdigit() or len(username) > 14:
               username_Entry.configure(fg_color = 'red')
               username_warning.configure(text = 'Username must be from 3 to 14 alphabets')
          else:
               username_Entry.configure(fg_color = Background)
               username_warning.configure(text = '')
          cvv = cvvVar.get()
          if len(str(cvv)) != 3 or cvv.isalpha():
               cvv_warning.configure(text = 'Type Correct CVV')
               cvv_Entry.configure(fg_color = 'red')
          else:
               cvv_warning.configure(text = '')    
               cvv_Entry.configure(fg_color = Background)
          first_NO = First_number.get()
          second_NO = Second_number.get()
          third_NO = Third_number.get()
          fourth_NO = Fourth_number.get()
          if (first_NO.isalpha() or second_NO.isalpha() or third_NO.isalpha() or fourth_NO.isalpha()) or (len(first_NO) != 4 or len(second_NO) != 4 or len(third_NO) != 4 or len(fourth_NO) != 4):
               Card_number_warning.configure(text = 'Incorrect Card Number')
               if first_NO.isalpha() or len(first_NO) != 4:
                 card_no_part_1.configure(fg_color = 'red')
               else:
                   card_no_part_1.configure(fg_color = Background)
               if second_NO.isalpha() or len(second_NO) != 4:
                 card_no_part_2.configure(fg_color = 'red')
               else:
                   card_no_part_2.configure(fg_color = Background)
               if third_NO.isalpha() or len(third_NO) != 4:
                  card_no_part_3.configure(fg_color = 'red')
               else:
                   card_no_part_3.configure(fg_color = Background)
               if fourth_NO.isalpha() or len(fourth_NO) != 4:
                   card_no_part_4.configure(fg_color = 'red')
               else:
                   card_no_part_4.configure(fg_color = Background)
          else:
               Card_number_warning.configure(text = '')
               card_no_part_4.configure(fg_color = Background)
               card_no_part_3.configure(fg_color = Background)
               card_no_part_2.configure(fg_color = Background)
               card_no_part_1.configure(fg_color = Background)
          Bank_info = bank_type_saver.cget('text')
          if len(Bank_info) <1:
              Type_of_bank.configure(fg_color = 'red')
              Bank_type_warning.configure(text = 'Select the Bank')
          else:
              Type_of_bank.configure(fg_color = Front_Background)
              Bank_type_warning.configure(text = '')
          Card_info = card_type_saver.cget('text')
          if len(Card_info) < 1:
               types_of_cards.configure(fg_color = 'red')
               card_type_warning.configure(text = 'Select the Card Type')
          else:
               types_of_cards.configure(fg_color = Front_Background)
               card_type_warning.configure(text = '')
          pin = pinVar.get()
          if len(pin) != 4 or pin.isalpha():
               pin_entry.configure(fg_color = 'red')
               pin_warning.configure(text = 'PIN Should Be 4 Digits')
          else:
               pin_entry.configure(fg_color = Background)
               pin_warning.configure(text = '')

          if Fingerprint_Final:
               print(TEXTFILE_NO)
               if TEXTFILE_NO == 0:
                    f_p.configure(text = "First Register At Least One Fingerprint Then Submit")
                    f_p.configure(text_color = 'red')
               if TEXTFILE_NO == 0 or len(username) < 3 or username.isdigit() or len(str(cvv)) != 3 or cvv.isalpha() or (first_NO.isalpha() or second_NO.isalpha() or third_NO.isalpha() or fourth_NO.isalpha()) or (len(first_NO) != 4 or len(second_NO) != 4 or len(third_NO) != 4 or len(fourth_NO) != 4) or  len(Bank_info) <1 or  len(Card_info) < 1 or  len(pin) != 4 or pin.isalpha():
                    pass
               else:
                    Real_username = ''
                    for i in username:
                         if i == ' ':
                              Real_username = Real_username+"_"
                         else:
                              Real_username = Real_username+i


                    CARD_INFO = Card_info
                    BANK_INFO = Bank_info
                    CARD_NO = first_NO + second_NO + third_NO + fourth_NO
                    USERNAME = Real_username
                    CVV = cvv
                    PIN = pin
                    destroyer()
          else:

               if len(username) < 3 or username.isdigit() or len(str(cvv)) != 3 or cvv.isalpha() or (first_NO.isalpha() or second_NO.isalpha() or third_NO.isalpha() or fourth_NO.isalpha()) or (len(first_NO) != 4 or len(second_NO) != 4 or len(third_NO) != 4 or len(fourth_NO) != 4) or  len(Bank_info) <1 or  len(Card_info) < 1 or  len(pin) != 4 or pin.isalpha():
                    pass
               else:
                    Real_username = ''
                    for i in username:
                         if i == ' ':
                              Real_username = Real_username+"_"
                         else:
                              Real_username = Real_username+i


                    CARD_INFO = Card_info
                    BANK_INFO = Bank_info
                    CARD_NO = first_NO + second_NO + third_NO + fourth_NO
                    USERNAME = Real_username
                    CVV = cvv
                    PIN = pin
                    destroyer()
     
     Submit_Button = ctk.CTkButton(Main_Frame,
                                   text = "Submit",
                                   height = 30,
                                   corner_radius=30,
                                   bg_color=Background
                                   ,fg_color=Background
                                   ,border_width=1
                                   ,command = submit
                                   ,border_color=Front_Background
                                   )
     Submit_Button.place(relx = 0.40,rely = 0.87)

def Data_Base():


     
     
     
     
     
     global CARD_INFO
     global BANK_INFO
     global CARD_NO
     global USERNAME
     global CVV
     global PIN
    
     with open("index NO.txt",'r') as file:
          number = file.read()
          index = int(number)



     with open("Account ID.txt",'r') as file:
          Acc_ID_saver = file.read()
     Acc_ID_Array = Acc_ID_saver.split()    
     no1 = random.randint(0,9)
     no2 = random.randint(0,9)
     no3 = random.randint(0,9)
     no4 = random.randint(0,9)
     no5 = random.randint(0,9)
     Acc_id = str(no1)+str(no2)+str(no3)+str(no4)+str(no5)

     for i in Acc_ID_Array:
          if Acc_id == i: 
                    no1 = random.randint(0,9)
                    no2 = random.randint(0,9)
                    no3 = random.randint(0,9)
                    no4 = random.randint(0,9)
                    no5 = random.randint(0,9)
                    Acc_id = str(no1)+str(no2)+str(no3)+str(no4)+str(no5)

     Acc_ID_Array.insert(index,Acc_id)
     Acc_List = " ".join(Acc_ID_Array)
     with open("Account ID.txt","w") as file:
          file.write(Acc_List)




     with open('Card Type.txt','r') as file:
          card_info_saver= file.read()
     with open('Bank Type.txt','r') as file:
          bank_info_saver = file.read()
     with open('Card NO.txt','r') as file:
          card_no_saver = file.read()
     with open('CVV.txt','r') as file:
          cvv_saver = file.read()
     with open('PIN.txt','r') as file:
          pin_saver = file.read()
     with open('Username.txt','r') as file:
          username_saver = file.read()
     with open("Balance.txt","r") as file:
          balance_saver = file.read()
     
     Card_Info_Array= card_info_saver.split()
     Bank_Info_Array = bank_info_saver.split()
     Card_NO_Array = card_no_saver.split()
     CVV_Array = cvv_saver.split()
     PIN_Array = pin_saver.split()
     Username_Array = username_saver.split()
     balance_Array = balance_saver.split()

     Card_Info_Array.insert(index,CARD_INFO)
     Bank_Info_Array.insert(index,BANK_INFO)
     Card_NO_Array.insert(index,CARD_NO)
     CVV_Array.insert(index,CVV)
     PIN_Array.insert(index,PIN)
     Username_Array.insert(index,USERNAME)
     balance_Array.insert(index,'0')

     Card_Info_List = " ".join(Card_Info_Array)
     Bank_Info_List = " ".join(Bank_Info_Array)
     Card_NO_List = " ".join(Card_NO_Array)
     CVV_List = " ".join(CVV_Array)
     PIN_List = " ".join(PIN_Array)
     Username_List = " ".join(Username_Array)
     balance_List = " ".join(balance_Array)

     with open('Card Type.txt','w') as file:
          file.write(Card_Info_List)
     with open('Bank Type.txt','w') as file:
          file.write(Bank_Info_List)
     with open('Card NO.txt','w') as file:
          file.write(Card_NO_List)
     with open('CVV.txt','w') as file:
          file.write(CVV_List)
     with open('PIN.txt','w') as file:
          file.write(PIN_List)
     with open('Username.txt','w') as file:
          file.write(Username_List)
     with open("Balance.txt",'w') as file:
          file.write(balance_List)



     Final_index = index+1
     print(Final_index)
     with open("index NO.txt", "w") as file:
          file.write(str(Final_index))
     


     info = messagebox.showinfo("Info",f"Your Account Id is {Acc_id}")
     ATM_Login_page()

def ATM_Login_page():


     global x_res
     global y_res
     x_res = 500
     y_res = 600
     p.minsize(x_res,y_res)
     p.maxsize(x_res,y_res)

     Main_Frame = ctk.CTkFrame(p,fg_color='#323335')
     Main_Frame.pack(expand = True,fill = 'both')
     
     def Register():
          Main_Frame.destroy()
          Card_Detail_input_page()


     Tab = ctk.CTkTabview(Main_Frame,
                          width = 420,
                          height=600,
                          segmented_button_fg_color=Background,
                          segmented_button_selected_color=Medium_Background,
                          segmented_button_unselected_color= Background,
                          corner_radius=20,
                          fg_color=Background
                          )
     Tab.pack(padx = 30,pady = 10,anchor = 'center')
     Tab.add('Login Through PIN')
     Tab.add('Login Through Fingerprint')

     bgimg = Image.open("grey.png")
     img = ctk.CTkImage(bgimg,size=(320,100))
     Pin = ''

     ATM_pic = ctk.CTkLabel(Tab.tab("Login Through PIN"),
                          
                          text = Pin,
                          width=355,height=150,
                          corner_radius=25,
                          fg_color = Medium_Background,
                          font = ('ubuntu' , 35,'bold'))
     ATM_pic.place(relx = 0.03,rely = 0)

     def Digit_Checker():
          nonlocal Pin
          if len(Pin) > 4:
               Pin = Pin[:-1]
               ATM_pic.configure(text = Pin)




     def b1func():
          nonlocal Pin
          Pin = Pin+'1'
          ATM_pic.configure(text = Pin)
          Digit_Checker()
     b1 = ctk.CTkButton(Tab.tab("Login Through PIN"),
                        text = '1',
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        width=47,
                        height=47,
                        font=("PT Sans" , 18,"bold"),
                        command=b1func)
     b1.place(relx = 0.17,rely = 0.35)

     def b2func():
          nonlocal Pin
          Pin = Pin+'2'
          ATM_pic.configure(text = Pin)
          Digit_Checker()
     b2 = ctk.CTkButton(Tab.tab("Login Through PIN"),
                        text = '2',
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        width=47,
                        font=("PT Sans" , 18,"bold"),
                        height=47,command=b2func)
     b2.place(relx = 0.42,rely = 0.35)


     def b3func():
          nonlocal Pin
          Pin = Pin+'3'
          ATM_pic.configure(text = Pin)
          Digit_Checker()
     b3 = ctk.CTkButton(Tab.tab("Login Through PIN"),
                        text = '3',
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        font=("PT Sans" , 18,"bold"),
                        width=47,
                        height=47,command=b3func)
     b3.place(relx = 0.67,rely = 0.35)


     def b4func():
          nonlocal Pin
          Pin = Pin+'4'
          ATM_pic.configure(text = Pin)
          Digit_Checker()
     b4 = ctk.CTkButton(Tab.tab("Login Through PIN"),
                        text = '4',
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=40,
                        font=("PT Sans" , 18,"bold"),
                        width=47,
                        height=47,command=b4func)
     b4.place(relx = 0.17,rely = 0.47)


     def b5func():
          nonlocal Pin
          Pin = Pin+'5'
          ATM_pic.configure(text = Pin)
          Digit_Checker()
     b5 = ctk.CTkButton(Tab.tab("Login Through PIN"),
                        text = '5',
                        font=("PT Sans" , 18,"bold"),
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        width=47,
                        height=47,command=b5func)
     b5.place(relx = 0.42,rely = 0.47)


     def b6func():
          nonlocal Pin
          Pin = Pin+'6'
          ATM_pic.configure(text = Pin)
          Digit_Checker()
     b6 = ctk.CTkButton(Tab.tab("Login Through PIN"),
                        text = '6',
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        font=("PT Sans" , 18,"bold"),
                        width=47,
                        height=47,command=b6func)
     b6.place(relx = 0.67,rely = 0.47)


     def b7func():
          nonlocal Pin
          Pin = Pin+'7'
          ATM_pic.configure(text = Pin)
          Digit_Checker()
     b7 = ctk.CTkButton(Tab.tab("Login Through PIN"),
                        text = '7',
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        font=("PT Sans" , 18,"bold"),
                        width=47,
                        height=47,command=b7func)
     b7.place(relx = 0.17,rely = 0.59)


     def b8func():
          nonlocal Pin
          Pin = Pin+'8'
          ATM_pic.configure(text = Pin)
          Digit_Checker()
     b8 = ctk.CTkButton(Tab.tab("Login Through PIN"),
                        text = '8',
                        fg_color = Background,
                        bg_color=Background,
                        font=("PT Sans" , 18,"bold"),
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        width=47,
                        height=47,command=b8func)
     b8.place(relx = 0.42,rely = 0.59)


     def b9func():
          nonlocal Pin
          Pin = Pin+'9'
          ATM_pic.configure(text = Pin)
          Digit_Checker()
     b9 = ctk.CTkButton(Tab.tab("Login Through PIN"),
                        text = '9',
                        fg_color = Background,
                        bg_color=Background,
                        font=("PT Sans" , 18,"bold"),
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        width=47,
                        height=47,command=b9func)
     b9.place(relx = 0.67,rely = 0.59)


     def erase():
          nonlocal Pin
          Pin = Pin[:-1]
          ATM_pic.configure(text = Pin)
     b_erase = ctk.CTkButton(Tab.tab("Login Through PIN"),
                        text = 'X',
                        fg_color = Background,
                        bg_color=Background,
                        corner_radius=25,
                        border_color = Front_Background,
                        border_width=1,
                        font=("PT Sans" , 18,"bold"),
                        width=47,
                        height=47,command=erase)
     b_erase.place(relx = 0.17,rely = 0.71)


     def b0func():
          nonlocal Pin
          Pin = Pin+'0'
          ATM_pic.configure(text = Pin)
          Digit_Checker()
     b0 = ctk.CTkButton(Tab.tab("Login Through PIN"),
                        text = '0',
                        fg_color = Background,
                        bg_color=Background,
                        corner_radius=25,
                        border_color = Front_Background,
                        border_width=1,
                        width=47,
                        font=("PT Sans" , 18,"bold"),
                        height=47,command=b0func)
     b0.place(relx = 0.42,rely = 0.71)




     warning_label = ctk.CTkLabel(Main_Frame,
                                  text = '',
                                  bg_color = Medium_Background
                                  ,fg_color = Medium_Background,
                                  text_color='red')
     warning_label.place(relx = 0.40,rely = 0.16)

     def check():
          if len(Pin) == 4:
               global PIN_For_Checking
               PIN_For_Checking = Pin
               Main_Frame.destroy()
               Account_ID_Verifying()
          else:
               warning_label.configure(text = 'Enter Correct PIN')
     b_pass = ctk.CTkButton(Tab.tab("Login Through PIN"),
                        text = '->',
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        font=("PT Sans" , 18,"bold"),
                        width=47,
                        height=47,
                        command = check)
     b_pass.place(relx = 0.67,rely = 0.71)


     Registeration = ctk.CTkButton(Tab.tab("Login Through PIN"),
                        text = 'Not Registered? Click Here to Register',
                        fg_color = Background,
                        bg_color=Background,
                        corner_radius=25,
                        hover_color=Background,
                        width=47,
                        height=20,command=Register,
                        font=("PT Sans" , 13,"bold"),
                        text_color=Front_Background)
     Registeration.place(relx = 0.16,rely = 0.85)

     def Back():
          Main_Frame.destroy()
          Card_Input_Page()

     back_button = ctk.CTkButton(Tab.tab("Login Through PIN"),
                        text = 'Back',
                        fg_color = 'black',
                        bg_color=Background,
                        font=("PT Sans" , 13,"bold"),
                        corner_radius=25,
                        width=30,
                        height=30,command=Back)
     back_button.place(relx = 0.00001,rely = 0.92)
     
     bgimg = Image.open("FP.jpeg")
     img = ctk.CTkImage(bgimg,size=(350,350))
     
     image = ctk.CTkLabel(Tab.tab("Login Through Fingerprint"),image = img,text = '')
     image.place(relx = 0.04,rely = 0)


     post = 0
     browser_checker = 0
     def fingerprint():
          global REAL_USER_INDEX
          nonlocal browser_checker
          nonlocal post
          if browser_checker == 0:
               webbrowser.open("project.html")
               fp.configure(text = "Place your Finger on the reader Single Time")
               fp.configure(text_color = 'white')
               FingerPrint.configure(text = "Done")
               browser_checker = 1
               post = 0
          if post > 0:
               with open("index NO.txt","r") as file:
                         x = file.read()
               if os.path.exists("C:\\Users\\DELL\\Downloads\\t.txt"):
                    shutil.move("C:\\Users\\DELL\\Downloads\\t.txt" , f"LoginFingerPrints\\{x}.txt")
                    with open(f"LoginFingerPrints\\{x}.txt", "r") as file:
                         image_1_base64 = file.read()
                    for file in [file for file in os.listdir("text folder")]:
                         print(file)
                         with open(f"text folder\\{file}","r") as file2:
                              image_2_base64 = file2.read()

                         if match_fingers(image_1_base64,image_2_base64):
                              print("Matching")
                              b = ''
                              for i in file:
                                   b = b+i
                                   break
                              
                              REAL_USER_INDEX = int(b)
                              Main_Frame.destroy()
                              User_Option_Page()
                              break
                         else:
                              print("not matching")
                              fp.configure(text = "Fingerprint didn't matched")
                              fp.configure(text_color = 'red')
                              browser_checker = 0
                              FingerPrint.configure(text = "Try Again")

               else:
                    fp.configure(text = "try again")
                    fp.configure(text_color = 'red')         
          
          else:
               post = 1


     fp = ctk.CTkLabel(Tab.tab("Login Through Fingerprint"),text = 'Place Your Finger in Fingerprint Scanner',font = ( 'san serif', 15 , 'bold'),fg_color=Background)
     fp.place(relx = 0.1,rely = 0.90)


     FingerPrint = ctk.CTkButton(Tab.tab('Login Through Fingerprint'),
                                 text = "Click Here to Login With Fingerprint",
                                 width = 200,height = 60,
                                 fg_color = Background,
                                 border_width=2,
                                 border_color=Front_Background,
                                 command = fingerprint,
                                 corner_radius=25)
     FingerPrint.place(relx = 0.2,rely = 0.75)

def Account_ID_Verifying():
     global x_res
     global y_res
     x_res = 650
     y_res = 300
     p.minsize(x_res,y_res)
     p.maxsize(x_res,y_res)
     
     Main_Frame = ctk.CTkFrame(p,fg_color='#323335')
     Main_Frame.pack(expand = True,fill = 'both')


     Main_tab = ctk.CTkTabview(Main_Frame,fg_color=Background,height = 600,width = 600,corner_radius=30,bg_color=Background,segmented_button_selected_color=Medium_Background,segmented_button_unselected_color=Background
                               ,segmented_button_fg_color=Background)

     Main_tab.pack(padx = 5,pady = 12,anchor = 'center')
     Main_tab.add("Login Through Username")
     Main_tab.add("Login through Account ID")



     Heading_label = ctk.CTkLabel(Main_tab.tab("Login Through Username"),
                           text = 'Enter Your Username to Login',
                           font = ( 'san serif',18 , 'bold','underline'),
                           fg_color=Background
                           )
     Heading_label.place(relx = 0.24,rely = 0.00001)
     
     
     Card_Type_label = ctk.CTkLabel(Main_tab.tab("Login Through Username"),
                           text = 'Username',
                           font = ( 'san serif',18 , 'bold'),
                           fg_color=Background
                           )
     Card_Type_label.place(relx = 0.23,rely = 0.35)

     username_str = ctk.StringVar()
     username_Entry = ctk.CTkEntry(Main_tab.tab("Login Through Username"),
                           textvariable=username_str,
                           width = 150,
                           corner_radius=15,
                           fg_color=Background,
                           border_width=2,
                           border_color = Front_Background,
                           bg_color='transparent',
                           placeholder_text='Enter Username here',
                           placeholder_text_color='red')
     username_Entry.place(relx = 0.42,rely = 0.35)

     Account_label = ctk.CTkLabel(Main_tab.tab("Login through Account ID"),
                           text = 'Enter Your Account ID to Login',
                           font = ( 'san serif',18 , 'bold','underline'),
                           fg_color=Background
                           )
     Account_label.place(relx = 0.24,rely = 0.0001)

     
     Account_id_label = ctk.CTkLabel(Main_tab.tab("Login through Account ID"),
                           text = 'Account ID',
                           font = ( 'san serif',18 , 'bold'),
                           fg_color=Background
                           )
     Account_id_label.place(relx = 0.23,rely = 0.35)



     Acc_str = ctk.StringVar()
     Acc_ID_Entry = ctk.CTkEntry(Main_tab.tab("Login through Account ID"),
                           textvariable=Acc_str,
                           corner_radius=15,
                           fg_color=Background,
                           border_width=2,
                           border_color = Front_Background,
                           width = 150,
                           bg_color='transparent',
                           placeholder_text='Enter Username here',
                           placeholder_text_color='red')
     Acc_ID_Entry.place(relx = 0.42,rely = 0.35)

     Error_Label = ctk.CTkLabel(Main_tab.tab("Login through Account ID"),
                                text = "",fg_color=Background,bg_color=Background,
                                text_color='red')
     Error_Label.place(relx = 0.34,rely = 0.53)

     Eror_Label = ctk.CTkLabel(Main_tab.tab("Login Through Username"),
                                text = "",fg_color=Background,bg_color=Background,
                                text_color='red')
     Eror_Label.place(relx = 0.34,rely = 0.53)


     def Checking_Account_ID():
          nonlocal Acc_str
          global PIN_For_Checking
          global REAL_USER_INDEX
          Account_ID = Acc_str.get()

          if Account_ID.isalpha() or len(Account_ID) != 5:
               Acc_ID_Entry.configure(fg_color = 'red')
          else:
               Acc_ID_Entry.configure(fg_color = Background)
               with open("Account ID.txt", "r") as file:
                    u = file.read()
                    acc_data= u.split()
                    
                    for i in acc_data:
                        
                         print(i)
                         if i==Account_ID:
                              print("YES")
                              Error_Label.configure(text = "")

                              Index = acc_data.index(i)
                              with open("PIN.txt") as file:
                                   o = file.read()
                                   pin_data = o.split()
                                   if pin_data[Index] == PIN_For_Checking:
                                        REAL_USER_INDEX = Index
                                        Main_Frame.destroy()
                                        User_Option_Page()
                                   else:
                                        Error_Label.configure(text = "Account ID didn't Matched with PIN")
                         else:
                              Error_Label.configure(text = "Account ID not Found")
                                        

          



     def Checking_Username():
          nonlocal username_str
          global PIN_For_Checking
          global REAL_USER_INDEX
          
          Username = username_str.get()
          if Username.isdigit() or len(Username) == 0:
               username_Entry.configure(fg_color = 'red')
          else:
               username_Entry.configure(fg_color = Background)
               Acc_ID_Entry.configure(fg_color = Background)
               with open("Username.txt", "r") as file:
                    u = file.read()
                    acc_data= u.split()
                    
                    for i in acc_data:
                         print(i)
                         if i==Username:
                              Index = acc_data.index(i)
                              with open("PIN.txt") as file:
                                   o = file.read()
                                   pin_data = o.split()
                                   if pin_data[Index] == PIN_For_Checking:
                                        REAL_USER_INDEX = Index
                                        Main_Frame.destroy()
                                        User_Option_Page()
                                   else:
                                        Eror_Label.configure(text = "Username didn't Matched with PIN")
                         else:
                             Eror_Label.configure(text = "Username not Found")
                                        


     U_Submit_button = ctk.CTkButton(Main_tab.tab("Login through Account ID"),
                                   text = 'Login',
                                   fg_color=Background,
                                   bg_color=Background,
                                   corner_radius=25 ,
                                   border_width=1,
                                   border_color=Front_Background,
                                   command = Checking_Account_ID)
     U_Submit_button.place(relx = 0.37,rely = 0.8)

     A_Submit_button = ctk.CTkButton(Main_tab.tab("Login Through Username"),
                                   text = 'Login',
                                   fg_color=Background,
                                   bg_color=Background,
                                   border_width=1,
                                   border_color=Front_Background,
                                   corner_radius=25,
                                   command = Checking_Username
                                  )
     A_Submit_button.place(relx = 0.37,rely = 0.8)


     def back():
          Main_Frame.destroy()
          ATM_Login_page()

     Back_button = ctk.CTkButton(Main_tab.tab("Login Through Username"),
                                   text = 'Back',
                                   fg_color='black',
                                   bg_color=Background,
                                   corner_radius=25,
                                   command = back
                                   ,width = 50
                                  )
     Back_button.place(relx = 0,rely = 0.8)

     Back_button = ctk.CTkButton(Main_tab.tab("Login through Account ID"),
                                   text = 'Back',
                                   fg_color='black',
                                   bg_color=Background,
                                   corner_radius=25,
                                   command = back
                                   ,width = 50
                                  )
     Back_button.place(relx = 0,rely = 0.8)

def User_Option_Page():
     global x_res
     global y_res
     x_res = 1000
     y_res = 600
     p.minsize(x_res,y_res)
     p.maxsize(x_res,y_res)
     
     Main_Frame = ctk.CTkFrame(p,fg_color='#323335')
     Main_Frame.pack(expand = True,fill = 'both')


     Main_label = ctk.CTkLabel(Main_Frame,text='',fg_color=Background,height = 600,width = 1000,corner_radius=30,bg_color='#323335')
     Main_label.pack(padx = 20,pady = 10,anchor = 'center')
     

     def Withdraw():
          Main_Frame.destroy()
          Withdraw_Page()
     
     def Deposit():
          Main_Frame.destroy()
          Deposit_Page()
     
     def Fund_Transfer():
          Main_Frame.destroy()
          Fund_Transfer_Page()

     def balance_inquiry():
          Main_Frame.destroy()
          Balance_Inquiry()

     def pin_change():
          Main_Frame.destroy()
          Pin_Change()

     def Add_Fingerprint():
          Main_Frame.destroy()
          Add_FingerPrint()

     def fastcash():
          Main_Frame.destroy()
          Fast_Cash()


     opt_1 = ctk.CTkButton(Main_Frame,
                           text = 'Cash Withdraw',
                           fg_color = Background,
                           border_color = Front_Background,
                           border_width=2, 
                           width = 300,height=100,
                           corner_radius=25,
                           bg_color=Background,
                           command = Withdraw)
     opt_1.place(relx = 0.1,rely = 0.1)

     opt_2 = ctk.CTkButton(Main_Frame,
                           text = 'PIN Change',
                           width = 300,height=100,
                           fg_color = Background,
                           border_color = Front_Background,
                           border_width=2,
                           corner_radius=25,
                           bg_color=Background,
                           command = pin_change)
     opt_2.place(relx = 0.1,rely = 0.3)


     opt_3 = ctk.CTkButton(Main_Frame,
                           text = 'Deposit',
                           width = 300,height=100,
                           fg_color = Background,
                           border_color = Front_Background,
                           border_width=2,
                           corner_radius=25,
                           bg_color=Background,
                           command = Deposit)
     opt_3.place(relx = 0.1,rely = 0.5)


     opt_4 = ctk.CTkButton(Main_Frame,
                           text = 'Balance Inquiry',
                           width = 300,height=100,
                           corner_radius=25,
                           fg_color = Background,
                           border_color = Front_Background,
                           border_width=2,
                           bg_color=Background,
                           command = balance_inquiry)
     opt_4.place(relx = 0.36,rely = 0.7)


     opt_5 = ctk.CTkButton(Main_Frame,
                           text = 'Fund Transfer',
                           width = 300,height=100,
                           corner_radius=25,
                           fg_color = Background,
                           border_color = Front_Background,
                           border_width=2,
                           bg_color=Background,
                           command = Fund_Transfer)
     opt_5.place(relx = 0.6,rely = 0.1)


     opt_6 = ctk.CTkButton(Main_Frame,
                           text = 'Add Fingerprint',
                           width = 300,height=100,
                           corner_radius=25,
                           fg_color = Background,
                           border_color = Front_Background,
                           border_width=2,
                           bg_color=Background,
                           command = Add_Fingerprint)
     opt_6.place(relx = 0.6,rely = 0.3)


     opt_7 = ctk.CTkButton(Main_Frame,
                           text = 'Fast Cash',
                           width = 300,height=100,
                           corner_radius=25,
                           fg_color = Background,
                           border_color = Front_Background,
                           border_width=2,
                           bg_color=Background,
                           command = fastcash)
     opt_7.place(relx = 0.6,rely = 0.5)


     def LogOut():
          global REAL_USER_INDEX
          REAL_USER_INDEX = 0
          Main_Frame.destroy()
          ATM_Login_page()
     opt_Log_Out = ctk.CTkButton(Main_Frame,
                           text = 'Log Out',
                           width = 130,height=45,
                           corner_radius=25,
                           fg_color = Background,
                           border_color = 'red',
                           border_width=2,
                           bg_color=Background,
                           command=LogOut)
     opt_Log_Out.place(relx = 0.43,rely = 0.9)

def Withdraw_Page():
     global x_res
     global y_res
     x_res = 400
     y_res = 400
     p.minsize(x_res,y_res)
     p.maxsize(x_res,y_res)
     
     Main_Frame = ctk.CTkFrame(p,fg_color='#323335')
     Main_Frame.pack(expand = True,fill = 'both')


     Main_label = ctk.CTkLabel(Main_Frame,text='',fg_color=Background,height = 600,width = 400,corner_radius=30,bg_color='#323335')
     Main_label.pack(padx = 30,pady = 15,anchor = 'center')
     
     
     
     def withdraw():
          global REAL_USER_INDEX
          print(REAL_USER_INDEX)
          Amount = ammount.get()
          if Amount.isalpha() or len(Amount) == 0:
               Amount_Entry.configure(fg_color = 'red')
          else:
               Amount_Entry.configure(fg_color = Background)
               with open("Balance.txt","r") as file:
                    f = file.read()
                    b = f.split()
                    balance = b[REAL_USER_INDEX]
                    balance = int(balance)
                    Amount = int(Amount)   
                    print(balance)
                    print(Amount)
               
                    if balance < Amount:
                         error.configure(text = "insufficient Balance")
                         error.configure(text_color = "red")
                    else:
                         if Amount%500==0:
                              error.configure(text = "Withdraw Successful")
                              error.configure(text_color = 'white')
                              remaining = balance - Amount
                              b[REAL_USER_INDEX] = str(remaining)
                              k = " ".join(b)
                              with open("Balance.txt","w") as file:
                                   file.write(k)
                              ok_Button.configure(text = 'OK')
                              Withdraw_Button.destroy()
                         else:
                              error.configure(text = "Amount Should Be The Multiple of 500")
                              error.configure(text_color = "red")
                         


     def back():
          Main_Frame.destroy()
          User_Option_Page()
              

              

     ok_Button = ctk.CTkButton(Main_Frame,
                           text = '',
                           width = 100,height=55,
                           corner_radius=25,
                           fg_color=Background,
                           border_color=Front_Background,
                           border_width=2,
                           bg_color=Background,
                           command=back)
     ok_Button.place(relx = 0.37,rely = 0.7)
     
     Withdraw_Button = ctk.CTkButton(Main_Frame,
                           text = 'Withdraw',
                           width = 100,height=55,
                           corner_radius=25,
                           fg_color=Background,
                           border_color=Front_Background,
                           border_width=2,
                           bg_color=Background,
                           command=withdraw)
     Withdraw_Button.place(relx = 0.37,rely = 0.7)

     
     
     Heading = ctk.CTkLabel(Main_Frame,
                            bg_color=Background,
                            text = "Enter Withdraw Amount",
                            font = ('ubuntu' , 20 , 'bold'))
     Heading.place(relx = 0.23,rely = 0.16)

     error = ctk.CTkLabel(Main_Frame,
                            bg_color=Background,
                            text = "Amount Should Be The Multiple of 500",
                            text_color='white',
                            font = ('ubuntu' , 12 , 'bold','underline'))
     error.place(relx = 0.2,rely = 0.3)

     back_Button = ctk.CTkButton(Main_Frame,
                           text = 'Back',
                           width = 50,height=25,
                           corner_radius=25,
                           fg_color='black',
                           bg_color=Background,
                           command=back)
     back_Button.place(relx = 0.1,rely = 0.85)


     ammount = ctk.StringVar()
     Amount_Entry = ctk.CTkEntry(Main_Frame,textvariable=ammount,fg_color=Background,border_color=Front_Background,border_width=2 )
     Amount_Entry.place(relx = 0.33,rely = 0.4)

def Deposit_Page():
     global x_res
     global y_res
     x_res = 400
     y_res = 400
     p.minsize(x_res,y_res)
     p.maxsize(x_res,y_res)
     
     Main_Frame = ctk.CTkFrame(p,fg_color='#323335')
     Main_Frame.pack(expand = True,fill = 'both')


     Main_label = ctk.CTkLabel(Main_Frame,text='',fg_color=Background,height = 600,width = 400,corner_radius=30,bg_color='#323335')
     Main_label.pack(padx = 30,pady = 15,anchor = 'center')
     
     
     
     def deposit():
          global REAL_USER_INDEX
          print(REAL_USER_INDEX)
          Amount = ammount.get()
          if Amount.isalpha() or len(Amount) == 0:
               Amount_Entry.configure(fg_color = 'red')
          else:
               Amount_Entry.configure(fg_color = Background)
               with open("Balance.txt","r") as file:
                    f = file.read()
                    b = f.split()
                    balance = b[REAL_USER_INDEX]
                    balance = int(balance)
                    Amount = int(Amount)   
                    remaining = balance + Amount
                    b[REAL_USER_INDEX] = str(remaining)
                    k = " ".join(b)
                    with open("Balance.txt","w") as file:
                         file.write(k)
                    error.configure(text = "Deposit Successful")
                    error.configure(text_color = 'green')
                    ok_Button.configure(text = 'OK')
                    Withdraw_Button.destroy()
     
     def back():
          Main_Frame.destroy()
          User_Option_Page()



     ok_Button = ctk.CTkButton(Main_Frame,
                           text = '',
                           width = 100,height=55,
                           corner_radius=25,
                           fg_color=Background,
                           border_color=Front_Background,
                           border_width=2,
                           bg_color=Background,
                           command=back)
     ok_Button.place(relx = 0.37,rely = 0.7)

     
     Withdraw_Button = ctk.CTkButton(Main_Frame,
                           text = 'Deposit',
                           width = 100,height=55,
                           corner_radius=25,
                           fg_color=Background,
                           border_color=Front_Background,
                           border_width=2,
                           bg_color=Background,
                           command=deposit)
     Withdraw_Button.place(relx = 0.37,rely = 0.7)

     back_Button = ctk.CTkButton(Main_Frame,
                           text = 'Back',
                           width = 50,height=25,
                           corner_radius=25,
                           fg_color='black',
                           bg_color=Background,
                           command=back)
     back_Button.place(relx = 0.1,rely = 0.85)
     
     Heading = ctk.CTkLabel(Main_Frame,
                            bg_color=Background,
                            fg_color=Background,
                            text = "Enter Deposit Amount",
                            font = ('ubuntu' , 20 , 'bold'))
     Heading.place(relx = 0.23,rely = 0.16)

     error = ctk.CTkLabel(Main_Frame,
                            bg_color=Background,
                            fg_color=Background,
                            text = "",
                            font = ('ubuntu' , 12 , 'bold'))
     error.place(relx = 0.32,rely = 0.3)



     ammount = ctk.StringVar()
     Amount_Entry = ctk.CTkEntry(Main_Frame,textvariable=ammount,fg_color=Background,border_color=Front_Background,border_width=2 )
     Amount_Entry.place(relx = 0.33,rely = 0.4)

def Fund_Transfer_Page():
     global x_res
     global y_res
     x_res = 400
     y_res = 400
     p.minsize(x_res,y_res)
     p.maxsize(x_res,y_res)
     global TRANSACTION_INDEX 
     global Balance_Of_Sender
     global Balance_Of_Receiver 
     global Transaction_Amount 
     global Sender_Index 
     global Receiver_Index 

     
     Main_Frame = ctk.CTkFrame(p,fg_color='#323335')
     Main_Frame.pack(expand = True,fill = 'both')


     Main_label = ctk.CTkLabel(Main_Frame,text='',fg_color=Background,height = 600,width = 400,corner_radius=30,bg_color='#323335')
     Main_label.pack(padx = 30,pady = 15,anchor = 'center')

     def Fund_Transfer():
          global REAL_USER_INDEX
          global TRANSACTION_INDEX 
          global Balance_Of_Sender
          global Balance_Of_Receiver 
          global Transaction_Amount 
          global Sender_Index 
          global Receiver_Index
          print(REAL_USER_INDEX)
          Amount = ammount.get()
          Amount2 = ammount_2.get()
          if Amount.isalpha() or len(Amount) == 0:
               Amount_Entry.configure(fg_color = 'red')
          else:
               Amount_Entry.configure(fg_color = Background)
          if Amount2.isalpha() or len(Amount2) == 0:
               Amount_Entry_2.configure(fg_color = 'red')
          else:
               Amount_Entry_2.configure(fg_color = Background)
          if Amount.isalpha() or len(Amount) == 0 or Amount2.isalpha() or len(Amount2) == 0:
               pass
          else:
               Amount_Entry.configure(fg_color = Background)
               Amount_Entry_2.configure(fg_color = Background)
               with open("Account ID.txt","r") as file:
                    x = file.read()
                    y = x.split()
                    print(y)
                    for i in y:
                         if i==Amount2 and i!=y[REAL_USER_INDEX]:
                              w = y.index(i)
                              print(w)
                              error.configure(text = "")
                              with open("Balance.txt","r") as file:
                                   f = file.read()
                                   b = f.split()
                                   print(REAL_USER_INDEX)
                                   balance_of_sender = b[REAL_USER_INDEX]
                                   balance_of_sender = int(balance_of_sender)
                                   balance_of_receiver = b[w]
                                   balance_of_receiver = int(balance_of_receiver)
                                   Amount = int(Amount)
                                   if balance_of_sender >= Amount:
                                        balance_of_sender = balance_of_sender-Amount
                                        balance_of_receiver = balance_of_receiver+Amount
                                        Balance_Of_Sender = balance_of_sender
                                        Balance_Of_Receiver = balance_of_receiver
                                        Transaction_Amount = Amount
                                        Sender_Index = REAL_USER_INDEX
                                        Receiver_Index = w
                                        b[REAL_USER_INDEX] =str( balance_of_sender)
                                        b[w] = str(balance_of_receiver)
                                        k = " ".join(b)
                                        with open("Balance.txt","w") as file:
                                             file.write(k)
                                        error.configure(text = "Fund Transfer Successful")
                                        error.configure(text_color = 'green')
                                        ok_Button.configure(text = 'OK')
                                        Withdraw_Button.destroy()
                                        break
                                   else:
                                        error.configure(text = 'Not Enough Balance')    
                                        break
                         else:
                              error.configure(text = "Account ID not found")
     def back():
          Main_Frame.destroy()
          User_Option_Page()



     ok_Button = ctk.CTkButton(Main_Frame,
                           text = '',
                           width = 100,height=55,
                           corner_radius=25,
                           fg_color=Background,
                           border_color=Front_Background,
                           border_width=2,
                           bg_color=Background,
                           command=back)
     ok_Button.place(relx = 0.37,rely = 0.7)

     
     Withdraw_Button = ctk.CTkButton(Main_Frame,
                           text = 'Transfer',
                           width = 100,height=55,
                           corner_radius=25,
                           fg_color=Background,
                           border_color=Front_Background,
                           border_width=2,
                           bg_color=Background,
                           command=Fund_Transfer)
     Withdraw_Button.place(relx = 0.37,rely = 0.7)

     back_Button = ctk.CTkButton(Main_Frame,
                           text = 'Back',
                           width = 50,height=25,
                           corner_radius=25,
                           fg_color='black',
                           bg_color=Background,
                           command=back)
     back_Button.place(relx = 0.1,rely = 0.85)
     
     Heading = ctk.CTkLabel(Main_Frame,
                            bg_color=Background,
                            fg_color=Background,
                            text = "Enter Fund Transfer Amount",
                            font = ('ubuntu' , 20 , 'bold'))
     Heading.place(relx = 0.15,rely = 0.16)

     Heading_2 = ctk.CTkLabel(Main_Frame,
                            bg_color=Background,
                            fg_color=Background,
                            text = "Enter Account ID to Transfer",
                            font = ('ubuntu' , 20 , 'bold'))
     Heading_2.place(relx = 0.14,rely = 0.40)

     error = ctk.CTkLabel(Main_Frame,
                            bg_color=Background,
                            fg_color=Background,
                            text = "",
                            font = ('ubuntu' , 12 , 'bold'))
     error.place(relx = 0.32,rely = 0.32)



     ammount = ctk.StringVar()
     Amount_Entry = ctk.CTkEntry(Main_Frame,textvariable=ammount ,bg_color = Background,fg_color = Background,border_color=Front_Background,border_width=2)
     Amount_Entry.place(relx = 0.33,rely = 0.25)


     ammount_2 = ctk.StringVar()
     Amount_Entry_2 = ctk.CTkEntry(Main_Frame,textvariable=ammount_2,bg_color = Background,fg_color = Background,border_color=Front_Background,border_width=2 )
     Amount_Entry_2.place(relx = 0.33,rely = 0.50)

def Balance_Inquiry():
     global x_res
     global y_res
     x_res = 400
     y_res = 400
     p.minsize(x_res,y_res)
     p.maxsize(x_res,y_res)
     
     Main_Frame = ctk.CTkFrame(p,fg_color='#323335')
     Main_Frame.pack(expand = True,fill = 'both')
     bgimg = Image.open("grey.png")
     img = ctk.CTkImage(bgimg,size=(300,300))


     Main_label = ctk.CTkLabel(Main_Frame,text='',fg_color=Background,height = 600,width = 400,corner_radius=30,bg_color='#323335')
     Main_label.pack(padx = 30,pady = 15,anchor = 'center')
     



     def back():
          Main_Frame.destroy()
          User_Option_Page()
     
     ok_Button = ctk.CTkButton(Main_Frame,
                           text = 'OK',
                           width = 100,height=55,
                           corner_radius=25,
                           bg_color = Background,fg_color = Background,border_color=Front_Background,border_width=2,
                           command=back)
     ok_Button.place(relx = 0.37,rely = 0.7)

     Heading = ctk.CTkLabel(Main_Frame,
                            bg_color=Background,
                            fg_color=Background,
                            text = "",
                            font = ('ubuntu' , 25 , 'bold'))
     Heading.place(relx = 0.34,rely = 0.16)

     with open("Balance.txt","r") as file:
          var = file.read()
          const = var.split()
          balance = const[REAL_USER_INDEX]
          Heading.configure(text = f"Rs {balance}/-")

def Pin_Change():
     global x_res
     global y_res
     x_res = 400
     y_res = 400
     p.minsize(x_res,y_res)
     p.maxsize(x_res,y_res)
     
     Main_Frame = ctk.CTkFrame(p,fg_color='#323335')
     Main_Frame.pack(expand = True,fill = 'both')
     bgimg = Image.open("grey.png")
     img = ctk.CTkImage(bgimg,size=(300,300))


     Main_label = ctk.CTkLabel(Main_Frame,text='',fg_color=Background,height = 600,width = 400,corner_radius=30,bg_color='#323335')
     Main_label.pack(padx = 30,pady = 15,anchor = 'center')


     
     
     def change():
          pin = z.get()
          if pin.isalpha() or len(pin) == 0 or len(pin) != 4:
               error.configure(text = "Invalid PIN")
               error.configure(text_color = 'red')
          else:
               error.configure(text = "")
               error.configure(text_color = 'white')
               with open("PIN.txt" , "r") as file:
                    f = file.read()
                    pin_data = f.split()
                    pin_data[REAL_USER_INDEX] = pin
                    d = " ".join(pin_data)
                    with open("PIN.txt" , "w") as file:
                         file.write(d)
                    error.configure(text = "PIN successfully Changed")
                    error.configure(text_color = 'green')
                    
                    ok_Button.configure(text = "OK")
                    
                    Pin_Change_Button.destroy()

     
     def back():
          Main_Frame.destroy()
          User_Option_Page()
     
     
     ok_Button = ctk.CTkButton(Main_Frame,
                           text = '',
                           width = 100,height=55,
                           corner_radius=25,
                           bg_color = Background,fg_color = Background,border_color=Front_Background,border_width=2,
                           command=back)
     ok_Button.place(relx = 0.37,rely = 0.7)
     
     Pin_Change_Button = ctk.CTkButton(Main_Frame,
                           text = 'Change',
                           width = 100,height=55,
                           corner_radius=25,
                           bg_color = Background,fg_color = Background,border_color=Front_Background,border_width=2,
                           command = change)
     Pin_Change_Button.place(relx = 0.37,rely = 0.7)

     
     
     Heading = ctk.CTkLabel(Main_Frame,
                            bg_color=Background,
                            fg_color=Background,
                            text = "Enter New Pin",
                            font = ('ubuntu' , 20 , 'bold'))
     Heading.place(relx = 0.23,rely = 0.16)

     error = ctk.CTkLabel(Main_Frame,
                            bg_color=Background,
                            fg_color=Background,
                            text = "",
                            text_color='red',
                            font = ('ubuntu' , 12 , 'bold'))
     error.place(relx = 0.32,rely = 0.3)

     back_Button = ctk.CTkButton(Main_Frame,
                           text = 'Back',
                           width = 50,height=25,
                           corner_radius=25,
                           fg_color='black',
                           bg_color=Background,
                           command=back)
     back_Button.place(relx = 0.1,rely = 0.85)


     z = ctk.StringVar()
     Pin_Entry = ctk.CTkEntry(Main_Frame,textvariable=z ,fg_color = Background,border_color=Front_Background,border_width=2)
     Pin_Entry.place(relx = 0.33,rely = 0.4)

def Login_Page():
     global x_res
     global y_res
     x_res = 400
     y_res = 400
     p.minsize(x_res,y_res)
     p.maxsize(x_res,y_res)
     
     Main_Frame = ctk.CTkFrame(p,fg_color='#323335')
     Main_Frame.pack(expand = True,fill = 'both')

     Main_label = ctk.CTkLabel(Main_Frame,text='',fg_color=Background,height = 600,width = 400,corner_radius=30,bg_color='#323335')
     Main_label.pack(padx = 10,pady = 7,anchor = 'center')

     Username_Label = ctk.CTkLabel(Main_Frame,
                           text = 'username',
                           font = ( 'san serif',18 , 'bold'),
                           fg_color=Background
                           )
     Username_Label.place(relx = 0.18,rely = 0.35)


     Password_Label = ctk.CTkLabel(Main_Frame,
                           text = 'Password',
                           font = ( 'san serif',18 , 'bold'),
                           fg_color=Background
                           )
     Password_Label.place(relx = 0.18,rely = 0.50)

     Heading = ctk.CTkLabel(Main_Frame,
                           text = 'Enter Username and Password',
                           font = ( 'san serif',22, 'bold','underline'),
                           fg_color=Background
                           )
     Heading.place(relx = 0.10,rely = 0.15)

     warning = ctk.CTkLabel(Main_Frame,
                           text = '',
                           font = ( 'san serif',14 , 'bold'),
                           fg_color=Background,
                           bg_color=Background
                           )
     warning.place(relx = 0.2,rely = 0.60)


     username_str = ctk.StringVar()
     username_Entry = ctk.CTkEntry(Main_Frame,
                           textvariable=username_str,
                           width = 150,
                           bg_color = Background,fg_color = Background,border_color=Front_Background,border_width=2,
                           placeholder_text='Enter Username here',
                           placeholder_text_color='red')
     username_Entry.place(relx = 0.42,rely = 0.35)
     username_Entry.configure(placeholder_text = 'Enter')

     Password_str = ctk.StringVar()
     Password_Entry = ctk.CTkEntry(Main_Frame,
                           textvariable=Password_str,
                           width = 150,
                           bg_color = Background,fg_color = Background,border_color=Front_Background,border_width=2,
                           placeholder_text='Enter Username here',
                           placeholder_text_color='red')
     Password_Entry.place(relx = 0.42,rely = 0.50)
     Password_Entry.configure(placeholder_text = 'Enter')

     def login():
          nonlocal Password_str
          nonlocal username_str
          password = Password_str.get()
          username = username_str.get()
          username = username
          if username == "admin" and password == "12345":
               Main_Frame.destroy()
               Admin_Page()
          else:
               warning.configure(text = "Wrong Input")
               warning.configure(text_color = 'red')

     button = ctk.CTkButton(Main_Frame,
                            text = "Login",
                            command = login)
     button.place(relx = 0.35,rely = 0.75)

     
     def Back():
          Main_Frame.destroy()
          Card_Input_Page()

     back_button = ctk.CTkButton(Main_Frame,
                        text = 'Back',
                        fg_color = 'black',
                        bg_color=Background,
                        corner_radius=25,
                        width=30,
                        height=30,command=Back)
     back_button.place(relx = 0.07,rely = 0.89)

def Admin_Page():



     global x_res
     global y_res
     x_res = 1000
     y_res = 600
     p.minsize(x_res,y_res)
     p.maxsize(x_res,y_res)
     global Table2
     sv_ttk.set_theme("dark")

     
     Main_Frame = ctk.CTkFrame(p,fg_color='#323335')
     Main_Frame.pack(expand = True,fill = 'both')

     Tab = ctk.CTkTabview(Main_Frame,
                          width = 1000,
                          height=600,
                          corner_radius=20,
                          fg_color=Background
                          )
     Tab.pack()
     Tab.add('All Accounts')

     Table = ttk.Treeview(Tab.tab("All Accounts"),columns=("No","Account ID","Username","Balance","Card NO","Bank Type","CVV","PIN"),show = 'headings',height = 50)
     Table.pack(expand = True,fill = 'both')
     Table.heading('No',text = "No")
     Table.heading('Account ID',text = "Account ID")
     Table.heading('Username',text = "Username")
     Table.heading('Balance',text = "Balance")
     Table.heading('Bank Type',text = "Bank Type")
     Table.heading('Card NO',text = "Card Number")
     Table.heading('CVV',text = "CVV")
     Table.heading('PIN',text = "PIN")
     
     Table.column("No",width=50)
     Table.column("Account ID",width=70)
     Table.column("Username",width=120)
     Table.column("Balance",width=80)
     Table.column("Card NO",width=200)
     Table.column("Bank Type",width=70)
     Table.column("CVV",width=50)
     Table.column("PIN",width=50)


     with open("index NO.txt",'r') as file:
          number = file.read()
          index = int(number)
     with open("Account ID.txt",'r') as file:
          Acc_ID_saver = file.read()
          Acc_ID_Array = Acc_ID_saver.split()    
     with open('Card Type.txt','r') as file:
          card_info_saver= file.read()
          card_type = card_info_saver.split()
     with open('Bank Type.txt','r') as file:
          bank_info_saver = file.read()
          bank = bank_info_saver.split()
     with open('Card NO.txt','r') as file:
          card_no_saver = file.read()
          card_number = card_no_saver.split()
     with open('CVV.txt','r') as file:
          cvv_saver = file.read()
          Cvv = cvv_saver.split()
     with open('PIN.txt','r') as file:
          pin_saver = file.read()
          Pin = pin_saver.split()
     with open('Username.txt','r') as file:
          username_saver = file.read()
          username = username_saver.split()
     with open("Balance.txt","r") as file:
          balance_saver = file.read()
          balance = balance_saver.split()
     
     for i in range(index):
          Name = ""
          for j in username[i]:
               if j == "_":
                    Name = Name+" "
               else:
                    Name = Name+j
               
          Table.insert(parent='' , index = i , values =(i ,Acc_ID_Array[i],Name,balance[i],card_number[i],bank[i],Cvv[i],Pin[i]))

     def back():
          Main_Frame.destroy()
          Card_Input_Page()
     
     ok_Button = ctk.CTkButton(Tab.tab("All Accounts"),
                           text = 'Back',
                           width = 50,height=50,
                           corner_radius=20,
                           fg_color='black',
                           bg_color="grey",
                           command=back)
     ok_Button.place(relx = 0.05,rely = 0.9)

def Add_FingerPrint():
     global x_res
     global y_res
     x_res = 400
     y_res = 450
     p.minsize(x_res,y_res)
     p.maxsize(x_res,y_res)
     
     Main_Frame = ctk.CTkFrame(p,fg_color='#323335')
     Main_Frame.pack(expand = True,fill = 'both')


     Main_label = ctk.CTkLabel(Main_Frame,text='',fg_color=Background,height = 600,width = 400,corner_radius=30,bg_color='#323335')
     Main_label.pack(padx = 30,pady = 15,anchor = 'center')


     browser_checker=0
     post = 0
     num = 0
     done = False
     def enroll():
          nonlocal done
          if done == False:

               nonlocal browser_checker
               nonlocal post
               nonlocal num
               global REAL_USER_INDEX
               def Again():
                    nonlocal browser_checker
                    nonlocal post
                    nonlocal num  
                    ans = messagebox.askyesno("Alert",f"Do you want to add another Fingerprint? {num} Fingerprints Added for this registeration")
                    if ans:
                         browser_checker=0
                         post = 0
                         enroll()
                    else:
                         f_p.configure(text = "Fingerprint Registration Successful")
                         f_p.configure(text_color = 'green')
                         FingerPrint_Enrollment.destroy()
                         ok_button.place(relx = 0.64,rely = 0.7)
               if browser_checker == 0:
                    webbrowser.open("project.html")
                    f_p.configure(text = "Place your Finger on the reader Single Time")
                    f_p.configure(text_color = 'white')
                    FingerPrint_Enrollment.configure(text = "Done")
                    browser_checker = 1
                    post = 0
               
               if post > 0:
                    x = REAL_USER_INDEX
                    if os.path.exists("C:\\Users\\DELL\\Downloads\\t.txt"):
                         shutil.move("C:\\Users\\DELL\\Downloads\\t.txt" , f"text folder\\{x}.{num}.txt")
                         num = num+1
                         Again()
                    else:
                         f_p.configure(text = "Something Went Wrong")
                         FingerPrint_Enrollment.configure(text = "Try Again")
                         browser_checker = 0
               else:
                    post = 1



     FingerPrint_Enrollment = ctk.CTkButton(Main_Frame,
                                            text = "Register Your FingerPrint",
                                            width = 130,
                                            fg_color=Background,
                                            corner_radius=16,
                                            border_width=2,
                                            border_color = Front_Background,
                                            height = 50,
                                            bg_color = Background,
                                            command = enroll)
     FingerPrint_Enrollment.place(relx = 0.34,rely = 0.63)

     def Back():
          Main_Frame.destroy()
          User_Option_Page()
     ok_button = ctk.CTkButton(Main_Frame,
                                            text = "",
                                            width = 130,
                                            fg_color=Background,
                                            corner_radius=16,
                                            border_width=2,
                                            border_color = Front_Background,
                                            height = 50,
                                            bg_color = Background,
                                            command = Back)

     f_p = ctk.CTkLabel(Main_Frame,
                           text = '',
                           font = ( 'san serif',12 , 'bold'),
                           fg_color=Background,
                           bg_color = Background
                           )
     
     f_p.place(relx = 0.2,rely = 0.75)

     back_Button = ctk.CTkButton(Main_Frame,
                           text = 'Back',
                           width = 50,height=25,
                           corner_radius=25,
                           fg_color='black',
                           bg_color=Background,
                           command=Back)
     back_Button.place(relx = 0.13,rely = 0.85)

     bgimg = Image.open("FP.jpeg")
     img = ctk.CTkImage(bgimg,size=(225,225))
     
     image = ctk.CTkLabel(Main_Frame,image = img,text = '')
     image.place(relx = 0.22,rely = 0.1)

def Fast_Cash():
     global x_res
     global y_res
     x_res = 400
     y_res = 400
     p.minsize(x_res,y_res)
     p.maxsize(x_res,y_res)
     
     Main_Frame = ctk.CTkFrame(p,fg_color='#323335')
     Main_Frame.pack(expand = True,fill = 'both')


     Main_label = ctk.CTkLabel(Main_Frame,text='',fg_color=Background,height = 600,width = 400,corner_radius=30,bg_color='#323335')
     Main_label.pack(padx = 30,pady = 15,anchor = 'center')

     Heading = ctk.CTkLabel(Main_Frame,
                            bg_color=Background,
                            text = "Select Withdraw Amount",
                            font = ('ubuntu' , 20 , 'bold'))
     Heading.place(relx = 0.23,rely = 0.16)

     def back():
          Main_Frame.destroy()
          User_Option_Page()

     back_Button = ctk.CTkButton(Main_Frame,
                           text = 'Back',
                           width = 50,height=25,
                           corner_radius=25,
                           fg_color='black',
                           bg_color=Background,
                           command=back)
     back_Button.place(relx = 0.1,rely = 0.85)

     Amount = None
     def withdraw():
          global REAL_USER_INDEX
          nonlocal Amount
          with open("Balance.txt","r") as file:
                    f = file.read()
                    b = f.split()
                    balance = b[REAL_USER_INDEX]
                    balance = int(balance)
                    Amount = int(Amount)   
               
                    if balance < Amount:
                         error.configure(text = "insufficient Balance")
                         error.configure(text_color = "red")
                    else:
                              error.configure(text = "Withdraw Successful")
                              error.configure(text_color = 'white')
                              remaining = balance - Amount
                              b[REAL_USER_INDEX] = str(remaining)
                              k = " ".join(b)
                              with open("Balance.txt","w") as file:
                                   file.write(k)
                              ok.place(relx = 0.42,rely = 0.5)
                              b1.destroy()
                              b2.destroy()
                              b3.destroy()
                              b4.destroy()
                              b5.destroy()
                              b6.destroy()

     error = ctk.CTkLabel(Main_Frame,
                            bg_color=Background,
                            text = "",
                            text_color='white',
                            font = ('ubuntu' , 12 , 'bold','underline'))
     error.place(relx = 0.2,rely = 0.25)

     def b1func():
          nonlocal Amount
          Amount = 500
          withdraw()

     b1 = ctk.CTkButton(Main_Frame,
                        text = '500',
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        width=47,
                        height=47,
                        font=("PT Sans" , 18,"bold"),
                        command=b1func)
     b1.place(relx = 0.17,rely = 0.35)


     def b2func():
          nonlocal Amount
          Amount = 1000
          withdraw()

     b2 = ctk.CTkButton(Main_Frame,
                        text = '1000',
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        width=47,
                        height=47,
                        font=("PT Sans" , 18,"bold"),
                        command=b2func)
     b2.place(relx = 0.17,rely = 0.5)


     def b3func():
          nonlocal Amount
          Amount = 2000
          withdraw()

     b3 = ctk.CTkButton(Main_Frame,
                        text = '2000',
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        width=47,
                        height=47,
                        font=("PT Sans" , 18,"bold"),
                        command=b3func)
     b3.place(relx = 0.17,rely = 0.65)


     def b4func():
          nonlocal Amount
          Amount = 5000
          withdraw()

     b4 = ctk.CTkButton(Main_Frame,
                        text = '5000',
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        width=47,
                        height=47,
                        font=("PT Sans" , 18,"bold"),
                        command=b4func)
     b4.place(relx = 0.57,rely = 0.35)


     def b5func():
          nonlocal Amount
          Amount = 10000
          withdraw()

     b5 = ctk.CTkButton(Main_Frame,
                        text = '10,000',
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        width=47,
                        height=47,
                        font=("PT Sans" , 18,"bold"),
                        command=b5func)
     b5.place(relx = 0.57,rely = 0.5)

     def b5func():
          nonlocal Amount
          Amount = 20000
          withdraw()

     b6 = ctk.CTkButton(Main_Frame,
                        text = '20,000',
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        width=47,
                        height=47,
                        font=("PT Sans" , 18,"bold"),
                        command=b5func)
     b6.place(relx = 0.57,rely = 0.65)

     ok = ctk.CTkButton(Main_Frame,
                        text = 'OK',
                        fg_color = Background,
                        bg_color=Background,
                        border_color = Front_Background,
                        border_width=1,
                        corner_radius=25,
                        width=47,
                        height=47,
                        font=("PT Sans" , 18,"bold"),
                        command=back)

def match_fingers(image_1_base64, image_2_base64, threshold=100):
          # Decode base64 strings to image arrays
          image_1_data = base64.b64decode(image_1_base64)
          image_2_data = base64.b64decode(image_2_base64)


         #Convert image data to OpenCV format
          image_1 = cv2.imdecode(np.frombuffer(image_1_data, np.uint8), cv2.IMREAD_GRAYSCALE)
          image_2 = cv2.imdecode(np.frombuffer(image_2_data, np.uint8), cv2.IMREAD_GRAYSCALE)

          # Create a SIFT object
          sift = cv2.SIFT_create()

          # Find key points and descriptors for both images
          keypoints_1, descriptors_1 = sift.detectAndCompute(image_1, None)
          keypoints_2, descriptors_2 = sift.detectAndCompute(image_2, None)

          # Initialize a Brute-Force Matcher
          bf = cv2.BFMatcher()

          # Match keypoint descriptors
          matches = bf.knnMatch(descriptors_1, descriptors_2, k=2)

          # Apply ratio test to select good matches
          good_matches = []
          for m, n in matches:
              if m.distance < 0.75 * n.distance:
                  good_matches.append(m)

          # Calculate the matching score
          matching_score = len(good_matches)
          print(f"Matching Score: {matching_score}")

          # Check if the matching score exceeds the threshold
          if matching_score >= threshold:
              print("Fingerprints match!")
              return True
          else:
              print("Fingerprints do not match.")
              return False

Card_Input_Page()

p.mainloop()