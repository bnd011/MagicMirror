
####################################################
# Names: Jonah Landry, Behram Dossabhoy, Jason Miles
# Date:
# Description: Mirror Assistant GUI 
####################################################
from Tkinter import *
from time import *
import tkFont

#Add the degree symbol
deg = "oF"

#For now, just uses the resolution from the pi
WIDTH = 800
HEIGHT = 600


#inherits frame from Tkinter
class GUI(Frame):
    global WIDTH
    global HEIGHT
    global deg
    global img
    
    def __init__(self, parent):
        #constructor calls superclass' constructor
        Frame.__init__(self, parent)

        #Various font styles. By dividing the set width by the original width, scales the text with the gui.
        self.largeFont = tkFont.Font(family = "Helvetica", size = (15 * (WIDTH/800)))
        self.normalFont = tkFont.Font(family= "Helvetica", size = (8 * (WIDTH/800)))
        self.smallFont = tkFont.Font(family= "Helvetica", size = (6 * (WIDTH/800)))


    def setupGUI(self):
        
        
        #Organize the GUI
        self.pack(fill=BOTH, expand = 1)

        #Date and time on the opposite side. 
        time_frame = Frame(self, width = WIDTH / 5, height = HEIGHT / 7) #sets up the GUI window itself for time
        GUI.textTime = Text(time_frame, bg = 'black', fg='white', state= DISABLED, font=self.largeFont, bd= 0) #Creates what is essentially an empty text box
        GUI.textTime.pack(expand = 1)
        time_frame.pack(side = RIGHT, anchor = N) #Tells it where to go
        time_frame.pack_propagate(False)

        #The top left corner is for the weather report
        #Labels for Image + Text
        weather_label0 = Frame(self, bg= 'black', bd = 0, width = WIDTH / 2, height = HEIGHT/10)
        GUI.textW0 = Text(weather_label0, bg='black', fg='white', state = DISABLED, font=self.largeFont, bd = 0)
        GUI.textW0.pack( expand = 1)
        weather_label0.pack(side = TOP, anchor = W)
        weather_label0.pack_propagate(False)
        
        
                
        weather_label1 = Frame(self, width=WIDTH / 2, height=HEIGHT / 16)
        GUI.textW1 = Text(weather_label1, bg='black', fg='white', state = DISABLED, font= self.normalFont, bd = 0)
        GUI.textW1.pack(fill = BOTH, expand = 1)
        weather_label1.pack(side=TOP, anchor= W)
        weather_label1.pack_propagate(False)

        weather_label2 = Frame(self, width=WIDTH / 2, height=HEIGHT / 16)
        GUI.textW2 = Text(weather_label2, bg='black', fg='white', state = DISABLED, font= self.normalFont, bd = 0)
        GUI.textW2.pack(fill = BOTH, expand = 1)
        weather_label2.pack(side=TOP, anchor= W)
        weather_label2.pack_propagate(False)

        weather_label3 = Frame(self, width=WIDTH / 2, height=HEIGHT / 16)
        GUI.textW3 = Text(weather_label3, bg='black', fg='white', state = DISABLED, font= self.normalFont, bd = 0)
        GUI.textW3.pack(fill = BOTH, expand = 1)
        weather_label3.pack(side=TOP, anchor= W)
        weather_label3.pack_propagate(False)

        
               
        

        #Sets aside an area for calendar, done in reverse order due to the nature of the stack
        cal_label3 = Frame(self, height = HEIGHT/13, width = WIDTH)
        GUI.textC3 = Text(cal_label3, bg = 'black', fg = 'white', bd = 0, state = DISABLED, font = self.normalFont)
        GUI.textC3.pack(fill = BOTH, expand = 1)
        cal_label3.pack(side = BOTTOM, anchor = W)
        cal_label3.pack_propagate(False)

        cal_label2 = Frame(self, height = HEIGHT/13, width = WIDTH)
        GUI.textC2 = Text(cal_label2, bg = 'black', fg = 'white', bd = 0, state = DISABLED, font = self.normalFont)
        GUI.textC2.pack(fill = BOTH, expand = 1)
        cal_label2.pack(side = BOTTOM, anchor = W)
        cal_label2.pack_propagate(False)

        cal_label1 = Frame(self, height = HEIGHT/13, width = WIDTH)
        GUI.textC1 = Text(cal_label1, bg = 'black', fg = 'white', bd = 0, state = DISABLED, font = self.normalFont)
        GUI.textC1.pack(fill = BOTH, expand = 1)
        cal_label1.pack(side = BOTTOM, anchor = W)
        cal_label1.pack_propagate(False)

        cal_label0 = Frame(self, height = HEIGHT/15, width = WIDTH)
        GUI.textC0 = Text(cal_label0, bg = 'black', fg = 'white', bd = 0, state = DISABLED, font = self.largeFont)
        GUI.textC0.pack(fill = BOTH, expand = 1)
        cal_label0.pack(side = BOTTOM, anchor = W)
        cal_label0.pack_propagate(False)

        #Sets the title for the calendar
        GUI.textC0.config(state = NORMAL)
        GUI.textC0.insert(END, "Upcoming Events")
        
        #sets background to black for maximum reflection
        self.configure(background = 'black')


    def timeCalc(self, event):
        #Calculates the difference in a given time (HH:MM 24 hr clock) and gives the difference
        #Gets the current time in military
        timeC = strftime("%H:%M", localtime())
        #Gets both times in terms of minutes since midnight.
        t1 = ((int(event.time[0]) * 10) + int(event.time[1])) * 60 + ((int(event.time[3]) * 10) + int(event.time[4]))
        t2 = ((int(timeC[0]) * 10) + int(timeC[1])) * 60 + ((int(timeC[3]) * 10) + int(timeC[4]))
        result = t1 - t2
        if (result < 0):
            result = 61
        return result

    def MilTo12(self, event):
        #Takes an event's time and converts it to 12HR AM PM
        time = ""
        hour = ((int(event.time[0]) * 10) + int(event.time[1]))
        if (hour >= 12):
            hour = hour - 12
            if (hour < 10):
                time = "0{}:{}{}".format(hour, event.time[3], event.time[4])
            else:
                time = "{}:{}{}".format(hour, event.time[3], event.time[4])
            return time + " PM"
        else:
            return event.time + " AM"

    def dispWeather(self, weather, frameNum):
        #First figures out if you're setting the current date, or the future dates.
        if (frameNum == 0):
            GUI.textW0.delete("1.0",END)
            GUI.textW0.config(state=NORMAL)
            GUI.textW0.image_create(END, image = img0)
            GUI.textW0.insert(END, "High:{} {} | Low: {} {}".format( weather.high,deg, weather.low, deg))

        if (frameNum == 1):
            GUI.textW1.delete("1.0",END)
            GUI.textW1.config(state=NORMAL)
            GUI.textW1.insert(END, "{}:   High:{} {} | Low: {} {}".format(weather.date, weather.high,deg, weather.low, deg))
            GUI.textW1.image_create(END, image = img1)

        if (frameNum == 2):
            GUI.textW2.delete("1.0",END)
            GUI.textW2.config(state=NORMAL)
            GUI.textW2.insert(END, "{}:   High:{} {} | Low: {} {}".format(weather.date, weather.high,deg, weather.low, deg))
            GUI.textW2.image_create(END, image = img2)
            
        if (frameNum == 3):
            GUI.textW3.delete("1.0",END)
            GUI.textW3.config(state=NORMAL)
            GUI.textW3.insert(END, "{}:   High:{} {} | Low: {} {}".format(weather.date, weather.high,deg, weather.low, deg))
            GUI.textW3.image_create(END, image = img3)

    def dispEvent(self, event, frameNum):
        #Displays upcoming events
        timeDif = self.timeCalc(event)
        if (timeDif >= 60):
            time = self.MilTo12(event)
        if (frameNum == 1):
            GUI.textC1.delete("1.0", END)
            GUI.textC1.config(state=NORMAL)
            if (timeDif < 60):
                GUI.textC1.insert(END,"In {} minutes: {}".format(timeDif, event.what)) 
            else:
                GUI.textC1.insert(END,"On {}, at {} : {}".format(event.date, time, event.what))

        if (frameNum == 2):
            GUI.textC2.delete("1.0", END)
            GUI.textC2.config(state=NORMAL)
            if (timeDif < 60):
                GUI.textC2.insert(END,"In {} minutes: {}".format(event.timeDif, event.what))
            else:
                GUI.textC2.insert(END,"On {}, at {} : {}".format(event.date, time, event.what))

        if (frameNum == 3):
            GUI.textC3.delete("1.0", END)
            GUI.textC3.config(state=NORMAL)
            if (timeDif < 60):
                GUI.textC3.insert(END,"In {} minutes: {}".format(event.timeDif, event.what))
            else:
                GUI.textC3.insert(END,"On {}, at {} : {}".format(event.date, time, event.what))
    
    def updateGUI(self):
        #Constantly updates the time until the program is stopped
        GUI.textTime.config(state=NORMAL)
        GUI.textTime.delete("1.0", END)
        GUI.textTime.insert(END, strftime("%I:%M %p \n%A, %B %d ", localtime()))

        #Updates the weather as well
        ##########################  Weather update needs to give a high and a low as well as a status for each date.
        #WEATHER UPDATE GOES HERE# Once we have the status, go back and add more images and if statements to cover each one
        ########################## given by whatever weather database we end up using.
        #Fetches new images
        imageFetch()
        #Displays new weather
        self.dispWeather(weather0, 0)
        self.dispWeather(weather1, 1)
        self.dispWeather(weather2, 2)
        self.dispWeather(weather3, 3)

        #Also updates the upcoming events
        ########################  Event update needs to be able to look at the calendar and place the three most recent events in order, 
        #EVENT UPDATE GOES HERE# no longer displaying events when they pass their time. Also bumping up the other events after that.
        ######################## 
        #Displays the new events
        self.dispEvent(event1, 1)
        self.dispEvent(event2, 2)
        self.dispEvent(event3, 3)
        window.after(1000, mirror.updateGUI)

#Example weather class that gives the GUI what it needs. Location is no longer needed for the GUI, but left it in.
class weatherOriginal(object):
    def __init__(self, location, status, high, low, date):
        self.location = location
        self.status = status
        self.high = high
        self.low = low
        self.date = date
        
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if (value == "Sunny"):
            self._status = r"sun.gif" #Only one image for now, don't know the other status' names so have only done the one.

class weather(object):
    def __init__(self, location, status, high, low, date):
        self.location = location
        self.status = status
        self.high = high
        self.low = low
        self.date = date
        
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if (value == "Sunny"):
            self._status = r"ssun.gif" #Only one image for now, don't know the other status' names so have only done the one.

#Example Event class. Date is the day in "MM/DD/YYYY" format, the time is the time it's at in 24 hour "HH:MM", and the what is what the event is like "Presentation at Nethkin"
class event(object):
    def __init__(self, date, time, what):
        self.date = date 
        self.time = time
        self.what = what

#The first weather report needs to select from a pool of larger images. Accomplished this by using a different variable.
weather0 = weatherOriginal("Ruston, LA", "Sunny", 72.23, 56, "Sunday")

#Otherwise, weather should be as follows.
weather1 = weather("Ruston, LA", "Sunny", 90.45, 75, "Monday")
weather2 = weather("Ruston, LA", "Sunny", 91, 56, "Tuesday")
weather3 = weather("Ruston, LA", "Sunny", 91, 43, "Wednesday")

#Sample events
event1 = event("05/13/2018", "21:00", "Jonah finishes his GUI for now.")
event2 = event("05/16/2018", "08:00", "This project is due.")
event3 = event("05/18/2018", "13:30", "No more school!")



#create the window
window = Tk()
window.title("Personal Assistant")
mirror = GUI(window)
window.geometry('800x500')



#Images to be displayed in GUI need to be declared before hand.
img0 = None
img1 = None
img2 = None
img3 = None
#Put into a function so it can be called by update and updated along with the rest of the weather.
def imageFetch():
    global img0
    global img1
    global img2
    global img3
    img0 = PhotoImage(file = weather0.status)
    img1 = PhotoImage(file = weather1.status)
    img2 = PhotoImage(file = weather2.status)
    img3 = PhotoImage(file = weather3.status)

#setup the gui and play it
mirror.setupGUI()
window.after(1000, mirror.updateGUI)
window.mainloop()

