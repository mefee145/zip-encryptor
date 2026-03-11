# 🔐 Encrypted ZIP Creator
This Python script creates a password-protected ZIP file containing image files from a selected folder.
# 📌 Features
- Scans a folder for image files (.jpg, .jpeg, .png, .bmp, .gif)
- Compresses them into a .zip archive
- Encrypts the ZIP using AES encryption with a user-defined password
# 🧠 How It Works
- User inputs:
- Folder path
- ZIP file name
- Password
- The script filters image files in the folder
- It creates a ZIP file with AES encryption
- Each image is added to the archive
- A confirmation message is printed
# 🛠 Requirements
- pyzipper
- zipfile (standard library)
# 🚀 Example Usage
Enter The Folder Path: C:\Users\name\Pictures

Enter The Zip Name: images

Enter Password: mysecurepass
