from tkinter import *
data = Tk()
data.title("Bio-Data")
data.geometry("700x1500")
data.configure(background="black")
BioData = Label(data, text="Bio-data by Stark Industries® 2020 All Rights Reserved ", font= "Arial", bg="#00cc44", fg="white")
Biodata2 = Label(data, text="I hereby certify that the above information is", font="Arial", bg="#00284d", fg="white")
Biodata3 = Label(data, text="true and correct to the best of my knowledge", font="Arial", bg="#00284d", fg="white")

def bio():
    filewindow = Toplevel(data)
    filewindow.title("Your Biography")
    txtinput = "My name is " + E3.get() + ". I graduated from " + E34.get() + " last " + E35.get() + " where I Majored in " + E36.get() + ". My email is " + E9.get()
    labeln= Label(filewindow, text = txtinput)
    nbutton = Button(filewindow, text="Exit", command=filewindow.destroy)
    labeln.grid(row=0, column=0, sticky=W)
    nbutton.grid(row=1, column=0)
    txtinput = "My name is " + E3.get() + ". I graduated from " + E34.get() + " last " + E35.get() + " where I Majored in " + E36.get() + ". My email is " + E9.get()

Pic = Label(text ="I.D. Photo", bg = "white", fg = "black",width = 8, height = 8,font = ("times new roman", 13))
Pic.grid(row = 1, column = 10)
Personal_data = Label(data,text="PERSONAL DATA:", bg="orange", fg="white")
Position = Label(data,text='Position Desired:', bg="#00284d", fg="white")
Date = Label(data,text='Date:', bg="#00284d", fg="white")
Name = Label(data,text='Name:', bg="#00284d", fg="white")
Sex = Label(data,text='Sex:', bg="#00284d", fg="white")
City = Label(data,text='City Address:', bg="#00284d", fg="white")
Province = Label(data,text='Provincial Address:', bg="#00284d", fg="white")
Telephone = Label(data,text='Telephone number:', bg="#00284d", fg="white")
Cellphone = Label(data,text='Cell phone number:', bg="#00284d", fg="white")
Email = Label(data,text='E-mail Address:', bg="#00284d", fg="white")
DoB = Label(data,text='Date of Birth:', bg="#00284d", fg="white")
Place = Label(data,text="Place:", bg="#00284d", fg="white")
CivilStatus = Label(data,text='Civil Status:', bg="#00284d", fg="white")
Citizenship = Label(data,text='Citizenship:', bg="#00284d", fg="white")
Height = Label(data,text='Height:', bg="#00284d", fg="white")
Weight = Label(data,text='Weight:', bg="#00284d", fg="white")
Religion = Label(data,text='Religion:', bg="#00284d", fg="white")
Spouse = Label(data,text='Spouse:', bg="#00284d", fg="white")
Occupation = Label(data,text="Occupation:", bg="#00284d", fg="white")
Children = Label(data,text="Name of Children:", bg="#00284d", fg="white")
DoBII = Label(data,text="Date of Birth:", bg="#00284d", fg="white")
Father = Label(data,text="Father's Name:", bg="#00284d", fg="white")
FOcc = Label(data,text="Occupation:", bg="#00284d", fg="white")
Mother = Label(data,text="Mother's Name:", bg="#00284d", fg="white")
MOcc = Label(data,text="Occupation:", bg="#00284d", fg="white")
Address = Label(data,text="Parent's address", bg="#00284d", fg="white")
Language = Label(data,text="Language:", bg="#00284d", fg="white")
Person2Be = Label(data,text="Person to be contacted in case of emergency:", bg="#00284d", fg="white")
AddxTel = Label(data,text="His/her address and telephone number:", bg="#00284d", fg="white")

EduAtt = Label(data,text="EDUCATIONAL ATTAINMENT:", bg="orange", fg="white")
Elementary = Label(data,text="Elementary:", bg="#00284d", fg="white")
EYearGrad = Label(data,text="Year Graduated:", bg="#00284d", fg="white")
HS = Label(data,text="High School:", bg="#00284d", fg="white")
HSYearGrad = Label(data,text="Year Graduated:", bg="#00284d", fg="white")
College = Label(data,text="College:", bg="#00284d", fg="white")
CYearGrad = Label(data,text="Year Graduated:", bg="#00284d", fg="white")
Degree = Label(data,text="Degree Received:", bg="#00284d", fg="white")
SS = Label(data,text="Special Skills:", bg="#00284d", fg="white")


E1=Entry(data)
E2=Entry(data)
E3=Entry(data)
E4=Entry(data)
E5=Entry(data)
E6=Entry(data)
E7=Entry(data)
E8=Entry(data)
E9=Entry(data)
E10=Entry(data)
E11=Entry(data)
E12=Entry(data)
E13=Entry(data)
E14=Entry(data)
E15=Entry(data)
E16=Entry(data)
E17=Entry(data)
E18=Entry(data)
E19= Entry(data)
E20=Entry(data)
E21=Entry(data)
E22=Entry(data)
E23=Entry(data)
E24=Entry(data)
E25=Entry(data)
E26=Entry(data)
E27=Entry(data)
E28=Entry(data)
E30=Entry(data)
E31=Entry(data)
E32=Entry(data)
E33=Entry(data)
E34=Entry(data)
E35=Entry(data)
E36=Entry(data)
E37=Entry(data)


Personal_data.grid(row = 0, column = 0)
Position.grid(row = 1, column = 0)
E1.grid(row = 1, column = 1)
Date.grid(row = 1, column = 2)
E2.grid(row = 1, column = 3)
Name.grid(row = 2, column = 0)
E3.grid(row = 2, column = 1)
Sex.grid(row = 2, column = 2)
E4.grid(row = 2, column = 3)
City.grid(row = 3, column = 0)
E5.grid(row = 3, column = 1)
Province.grid(row = 4, column = 0)
E6.grid(row = 4, column = 1)
Telephone.grid(row = 5, column = 0)
E7.grid(row = 5, column = 1)
Cellphone.grid(row = 5, column = 2)
E8.grid(row = 5, column = 3)
Email.grid(row = 6, column = 0)
E9.grid(row = 6, column = 1)
DoB.grid(row = 7, column = 0)
E10.grid(row = 7, column = 1)
Place.grid(row = 7, column = 2)
E11.grid(row = 7, column = 3)
CivilStatus.grid(row = 8, column = 0)
E12.grid(row = 8, column = 1)
Citizenship.grid(row = 8, column = 2)
E13.grid(row = 8, column = 3)
Height.grid(row = 9, column = 0)
E14.grid(row = 9, column = 1)
Weight.grid(row = 9, column = 2)
E15.grid(row = 9, column = 3)
Religion.grid(row = 10, column = 0)
E16.grid(row = 10, column = 1)
Spouse.grid(row = 11, column = 0)
E17.grid(row = 11, column = 1)
Occupation.grid(row = 11, column = 2)
E18.grid(row = 11, column = 3)
Children.grid(row = 12, column = 0)
E19.grid(row = 12, column = 1)
DoBII.grid(row = 12, column = 2)
E20.grid(row = 12, column = 3)
Father.grid(row = 13, column = 0)
E21.grid(row = 13, column = 1)
FOcc.grid(row = 13, column = 2)
E22.grid(row = 13, column = 3)
Mother.grid(row = 14, column = 0)
E23.grid(row = 14, column = 1)
MOcc.grid(row = 14, column = 2)
E24.grid(row = 14, column = 3)
Address.grid(row = 15, column = 0)
E25.grid(row = 15, column = 1)
Language.grid(row = 16, column = 0)
E26.grid(row = 16, column = 1)
Person2Be.grid(row = 17, column = 0)
E27.grid(row = 17, column = 1)
AddxTel.grid(row = 18, column = 0)
E28.grid(row = 18, column = 1)
EduAtt.grid(row = 19, column = 0)
Elementary.grid(row = 20, column = 0)
E30.grid(row = 20, column = 1)
EYearGrad.grid(row = 20, column = 2)
E31.grid(row = 20, column = 3)
HS.grid(row = 21, column = 0)
E32.grid(row = 21, column = 1)
HSYearGrad.grid(row = 21, column = 2)
E33.grid(row = 21, column = 3)
College.grid(row = 22, column = 0)
E34.grid(row = 22, column = 1)
CYearGrad.grid(row = 22, column = 2)
E35.grid(row = 22, column = 3)
Degree.grid(row = 23, column = 0)
E36.grid(row = 23, column = 1)
SS.grid(row = 24, column = 0)
E37.grid(row = 24, column = 1)
BioData.grid(row =40 , column=1)
Biodata2.grid(row = 41, column=1)
Biodata3.grid(row=42, column =1)    



B1 = Button(data, text="Submit", command=bio)
B2 = Button(data, text="Cancel/Exit", command=data.destroy)
B1.grid(row =43, column = 1)
B2.grid(row = 44, column = 1)
data.mainloop()