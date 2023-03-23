import tkinter as tk
root = tk.Tk()
root.title('Tkinter Window Demo')
root.bind('<F2>', root.geometry('600x400+0+0'))
root.bind('<F1>', root.geometry('600x400+50+50'))

root.mainloop()