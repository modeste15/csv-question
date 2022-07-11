from tkinter import *
from csv import writer

"""
def insert() : 
    print('ok')
    code=eCode.get()
    commune=eCommune.get()
    type_commune=eType.get()
    nom_departement=eDepartement.get()

    row_contents = ['xxxx', code, commune,type_commune,eDepartement]

    # Open file in append mode
    with open('users.csv', 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj, delimiter = ";")
        # Add contents of list as last row in the csv file
        csv_writer.writerow(row_contents)

"""

def users() :
    import csv

    with open( "users.csv")  as file_name:
        file_read = csv.reader(file_name)

        array = list(file_read)
        
    return array


master = Tk()

variable = StringVar(master)
variable.set("one") # default value
master.geometry("500x300") 
users = users()


v = StringVar()
#v.set(listeOptions[0])
om = OptionMenu(master, v, *users)
om.pack()

mainloop()