from csv import writer

def append_list_as_row(file_name) :
    code_postal = input("code_postal :")
    commune = input("Commune :")
    type_commune = input("Type :")
    nom_departement = input("Nom departement :")
    row_contents = [32, code_postal, commune,type_commune, nom_departement]

    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(row_contents)


append_list_as_row("users.csv")