import os, pyzipper, zipfile 

def zip_encrypt(folder_path, zip_name, password):
    Extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')# for photos
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(Extensions)]

    with pyzipper.AESZipFile(zip_name, 'w',
                             compression=zipfile.ZIP_DEFLATED,
                             encryption=pyzipper.WZ_AES) as zipf:
        zipf.setpassword(password.encode())
        for file in files:
            path = os.path.join(folder_path, file)
            zipf.write(path, arcname=file)
            print(f"Added: {file}")
        
        print(f"\n ZIP file created: {zip_name}")

# example
folder = input(r"Enter The Folder Path: ")
zip_name = input("Enter The Zip Name: ")
password = input("Enter Password: ")

zip_encrypt(folder_path=folder, zip_name=zip_name + ".zip", password=password)