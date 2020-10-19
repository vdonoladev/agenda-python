# Autor: Víctor Donola Ferreira (vdonoladev)


lista = []  # define variable for the list


# reads data from file and plays to list
arc2 = open("agenda.csv", "a+")
lista = arc2.readlines()
arc2.close()


# function: menu, build the menu
def menu():
    print("\n", "=" * 50)
    print("""\nSCHEDULE\n\n
             Choose the option:\n
             (1) Insert contact:\n
             (2) Delete:\n
             (3) Show:\n
             (4) End program:\n""")
# end of menu function


# function: schedule_list, add, remove and show the list
def schedule_list(nome, data, opc):

    if(opt == 1):
        contact = name + ";" + date + "\n"  # concatenates the 'name' ';' and 'date'
        lista.append(contact)
        lista.sort()  # sorts the list by priority

    elif (opt == 2):
        print("=" * 30)
        if (lista == []):  # if list is empty
            print("Empty List\n")
        else:
            # removes the highest priority element, that is, index 0 from the list
            lista.pop(0)
            print("Removed the highest priority element")
        print("=" * 30)

    elif (opt == 3):
        print("=" * 30)
        if (lista == []):
            print("Empty List!")
        else:
            print("Name:   | Date: ")
            for i in lista:
                print(i)
        print("=" * 30)

    elif (opt == 4):
        arc = open("agenda.csv", "w")  # write over the old file (update list)
        siz = len(lista)  # receives list size

        # which inserts the values in the file separated by ';' being name = even index and date = odd
        for i in range(siz):
            arc.write(lista[i])
        arc.close()

# end of function schedule_list


# main function
opt = 0  # variable for the menu

while (opt != 4):

    menu()  # calls the menu

    while True:
        try:
            opt = int(input(''))  # receives the option
            break
        except:
            print("Please enter only valid numbers")

    if (opt == 1):
        name = input("Enter the contact name: ")

        date = input("Enter the date of birth: ")

        # calls the function to insert in the list
        schedule_list(name, date, 1)

    elif (opt == 2):
        # calls the function to delete the name in the list
        schedule_list(0, 0, 2)

    elif (opt == 3):  # calls the function to show on the screen
        print("Contact list: ")
        schedule_list(0, 0, 3)


schedule_list(0, 0, 4)  # save the list
print("END OF PROGRAM!")
