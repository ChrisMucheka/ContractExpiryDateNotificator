import csv
import datetime
import smtplib
from twilio.rest import Client
from tkinter import filedialog
from tkinter import *
now = datetime.datetime.now()
filedir=""
darray=[]
fields = 'Email', 'Password'
def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
def makeform(root, fields):
   root.title ( "Send Notification 1.0.1" )
   entries = {}
   for field in fields:
    if field=="Password":
      row = Frame(root)
      lab = Label(row, width=30, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"")
      ent.config ( show="*" )
      row.pack(side=TOP, fill=X, padx=7, pady=10)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
    else:
      row = Frame(root)
      lab = Label(row, width=30, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"")
      ent.config ( show="" )
      row.pack(side=TOP, fill=X, padx=7, pady=10)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries[field] = ent
   return entries
def uploadFile():
    try:
        global filedir
        filename = filedialog.askopenfile ( initialdir="/", title="Select file",
                                             filetypes=(("csv files", "*.csv"), ("all files", "*.*")) )

        filedir = filename.name
    except:
         pass
def readFile(filename):
 dates=[]
 if filename=="":
    popupmsg ( "Please select the file \nwith you clients details" )
 else:
  try:
    with open(filename) as csvfile:
        readCSV=csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            date=row[2]
            dates.append(date)
  except:
    popupmsg ( "You notification request wasn't successful \nsome of the details in the file are not correct" )

 return dates

def daysLeft(dates):
  dayLeft=[]
  try:
    for i in range(len(dates)):
        date_time_obj = datetime.datetime.strptime ( dates[i], '%Y/%m/%d' )
        no=date_time_obj-datetime.datetime.strptime("2018/03/03",'%Y/%m/%d')
        day=no.days
        dayLeft.append(day)
  except:
       popupmsg ( "You notification request wasn't successful \nsome of the details in the file are not correct" )
       pass
  return dayLeft
def getIndexOf(days):
    array1=[]
    for i in range(len(days)):
        if days[i]<=7:
            array1.append(i)
    return array1
def getName(nameIndex,filename):
    namesList=[]
    names=[]
    with open ( filename ) as csvfile:
        readCSV = csv.reader ( csvfile, delimiter=',' )
        next ( readCSV )
        for row in readCSV:
            namesList.append(row[0])
        for i in nameIndex:
            names.append(namesList[i])
    return names
def getEmail(nameIndex,filename):
    namesList=[]
    names=[]
    with open ( filename ) as csvfile:
        readCSV = csv.reader ( csvfile, delimiter=',' )
        next ( readCSV )
        for row in readCSV:
            namesList.append(row[1])
        for i in nameIndex:
            names.append(namesList[i])
    return names
def getPhoneNo(noIndex,filename):
    namesList = []
    names = []
    with open (filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next ( readCSV )
        for row in readCSV:
            namesList.append ( row[3] )
        for i in noIndex:
            names.append ( namesList[i] )
    return names
def sendMail(name,email,entries):
 senderEmail=(str(entries["Email"].get()))
 senderPassword=(str(entries['Password'].get()))
 if senderEmail=="":
     popupmsg("Please enter your email address")
 elif senderPassword=="":
     popupmsg ( "Please enter your email password" )
 elif senderPassword=="" and senderEmail=="":
     popupmsg ( "Please enter your email and password" )
 else:
         domain = senderEmail.split ( '@' )[1]
         hostname='smtp.'+domain
         s = smtplib.SMTP ( host=hostname, port=587 )
         s.starttls ()
         try:
             s.login ( senderEmail, senderPassword )
         except:
             popupmsg("Login failed")
             pass
         else:
             for i in range ( len ( name ) ):
                 txt = "Good morning " + name[i] + " hope you are well.\nThis is a kind reminder that your contract is " \
                                               "expirying within next 7 days make sure you renew it before it expires";
                 message = 'Subject: {}\n\n{}'.format ( "DOE Contract Expiring Reminder", txt )
                 s.sendmail ( senderEmail, email[i], "\n" + message )
             popupmsg("Your notification has been successfully sent")
def sendSMS(name,phoneNo):
    account_sid = 'ACd15a3ce952d21ac0b63b459224b0f106'
    auth_token = '0f6ce6f06d83e1161f047d8f57a46db6'
    client = Client ( account_sid, auth_token )
    for i in range(len(name)):
        client.create (
        body='Good morning '+ name[i] +' hope you are well.This is a kind reminder that your contract is '
                                       'expirying within next 7 days make sure you renew it before it expires',
        from_='+18303650760',
        to='+'+phoneNo[i])

def popupmsg(msg):
        popup = Tk ()
        popup.wm_title ( "Status info" )
        popup.geometry ( "300x100" )
        label = Label ( popup, text=msg )
        label.pack ( side="top", fill="x", pady=10 )
        B1 = Button ( popup, text="Okay", command=popup.destroy )
        B1.pack ()
        popup.mainloop ()
def run():
    root = Tk()
    root.wm_resizable ( 0, 0 )

    root.iconbitmap ( r'favicon.ico' )
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))

    b2=Button ( root, text="Select file with clients info", fg="maroon", command=uploadFile )
    b2.pack(side=LEFT, padx=5, pady=5)
    b1 = Button ( root, text='Send Notifications',
                  command=(lambda e=ents:
                           sendMail ( getName ( getIndexOf ( daysLeft ( readFile ( filedir ) ) ), filedir ),
                                      getEmail ( getIndexOf ( daysLeft ( readFile ( filedir ) ) ), filedir ), e )
                           ) )

    b1.pack ( side=LEFT, padx=5, pady=5 )
    root.mainloop()

if __name__ == '__main__':
    run()




