import tkinter as tk
from functools import partial
from Admin import Admin
from Worker import Worker
from Machinery import Machinery
from Product import Product

def backAdmin(screen, backScreen, id, name, des, pos):
    """saving object to the file"""
    # get() is used because all of them are Entries
    if Admin.isExist(id.get()) == False:
        Admin(id.get(), name.get(), des.get(),pos.get()).save()

    # going back to the previous screen
    screen.pack_forget()
    backScreen.pack()

def backWorker(screen, backScreen, id, name, des, pos):
    """saving object to the file"""
    # get() is used because all of them are Entries object
    if Worker.isExist(id.get()) == False:
        Worker(id.get(), name.get(), des.get(),pos.get()).save()

    # going back to the previous screen
    screen.pack_forget()
    backScreen.pack()

def backMachine(screen, backScreen, id, name, type):
    """saving object to the file"""
    # get() is used because all of them are Entries object
    if Machinery.isExist(id.get()) == False:
        Machinery(id.get(), name.get(), type.get()).save()

    # going back to the previous screen
    screen.pack_forget()
    backScreen.pack()

def backProduct(screen, backScreen, id, name, amount):
    """saving object to the file"""
    # get() is used because all of them are Entries object
    if Product.isExist(id.get()) == False:
        Product(id.get(), name.get(), amount.get()).save()

    # going back to the previous screen
    screen.pack_forget()
    backScreen.pack()


def onclickEmployee(screen, previous, worker):
    # getting ID
    id = tk.Label(screen, text="ID",font=("Times New Roman", 15))
    id.grid(row=0, column=0, pady=20, padx=5)
    inputId = tk.Entry(screen, width=60)
    inputId.grid(row=0,column=1)

    # getting Name
    name = tk.Label(screen, text="Name",font=("Times New Roman", 15))
    name.grid(row=1, column=0)
    inputName = tk.Entry(screen, width=60)
    inputName.grid(row=1,column=1, pady=20, padx=5)

    # getting Designation
    designation = tk.Label(screen, text="Designation",font=("Times New Roman", 15))
    designation.grid(row=2, column=0)
    inputDes = tk.Entry(screen, width=60)
    inputDes.grid(row=2,column=1, pady=20, padx=5)

    # getting possessions
    possession = tk.Label(screen, text="Possessions",font=("Times New Roman", 15))
    possession.grid(row=3, column=0)
    inputPos = tk.Entry(screen, width=60)
    inputPos.grid(row=3,column=1, pady=20, padx=5)

    # Button for going back
    if worker == False: # checking if it is called for admin
        backButton = tk.Button(screen, text="Add Admin", background="lightblue", font=("Times New Roman", 20), command=partial(backAdmin, screen=screen, backScreen=previous, id=inputId, name=inputName, des=inputDes, pos=inputPos))
        backButton.grid(row=4, column=1)
    else:
        backButton = tk.Button(screen, text="Add Worker", background="lightblue", font=("Times New Roman", 20), command=partial(backWorker, screen=screen, backScreen=previous, id=inputId, name=inputName, des=inputDes, pos=inputPos))
        backButton.grid(row=4, column=1)

    # Rendering Screen
    previous.pack_forget()
    screen.pack()

def onclickProperty(screen, previous, machine):
    # getting id
    id = tk.Label(screen, text="ID",font=("Times New Roman", 15))
    id.grid(row=0, column=0, pady=20, padx=5)
    inputId = tk.Entry(screen, width=60)
    inputId.grid(row=0,column=1)

    # getting Name
    name = tk.Label(screen, text="Name",font=("Times New Roman", 15))
    name.grid(row=1, column=0)
    inputName = tk.Entry(screen, width=60)
    inputName.grid(row=1,column=1, pady=20, padx=5)

    # checking if it is called for machine
    if machine == True: 
        # getting type of machine
        type = tk.Label(screen, text="Type",font=("Times New Roman", 15))
        type.grid(row=2, column=0)
        inputtype = tk.Entry(screen, width=60)
        inputtype.grid(row=2,column=1, pady=20, padx=5)

        # Button for going back for machine
        backButton = tk.Button(screen, text="Add Machine", background="lightblue", font=("Times New Roman", 20), command=partial(backMachine, screen=screen, backScreen=previous, id=inputId, name=inputName, type=inputtype))
        backButton.grid(row=4, column=1)
    else:
        # getting type of machine
        amount = tk.Label(screen, text="Amount",font=("Times New Roman", 15))
        amount.grid(row=2, column=0)
        inputamount = tk.Entry(screen, width=60)
        inputamount.grid(row=2,column=1, pady=20, padx=5)

        # button for going back for product
        backButton = tk.Button(screen, text="Add Product", background="lightblue", font=("Times New Roman", 20), command=partial(backProduct, screen=screen, backScreen=previous, id=inputId, name=inputName, amount=inputamount))
        backButton.grid(row=4, column=1)

    # Rendering Screen
    previous.pack_forget()
    screen.pack()

def onBackInfo(screen, previous):
    """going back from information screen"""
    screen.pack_forget()
    previous.pack()

def onclickInformatiton(screen, previous, button):
    
    # Headings
    tk.Label(screen, text="ADMINS", font=("Times New Roman", 15, "bold")).grid(row=0, column=2)
    tk.Label(screen, text="ID", foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=1, column=0, padx=15)
    tk.Label(screen, text="Name", foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=1, column=1,padx=15)
    tk.Label(screen, text="Designation", foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=1, column=2,padx=15)
    tk.Label(screen, text="Possession", foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=1, column=3,padx=15)
    # giving row value 2 because first lines is occupied by the headings
    # giving all information about admins
    nextRow = Admin.giveReport(screen, 2)  

    # Headings
    tk.Label(screen, text="WORKERS", font=("Times New Roman", 15, "bold")).grid(row=nextRow, column=2)
    tk.Label(screen, text="ID",foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=nextRow+1, column=0, padx=15)
    tk.Label(screen, text="Name",foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=nextRow+1, column=1,padx=15)
    tk.Label(screen, text="Designation", foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=nextRow+1, column=2,padx=15)
    tk.Label(screen, text="Possession", foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=nextRow+1, column=3,padx=15)
    # information of the worker
    # giving row value 2 because first lines is occupied by the headings
    nextRow = Worker.giveReport(screen, nextRow+2)

    # Headings
    tk.Label(screen, text="MACHINES", font=("Times New Roman", 15, "bold")).grid(row=nextRow, column=2)
    tk.Label(screen, text="ID",foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=nextRow+1, column=0, padx=15)
    tk.Label(screen, text="Name",foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=nextRow+1, column=1,padx=15)
    tk.Label(screen, text="Type", foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=nextRow+1, column=2,padx=15)
    # information of the Machines
    # giving row value 2 because first lines is occupied by the headings
    nextRow = Machinery.giveReport(screen, nextRow+2)

    #headings
    tk.Label(screen, text="PRODUCTS", font=("Times New Roman", 15, "bold")).grid(row=nextRow, column=2)
    tk.Label(screen, text="ID",foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=nextRow+1, column=0, padx=15)
    tk.Label(screen, text="Name",foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=nextRow+1, column=1,padx=15)
    tk.Label(screen, text="Amount", foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=nextRow+1, column=2,padx=15)
    # information of the Products
    # giving row value 2 because first lines is occupied by the headings
    nextRow = Product.giveReport(screen, nextRow+2)

    # # Button for back
    # backInfo = tk.Button(screen, text="Back", background="lightblue", font=("Times New Roman", 15), command=partial(onBackInfo, screen=screen, previous=previous))
    button.grid(row=nextRow, column=2, pady=7)

    # rendering new screen
    previous.pack_forget()
    screen.pack()

def backOrder(screen, previous, adminId, workerId, machineId, productId, toWork, toDo):
    """Going back from order screen"""
    # using get() mehtod because these are input fields nor actual ids
    admin = Admin.findAdmin(adminId.get())
    admin.giveOrder(workerId.get(), machineId.get(), productId.get(), toWork.get(), toDo.get())

    # back to the main screen
    screen.pack_forget()
    previous.pack()
    
def onclickOrder(screen, previous):
    # getting Admin ID
    adminId = tk.Label(screen, text="Admin Id",font=("Times New Roman", 15))
    adminId.grid(row=0, column=0, pady=20, padx=5)
    inputAdminId = tk.Entry(screen, width=60)
    inputAdminId.grid(row=0,column=1)

    # To Work
    toWork = tk.Label(screen, text="To Work",font=("Times New Roman", 15))
    toWork.grid(row=1, column=0, pady=20, padx=5)
    toWorkInput = tk.Entry(screen, width=60)
    toWorkInput.grid(row=1,column=1)

    # getting WorkerId
    workerId = tk.Label(screen, text="Worker Id",font=("Times New Roman", 15))
    workerId.grid(row=2, column=0, pady=20, padx=5)
    inputWorkerId = tk.Entry(screen, width=60)
    inputWorkerId.grid(row=2,column=1)

    # getting Machine ID
    machineId = tk.Label(screen, text="Machine Id",font=("Times New Roman", 15))
    machineId.grid(row=3, column=0, pady=20, padx=5)
    inputMachineId = tk.Entry(screen, width=60)
    inputMachineId.grid(row=3,column=1)

    # getting Product ID
    productId = tk.Label(screen, text="Product Id",font=("Times New Roman", 15))
    productId.grid(row=4, column=0, pady=20, padx=5)
    inputProductId = tk.Entry(screen, width=60)
    inputProductId.grid(row=4,column=1)

    # TO Do
    toDo = tk.Label(screen, text="To Do",font=("Times New Roman", 15))
    toDo.grid(row=5, column=0, pady=20, padx=5)
    toDoInput = tk.Entry(screen, width=60)
    toDoInput.grid(row=5,column=1)

    # Button for giving order
    orderButton = tk.Button(screen, text="Order", background="lightblue", font=("Times New Roman", 20), command=partial(backOrder, screen=screen, previous=previous, adminId=inputAdminId, workerId=inputWorkerId, machineId=inputMachineId, productId=inputProductId, toWork=toWorkInput, toDo=toDoInput))
    orderButton.grid(row=6, column=1)

    # Rendering Screen
    previous.pack_forget()
    screen.pack()

def onBackSeeInfo(screen, previous):
    screen.pack_forget()
    previous.pack()


def onClickSeeOrder(screen, previous, button):
    # Headings
    tk.Label(screen, text="ORDERS", font=("Times New Roman", 15, "bold")).grid(row=0, column=0, pady=20)
    # tk.Label(screen, text="Admin", foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=1, column=0, padx=25)
    # tk.Label(screen, text="Worker", foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=1, column=1,padx=25)
    # tk.Label(screen, text="machine", foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=1, column=2,padx=25)
    # tk.Label(screen, text="Prodcut", foreground="darkcyan", font=("Times New Roman", 13, "bold")).grid(row=1, column=3,padx=25)
    r = Admin.seeOrders(screen)

    button.grid(row=r, column=0, pady=15)

    previous.pack_forget()
    screen.pack()

def onBackSeeOrder(screen, previous):
    screen.pack_forget()
    previous.pack()

def main():
    # making main menu screen
    window = tk.Tk()
    window.state("zoomed")

    screenMenu = tk.Frame(window)
    screenAdmin = tk.Frame(window) # making of admin screen
    screenWorker = tk.Frame(window) # making frame for worker
    screenMachine = tk.Frame(window) # making frame for machine
    screenProduct = tk.Frame(window) # making frame for product
    screenInfo = tk.Frame(window) # making frame for information
    screenOrder = tk.Frame(window) # making frame for Order
    screenSeeOrder = tk.Frame(window) # making frame for seeing all orders

    title = tk.Label(screenMenu, text="MAIN MENU",font=("Times New Roman", 50))
    title.pack(pady=30, padx=20)

    # adding button for administrator
    addAdmin = tk.Button(screenMenu, text="Add Admin", background="lightblue", font=("Times New Roman", 15), command=partial(onclickEmployee, screen=screenAdmin, previous=screenMenu, worker=False))
    addAdmin.pack(pady=10)

    # adding button for worker
    addWorker = tk.Button(screenMenu, text="Add Worker", background="lightblue", font=("Times New Roman", 15), command=partial(onclickEmployee, screen=screenWorker, previous=screenMenu, worker=True))
    addWorker.pack(pady=10)

    #adding button for machines
    addMachine = tk.Button(screenMenu, text="Add Machine", background="lightblue", font=("Times New Roman", 15), command=partial(onclickProperty, screen=screenMachine, previous=screenMenu, machine=True))
    addMachine.pack(pady=10)

    #adding button for products
    addProduct = tk.Button(screenMenu, text="Add Product", background="lightblue", font=("Times New Roman", 15), command=partial(onclickProperty, screen=screenProduct, previous=screenMenu, machine=False))
    addProduct.pack(pady=10)

    # Button for getting back from Information screen
    getBackInformation = tk.Button(screenInfo, text="Back", background="lightblue", font=("Times New Roman", 15), command=partial(onBackInfo, screen=screenInfo, previous=screenMenu))
    getBackInformation.grid(row=5000, column=2)

    #Button to see all objects in application
    seeAllObj = tk.Button(screenMenu, text="Information", background="lightblue", font=("Times New Roman", 15), command=partial(onclickInformatiton, screen=screenInfo, previous=screenMenu, button=getBackInformation))
    seeAllObj.pack(pady=10)
    
    #Button to give order from a admin to worker
    giveOrder = tk.Button(screenMenu, text="Give Order", background="lightblue", font=("Times New Roman", 15), command=partial(onclickOrder, screen=screenOrder, previous=screenMenu))
    giveOrder.pack(pady=10)

    # Button for getting back from Information screen
    getBackSeeOrders = tk.Button(screenSeeOrder, text="Back", background="lightblue", font=("Times New Roman", 15), command=partial(onBackSeeOrder, screen=screenSeeOrder, previous=screenMenu))
    getBackSeeOrders.grid(row=5000, column=0)

    # Button to show All orders
    seeOrder = tk.Button(screenMenu, text="See All Orders", background="lightblue", font=("Times New Roman", 15), command=partial(onClickSeeOrder, screen=screenSeeOrder, previous=screenMenu, button=getBackSeeOrders))


    seeOrder.pack(pady=10)
    screenMenu.pack()
    window.mainloop()
  

if __name__ == "__main__":
    main()

