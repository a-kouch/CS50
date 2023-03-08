# ask user for name of file
file_name = input("File name: ")

#conditional statement for each file type
if file_name.endswith("gif"):
    print(f"image/{file_name[-3:]}")
elif file_name.endswith("jpg"):
    print(f"image/{file_name[-3:]}")
elif file_name.endswith("jpeg"):
    print(f"image/{file_name[-4:]}")
elif file_name.endswith("png"):
    print(f"image/{file_name[-3:]}")
elif file_name.endswith("pdf"):
    print(f"application/{file_name[-3:]}")
elif file_name.endswith("txt"):
    print(f"application/{file_name[-3:]}")
elif file_name.endswith("zip"):
    print(f"application/{file_name[-3:]}")

#else default output
else:
    print("application/octet-stream")