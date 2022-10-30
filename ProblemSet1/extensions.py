def find_extention(file_name): # return file type
    if file_name.endswith(".gif"):
        file_type = "image/gif"
        return file_type
    elif file_name.endswith(".jpg"):
        file_type = "image/jpeg"
        return file_type
    elif file_name.endswith(".jpeg"):
        file_type = "image/jpeg"
        return file_type
    elif file_name.endswith(".png"):
        file_type = "image/png"
        return file_type
    elif file_name.endswith(".pdf"):
        file_type = "application/pdf"
        return file_type
    elif file_name.endswith(".txt"):
        file_type = "text/plain"
        return file_type
    elif file_name.endswith(".zip"):
        file_type = "application/zip"
        return file_type
    else: 
        file_type = "application/octet-stream"
        return file_type

user_download_type = find_extention(input()) # calls the function and get file type
print(user_download_type)
