import customtkinter
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
import os
import shutil

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
resaltion="1000x600"
root=customtkinter.CTk()
root.geometry(resaltion)
root.title("File Organizer")

images=[".jpeg",".jpg",".png",".gif",".bmp"]
vedios=[".mp4",".avi",".mov",".wmv",".flv",".mkv",".mpg",".mpeg"]
fil=[".doc",".docx",".csv",".pptx",".xls",".xlsx",".ppt",".rtf",".odt",".ods",".odp"]
others=images+vedios+fil+[".pdf"]
def path_f():
    global path_from
    path_from = askdirectory()
    path2_label.configure(text=path_from)
    

def path_s():
    global path_save
    path_save = askdirectory()
    path4_label.configure(text=path_save)
    

def start():
    try:
        global count ,total,other
        pathf=path_from
        patht=path_save
        count=0
        for root,dirs,files in os.walk(pathf):
                for file in files:
                    file_path = os.path.join(root, file)
                    count+=1
        total=count
        os.makedirs(patht+"\PHOTOS")
        os.makedirs(patht+"\VIDEOS")
        os.makedirs(patht+"\PDF")
        os.makedirs(patht+"\OFFICE")
        os.makedirs(patht+"\OTHERS")

        
        if mode.get()=="Orginazing With Save The Orignal Files":
            count=0
            for root,dirs,files in os.walk(pathf):
                for file in files:
                    other=0
                    file_path = os.path.join(root, file)
                    for i in images:
                        if os.path.isfile(file_path) and file_path.lower().endswith(i):
                            destination_file =patht+"\PHOTOS"
                            shutil.copy(file_path, destination_file)
                            count+=1
                            break
                        
                    for v in vedios:
                        if os.path.isfile(file_path) and file_path.lower().endswith(v):
                            destination_file =patht+"\VIDEOS"
                            shutil.copy(file_path, destination_file)
                            count+=1
                            break
                    for f in fil:
                        if os.path.isfile(file_path) and file_path.lower().endswith(f):
                            destination_file =patht+"\OFFICE"
                            shutil.copy(file_path, destination_file)
                            count+=1
                            break
                    for o in others:
                        other+=1
                        if os.path.isfile(file_path) and file_path.lower().endswith(o):
                            break
                        elif other==len(others):
                            destination_file =patht+"\OTHERS"
                            shutil.copy(file_path, destination_file)
                            count+=1
                    
                    if os.path.isfile(file_path) and file_path.lower().endswith(".pdf"):
                            destination_file =patht+"\PDF"
                            shutil.copy(file_path, destination_file)
                            count+=1
                    
                    proc.configure(text=str(count)+"/"+str(total))
            showinfo(title="Notfication",message="Your Data Organized")
        elif mode.get()=="Orginazing Without Save The Orignal Files":
            count=0
            for root,dirs,files in os.walk(pathf):
                    for file in files:
                        file_path = os.path.join(root, file)
                        
                        for i in images:
                            if os.path.isfile(file_path) and file_path.lower().endswith(i):
                                destination_file =patht+"\PHOTOS"
                                shutil.copy(file_path, destination_file)
                                os.remove(file_path)
                                count+=1
                                break
                            
                        for v in vedios:
                            if os.path.isfile(file_path) and file_path.lower().endswith(v):
                                destination_file =patht+"\VIDEOS"
                                shutil.copy(file_path, destination_file)
                                os.remove(file_path)
                                count+=1
                                break
                            
                        for f in fil:
                            if os.path.isfile(file_path) and file_path.lower().endswith(f):
                                destination_file =patht+"\FILES"
                                shutil.copy(file_path, destination_file)
                                os.remove(file_path)
                                count+=1
                                break
                        
                        for o in others:
                            other+=1
                            if os.path.isfile(file_path) and file_path.lower().endswith(o):
                                break
                            elif other==len(others):
                                destination_file =patht+"\OTHERS"
                                shutil.copy(file_path, destination_file)
                                os.remove(file_path)
                                count+=1    
                            
                            
                        if os.path.isfile(file_path) and file_path.lower().endswith(".pdf"):
                                destination_file =patht+"\PDF"
                                shutil.copy(file_path, destination_file)
                                os.remove(file_path)
                                count+=1
                        
                        proc.configure(text=str(count)+"/"+str(total))
            showinfo(title="Notfication",message="Your Data Organized")
    except FileExistsError:
        count=count
    except NameError:
        showinfo(title="Erorr",message="Please Check Your Path")
    except shutil.SameFileError:
        count=count
  

modes=["Orginazing With Save The Orignal Files","Orginazing Without Save The Orignal Files"]
path1_label=customtkinter.CTkLabel(root,text="Select Path You Want To Organize:",font=("Roborto",20),text_color="#ffffff")
path1_label.place(x=100,y=50)

path2_label=customtkinter.CTkLabel(root,text="",font=("Roborto",20),text_color="#ffffff")
path2_label.place(x=450,y=50)

path_select=customtkinter.CTkButton(root,text="Browse",text_color="black",fg_color="#eaebed",command=path_f)
path_select.place(x=350,y=100)


path3_label=customtkinter.CTkLabel(root,text="Select Path You Want To Save:",font=("Roborto",20),text_color="#ffffff")
path3_label.place(x=100,y=170)

path4_label=customtkinter.CTkLabel(root,text="",font=("Roborto",20),text_color="#ffffff")
path4_label.place(x=450,y=170)

path_save1=customtkinter.CTkButton(root,text="Browse",text_color="black",fg_color="#eaebed",command=path_s)
path_save1.place(x=350,y=220)


mode_label=customtkinter.CTkLabel(root,text="Select Mode Of Organizing :",font=("Roborto",20),text_color="#ffffff")
mode_label.place(x=100,y=270)

mode=customtkinter.CTkOptionMenu(root,values=modes,fg_color="#eaebed",text_color="black")
mode.place(x=380,y=270)

start_button=customtkinter.CTkButton(root,text="Start",text_color="black",fg_color="#eaebed",command=start)
start_button.place(x=350,y=350)

process=customtkinter.CTkLabel(root,text="Files Organized:",font=("Roborto",20),text_color="#ffffff")
process.place(x=150,y=400)

proc=customtkinter.CTkLabel(root,text="0/0",font=("Roborto",20),text_color="#ffffff")
proc.place(x=380,y=400)
root.mainloop()
