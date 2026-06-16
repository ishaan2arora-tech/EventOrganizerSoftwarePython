event_list = []
customer_list = []



def checkEventID(eID):
    flag = False
    for event in event_list:
        if event[0] == eID:
            flag = True
            break
    return flag



def addEvent():
    event = []
    while True:
        eid = input("Enter event ID: ")
        if eid == "":
            print("Event ID cannot be blank")
        elif checkEventID(eid) == True:
            print("Event ID already exists.")
        else:
            break
    
    while True:
        ename = input("Enter the event name: ")
        if ename == "":
            print("Event name cannot be blank")
        else:
            break
    
    while True:
        edescp = input("Enter the event descriptiion: ")
        if edescp == "":
            print("Event description cannot be blank")
        else:
            break
        
    while True:
        edate = input("Enter the event date (mm/dd/yyyy): ")
        if edate == "":
            print("Event date cannot be blank.")
        else:
            break
        
    while True:
        etime = input("Enter the event time: ")
        if etime == "":
            print("Event time cannot be blank.")
        else:
            break
        
    while True:
        eplace = input("Enter where the event is taking place: ")
        if eplace == "":
            print("Event place cannot be blank. ")
        else:
            break
        
    while True:
        noofseats = input("Enter the number of seats: ")
        if noofseats == "":
            print("Number of seats cannot be blank. ")
        else:
            noofseats = int(noofseats)
            if noofseats <= 0:
                print("Number of seats cannot be 0 or less than 0. ")
            else:
                break
            
    bookedseats = 0
    availseats = noofseats-bookedseats
    cust_list = []
    event.append(eid)
    event.append(ename)
    event.append(edescp)
    event.append(edate)
    event.append(etime)
    event.append(eplace)
    event.append(noofseats)
    event.append(bookedseats)
    event.append(availseats)
    event.append(cust_list)
    event_list.append(event)
    print("Event record added successfully!")
    
    
    
def GetEventIDindex(eid):
    idx = -1
    for event in event_list:
        if event[0] == eid:
            idx = event_list.index(event)
            break
    return idx
    




def UpdateEvent():
    event = []
    while True:
        eid = input("Enter event ID: ")
        if eid == "":
            print("Event ID cannot be blank")
        elif checkEventID(eid) == True:
            idx = GetEventIDindex(eid)
            while True:
                ename = input("Enter the event name: ")
                if ename == "":
                    ename = event_list[idx][1]
                    break
                else:
                    break
            
            while True:
                edescp = input("Enter the event descriptiion: ")
                if edescp == "":
                    edescp = event_list[idx][2]
                    break
                else:
                    break
                
            while True:
                edate = input("Enter the event date (mm/dd/yyyy): ")
                if edate == "":
                    edate = event_list[idx][3]
                    break
                else:
                    break
                
            while True:
                etime = input("Enter the event time: ")
                if etime == "":
                    etime = event_list[idx][4]
                    break
                else:
                    break
                
            while True:
                eplace = input("Enter where the event is taking place: ")
                if eplace == "":
                    eplace = event_list[idx][5]
                    break
                else:
                    break
                
            while True:
                noofseats = input("Enter the number of seats: ")
                if noofseats == "":
                    noofseats = int(event_list[idx][6])
                    break
                else:
                    noofseats = int(noofseats)
                    if noofseats <= 0:
                        print("The number of seats cannot be below 0.")
                    else:
                        break
                    
            bookedseats = event_list[idx][7]
            availseats = noofseats-bookedseats
            cust_list = event_list[idx][9]
            event.append(eid)
            event.append(ename)
            event.append(edescp)
            event.append(edate)
            event.append(etime)
            event.append(eplace)
            event.append(noofseats)
            event.append(bookedseats)
            event.append(availseats)
            event.append(cust_list)
            event_list[idx] = event
            print("Event record updated successfully!")

            break
        elif eid == " ":
            break
        else:
            print("Event ID does not exist. Please try again.")
            return
    
                

def deleteEvent():
    while True:
        eid = input("Enter event ID: ")
        if eid == "":
            print("Event ID cannot be blank")
        elif checkEventID(eid) == True:
            idx = GetEventIDindex(eid)
            e = event_list.pop(idx)
            print("Event record deleted succesfully!")
            break
        else:
            print("Event ID does not exist.")
            return
        

def viewEventbyID():
    while True:
        eid = input("Enter event ID: ")
        if eid == "":
            print("Event ID cannot be blank")
        elif checkEventID(eid) == True:
            idx = GetEventIDindex(eid)
            print("Event ID is: ",eid)
            print("Event name is: ",event_list[idx][1])
            print("Event description is: ",event_list[idx][2])
            print("Event date is: ", event_list[idx][3])
            print("Event time is: ",event_list[idx][4])
            print("Event place is: ",event_list[idx][5])
            print("Total seats are: ",event_list[idx][6])
            print("Total booked seats are: ",event_list[idx][7])
            print("Total available seats are: ",event_list[idx][8])
            break
        else:
            print("Event ID does not exist.")
            return




def viewAllEvents():
    for event in event_list:
        print(event[0], event[1],event[2],event[3],event[4],event[5],event[6],event[7],event[8])
        print()



def checkCustomerID(cID):
        flag = False
        for cust in customer_list:
            if cust[0] == cID:
                flag = True
                break
        return flag


def addCustomer():
    cust = []
    while True:
        cid = input("Enter customer ID: ")
        if cid == "":
            print("Cusotomer ID cannot be blank")
        elif checkCustomerID(cid) == True:
            print("Customer ID already exists.")
        else:
            cid = int(cid)
            if cid < 10000 or cid > 99999:
                print("Customer ID should be a 5 digit number.")
            else:
                break
    
    while True:
        cname = input("Enter the customer name: ")
        if cname == "":
            print("Customer name cannot be blank")
        else:
            break
        
        
    while True:
        mobnum= input("Enter the mobile number: ")
        if mobnum == "":
            print("Mobile number cannot be blank. ")
        elif mobnum.isdigit() and len(mobnum) == 10:
            break
        else:
            print("Mobile number should be a 10 digit number. ")
    
    while True:
        email = input("Enter the email address")
        if email == "":
            print("Email address cannot be blank. ")
        elif "@" not in email:
            print("Email is in the wrong format. ")
        else:
            break
    
    
    while True:
        ctype = input("Enter customer type: adult or child: ")
        ctype = ctype.lower()
        if ctype == "":
            print("Customer type cannot be blank. ")
        elif ctype == "adult" or ctype == "child":
            break
        else:
            print("Customer type can only be adult or child. ")
    cust.append(cid)
    cust.append(cname)
    cust.append((mobnum))
    cust.append(email)
    cust.append(ctype)
    customer_list.append(cust)
    print("Customer record added succesfully!")
    
    
    
    
    
def GetCustomerIDindex(cid):
    idx = -1
    for cust in customer_list:
        if cust[0] == cid:
            idx = customer_list.index(cust)
            break
    return idx



def UpdateCustomer():
    cust = []
    while True:
        cid = input("Enter customer ID: ")
        if cid == "":
            print("Customer ID cannot be blank")
        else:
            cid = int(cid)
            if checkCustomerID(cid) == True:
                idx = GetCustomerIDindex(cid)
        
            
            
                while True:
                    cname = input("Enter the customer name: ")
                    if cname == "":
                        cname = customer_list[idx][1]
                        break
                    else:
                        break
                    
                    
                while True:
                    mobnum= input("Enter the mobile number: ")
                    if mobnum == "":
                        mobnum = customer_list[idx][2]
                        break
                    elif mobnum.isdigit() and len(mobnum) == 10:
                        break
                    else:
                        print("Mobile number should be a 10 digit number. ")
                
                while True:
                    email = input("Enter the email address")
                    if email == "":
                        email = customer_list[idx][3]
                        break
                    elif "@" not in email:
                        print("Email is in the wrong format. ")
                    else:
                        break
                
                
                while True:
                    ctype = input("Enter customer type: adult or child: ")
                    ctype = ctype.lower()
                    if ctype == "":
                        ctype = customer_list[idx][4]
                        break
                    elif ctype == "adult" or ctype == "child":
                        break
                    else:
                        print("Customer type can only be adult or child. ")
                        
                        
                        
                cust.append(cid)
                cust.append(cname)
                cust.append((mobnum))
                cust.append(email)
                cust.append(ctype)
                customer_list[idx] = cust
                print("Customer record updated succesfully!")
                
                
                break
            else:
                print("Customer ID doesn't exist. ")
                break
            



def deleteCustomer():
    while True:
        cid = input("Enter customer ID: ")
        if cid == "":
            print("Customer ID cannot be blank")
        elif checkCustomerID(cid) == True:
            idx = GetCustomerIDindex(cid)
            c = customer_list.pop(idx)
            print("Customer record deleted succesfully!")
            break
        else:
            print("Customer ID does not exist.")
            return


def viewCustomerbyID():
    while True:
        cid = int(input("Enter customer ID: "))
        if cid == "":
            print("Customer ID cannot be blank")
        elif checkCustomerID(cid) == True:
            idx = GetCustomerIDindex(cid)
            print("Customer ID is: ",cid)
            print("Customer name is: ",customer_list[idx][1])
            print("Customer number is: ",customer_list[idx][2])
            print("Customer email is: ", customer_list[idx][3])
            print("customer type is: ",customer_list[idx][4])
            break
        else:
            print("Customer ID does not exist.")
            return


def viewAllCustomers():
    for cust in customer_list:
        print(cust[0], cust[1],cust[2],cust[3],cust[4])
        print()


def makeReservation():
    while True:
        cid = input("Enter customer ID: ")
        if cid == "":
            print("Customer ID cannot be blank")
        else:
            cid = int(cid)
            if checkCustomerID(cid) == True:
                idx = GetCustomerIDindex(cid)
                break
            else:
                print("Customer ID does not exist. ")
                return
    while True:
        eid = input("Enter event ID: ")
        if eid == "":
            print("Event ID cannot be blank")
        elif checkEventID(eid) == True:
            idx1 = GetEventIDindex(eid)
            break
        else:
            print("Event ID does not exist. ")
            return
    if event_list[idx1][8] > 0:
        event_list[idx1][9].append(customer_list[idx])
        event_list[idx1][7] = event_list[idx1][7]+1
        event_list[idx1][8] = event_list[idx1][6] - event_list[idx1][7]
        print("Reserervation added succsessfully")
    else:
        print("Event is sold out. ")
    
def deleteReservation():
    while True:
        cid = input("Enter customer ID: ")
        if cid == "":
            print("Customer ID cannot be blank")
        else:
            cid = int(cid)
            if checkCustomerID(cid) == True:
                idx = GetCustomerIDindex(cid)
                break
            else:
                print("Customer ID does not exist. ")
                return
    while True:
        eid = input("Enter event ID: ")
        if eid == "":
            print("Event ID cannot be blank")
        elif checkEventID(eid) == True:
            idx1 = GetEventIDindex(eid)
            break
        else:
            print("Event ID does not exist. ")
            return
    for cust in event_list[idx1][9]:
        if cust[0] == customer_list[idx][0]:
            idx2 = event_list[idx1][9].index(cust)
            d = event_list[idx1][9].pop(idx2)
            print("Reserervation canceled succsessfully")
            event_list[idx1][7] = event_list[idx1][7]-1
            event_list[idx1][8] = event_list[idx1][6] - event_list[idx1][7]
            break
        
            
def displayCustomerinEvent():
    while True:
        eid = input("Enter event ID: ")
        if eid == "":
            print("Event ID cannot be blank")
        else:
            if checkEventID(eid) == True:
                idx = GetEventIDindex(eid)
                for cust in event_list[idx][9]:
                    print(cust[0], cust[1], cust[2], cust[3], cust[4])
                    print()
                break
            else:
                print("Event ID not found. Try again.")
                break


def main():
    while True:
        print("1.  ADD A NEW EVENT")
        print("2.  UPDATE A EVENT BY ID")
        print("3. DELETE A EVENT BY ID")
        print("4.  VIEW A EVENT BY ID")
        print("5.  VIEW ALL EVENTS")
        print("6.  REGISTER/ADD A NEW CUSTOMER")
        print("7.  UPDATE A CUSTOMER BY ID")
        print("8.  DELETE A CUSTOMER BY ID")
        print("9.  VIEW A CUSTOMER BY ID")
        print("10. VIEW ALL CUSTOMERS")
        print("11. MAKE RESERVATION FOR A EVENT")
        print("12. CANCEL RESERVATION FOR THE EVENT")
        print("13. SHOW THE CUSTOMER LIST OF AN EVENT")
        print("14. EXIT")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            addEvent()
        elif ch == 2:
            UpdateEvent()
        elif ch == 3:
            deleteEvent()
        elif ch == 4:
            viewEventbyID()
        elif ch == 5:
            viewAllEvents()
        elif ch == 6:
            addCustomer()
        elif ch == 7:
            UpdateCustomer()
        elif ch == 8:
            deleteCustomer()
        elif ch == 9:
            viewCustomerbyID()
        elif ch == 10:
            viewAllCustomers()
        elif ch == 11:
            makeReservation()
        elif ch == 12:
            deleteReservation()
        elif ch == 13:
            displayCustomerinEvent()
        elif ch == 14:
            break
        else:
            print("You entered the wrong number. Try again")
            

main()