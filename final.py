import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


userDetails = {
    "kavindu": "1234",
    "lakindu": "2468",
    "dewmini": "369"
}



def navigate_to_window2():
    if 'window2' in globals():
        window2.destroy()  # Destroy current window
    create_window2()

def navigate_to_window3():
    if 'window3' in globals():
        window3.destroy()  # Destroy current window
    create_window3()

def navigate_to_window5():
    if 'window5' in globals():
        window5.destroy()  # Destroy current window
    create_window5()


def navigate_to_window4():
    if 'window1' in globals():
        window1.destroy()  # Destroy current window
    messagebox.showinfo("Message", "Good Bye !")
    window1.quit()  # Exit the application

def navigate_to_window1():
    if 'window1' in globals():
        window1.destroy()  # Destroy current window
        create_window1()

def create_window1():   # Dashboard Area
    global window1
    window1 = tk.Tk()
    window1.title("Window 1")
    window1.geometry('500x500')
    window1.resizable(False, False)

    label1 = tk.Label(window1, text="============DASHBOARD=============")
    label1.pack()

    button2 = tk.Button(window1, text="Go to LOGIN   ", command=navigate_to_window2)
    button2.pack()

    button3 = tk.Button(window1, text="Go to REGISTER", command=navigate_to_window3)
    button3.pack()

    button1 = tk.Button(window1, text="Go to EXIT     ", command=navigate_to_window4)
    button1.pack()

def create_window2(): #log in area
    global window2
    window2 = tk.Toplevel(window1)
    window2.title("Window 2")
    window2.geometry('500x500')
    window2.resizable(False, False)

    label2 = tk.Label(window2, text="=================LOGIN FORM=====================")
    label2.pack()

    button2 = tk.Button(window2, text="Go to Dashboard", command=navigate_to_window1)
    button2.pack()

    #button1 = tk.Button(window2, text="View Resturants", command=navigate_to_window5)
    #button1.pack()

    def get_value12():
        global value11  # Use the global variable
        value11 = entry1.get()  # Assign the value from the entry widget to the global variable
        print("Value username:", value11)

    def get_value21():
        global value22 # Use the global variable
        value22 = entry2.get()  # Assign the value from the entry widget to the global variable
        print("Value password:", value22)

    def addToDict2(username, password):
        if username in userDetails:
            value = userDetails[username]

            if value == password:
                messagebox.showinfo("Message", "Log In Successful!")
                create_window5()
                print("===================================Log in successful=================================")
                print("1 - Browse Restaurants")
                print("2 - View Cart")
                print("3 - Logout")

                # You can add GUI elements here for user choice
                # For example, buttons to browse restaurants, view cart, and logout

            else:
                messagebox.showerror("Error", "Wrong password!")
        else:
            messagebox.showerror("Error", "Invalid Input!")







    #get input from user
    label = tk.Label(window2, text="Please enter your user Name:")
    label.pack()

    # Create a text field for user input
    entry1 = tk.Entry(window2)
    entry1.pack()

    # Create a button to trigger the action
    button = tk.Button(window2, text="Username OK", command=get_value12)
    button.pack()

    label = tk.Label(window2, text="Please enter your Password:")
    label.pack()

    # Create a text field for user input
    entry2 = tk.Entry(window2)
    entry2.pack()

    # Create a button to trigger the action
    button = tk.Button(window2, text="Password OK", command=get_value21)
    button.pack()

    button3 = tk.Button(window2, text="Submit", command=lambda: addToDict2(value11, value22))
    button3.pack()

def create_window3():  # Register area
    global window3
    window3 = tk.Toplevel(window1)
    window3.title("Window 3")
    window3.geometry('500x500')
    window3.resizable(False, False)

    label3 = tk.Label(window3, text="======================REGISTER FORM ========================")
    label3.pack()

    button3 = tk.Button(window3, text="Go to Dashboard", command=navigate_to_window1)
    button3.pack()

    def get_value1():
        global value1  # Use the global variable
        value1 = entry1.get()  # Assign the value from the entry widget to the global variable
        print("Value username:", value1)

    def get_value2():
        global value2  # Use the global variable
        value2 = entry2.get()  # Assign the value from the entry widget to the global variable
        print("Value password:", value2)

    def addToDict(name, password):
        userDetails[name] = password
        print("REGISTER SUCCESSFUL!")
        messagebox.showinfo("Message", "Registration Successful!")
        print(userDetails)

    label = tk.Label(window3, text="Please enter your user Name:")
    label.pack()

    # Create a text field for user input
    entry1 = tk.Entry(window3)
    entry1.pack()

    # Create a button to trigger the action
    button = tk.Button(window3, text="Username OK", command=get_value1)
    button.pack()

    label = tk.Label(window3, text="Please enter your Password:")
    label.pack()

    # Create a text field for user input
    entry2 = tk.Entry(window3)
    entry2.pack()

    # Create a button to trigger the action
    button = tk.Button(window3, text="Password OK", command=get_value2)
    button.pack()

    button3 = tk.Button(window3, text="Submit", command=lambda: addToDict(value1, value2))
    button3.pack()

    print("==================================REGISTER FORM================================================")


def create_window5():  # Restaurant in area
    global window5
    window5 = tk.Toplevel(window1)
    window5.title("Window 5")  # Fix window title
    window5.geometry('1000x1000')
    window5.resizable(False, False)

    # Add widgets for the restaurant window here
    label5 = tk.Label(window5, text="=================Welcome to the Restaurant Area================")
    label5.pack()


    def get_value5():
        global value5  
        value5 = entry5.get()  
        print("Resturant No:", value5)

    def get_value6():
        global value6 
        value6 = entry6.get()  
        print("Food No:", value6)

    def get_value7():
        global value7 
        value7 = entry7.get()  
        print("Quantity:", value7)

        
    def calTotal(resturant, food,quantity):
        print("Calculate Total SUCSESSFUL!")

        thirdChoice = int(resturant)
        print(thirdChoice)

        if(thirdChoice == 1):
            print("===============================Welcome to Pizza place=====================================")
            
            margherite_Pizzae = 700
            pepperoni_Pizzae = 800
            vegge_Pizzae = 900

            forthChoice = int(food)
            quantity = int(quantity)

            print(forthChoice)
            print(quantity)

            if(forthChoice == 1):
                total = margherite_Pizzae * quantity
                print("Total is:",total)
                messagebox.showinfo("Message", total)
    

            elif(forthChoice == 2):
                total = pepperoni_Pizzae * quantity
                print("Total is:", total)
                messagebox.showinfo("Message", total)

            elif(forthChoice == 3):
                total = vegge_Pizzae * quantity
                print("Total is:",total)
                messagebox.showinfo("Message", total)
    
    
            else:
               print("Inavalid Input")
               messagebox.showerror("Error", "Invalid Input!")
    

        elif(thirdChoice == 2):
            print("===============================Welcome to Sushi Heaven=====================================")

            nigiri_Sushi = 1000
            marki_Sushi = 1200
            temaki_Sushi = 1400

            forthChoice = int(food)
            quantity = int(quantity)

            print(forthChoice)
            print(quantity)

            if(forthChoice == 1):
                total = nigiri_Sushi * quantity
                print("Total is:",total)
                messagebox.showinfo("Message", total)
    

            elif(forthChoice == 2):
                total = marki_Sushi * quantity
                print("Total is:", total)
                messagebox.showinfo("Message", total)

            elif(forthChoice == 3):
                total = temaki_Sushi * quantity
                print("Total is:",total)
                messagebox.showinfo("Message", total)
    
    
            else:
               print("Inavalid Input")
               messagebox.showerror("Error", "Invalid Input!")
            
    

        elif(thirdChoice == 3):
            print("===============================Welcome to Burger Barn=====================================")

            seed_bun = 1600
            wheat_bun = 1800
            pretzel_bun = 2000

            forthChoice = int(food)
            quantity = int(quantity)

            print(forthChoice)
            print(quantity)

            if(forthChoice == 1):
                total = seed_bun * quantity
                print("Total is:",total)
                messagebox.showinfo("Message", total)
    

            elif(forthChoice == 2):
                total = wheat_bun * quantity
                print("Total is:", total)
                messagebox.showinfo("Message", total)

            elif(forthChoice == 3):
                total = pretzel_bun * quantity
                print("Total is:",total)
                messagebox.showinfo("Message", total)
    
    
            else:
               print("Inavalid Input")
               messagebox.showerror("Error", "Invalid Input!")
            

    
    
        else:
           print("Inavalid Input") 
       



    label = tk.Label(window5, text="Please enter Resturant No:")
    label.pack()

    # Create a text field for user input
    entry5 = tk.Entry(window5)
    entry5.pack()

    # Create a button to trigger the action
    button = tk.Button(window5, text="Enter Resturant No", command=get_value5)
    button.pack()

    #========================================


    label = tk.Label(window5, text="Please enter Food No:")
    label.pack()

    # Create a text field for user input
    entry6 = tk.Entry(window5)
    entry6.pack()

    # Create a button to trigger the action
    button = tk.Button(window5, text="Enter Food N0", command=get_value6)
    button.pack()

    #========================================

    label = tk.Label(window5, text="Please enter Quantity:")
    label.pack()

    # Create a text field for user input
    entry7 = tk.Entry(window5)
    entry7.pack()

    # Create a button to trigger the action
    button = tk.Button(window5, text="Enter Quantity", command=get_value7)
    button.pack()

    #========================================

    button = tk.Button(window5, text="Place Order", command=lambda: calTotal(value5, value6,value7))
    button.pack()



    tree = ttk.Treeview(window5, columns=("column1", "column2","column3"), show="headings")

    # Define column headings
    tree.heading("column1", text="NO")
    tree.heading("column2", text="NAME")
    tree.heading("column3", text="PRIZE")

    # Add some sample data
    data = [
        ("NO", "RESTURANT NAME","  "),
        ("1", "Pizza Place","   "),
        ("2", "Sushi Heaven","  "),
        ("3", "Burger Barn","   "),
        ("===============", "================","================"),
        ("1", "margherite_Pizzae","LKR 700"),
        ("2", "pepperoni_Pizzae","LKR 800"),
        ("3", "pepperoni_Pizzae","LKR 900"),
        ("===============", "===============","==============="),
        ("1", "nigiri_Sushi","LKR 1000"),
        ("2", " marki_Sushi","LKR 1200"),
        ("3", "temaki_Sushi","LKR 1400"),
        ("===============", "===============","==============="),
        ("1", "seed_bun","LKR 1600"),
        ("2", " wheat_bun","LKR 1800"),
        ("3", "pretzel_bun","LKR 2000")
                       
    ]

    for row in data:
        tree.insert("", "end", values=row)

    # Pack the Treeview widget
    tree.pack(expand=True, fill="both")

create_window1()

# Run the main event loop
window1.mainloop()
