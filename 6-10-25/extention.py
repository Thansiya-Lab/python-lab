filename=input("Enter the filename: ")
if "." in filename:
    parts=filename.split(".")
    extention=parts[-1]
    print("The extention of the file is :", extention)
else:
    print("The file has no extention")
