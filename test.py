# import tkinter as tk
# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
# import csv
# import subprocess

# Logs = Tk()  # Loga objekts
# Logs.title("Mācību konsultācijas")
# Logs.geometry("300x500")
# Logs.configure(background="#f9f9f9")


# def login():
#     lietotaji = {}
#     username = username_entry.get()
#     password = password_entry.get()

#     with open('Skoleni.csv', mode='r', newline='', encoding="utf-8") as file:
#         csv1 = csv.DictReader(file)
#         for row in csv1:
#             lietotaji[row['lietotajs']] = row  # Ensure this matches the actual column name in your CSV
#             # Check if the username and password match
#             if row['lietotajs'] == username and row['parole'] == password:
#                 Logs.destroy()
#                 subprocess.call(['python', 'logs1stud.py'])  # Launch the next script if login is successful
#                 return  # Exit the function after successful login
#         messagebox.showerror("Kļūda", "Nepareizs lietotāja vārds vai parole!")  # Error message if no match is found


# # UI components
# ttk.Label(Logs, text="Lietotājvārds", font="Arial 20", background='#f9f9f9').grid(row=2, column=1, padx=30, pady=40)
# username_entry = ttk.Entry(Logs, font="Arial", background='#f9f9f9')
# username_entry.grid(row=3, column=1, padx=30, pady=10)

# ttk.Label(Logs, text="Parole", font="Arial 20", background='#f9f9f9').grid(row=4, column=1, padx=30, pady=40)
# password_entry = ttk.Entry(Logs, font="Arial", background='#f9f9f9', show="*")  # 'show' hides the password input
# password_entry.grid(row=5, column=1, padx=30, pady=10)

# tk.Button(Logs, text="Pieslēgties", font="Arial", bd=5, command=login).grid(row=6, column=1, padx=100, pady=40)

# Logs.mainloop()

# with open('Skoleni.csv',mode='r',newline='', encoding="utf-8") as file:
#          csv1 = csv.DictReader(file)
# print(csv1)

# with open("Skoleni.csv",encoding="utf-8") as file:
#     csv1 = csv.reader(file)
#     saraksts = list(csv1)
#     print("Izdruka ir: ", saraksts)
#     print("--------------------------------------------------------")



# name = "Alie"
# age = 30
# city = "New York"

# with open("pieteikumi.txt","a") as file:
#     file.write(f"Name: {name}, Age: {age}, City: {city}.\n")

import datetime
from tkinter import *
from tkcalendar import *


def showEvent(event):

    y = cal.get_calevents(date = cal.selection_get())#iegūst izvēlētos datumu

    t.delete(1.0,'end')#izdzēš visu iepriekš ievadīto, lai ievadītu jaunu informāciju
    t.insert('end', f" ~ ~   {cal.selection_get().strftime('%d-%B-%Y')}   ~ ~ \n\n")#headers
    t.tag_add("here", "1.0", "2.0")#ievieto tagu here, kur it 1. un 2. kolona, header
    t.tag_config("here", background = "#FFEDC5", foreground = "black", underline = True, justify = 'center')#header

    for i in y:#cikls iziet cauri katrai eventam izvēlētajā datumā

        aux = cal.calevent_cget(i, 'tags')#dabūj tagus par iepriekš uzrakstīto informāciju

        if len(aux) > 1:# ja tagu garums ir lielāks par 1

            t.insert('end', f"{aux[i]}\n")#izdrukā jau iepriekš izveidotos tagus/informāciju
        else:

            t.insert('end', f"{aux[0]}\n")#ja ir tikai viens tafs tad ieraksta tikai to tagu


def load_task():
    
    
    with open('saved_events.txt', 'a+') as f:# Atver teksta failu 

        f.close()#Aizver failu
    
    with open('saved_events.txt', 'r') as f:# Atver teksta failu nolasīšanas režīmā

        txt_reader = f.readlines()#Nolasa visas faila rindas una saglabā kā stringus
        txt_reader = [txt_reader[i].split('\n') for i in range(len(txt_reader))]#Sadala tekstu 
        [txt_reader[i].remove('') for i in range(len(txt_reader)) if len(txt_reader[i]) > 1]#Izņem tukšos elementus


    global tag_list
    global date_list
    global datetime_format#Mainīgie definēti kā globālie, izmantojami visur

    for i in range(len(txt_reader)):

        if txt_reader[i][0] != '':#parbauda vai rindiņas pirmais elements nav tukšs

            tag_list.append(txt_reader[i][0])#pievieno pirmo elementu pie tag_list
        else:

            del txt_reader[0:i+1]#Ja pirmais elements ir tukšs to izdzēš
            date_list = [int(k[0]) for k in txt_reader]#katras linijas pirmo elementu pārveido par veselu skaitli

            break#pārtrauc ciklu kad datumi ir apstrādāti

    datetime_format = []#tukšs saraksts kurā saglabāt apstrādātos datumus

    i = 0# Initialize the loop index variable 'i'
    while i in range(len(date_list)):# Loop through the 'date_list' in chunks of 3 items (representing year, month, day)

        datetime_format.append(datetime.date(date_list[i], date_list[i+1], date_list[i+2]))# Create a date object from the year, month, and day extracted from the 'date_list' and append it to 'datetime_format'
        
        i += 3# Increment 'i' by 3 to move to the next set of year, month, day

    
    for i in range(len(tag_list)):# Iterate through the 'tag_list' and create calendar events based on the tag and date information

        id = cal.calevent_create(datetime_format[i], 'Task', tags = tag_list[i])
        cal.tag_config(tag_list[i], background = 'red', foreground = 'yellow')#vizualais, krāsas
    

def update_fun():

    textbox_list = t.get(3.0, 'end') # Correspond to everything in textbox, less first line

    # These two lines prepare the word or sentence to be treated
    textbox_list = textbox_list.split("\n")
    textbox_list = list(filter(('').__ne__, textbox_list))#izdzēš visas rindas 

    dif_insert = list(set(textbox_list).difference(set(tag_list))) # If there is a new item to insert (or several)

    for i in dif_insert:#pievieno visu jaunos tagus

        tag_list.append(i)

        date_list.append(cal.selection_get().year)
        date_list.append(cal.selection_get().month)
        date_list.append(cal.selection_get().day)

        id = cal.calevent_create(cal.selection_get(), 'Task', tags = i)## Izveidojiet jaunu kalendāra notikumu ar jauno tagu un atlasīto datumu
 # "Uzdevums" tiek izmantots kā notikuma nosaukums, un notikumam tiek lietots tags i
        cal.tag_config(tag_list[-1], background = 'red', foreground = 'yellow')#ja tajā dienā kaut kas ir, tad izīmējās citā krāsā


    y = cal.get_calevents(date = cal.selection_get())#visus events iegūst konkrētajā datumā
    aux = []#izveido jaunu sarakstu

    for i in y:

        aux.append(cal.calevent_cget(i,'tags')[0])#caur ciklu pievieno 1. tagu

    dif_delete = list(set(aux).difference(set(textbox_list))) # If there is a new item to delete (or several)

    for j in dif_delete:#noņem lietas, kuras ir izdzēstas

        id2 = cal.get_calevents(date = cal.selection_get(), tag = j)#iegūst visus jau uzrakstītos tagus

        cal.calevent_remove(tag = j)#moņems informāciju tagos

        date_list.pop(3*tag_list.index(j))#izņem informāciju no saraksta
        date_list.pop(3*tag_list.index(j))#izņem informāciju no saraksta
        date_list.pop(3*tag_list.index(j))#izņem informāciju no saraksta

        tag_list.remove(j)#noņem tagu j
        
    # Lines to check that everything is going well
    # '''print(f'\nDiff Insert: {dif_insert}\n')
    # print(f'\nDiff Delete: {dif_delete}\n')

    # print(f'Update List(textbox_list): {textbox_list}\n')
    
    # print(f'Tag List: {tag_list}')
    # print(f'Date List: {date_list}')
    # print(f'IDs: {cal.get_calevents()}')'''

    with open('saved_events.txt', 'w') as f:#atver failu lasīšanas rež

        for i in tag_list:# Write each tag from 'tag_list' into the file, one per line.

            f.write(f'{i}\n')# Write each tag followed by a newline character.
        
        f.write('\n')#pievieno tukšu rindu lai atdalītu tagus no datumiem failā

        for i in date_list:# Write each tag from 'tag_list' into the file, one per line.

            f.write(f'{i}\n')# Write each tag followed by a newline character.


# Hover functions
def enter_fun(e):

    update_button['background'] = '#8F8F87'
    update_button['foreground'] = '#FFEDC5'
    update_button['font'] = ('Pristina 15 bold')

def leave_fun(e):

    update_button['background'] = '#FFEDC5'
    update_button['foreground'] = 'black'
    update_button['font'] = ('Pristina 15 bold')



if __name__ == '__main__':

    tag_list = []
    date_list = []

    year = datetime.datetime.now().year
    
    root = Tk()
    root.title('Calendar')
    #root.iconbitmap('ga2.ico') # https://icon-icons.com


    cal = Calendar(root, Year = year)

    cal.config(background = '#5A3E00', foreground = '#BCFFF9', font = ('Pristina 12 bold'), bordercolor = '#5A3E00', borderwidth = 0,
        headersbackground = '#FFEDC5', headersforeground = 'black', 
        normalbackground = 'white', normalforeground = 'black', weekendbackground = 'white', weekendforeground = 'black',
        othermonthforeground = '#464646', othermonthbackground = '#C5C5C5', othermonthweforeground = '#464646', othermonthwebackground = '#C5C5C5')


    cal.bind('<<CalendarSelected>>', showEvent)
    cal.pack(fill = 'both',expand = 1)


    load_task()


    t = Text(root, height = 12, width = 50)
    t.config(relief = 'solid', borderwidth = 2, font = ('Arial 13 bold'), padx = 10, pady = 10)
    t.pack(fill = 'both', expand = 1)


    update_button = Button(root, text = 'Update', command = update_fun)
    update_button.pack(fill = 'both', expand = 1)
    update_button.config(relief = 'solid', borderwidth = 1, cursor = 'hand2', background  = '#FFEDC5', font = ('Pristina 15 bold'))

    update_button.bind('<Enter>', enter_fun)
    update_button.bind('<Leave>', leave_fun)

    root.mainloop()