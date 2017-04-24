#!/usr/bin/python3.4m
#-------------------------------------------------------------------------------
# This is a simple student calendar program written in Python.  This is a simple
# program designed to track up to eighteeen weeks of classes for college
# students. The original version of the program was done in Lazarus.
#
# Lara Landis
# Personal Python Project
# 12/25/2015
#--------------------------------------------------------------------------------
try:
    import tkinter
    import tkinter.messagebox
    import datetime
    import os
except ImportError:
    from Tkinter import *
    print ("This program requires Python 3.5 or later")
    exit ()


class stdtinfo:

    def __init__(self, name, numclasses,class1,class2,class3,class4,class5,class6,class7,class8):
    # This class will be used throughout the program
        self.name = name
        self.numclasses = numclasses
        self.class1 = class1
        self.class2 = class2
        self.class3 = class3
        self.class4 = class4
        self.class5 = class5
        self.class6 = class6
        self.class7 = class7
        self.class8 = class8

    def set_name (self, name):
        self.name = name

    def set_numclasses (self, numclasses):
        self.numclasses = numclasses

    def sef_class1(self, class1):
        self.class1 = class1

    def set_class2(self, class2):
        self.class2 = class2

    def set_class3(self, class3):
        self.class3 = class3

    def set_class4(self, class4):
        self.class4 = class4

    def set_class5(self, class5):
        self.class5 = class5

    def set_class6(self, class6):
        self.class6 = class6

    def set_class7(self, class7):
        self.class7 = class7

    def set_class8(self, class8):
        self.class8 = class8

    def get_name(self, name):
        return self.name

    def get_numclasses(self, numclasses):
        return self.numclasses

    def get_class1(self):
        return self.class1

    def get_class2(self):
        return self.class2

    def get_class3(self):
        return self.class3

    def get_class4(self):
        return self.class4

    def get_class5(self):
        return self.class5

    def get_class6(self):
        return self.class6

    def get_class7(self):
        return self.class7

    def get_class8(self):
        return self.class8
#-------------------------------------------------------------------------------------------
# This function saves the temporary file that the program uses. It is called each time the
# user presses a button.  It will subtract the last date from the first date and then sort the
# data by dates. When the dates are sorted, it will write them  to the file
# in order.
#-------------------------------------------------------------------------------------------
def save_working (swworkingdate):

    
    # Just declare this for now, but remove it later
    lastdate = datetime.date
    date_change = timdelta(firstdate - lastdate)
    date_inc	= timdelta(days = 1)

    i = 1

    # Initialize varaibles I'll need for this function
    swfstdtinfo = []
    swfclass1info = ""
    swfclass2info = ""
    swfclass3info = ""
    swfclass4info = ""
    swfclass5info = ""
    swfclass6info = ""
    swfclass7info = ""
    swfclass8info = ""

    #Now, write things to the file.    
    try:
        swf = open('stntcal.tmp', 'w')
        swf.seek()

        
        for i in range(1, datechange):
            
            swf.write(swworkingdate)
            swf.write(swf.swfclass1info[i])
            swf.write(swf.swfclass2info[i])
            swf.write(swf.swfclass3info[i])
            swf.write(swf.swfclass4info[i])
            swf.write(swf.swfclass5info[i])
            swf.write(swf.swfclass6info[i])
            swf.write(swf.swfclass7info[i])
            swf.write(swf.swfclass8info[i])
            swworkingdate = swworkingdate + date_inc

        lastdate = swworkingdate  # Make sure that the file is at the end.
        swf.close                 # close to make sure the file ends properly
            
    except IOError:
        tkinter.messagebox.showinfo("Warning!","File Error Encountered")
#-------------------------------------------------------------------------------------------
# This function will read in data from stdtcal.cal after the presence of the file has been
# detected. If the presence of the file has not been detected, this function will not
# be called by the program. As with the previous example, it must use a list to bring
# in multiple data points.
#-------------------------------------------------------------------------------------------
def read_in_data ():
	  # Just declare this for now, but remove it later
    lastdate = datetime.date
    dateinc = timedelta(days = 1)

    i = 1

    # Initialize varaibles I'll need for this function
    ridstdtinfo = []
    ridclass1info = ""
    ridclass2info = ""
    ridclass3info = ""
    ridclass4info = ""
    ridclass5info = ""
    ridclass6info = ""
    ridclass7info = ""
    ridclass8info = ""

    # Read in the data the program uses, if it exists.
    try:
        rid = open('stntcal.cal', 'r')
        rid.seek()

        
        for i in range(1, datechange):
            
            rid.read(ridworkingdate)
            rid.read(rid.ridclass1info[i])
            rid.read(rid.ridclass2info[i])
            rid.read(rid.ridclass3info[i])
            rid.read(rid.ridclass4info[i])
            rid.read(rid.ridclass5info[i])
            rid.read(rid.ridclass6info[i])
            rid.read(rid.ridclass7info[i])
            rid.read(rid.ridclass8info[i])
            ridworkingdate = ridworkingdate + date_inc

        lastdate = ridworkingdate  # Make sure that the file is at the end.
        rid.close ()               # close to make sure the file ends properly

            
    except IOError:
        tkinter.messagebox.showinfo("Warning!","File Error Encountered")
        
#-------------------------------------------------------------------------------------------
# This sets up the GUi that will let the student access the calendar to save his or her
# files.
#--------------------------------------------------------------------------------------------
class Calendar_Gui:

    def __init__ (self, cgisthere):

        workingdate = datetime.date
        firstdate = datetime.date
        daychange = datetime.timedelta
        cg_classlist = []
        
        
        #Initialize some variables
        cgname = ""
        cgnumclasses = ""
        cgclass1 = ""
        cgclass2 = ""
        cgclass3 = ""
        cgclass4 = ""
        cgclass5 = ""
        cgclass6 = ""
        cgclass7 = ""
        cgclass8 = ""

        # Create an instance of this class
        cg_info = stdtinfo (cgname, cgnumclasses, cgclass1, cgclass2, cgclass3,\
                            cgclass4, cgclass5, cgclass6, cgclass7, cgclass8)

        #Assign variables to the class
        if (cgisthere == True):
            try:
                cg_Studentfile       = open('student.dta', 'r')
                firstdate            = cg_Studentfile.readline ()
                cg_info.cgname       = cg_Studentfile.readline()
                cg_info.cgnumclasses = cg_Studentfile.readline ()
                cg_info.cgclass1     = cg_Studentfile.readline ()
                cg_info.cgclass2     = cg_Studentfile.readline ()
                cg_info.cgclass3     = cg_Studentfile.readline ()
                cg_info.cgclass4     = cg_Studentfile.readline ()
                cg_info.cgclass5     = cg_Studentfile.readline ()
                cg_info.cgclass6     = cg_Studentfile.readline ()
                cg_info.cgclass7     = cg_Studentfile.readline ()
                cg_info.cgclass8     = cg_Studentfile.readline ()
            except IOError:
                tkinter.messagebox.showinfo("File Error!", "Is the Student.dta file corrupted?")
        else:
            pass

        # Check to see if stdtcal.cal exists. Get info from it if so.
        try:
            i = 1
            cg_fo = open('stdtcal.cal', 'r')

            with open('stdtcal.cal') as cg_fo:
                for line in cg_fo:
                    cg_fo.read(cg_workingdate[i])
                    cg_fo.read(cg_class1info[i])
                    cg_fo.read(cg_class2info[i])
                    cg_fo.read(cg_class3info[i])
                    cg_fo.read(cg_class4info[i])
                    cg_fo.read(cg_class5info[i])
                    cg_fo.read(cg_class5info[i])
                    cg_fo.read(cg_class6info[i])
                    cg_fo.read(cg_class7info[i])
                    cg_fo.read(cg_class8info[i])
                    i += 1
        except IOError:
            i = 0
        # Set up the frames
        self.main_window = tkinter.Tk()
        self.right_frame = tkinter.Frame()
        self.left_frame  = tkinter.Frame()
        self.bottom_frame= tkinter.Frame()
        self.main_window.title ("Sinister Software Solutions -- Student Calendar")
        
        # These stringviables will be useful
        self.str1var = tkinter.StringVar("")
        self.str2var = tkinter.StringVar("")
        self.str3var = tkinter.StringVar("")
        self.str4var = tkinter.StringVar("")
        self.str5var = tkinter.StringVar("")
        self.str6var = tkinter.StringVar("")
        self.str7var = tkinter.StringVar("")
        self.str8var = tkinter.StringVar("")

        #Initialize the dates for use in the program
        workingdate = firstdate
        currentdate = firstdate

        #Strip the newline characters if there is one.
        if (cg_info.cgclass1 != "\n"):
            cg_info.cgclass1.rstrip ()
        if (cg_info.cgclass2 != "\n"):
            cg_info.cgclass2.rstrip()
        if (cg_info.cgclass3 != "\n"):
            cg_info.cgclass3.rstrip ()
        if (cg_info.cgclass4 != "\n"):
            cg_info.cgclass4.rstrip()
        if (cg_info.cgclass5 != "\n"):
            cg_info.cgclass5.rstrip ()
        if (cg_info.cgclass6 != "\n"):
            cg_info.cgclass6.rstrip ()
        if (cg_info.cgclass7 != "\n"):
            cg_info.class7.rstrip ()
        if (cg_info.cgclass8 != "\n"):
            cg_info.class8.rstrip ()
            

        # The labels will get loaded into the left frame
      
        self.class1label = tkinter.Label(self.left_frame, text = cg_info.cgclass1)
        self.class2label = tkinter.Label(self.left_frame, text = cg_info.cgclass2)
        self.class3label = tkinter.Label(self.left_frame, text = cg_info.cgclass3)
        self.class4label = tkinter.Label(self.left_frame, text = cg_info.cgclass4)
        self.class5label = tkinter.Label(self.left_frame, text = cg_info.cgclass5)
        self.class6label = tkinter.Label(self.left_frame, text = cg_info.cgclass6)
        self.class7label = tkinter.Label(self.left_frame, text = cg_info.cgclass7)
        self.class8label = tkinter.Label(self.left_frame, text = cg_info.cgclass8)

      
        # These numbers get loaded into the right frame
        self.class1entry = tkinter.Entry(self.left_frame, width = 120, text = cg_info.cgclass1ingo[i])
        self.class2entry = tkinter.Entry(self.left_frame, width = 120, text = cg_info.cgclass2info[i])
        self.class3entry = tkinter.Entry(self.left_frame, width = 120, text = cg_info.cgclass3info[i])
        self.class4entry = tkinter.Entry(self.left_frame, width = 120, text = cg_info.cgclass4info[i])
        self.class5entry = tkinter.Entry(self.left_frame, width = 120, text = cg_info.cgclass5info[i])
        self.class6entry = tkinter.Entry(self.left_frame, width = 120, text = cg_info.cgclaas6info[i])
        self.class7entry = tkinter.Entry(self.left_frame, width = 120, text = cg_info.cgclass7info[i])
        self.class8entry = tkinter.Entry(self.left_frame, width = 120, text = cg_info.cgclass8info[i])

        # The buttons get loaded into the bottom frame
        self.datelabel = tkinter.Label (self.bottom_frame, \
                                        text = datetime.date.today ())
        self.first = tkinter.Button(self.bottom_frame, text = "First",\
                                    command = self.first_button(firstdate, workingdate))
        self.previous = tkinter.Button(self.bottom_frame, text = "Previous",\
                                       command = self.previous_button)
        self.next= tkinter.Button(self.bottom_frame, text = "Next",\
                                       command = self.next_button)
        self.last     = tkinter.Button(self.bottom_frame, text = "Last",\
                                       command = self.last_button)
        self.save     = tkinter.Button(self.bottom_frame, text = "Save",\
                                       command = self.save_button)

        # Pack the buttons, labels, entries, and label.
        self.left_frame.pack()
        self.right_frame.pack()
        self.bottom_frame.pack()
       

        if (cg_info.cgclass1 != "\n") or (cg_info.cgclass1 != ""):
            self.class1label.pack()
            self.class1entry.pack()
            # I am not putting the else statement here.
            # They should go back and create the file
            # if the student.dta file is missing
    
        if (cg_info.cgclass2 != "\n") or (cg_info.cgclass2 != ""):
            self.class2label.pack()
            self.class2entry.pack()
        else:
            self.class2label.pack_forget()
            self.class2entry.pack_forget()

        if (cg_info.cgclass3 != "\n") or (cg_info.cgclass3 != ""):
            self.class3label.pack()
            self.class3entry.pack()
        else:
            self.class3label.pack_forget()
            self.class4entry.pack_forget()
	    
        if (cg_info.cgclass4 != "\n") or (cg_info.cgclass4 != ""): 
            self.class4label.pack()
            self.class4entry.pack()
        else:
            self.class4label.pack_forget()
            self.class4entry.pack_forget()

        if (cg_info.cgclass5 != "\n") or (cg_info.cgclass5 != ""):
            self.class5label.pack()
            self.class5entry.pack()
        else:
            self.class5label.pack_forget()
            self.class5entry.pack_forget()

        if (cg_info.cgclass6 != "\n") or (cg_info.cgclass6 != ""):
            self.class6label.pack()
            self.class6entry.pack()
        else:
            self.class6label.pack_forget()
            self.class6entry.pack_forget()

        if (cg_info.cgclass7 != "\n") or (cg_info.cgclass7 != ""):
            self.class7label.pack()
            self.class7entry.pack()
        else:
            self.class7label.pack_forget()
            self.class7entry.pack_forget
            
        if (cg_info.class8 != "\n") or (cg_info.cgclass8 != ""):
            self.class8label.pack()
            self.class8entry.pack()
        else:
            self.class8label.pack_forget()
            self.class8entry.pack_forget()


        self.datelabel.pack (side = 'left')
        self.first.pack (side = 'left')
        self.previous.pack(side = 'left')
        self.next.pack(side = 'left')
        self.last.pack(side = 'left')
        self.save.pack (side = 'left')

        tkinter.mainloop ()

    def first_button(self, fbfirstdate, fbworkingdate):
        # Check to see if this is the earliest date read in the
        # student.     
            workingdate = fbfirstdate
            self.datelabel = tkinter.Label(self.bottom_frame, text = workingdate)
            save_temp (workingdate)
    def previous_button(self):
        pass
    def next_button(self):
        pass
    def last_button(self):
        pass
    def save_button(self):
        pass

#--------------------------------------------------------------------
# This procedure will get all of the information and then create
# the student.dta file. Other portions of the program use this file
# in order to display the calendar data appropriately.
#-------------------------------------------------------------------
class fccreateit:
    def __init__ (self):

        self.top_frame = tkinter.Toplevel ()
       
                   
        #Declare the IntVars and StringVarz
        self.fcclassnameentry = tkinter.StringVar()
        self.fcclassnum = tkinter.IntVar()
        self.fcclass1name=tkinter.StringVar()
        self.fcclass2name=tkinter.StringVar()
        self.fcclass3name=tkinter.StringVar()
        self.fcclass4name=tkinter.StringVar()
        self.fcclass5name=tkinter.StringVar()
        self.fcclass6name=tkinter.StringVar()
        self.fcclass7name=tkinter.StringVar()
        self.fcclass8name=tkinter.StringVar()

        #Set the values of these variables
        self.fcclassnameentry.set("")
        self.fcclassnum.set(0)
        self.fcclass1name.set("")
        self.fcclass2name.set("")
        self.fcclass3name.set("")
        self.fcclass4name.set("")
        self.fcclass5name.set("")
        self.fcclass6name.set("")
        self.fcclass7name.set("")
        self.fcclass8name.set("")

        #Set up the Labels and Entries
        self.fcclassnamelabel= tkinter.Label(self.top_frame, text = "Your Name?")
        self.fcclassnameentry= tkinter.Entry (self.top_frame, width = 25)
    
        self.fcclassnumlabel = tkinter.Label(self.top_frame, text ="Number of Classes:")
        self.fcclassnumentry = tkinter.Entry(self.top_frame, width = 1)
        self.fcclass1label   = tkinter.Label(self.top_frame,\
                                             text = "First Class Name:")
        self.fcclass1entry   = tkinter.Entry (self.top_frame, width = 40)
        self.fcclass2label   = tkinter.Label(self.top_frame,\
                                             text = "First Class Name:")
        self.fcclass2entry  = tkinter.Entry (self.top_frame, width = 40)
        self.fcclass2label  = tkinter.Label (self.top_frame, \
                                                     text = "Second Class Name: ")
        self.fcclass3entry    = tkinter.Entry (self.top_frame, width = 40)
        self.fcclass3label   = tkinter.Label (self.top_frame, \
                                                         text = "Third Class Name: ")
        self.fcclass4entry   = tkinter.Entry (self.top_frame, width = 40)
        self.fcclass4label   = tkinter.Label (self.top_frame, \
                                                          text = "Fourth Class Name:")
        self.fcclass5entry   = tkinter.Entry (self.top_frame, width = 40)
        self.fcclass5label   = tkinter.Label (self.top_frame, \
                                                      text = "Fifth Class Name:")
        self.fcclass6entry   = tkinter.Entry (self.top_frame, width = 40)
        self.fcclass6label   = tkinter.Label (self.top_frame, \
                                                      text = "Sixth Class Name:")
        self.fcclass7entry   = tkinter.Entry (self.top_frame, width = 40)
        self.fcclass7label   = tkinter.Label (self.top_frame, \
                                                      text = "Seventh Class Name:")
        self.fcclass8entry   = tkinter.Entry (self.top_frame, width = 40)
        self.fcclass8label   = tkinter.Label (self.top_frame, \
                                              text = "Eighth Class Name:")

        #Create the Save and Quit buttons
        self.fccreatebutton  = tkinter.Button(self.top_frame, text = "Create",\
                                              command = self.fccreate)
        self.fcquitbutton    = tkinter.Button(self.top_frame, text = "Quit",\
                                              command = self.fcquit)

        # Pack the FC Crete It Class Up
        self.fcclassnamelabel.pack()
        self.fcclassnameentry.pack()
        self.fcclassnumlabel.pack()
        self.fcclassnumentry.pack()
        self.fcclass1label.pack()
        self.fcclass1entry.pack()
        self.fcclass2label.pack()
        self.fcclass2entry.pack()
        self.fcclass3label.pack()
        self.fcclass3entry.pack()
        self.fcclass4label.pack()
        self.fcclass4entry.pack()
        self.fcclass5label.pack()
        self.fcclass5entry.pack()
        self.fcclass6label.pack()
        self.fcclass6entry.pack()
        self.fcclass7label.pack()
        self.fcclass7entry.pack()
        self.fcclass8label.pack()
        self.fcclass8entry.pack()
        self.fccreatebutton.pack()
        self.fcquitbutton.pack()
        
    #------------------------------------------------------------------
    # This procedure sets the string variables to the items in the
    # entry boxes. It will then write these files to the student.dta
    # file in binary format. It should use the pickle module to do this
    # as soon as I remember how.
    #-----------------------------------------------------------------
    def fccreate (self):
        fccreatefile = open('student.dta', 'w+')
        self.fcdate       = datetime.date.today ()
        self.fcclassname  = self.fcclassnameentry.get()
        self.fcclassnum   = self.fcclassnumentry.get()
        self.fcclass1name = self.fcclass1entry.get()
        self.fcclass2name = self.fcclass2entry.get()
        self.fcclass3name = self.fcclass3entry.get()
        self.fcclass4name = self.fcclass4entry.get()
        self.fcclass4name = self.fcclass4entry.get()
        self.fcclass5name = self.fcclass5entry.get()
        self.fcclass6name = self.fcclass6entry.get()
        self.fcclass7name = self.fcclass7entry.get()
        self.fcclass8name = self.fcclass8entry.get()
        
        fccreatefile.write (str(self.fcdate) + "\n")
        fccreatefile.write (self.fcclassname +"\n")
        fccreatefile.write (self.fcclassnum + "\n")
        fccreatefile.write (self.fcclass1name + "\n")
        fccreatefile.write (self.fcclass2name + "\n")
        fccreatefile.write (self.fcclass3name + "\n")
        fccreatefile.write (self.fcclass4name + "\n")
        fccreatefile.write (self.fcclass5name + "\n")
        fccreatefile.write (self.fcclass6name + "\n")
        fccreatefile.write (self.fcclass7name + "\n")
        fccreatefile.write (self.fcclass8name + "\n")

        fccreatefile.close ()
        self.top_frame.destroy ()
        
          
    #-----------------------------------------------------------------
    # See the comment directly below this one.
    #-----------------------------------------------------------------
    def fcquit (self):
        tkinter.messagebox.showinfo("Student.dta will not be created.\n", \
                                           "Exiting the program")
        exit ()

#----------------------------------------------------------------------------
# This function creates a box that asks the user if they want to create a
# file. If the user answers yes, the program will create the student.dta
# file that is used for configuration purposes. If the student answers no,
# the program will close this box, the tkinter box and then it will exit.
#----------------------------------------------------------------------------
class file_creation:

    def __init__ (self):

        # Set everything up
        self.fmain_window = tkinter.Toplevel ()
        # Set the labels and buttons up
        self.fcreatelabel = tkinter.Label(self.fmain_window, \
                                       text="Would you like to create student.dta?")
        self.yesbutton   = tkinter.Button(self.fmain_window, text = "Yes",\
                                             command = self.yes)
        self.nobutton    = tkinter.Button(self.fmain_window, text = "No",\
                                              command = self.no)
        # Pack everything up
        self.fcreatelabel.pack ()
        self.yesbutton.pack()
        self.nobutton.pack()
        
    #--------------------------------------------------------------------
    # This button will warn the user that he has not created the data yet
    # and then display a warning about this. It will then exit because
    # exiting is easier then creating more buttons.
    #---------------------------------------------------------------------
    def yes(self):
        self.fmain_window.destroy ()
        myfccreate = fccreateit()

    def no (self):
        exit ()    

#--------------------------------------------------------------------------
# this is the main part of our code. This is the main part of our code.
#--------------------------------------------------------------------------
def main ():

    # If the presence of the student.dta file is detected or creted, isthere
    # is set to true. This will be sent to calendar Gui and used by the program
    isthere = False    
    try:
        studentfile = open("student.dta", 'r')
        # workingfile = open('stdntcal.tmp', 'r+')
        # if os.isfile('stdntcal.cal'):
        #    mainfile = open('stdntcal.cal', 'r+')
        #    read_in_data()
        # else:
        #   mainfile = open('stdtcal.cal', 'w+')

        isthere =True
    except IOError:
        isthere = False
        tkinter.messagebox.showinfo("Sinister Software Solutions", "Student.dta could not be found.")
        student_data_entry = file_creation ()
        workingfile = open ('stdntcal.tmp', 'w+')
    except ValueError:
        tkinter.messagebox.showinfo("Sinister Software Solutions", "Value Error")
    except EOFError:
        tkinter.messagebox.showinfo("Sinister Software Solutins", "At end of file.")
    except OSError:
         tkinter.messagebox.showinfo("Sinister Software Soltions", "Something went wrong with the operating system.")
    except:
        tkinter.messagebox.showinfo("Sinister Software Solutions", "An Unspecified Error Occurred")
        exit ()

   
    MyGui =  Calendar_Gui(isthere)

main ()
