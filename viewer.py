try:
    import tkinter as tk
    from PIL import Image, ImageTk
    import tilemap_math as tm
    import map_creation

except:
    import Tkinter as tk
    from PIL import Image, ImageTk
    import tilemap_math as tm
    import map_creation

class Window(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self,master)
        self.master = master

        self.file_name = kwargs.get("file_name",None)

        self.map = ImageTk.PhotoImage(Image.open(self.file_name))
        self.map_width = self.map.width()
        self.map_height = self.map.height()

        self.canvas = tk.Canvas(width = self.map_width, height = self.map_height)
        self.canvas.pack(expand=True, fill=tk.BOTH)
        self.map_view = self.canvas.create_image(0,0,image = self.map, anchor= tk.NW)

        self.canvas.bind("<Button-1>", self.setpointer)
        self.canvas.bind("<B1-Motion>",self.pan)

    def pan(self,event):
        self.canvas.scan_dragto(event.x,event.y,gain= 1)

    def setpointer(self,event):
        self.canvas.scan_mark(event.x,event.y)

    def draw_drone(self,pixel,radius):
        print(pixel,self.canvas.winfo_width(),self.canvas.winfo_height())
        self.canvas.create_oval(pixel[0]-radius, (3000-pixel[1])-radius, pixel[0]+radius, (3000-pixel[1])+radius, fill="blue")


if __name__ == '__main__':

    if (input("Would you like to download a map?(yes/no): ").strip().lower() == "yes"):
        latlon = input("Enter latitude,longitude,zoomlevel e.g.'49.2134,-122.73832,17': ")
        user_inputs = latlon.strip().split(',')
        gmd = map_creation.createMap(float(user_inputs[0]),float(user_inputs[1]),int(user_inputs[2]))  # add the top left corner latlng coordinates of the area you want and the zoom level
        img = gmd.generateImage()
        img.save('map.png')

    root = tk.Tk()
    root.title("UAV Tracking")
    root.minsize(width = 672, height = 493)
    root.maxsize(width=672,height = 493)

    map_bg = Window(root, file_name = "map.png")

    # sample of how to draw the drone location.
    map_bg.draw_drone(tm.latlng2pix(49.222531, -122.883727),10)


    map_bg.pack()
    root.mainloop()