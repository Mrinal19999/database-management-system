import tkinter as tk

root = tk.Tk()
root.title('DataBase')
title_frame = tk.LabelFrame(root);
title_frame.pack()
title = tk.Label(title_frame, text='The Is Frontend Window')
title.pack()

root.mainloop()