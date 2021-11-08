from os import access
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def uploadFile(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = "44jlPe4GJJkAAAAAAAAAARCxuUuE8sDp_qrCpvBRxPjk7ZnVBdsajRBexBbZfHTE"
    fileToUpload = TransferData(access_token)
    file_from = input("Enter folder path to transfer: ")
    fileName = input("Enter folder name: ")
    file_to = "/dropbox/" + fileName 
    fileToUpload.uploadFile(file_from,file_to)
    print("The file has been moved")

main()
