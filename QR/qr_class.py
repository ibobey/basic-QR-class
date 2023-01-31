"""
İBRAHİM TUNÇ 
30.01.2023
"""

#STUDENT QR GENERATOR

import qrcode #To generate qr codes
from qrcode import ERROR_CORRECT_M
import csv    #To save student's data as your prefence
import time

class Student:

    def __init__(self,school_number,name,surname,cell_number,e_mail):
        #Object Attributes    
        self.school_number = school_number
        self.name = name
        self.surname = surname
        self.cell_number = cell_number
        self.e_mail = e_mail

        #Create automaticly QR_code
        self.create_QR_code()

        #Save automaticly Student's data to csv
        self.save_to_csv()
        

    def create_QR_code(self):
        #Qr Data
        self.data = f"{self.school_number} {self.name} {self.surname} {self.cell_number} {self.e_mail}"

        #QR tickets
        self.QR_name = f"{self.school_number}.png"
    
        self.QR_saved_directory = f"qr_codes\\{self.QR_name}"

        #Create QR object from QR class
        self.QR = qrcode.QRCode(
            version=  2,
            error_correction=ERROR_CORRECT_M,
            box_size=5,
            border= 5
        )

        #Set data into QR object
        self.QR.add_data(self.data)
        
        #Create QR image
        self.img = self.QR.make_image(
            back_color = "white",
            fill_color = "black"
        )

        #Save QR image into local directory
        self.img.save(self.QR_saved_directory)
        print(f"QR '{self.cell_number}' Created!")
        
        time.sleep(0.25)
    
    def save_to_csv(self):
        data = [
            self.school_number,
            self.name,
            self.surname,
            self.cell_number,
            self.e_mail
        ]

        #Save Data (to csv)
        with open("data.csv","a",encoding="utf-8",newline="") as f:
            try:
                writer = csv.writer(f)
                writer = writer.writerow(data)
               
                print(f"Student {self.school_number} Saved !")

            except Exception as E:
                print(E)

    def student_informations(self):
        print(
            self.school_number,
            self.name,
            self.surname,
            self.e_mail,
            self.cell_number,
            sep="\n")


s1 = Student(
    school_number="Default",
    name="Default",
    surname="Default",
    cell_number="Default",
    e_mail="Default")