# USB_Physical_Security
The USB Physical Device Manager is a comprehensive application developed during my internship at Supraja Technologies. Its primary objective is to dynamically manage USB storage devices to enhance security and prevent unauthorized data transfers or potential malware threats.
### Project Objectives:
<ins>The application allows administrators to:</ins>
- Enable and disable USB storage dynamically for security purposes.
- Format connected USB drives.
- Ensure data security with passkey verification and USB state management (Enable State, Disable State, Format Pendrive).
- Access an intuitive and user-friendly interface for efficient management.

### Project Structure:
- __Main Application:__ A Tkinter-based GUI for managing USB storage devices.
- __Core Features:__ Includes functionality to enable/disable USB ports, format pendrives, and display project details.
- __Images and Resources:__ All necessary image files and a demo HTML file are included for UI enhancements.
- __Executable:__ The project is compiled into an executable file for easy distribution and use.

### Collaboration:
This project was completed with collaboration between two team members. I handled the coding part using Python and the Kivy platform for the backend development. My team member managed the HTML file and documentation, focusing on the frontend and UI/UX aspects.

### Files:
- __main.py:__ The primary Python script containing the core logic and Tkinter GUI for the application.
- __logo.jpg:__ The logo image displayed in the "About Us" section of the application.
- __bot.jpg:__ An image used in the "About Us" section, showcasing additional design elements.
- __wa.jpeg:__ The background image for the application's main window.
- __ques.png:__ The question mark icon used for the help button in the application.
- __ena.jpg:__ The image used for the "Enable USB" button.
- __disa.jpg:__ The image used for the "Disable USB" button.
- __ProjectDetails.html:__ An HTML file containing the project details, which can be opened from the "Project Details" button.
- __.exe file:__ The compiled executable file of the application for direct use without requiring Python installation.

### Installation:
To run this project locally, follow these steps:

- __Clone the repository:__
 git clone https://github.com/Shaikh-Aiman/USB-Physical-Security.git
- __Navigate to the project directory:__
cd USB-Physical-Security
- __Ensure you have Python installed on your system.__
- __Install the required dependencies.__
- __Run the application:__
python main.py
- __Alternatively, use the provided .exe file for a direct run without dependencies.__

### Working:
- __Launch the Application:__
         - The application is launched by executing the .exe file or running the main.py script if the Python environment is set up.
         - A user-friendly graphical interface, developed using the Tkinter library, is displayed.
- __Authentication:__
         - The application includes a passkey verification system to ensure that only authorized users can access and manage USB device settings.
         - Upon entering the correct passkey, users can access the application’s features.
- __Enable or Disable USB Access:__
         - The "Enable USB" button allows the user to restore functionality to USB storage devices.
         - Clicking the button runs backend logic to re-enable USB ports, ensuring they can read/write data.
         - The "Disable USB" button restricts access to USB storage devices.
         - Clicking this button prevents USB ports from reading or writing data, ensuring enhanced security against unauthorized transfers.
- __Format USB Drives:__
         - The application includes functionality to format connected USB drives.
         - Users can select the desired USB drive from a list and initiate formatting, removing all data and preparing it for reuse.
- __Help and Documentation:__
         - The application has a help feature, providing a guide on how to use the software.
         - A "Project Details" button opens the ProjectDetails.html file, containing comprehensive documentation about the application, including its features and usage.
- __Additional Features:__
         - __"About Us" Section:__ Displays project and developer details, including the application's purpose, contributors, and contact information.
- __Executable File for Ease of Use:__ The .exe file allows users to operate the application without installing Python or its dependencies, making it convenient for administrators to use the tool on any Windows system.

### Usage of All Buttons:
- __Enable USB:__ Re-enables USB storage ports on the system.
- __Disable USB:__ Disables USB storage ports to prevent unauthorized access.
- __Format Pendrive:__ Formats the detected pendrive (requires admin rights).
- __Help:__ Opens a popup with a description of all buttons.
- __About Us:__ Displays project details and team members.
- __Project Details:__ Opens a demo HTML file with additional information.

### Conclusion:
The USB Physical Device Manager is a reliable, efficient, and secure application for managing USB storage access. Developed with a focus on security and usability, this tool is ideal for environments that require strict control over data transfers. The inclusion of a passkey-protected interface ensures that only authorized personnel can manage USB access, making it an essential tool for organizations concerned about data security.

### Acknowledgements:
Special thanks to Supraja Technologies for providing the opportunity to develop this project.

### License
This project is licensed under the MIT License.











