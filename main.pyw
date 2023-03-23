import tkinter as tk
import win32api


def get_monitor_origin(window_origin):
    monitor_info = win32api.GetMonitorInfo(win32api.MonitorFromPoint(window_origin))
    return monitor_info['Monitor'][0], monitor_info['Monitor'][1]

def move_window_to_monitor_top_left(window):
    window_origin = window.winfo_x(), window.winfo_y()
    monitor_origin = get_monitor_origin(window_origin)
    window.geometry(f'+{monitor_origin[0]}+{monitor_origin[1]}')

#Creates a tkinter window
root = tk.Tk()
root.geometry("500x500")
root.title("Colour Picker")

screen_full = False
old_geometry = ""
old_location = ""

#toggle fullscreen function
def tog_full(event):
    global screen_full, old_geometry, old_location
    #Gets current monitors height & width
    mon_height, mon_width = root.winfo_screenheight(), root.winfo_screenwidth()
    #Gets current window height & width
    win_height, win_width = root.winfo_height(), root.winfo_width()
    print(win_height, win_width)
    
    if screen_full == False:
        root.overrideredirect(True)
        old_geometry = f"{win_width}x{win_height}"
        root.geometry(f"{mon_width}x{mon_height}")
        #moves window to top left corner
        move_window_to_monitor_top_left(root)
        screen_full = True
        
        
    else:
        root.overrideredirect(False)
        root.geometry(old_geometry)
        #moves window to old location
        root.geometry(old_location)
        screen_full = False


#New upgraded version (Still in progress)
'''
def tog_full(event):
    global screen_full, old_geometry, old_location
    mon_height, mon_width = root.winfo_screenheight(), root.winfo_screenwidth()
    win_height, win_width = root.winfo_height(), root.winfo_width()
    
    if screen_full == False:
        root.attributes('-fullscreen', True)
        root.geometry(f"+{mon_width}+{mon_height}")
        screen_full = True
'''   

        
root.bind('<F11>', tog_full)
root.bind('f', tog_full)
#Initializes the rgb values to 0
old_slider_r = 0
old_slider_g = 0
old_slider_b = 0

#Function that updates the colour of the window
def update_colour():
    #Gets the current rgb values and brightness value
    red = r.get()
    green = g.get()
    blue = b.get()
    brightness = bright.get()
    
    #Subtracts the brightness value from the rgb values
    if red >= brightness:
        red -= brightness
    else:
        red = 0
        
    if green >= brightness:
        green -= brightness
    else:
        green = 0
         
    if blue >= brightness:
        blue -= brightness
    else:
        blue = 0
    
    #Converts the rgb values to hex
    hex = "#{:02x}{:02x}{:02x}".format(red, green, blue)
    hex = hex.replace("-", "")
    #changes tkinter bg colour to the hex value
    root.configure(bg=hex)
    root.after(25, update_colour)
    
    #Changes the text colour of the sliders based on the brightness of the background
    if red <= 127.5 and green <= 127.5 and blue <= 127.5:
        
        r.configure(bg=hex, fg="white")
        g.configure(bg=hex, fg="white")
        b.configure(bg=hex, fg="white")
        b.configure(bg=hex, fg="white")
    
    else:        
        r.configure(bg=hex, fg="black")
        g.configure(bg=hex, fg="black")
        b.configure(bg=hex, fg="black")
        b.configure(bg=hex, fg="black")



    
#Creates 3 tkinter sliders that coresponds to rgb values in a variable called r, g, and b
r = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Red")
g = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Green")
b = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Blue")
bright = tk.Scale(root, from_=255, to=0, orient=tk.HORIZONTAL, label="Brightness", showvalue=0)

#Packs the sliders into the tkinter window
r.pack()
g.pack()
b.pack()
bright.pack()

#Calls the update_colour function
update_colour()

#Starts the tkinter mainloop
root.mainloop()
