import os
import tkinter as tk
from tkinter import messagebox
import psutil
import winreg as reg
from PIL import Image, ImageTk
import webbrowser
from tkinter import simpledialog
import sys
base_path=os.path.dirname(os.path.abspath(__name__))
print(base_path)
logo_path=os.path.join(base_path,"logo.jpg")
bottom_path=os.path.join(base_path,"bot.jpg")
html_path=os.path.join(base_path,"demo.html")
background_path=os.path.join(base_path,"wa.jpeg")
question_path=os.path.join(base_path,"ques.png")
enable_path=os.path.join(base_path,"ena.jpg")
disable_path=os.path.join(base_path,"disa.jpg")

PASSKEY = "asdfghjkl"  
def resource_path(relative_path):
    """Get the absolute path to resource, works for PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

logo_path = resource_path("logo.jpg")
bottom_path = resource_path("bot.jpg")
background_path = resource_path("wa.jpeg")
question_path = resource_path("ques.png")
enable_path = resource_path("ena.jpg")
disable_path = resource_path("disa.jpg")
html_path = resource_path("ProjectDetails.html")

def verify_passkey(action):
    """
    Prompts the user for a passkey before allowing sensitive actions.
    :param action: A callback function representing the action to perform after passkey verification.
    """
    def wrapper():
        passkey = tk.simpledialog.askstring("Passkey Verification", "Enter the passkey:", show="*")
        if passkey == PASSKEY:
            action()
        else:
            messagebox.showerror("Invalid Passkey", "The passkey you entered is incorrect.")
    return wrapper

def get_pendrive():
    """Detects the inserted pendrive."""
    for partition in psutil.disk_partitions():
        if sys.platform.startswith("win") and "removable" in partition.opts.lower():
            return partition.device
        elif sys.platform.startswith("linux") and "/media" in partition.mountpoint:
            return partition.device
        elif sys.platform == "darwin" and "/Volumes" in partition.mountpoint:
            return partition.device
    return None


def format_pendrive():
    """Formats the detected pendrive based on the operating system."""
    drive = get_pendrive()
    if not drive:
        messagebox.showerror("Error", "No pendrive detected! Please insert a pendrive.")
        return

    confirm = messagebox.askyesno("Confirm Format", f"Are you sure you want to format {drive}?")
    if confirm:
        try:
            if sys.platform.startswith("win"):
                os.system(f'format {drive[:-1]} /Q /FS:NTFS /Y')
            elif sys.platform.startswith("linux"):
                os.system(f"mkfs.vfat {drive}")
            elif sys.platform == "darwin":
                os.system(f"diskutil eraseDisk FAT32 UNTITLED MBRFormat {drive}")
            messagebox.showinfo("Success", f"{drive} formatted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to format {drive}.\nError: {e}")
    else:
        messagebox.showinfo("Cancelled", "Operation cancelled.")




def disable_usb():
    """Disables USB storage based on the operating system."""
    try:
        if sys.platform.startswith("win"):
            os.system(
                'powershell -Command "Get-PnpDevice -Class DiskDrive | Where-Object {$_.InstanceId -like \'USBSTOR*\'} | Disable-PnpDevice -Confirm:$false"'
            )
        elif sys.platform.startswith("linux"):
            os.system("echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/unbind")
        elif sys.platform == "darwin":
            os.system('osascript -e \'tell application "System Preferences" to quit\'')
            os.system('osascript -e \'do shell script "kextunload /System/Library/Extensions/IOUSBMassStorageClass.kext" with administrator privileges\'')
        messagebox.showinfo("Success", "USB storage has been disabled.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to disable USB: {e}")



def enable_usb():
    """Enables USB storage based on the operating system."""
    try:
        if sys.platform.startswith("win"):
            os.system(
                'powershell -Command "Get-PnpDevice -Class DiskDrive | Where-Object {$_.InstanceId -like \'USBSTOR*\'} | Enable-PnpDevice -Confirm:$false"'
            )
        elif sys.platform.startswith("linux"):
            os.system("echo '1-1' | sudo tee /sys/bus/usb/drivers/usb/bind")
        elif sys.platform == "darwin":
            os.system('osascript -e \'tell application "System Preferences" to quit\'')
            os.system('osascript -e \'do shell script "kextload /System/Library/Extensions/IOUSBMassStorageClass.kext" with administrator privileges\'')
        messagebox.showinfo("Success", "USB storage has been enabled.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to enable USB: {e}")
    


def open_about_us():
    """Opens a new popup window with project details."""
   
    details_window = tk.Toplevel(root)
    details_window.title("About us")
    details_window.geometry("600x700")
    details_window.configure(bg="#585858")  

    
    try:
        img_path_top = logo_path 
        img_top = Image.open(img_path_top)
        img_top = img_top.resize((200, 150), Image.Resampling.LANCZOS)
        img_top_tk = ImageTk.PhotoImage(img_top)

        top_img_label = tk.Label(details_window, image=img_top_tk, bg="#585858") 
        top_img_label.image = img_top_tk  
        top_img_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Image Load Error", f"Could not load top image: {e}")
 
    description_text = """
    This project was developed by a team of two members to implement a reliable and efficient USB management system that allows administrators to enable or disable USB access dynamically. The system enhances security by preventing unauthorized data transfers or potential malware threats by restricting or enabling USB ports as needed.
    
    Our team leveraged technical expertise, collaboration, and problem-solving skills to ensure the successful development of this system, utilizing Python with Tkinter for a user-friendly graphical interface. The application is designed with a focus on simplicity, efficiency and security, aligning with the organizational goals of 
    Supraja Technologies.

    Team Members:

    23E06-ST#IS#7002- N. Sri Laxmi Bhargavi
    23E06-ST#IS#7003- Shaikh Aiman
    """
    paragraph_label = tk.Label(
        details_window,
        text=description_text,
        justify="center",
        wraplength=500,
        bg="#585858",  
        fg="white",   
        font=("Arial", 12)
    )
    paragraph_label.pack(pady=10)

    
    try:
        img_path_bottom = bottom_path  
        img_bottom = Image.open(img_path_bottom)
        img_bottom = img_bottom.resize((700, 200), Image.Resampling.LANCZOS)
        img_bottom_tk = ImageTk.PhotoImage(img_bottom)

        bottom_img_label = tk.Label(details_window, image=img_bottom_tk, bg="#585858")  
        bottom_img_label.image = img_bottom_tk  
        bottom_img_label.pack(pady=5)
    except Exception as e:
        messagebox.showerror("Image Load Error", f"Could not load bottom image: {e}")




def open_help_popup():
    """Opens a popup window explaining the buttons."""
    messagebox.showinfo(
        "Help",
        "Enable USB: Allows USB storage to be enabled.\n"
        "Disable USB: Prevents USB storage access.\n"
        "Format Pendrive: Formats a detected USB drive."
    )


def open_project_details():
    webbrowser.open_new(html_path)


root = tk.Tk()
root.title("USB Physical Device")
root.geometry("700x600")


canvas = tk.Canvas(root, width=700, height=600)
canvas.pack(fill="both", expand=True)


def update_bg_image(event=None):
    try:
        canvas_width = root.winfo_width()
        canvas_height = root.winfo_height()

        
        padding = 10
        adjusted_width = canvas_width - 2 * padding
        adjusted_height = canvas_height - 2 * padding

        
        resized_bg_image = bg_image.resize((adjusted_width, adjusted_height), Image.Resampling.LANCZOS)
        resized_bg_image_tk = ImageTk.PhotoImage(resized_bg_image)

       
        canvas.create_image(padding, padding, image=resized_bg_image_tk, anchor="nw")
        canvas.image = resized_bg_image_tk  
    except Exception as e:
        messagebox.showerror("Image Resize Error", f"Could not resize background image: {e}")



try:
    bg_image_path = background_path 
    bg_image = Image.open(bg_image_path)

    
    bg_image_tk = ImageTk.PhotoImage(bg_image)
    canvas.create_image(10, 10, image=bg_image_tk, anchor="nw") 
    canvas.image = bg_image_tk  

   
    root.bind("<Configure>", update_bg_image)
except Exception as e:
    messagebox.showerror("Image Load Error", f"Could not load background image: {e}")


canvas = tk.Canvas(root, bg="white", highlightthickness=0)
canvas.place(relwidth=1.0, relheight=1.0)


top_frame = tk.Frame(root,bg="white") 
top_frame.place(relwidth=1.0, rely=0.1)


canvas.tag_lower("all")


try:
    help_img = Image.open(question_path)
    help_img = help_img.resize((40, 40), Image.Resampling.LANCZOS)
    help_img_tk = ImageTk.PhotoImage(help_img)

    help_button = tk.Button(
        top_frame,
        image=help_img_tk,
        command=open_help_popup,
        bd=0,
        bg="white",
        highlightthickness=0,
        cursor="hand2"
        
    )
    help_button.pack(side="right", padx=10)

    about_us_button = tk.Button(
        top_frame,
        text="About Us",
        command=open_about_us,
        bd=0,
        bg="white",
        highlightthickness=0,
        fg="black",
        cursor="hand2"
    )
    about_us_button.pack(side="right", padx=10)

   
    project_details_button = tk.Button(
        top_frame,
        text="Project Details",
        command=open_project_details,
        bd=0,
        bg="white",
        highlightthickness=0,
        fg="black",
        cursor="hand2"
    )
    project_details_button.pack(side="right", padx=10)
except Exception as e:
    messagebox.showerror("Image Load Error", f"Could not load help icon image: {e}")


button_frame = tk.Frame(root, bg="white")
button_frame.place(rely=0.45, relx=0.5, anchor="center")


try:
    enable_img = Image.open(enable_path)
    enable_img = enable_img.resize((100, 100), Image.Resampling.LANCZOS)
    enable_img_tk = ImageTk.PhotoImage(enable_img)

    disable_img = Image.open(disable_path)
    disable_img = disable_img.resize((100, 100), Image.Resampling.LANCZOS)
    disable_img_tk = ImageTk.PhotoImage(disable_img)
except Exception as e:
    messagebox.showerror("Image Load Error", f"Could not load images: {e}")


enable_button = tk.Button(
    button_frame,
    image=enable_img_tk,
    command=verify_passkey(enable_usb),
    bd=0,
    bg="white",
    highlightthickness=0,
    cursor="hand2"
)

enable_button.grid(row=0, column=0, padx=10, pady=10)

disable_button = tk.Button(
    button_frame,
    image=disable_img_tk,
    command=verify_passkey(disable_usb),
    bd=0,
    bg="white",
    highlightthickness=0,
    cursor="hand2"
)
disable_button.grid(row=0, column=1, padx=10, pady=10)


format_button = tk.Button(
    root,
    text="Format Pendrive",
    command=verify_passkey(format_pendrive), 
    bg="red",
    fg="white",
    height=2,
    width=15,
    bd=0,
    highlightthickness=0,
    cursor="hand2"
)

format_button.place(rely=0.7, relx=0.5, anchor="center")
root.mainloop()





