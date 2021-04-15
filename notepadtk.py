#notepad using tkinter 

import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser,filedialog,messagebox,font
import os


main_application=tk.Tk()
main_application.geometry("900x600")
main_application.title("MOHIT Notepad")

#photo = PhotoImage(file = "C:/Users/HP/Desktop/logo/notepad.png")
#main_application.iconphoto(False, photo)

main_menu=tk.Menu()



#file

file=tk.Menu(main_menu,tearoff=False)

main_menu.add_cascade(label="File",menu=file)

text_url=""
#new
def new_file(event=None):
    global text_url
    text_url=""
    text_editor.delete(1.0,tk.END)
#open
def open_file(event=None):
    global text_url
    text_url=filedialog.askopenfilename(initialdir=os.getcwd(),title="select file",filetypes=(("Text file","*.txt"),("All files","*.*")))
    try:
        with open(text_url,"r") as for_read:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,for_read.read())
    except FileNotFoundError:
           return
    except:
        return
    main_application.title(os.path.basename(text_url))
    
# save 
def save_file(event=None):
    global text_url
    try:
        if text_url:
            content=str(text_editor.get(1.0,tk.END))
            with open(text_url,"w",encoding="utf-8") as for_read:
                for_read.write(content)
        else:
            text_url=filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=(("Text file","*.txt"),("All files","*.*")))
            content2=text_editor.get(1.0,tk.END)
            text_url.write(content2)
            text_url.close()
    except:
        return
    
#save as
def save_as_file(event=None):
    global text_url
    try:
        content=text_editor.get(1.0,tk.END)
        text_url=filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=(("Text file","*.txt"),("All files","*.*")))
        text_url.write(content)
        text_url.close()
    except:
        return
# exit        
def exit_file(event=None):
    global text_change,text_url  
    try:
        if text_change:
            mbox=messagebox.askyesnocancel("warning","Do you want to save this file")
            if mbox is True:
                if text_url:
                    content=text_editor.get(1.0,tk.END)
                    with open(text_url,"w",encoding="urf-8") as for_read:
                        for_read.write(content)
                        main_application.destroy()

                else:
                    content2=text_editor.get(1.0,tk.END)
                    text_url=filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=(("Text file","*.txt"),("All files","*.*")))
                    text_url.write(content2)
                    text_url.close()
                    main_application.destroy()
            elif mbox is False:
                 main_application.destroy()
        else:
             main_application.destroy()
    except:
        return            
file.add_command(label="New",accelerator="Ctrl+N",command=new_file)
file.add_command(label="Open",accelerator="Ctrl+O",command=open_file)
file.add_command(label="Save",accelerator="Ctrl+S",command=save_file)
file.add_command(label="Save_as",accelerator="Ctrl+Alt+S",command=save_as_file)
file.add_command(label="Exit",accelerator="Ctrl+",command=exit_file)


#edit
edit=tk.Menu(main_menu,tearoff=False)

main_menu.add_cascade(label="Edit",menu=edit)

edit.add_command(label="Copy",compound=tk.LEFT,accelerator="Ctrl+c",command=lambda:text_editor.event_generate("<Control c>")) 
edit.add_command(label="Paste",compound=tk.LEFT,accelerator="Ctrl+v",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut",compound=tk.LEFT,accelerator="Ctrl+x",command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Clear all",compound=tk.LEFT,accelerator="Ctrl+Alt+x",command=lambda:text_editor.delete(1.0,tk.END))
# find 
def find_fun(event=None):
    def find():
        word=find_input.get()
        text_editor.tag_remove("match","1.0",tk.END)
        matches=0
        if word:
            start_pos="1.0"
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match",start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config("match",foreground="red",background="blue")
    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)
    find_popup=tk.Toplevel()
    find_popup.geometry("450x200")
    find_popup.title("Find word")
    find_popup.resizable(0,0)    
   
    
    #fram for find
    find_frame=ttk.LabelFrame(find_popup,text="Find and replace word")
    find_frame.pack(pady=20)
    #label
    text_find=ttk.Label(find_frame,text="Find")
    text_find.grid(row=0,column=0,padx=4,pady=4)
    text_replace=ttk.Label(find_frame,text="Replace")
    text_replace.grid(row=1,column=0,padx=4,pady=4)
    #entry box
    find_input=ttk.Entry(find_frame,width=30)
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input=ttk.Entry(find_frame,width=30)
    replace_input.grid(row=1,column=1,padx=4,pady=4)
    #button
    find_button=ttk.Button(find_frame,text="Find",command=find)
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button=ttk.Button(find_frame,text="Replace",command=replace)
    replace_button.grid(row=2,column=1,padx=8,pady=4)
    
    
    
edit.add_command(label="Find",compound=tk.LEFT,accelerator="Ctrl+f",command=find_fun)


#view
view=tk.Menu(main_menu,tearoff=False)

main_menu.add_cascade(label="View",menu=view)

#toolbar and statusbar
show_status_bar=tk.BooleanVar()
show_status_bar.set(True)
show_tool_bar=tk.BooleanVar()
show_tool_bar.set(True)

def hide_toolbar():
    global show_tool_bar
    if show_tool_bar:
        tool_bar_label.pack_forget()
        show_tool_bar=False
    else:
        text_editor.pack_forget()
        status_bars.pack_forget()
        tool_bar_label.pack(side=tk.TOP,fill=tk.X)        
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bars.pack(side=tk.BOTTOM)
        show_tool_bar=True
        
def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar=False
    else:
        status_bars.pack(side=tk.BOTTOM)
        show_status_bar=True
        
    
view.add_checkbutton(label="Tool Bar",onvalue=True,offvalue=0,compound=tk.LEFT,variable=show_tool_bar,command=hide_toolbar)
view.add_checkbutton(label="Status Bar",onvalue=True,offvalue=0,compound=tk.LEFT,variable=show_status_bar,command=hide_statusbar)

#color image

color_theme=tk.Menu(main_menu,tearoff=False)

main_menu.add_cascade(label="Color Theme",menu=color_theme)


color_dict={"Light Default":("#000000","#ffffff"),
            "Light Plus":("#474747","#e0e0e0"),
            "Dark":("#c4c4c4","#2d2d2d"),
            "Red":("#2d2d2d","#ffe8e8"),
            "Monokai":("#d3b774","#474747"),
            "Night Blue":("#ededed","#6b9dc2")
            }
theme_choose=tk.StringVar()  

def change_theme():
    get_theme=theme_choose.get()
    colour_tupel=color_dict.get(get_theme)
    fg_color,bg_color=colour_tupel[0],colour_tupel[1]
    text_editor.config(background=bg_color,foreground=fg_color)     
count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,compound=tk.LEFT,variable=theme_choose,command=change_theme)
    count=+1
    
#style

tool_bar_label=ttk.Label(main_application)
tool_bar_label.pack(side=tk.TOP,fill=tk.X)

font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar_label,width=30,textvariable=font_family,state="readonly")
font_box["values"]=font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0,column=0,padx=5,pady=5)

# size box

font_tuple=tk.font.families()
size_variable=tk.IntVar()
font_size=ttk.Combobox(tool_bar_label,width=20,textvariable=size_variable,state="readonly")
font_size["values"]=tuple(range(8,100,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5,pady=5)

# bold button

bold_btn=ttk.Button(tool_bar_label,text="Bold")
bold_btn.grid(row=0,column=3,padx=5)
    
# under line
underline_btn=ttk.Button(tool_bar_label,text="Under line")   
underline_btn.grid(row=0,column=4,padx=5)

#font color button
font_color_btn=ttk.Button(tool_bar_label,text="Color")
font_color_btn.grid(row=0,column=5,padx=5)

#align left
align_left_btn=ttk.Button(tool_bar_label,text="Left")
align_left_btn.grid(row=0,column=6,padx=5)

#align center 
align_center_btn=ttk.Button(tool_bar_label,text="Center")
align_center_btn.grid(row=0,column=7,padx=5)

# align right
align_right_btn=ttk.Button(tool_bar_label,text="Right")
align_right_btn.grid(row=0,column=8,padx=5) 

# text editior
text_editor=tk.Text(main_application)
text_editor.config(wrap="word",relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#status bar for count no-
status_bars=ttk.Label(main_application,text="Status bar")
status_bars.pack(side=tk.BOTTOM)

########################################################################################
text_change=False
# for count 
def change_word(event=None):
    global text_change
    if text_editor.edit_modified():
        text_change=True
        word=len(text_editor.get(1.0,"end-1c").split())
        character=len(text_editor.get(1.0,"end-1c").replace(" ",""))
        status_bars.config(text=f"character:{character},word:{word}")
    text_editor.edit_modified(False)
                              
text_editor.bind("<<Modified>>",change_word)     

# style,font
font_now="Arial"
font_size_now=16

def change_font(main_application):
    global font_now
    font_now=font_family.get()
    text_editor.configure(font=(font_now,font_size_now))

    
def change_size(main_application):
    global font_size_now
    font_size_now=size_variable.get()
    text_editor.configure(font=(font_now,font_size_now))
    
font_box.bind("<<ComboboxSelected>>",change_font)    
font_size.bind("<<ComboboxSelected>>",change_size)

#bold function

def bold_fun():
    text_get=tk.font.Font(font=text_editor["font"])
    if text_get.actual()["weight"]=="normal":
        text_editor.configure(font=(font_now,font_size_now,"bold"))
    if text_get.actual()["weight"]=="bold":
        text_editor.configure(font=(font_now,font_size_now,"normal"))  
        
bold_btn.configure(command=bold_fun)

#underline

def underline_fun():
    text_get=tk.font.Font(font=text_editor["font"])
    if text_get.actual()["underline"]==0:
        text_editor.configure(font=(font_now,font_size_now,"underline"))
    if text_get.actual()["underline"]==1:
        text_editor.configure(font=(font_now,font_size_now,"normal"))  
        
underline_btn.configure(command=underline_fun)

# color change

def color_chooser():
    color_var =tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
    
font_color_btn.configure(command=color_chooser)
    
# align left

def align_left():
    text_get_all=text_editor.get(1.0,"end")
    text_editor.tag_configure("left",justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"left")
    
align_left_btn.configure(command=align_left)

# align right 

def align_right():
    text_get_all=text_editor.get(1.0,"end")
    text_editor.tag_configure("right",justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"right")
    
align_right_btn.configure(command=align_right)

# align center 

def align_center():
    text_get_all=text_editor.get(1.0,"end")
    text_editor.tag_configure("center",justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"center")
    
align_center_btn.configure(command=align_center)






   
main_application.config(menu=main_menu)

main_application.mainloop()