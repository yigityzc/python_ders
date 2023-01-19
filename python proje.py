import tkinter as tk
import threading
import pyautogui as pyautogui

TRNAS_COLOR = '#abcdef'
def change_geometry():
    # Pencerenin ekrandaki konumunu rastgele değerlerle değiştirin
    currentMouseX, currentMouseY = pyautogui.position()

    root.geometry("+{}+{}".format(currentMouseX, currentMouseY))
    root.geometry("+{}+{}".format(currentMouseX, currentMouseY))
    root.after(100, change_geometry)

root = tk.Tk()
root.attributes("-topmost", True)
root.overrideredirect(1)
root.attributes('-transparentcolor', TRNAS_COLOR)
root.geometry("+1700+443")

image1 = tk.PhotoImage(file='./Drawing (5).png')
image2 = tk.PhotoImage(file='./Drawing (6).png')

images=[image1,image2]
label=tk.Label(root, image=image2, bg=TRNAS_COLOR)
label.pack()
counter=0
def update_image():
    global counter
    # label'ın resmini değiştirme
    label.config(image=images[counter])
    counter +=1
    if counter >= len(images):
        counter=0
    # update_image fonksiyonunu tekrar çağırma
    root.after(400, update_image)

root.after(500, update_image)
change_geometry()
root.mainloop()


