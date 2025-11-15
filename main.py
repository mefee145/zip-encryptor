import os, pyzipper, zipfile

def zip_encrypt(folder_path, zip_name, password):
    #Get all files in folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    with pyzipper.AESZipFile(zip_name, 'w',
                             compression=zipfile.ZIP_DEFLATED,
                             encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(password.encode())
        for file in files:
            path = os.path.join(folder_path, file)
            zipf.write(path, arcname=file)
            print(f"Added: {file}")
        
        print(f"\n✅ ZIP file created: {zip_name}")

#Example
folder = input(r"Enter the folder path: ")
zip_name = input("Enter the name of the ZIP file: ")
password = input("Enter password: ")

zip_encrypt(folder_path=folder, zip_name=zip_name + ".zip", password=password)

