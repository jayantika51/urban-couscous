from tkinter import *
from tkinter import filedialog as fd
import hashlib

root=Tk()
root.geometry("250x190")

def apply_md5():
    md5_file=open("md.txt",'w')
    md5_file.write(file_hexd)
    print("MD5 function")
    text_file = fd.askopenfilename(title="Open Text File", filetype=(("Text Files","*.txt"),))
 
    
def apply_sha256():
    sha256=open("sha.txt",'w')
    sha256_file.write(file_hexd)
    print("SHA function") 
    text_file = fd.askopenfilename(title="Open Text File", filetype=(("Text Files","*.txt"),))
 
    
    
btn=Button(root, text="Apply MD5",command=apply_md5, bg="pink", relief=FLAT)
btn.place(relx=0.3,rely=0.5, anchor=CENTER)
btn1=Button(root, text="Apply SHA256",command=apply_sha256, bg="green", relief=FLAT)
btn1.place(relx=0.7,rely=0.5, anchor=CENTER)
root.mainloop()