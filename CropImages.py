import tkinter as tk
from tkinter import filedialog, Text
import os
from PIL import Image

pngs = []
cropTop = 0
cropBottom = 0
cropLeft = 0
cropRight = 0

root = tk.Tk()
root.configure(background='black')
root.title("Crop Images")


def addImages():
    for widget in frame.winfo_children():
            widget.destroy()
    filename = filedialog.askopenfilenames(title="Select PNGs",
            filetypes=(("PNGs","*.png"), ("all files", "*.*")))
    
    lst = list(filename)
    pngs.clear()
    for l in lst:
            pngs.append(l)
    for png in pngs:
            label = tk.Label(frame, text=png, bg="grey")
            label.pack()

def CropImgs():
    cropTop = cropTopEntry.get()
    cropBottom = cropBottomEntry.get()
    cropLeft = cropLeftEntry.get()
    cropRight = cropRightEntry.get()
        
    for png in pngs:
        original = Image.open(png)
        orHeight = original.size[1]
        orWidth = original.size[0]
        newWidth = orWidth - (cropLeft + cropRight)
        newHeight = orHeight - (cropTop + cropBottom)

        if newWidth > 0 and newHeight > 0:
            oldPix = original.load()
            newIm = Image.new(mode = "RGBA", size = (newWidth, newHeight), color = (0,0,0,0))
            
            for x in range(newWidth):
                for y in range(newHeight):
                    newIm.putpixel((x,y), oldPix[x+cropLeft, y+cropTop])
                    
            newPath = png.rsplit('/',1)[0] + '/Cropped/' + png.rsplit('/',1)[1]
            directory = png.rsplit('/',1)[0] + '/Cropped'
            if not os.path.exists(directory):
                os.mkdir(directory)

            newIm.save(newPath)
        else:
            print("Crop amount is bigger than image. Aborting.")
        


canvas = tk.Canvas(root, height = 400, width = 400, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="grey")
frame.place(relwidth=.96,relheight=.3, relx=0.02, rely=0.02)

frame2 = tk.Frame(root, bg="#263D42")
frame2.place(relwidth=.45,relheight=.6, relx=0.02, rely=0.35)

frame3 = tk.Frame(root, bg="#263D42")
frame3.place(relwidth=.45,relheight=.6, relx=0.52, rely=0.35)

CTLabel = tk.Label(frame2, text="Crop Top Pixels:", padx = 10, pady = 5, fg = "white", bg="#263D42")
CTLabel.pack()
cropTopEntry = tk.IntVar(value=100)
CTEntry = tk.Entry(frame2, textvariable=cropTopEntry, fg = "white", bg="#263D42")
CTEntry.pack()

CBLabel = tk.Label(frame2, text="Crop Bottom Pixels:", padx = 10, pady = 5, fg = "white", bg="#263D42")
CBLabel.pack()
cropBottomEntry = tk.IntVar(value=100)
CBEntry = tk.Entry(frame2, textvariable=cropBottomEntry, fg = "white", bg="#263D42")
CBEntry.pack()

CLLabel = tk.Label(frame2, text="Crop Left Pixels:", padx = 10, pady = 5, fg = "white", bg="#263D42")
CLLabel.pack()
cropLeftEntry = tk.IntVar()
CLEntry = tk.Entry(frame2, textvariable=cropLeftEntry, fg = "white", bg="#263D42")
CLEntry.pack()

CRLabel = tk.Label(frame2, text="Crop Right Pixels:", padx = 10, pady = 5, fg = "white", bg="#263D42")
CRLabel.pack()
cropRightEntry = tk.IntVar()
CREntry = tk.Entry(frame2, textvariable=cropRightEntry, fg = "white", bg="#263D42")
CREntry.pack()

openFile = tk.Button(frame3, text="Open PNGs", padx = 10, pady = 5, fg = "white", bg="#263D42", command=addImages)
openFile.pack()

CropImg = tk.Button(frame3, text="Crop PNGs", padx = 10, pady = 5, fg = "white", bg="#263D42", command=CropImgs)
CropImg.pack()

root.mainloop()
