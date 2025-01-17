# Prerequisites

![usbdropattack1](https://github.com/user-attachments/assets/b36c23b4-54dc-4a4d-9ebe-aee0ff86399e)
<br>

---
__Ensure you have the following Python packages installed:__ <br>

- __os:__ Used to manage file system operations such as detecting USB devices, checking file paths, and handling system configurations related to USB storage.
- __tkinter:__ Provides the main graphical interface for the USB Physical Device Manager. The various widgets (buttons, labels, entry fields) are created using tkinter for user interaction with the application.
- __tkinter.messagebox:__ Utilized for displaying message boxes to provide user feedback. For example, it is used to show success messages after formatting a USB drive or to alert users about errors.
- __psutil:__ Monitors and retrieves system information about USB devices, helping detect connected USB storage devices and manage them dynamically within the GUI.
- __winreg:__ Manages system registry entries related to USB storage, enabling the application to control access to USB devices through registry modifications for enhanced security.
- __PIL (Pillow):__ Used for handling images in the GUI, such as background images, icons, or dynamically loaded images for buttons, enhancing the visual appeal and functionality of the application.
- __webbrowser:__ Opens web pages to provide links to user documentation or relevant project information from within the GUI interface, allowing administrators to access detailed resources quickly.
- __tkinter.simpledialog:__ Used to handle sensitive user input like passkeys required for certain actions (e.g., disabling/enabling USB devices), ensuring secure access to features.
- __sys:__ Helps manage platform-specific operations, ensuring the application works seamlessly on different Windows environments by handling USB device operations.
- __PyInstaller:__ Converts the Python script into an executable file (.exe) for easy deployment and usage without requiring a Python installation.


__<ins> NOTE: </ins>__ <br>

              python -m PyInstaller --onefile --noconsole --icon="icon image in .ico format" --add-data "logo.jpg;." --add-data "bot.jpg;." --add-data "wa.jpeg;." --add-data "ques.png;." --add-data "ena.jpg;." --add-data "disa.jpg;." --add-data "demo.html;." <filename>.py

---

- Here --add-data is used to include additional non-Python files (like images, HTML files, configuration files, etc.) in the executable. This ensures that these files are bundled with the application and can be accessed during runtime without the need of images in the other system where .exe file is added.
- This ensures that all necessary resources are bundled together, preventing path errors and allowing the application to run smoothly in any system.
