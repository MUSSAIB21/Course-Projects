print('\n\n')  #Welcome Screen for when opening program
print('''██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝''')
# ==== File Handler Functions ====
"""
These functions deal with saving and loading data on the files. Their job is to collect data
from the txt files and load them into the program and vice versa.

"""


def save(members,plans,trainers):  #This function takes the values from member dictionary and stores them into the file
    file=open('mohammadMussaib_members.txt', 'w')
    for member in members:
        line=f"{member['ID']}|{member['name']}|{member['age']}|{member['gender']}|{member['email']}|{member['plan_id']}|{member['attendance']}|{member['weight']}|{member['isAdult']}"
        file.write(line+'\n')
    file.close()


    file = open('mohammadMussaib_plans.txt', 'w')
    for plan in plans:
        line = f"{plan['ID']}|{plan['name']}|{plan['price']}|{plan['facilities']}|{plan['isPremium']}|{plan['members enrolled']}"
        file.write(line + '\n')
    file.close()


    file = open('mohammadMussaib_trainers.txt', 'w')
    for trainer in trainers:
        line = f"{trainer['ID']}|{trainer['name']}|{trainer['age']}|{trainer['gender']}|{trainer['email']}|{trainer['plan_id_list']}|{trainer['experience']}|{trainer['salary']}|{trainer['isExpert']}"
        file.write(line + '\n')
    file.close()

"""
The save function only saves the values for the records and not the title for values as
its only meant to only be accessed by the program
"""
def load(members, plans, trainers):
    try:
        file=open('mohammadMussaib_members.txt', 'r')
        for line in file:
            line=line.strip()
            if line:
                ID,name,age,gender,email,plan_id,attendance,weight,isAdult=line.split('|')
                members.append({
                    "ID": ID,
                    "name": name,
                    "age": int(age),
                    "gender": gender,
                    "email": email,
                    "plan_id": plan_id,
                    "attendance": int(attendance),
                    "weight": float(weight),
                    "isAdult":isAdult=='True',
                })
        file.close()

    except FileNotFoundError:
        print("Member File Not Found")

    try:
        file=open('mohammadMussaib_plans.txt', 'r')
        for line in file:
            line=line.strip()
            if line:
                ID,name,price,facilities,is_premium,members_enrolled=line.split('|')
                plans.append({
                    "ID": ID,
                    "name": name,
                    "price": float(price),
                    "facilities": facilities,
                    "members enrolled": int(members_enrolled),
                    "isPremium":is_premium=='True',
                })
        file.close()

    except FileNotFoundError:
        print("Plans File Not Found")

    try:
        file=open('mohammadMussaib_trainers.txt', 'r')
        for line in file:
            line=line.strip()
            if line:
                ID,name,age,gender,email,plan_id_list,experience,salary,isExpert=line.split('|')
                trainers.append({
                    "ID": ID,
                    "name": name,
                    "age": int(age),
                    "gender": gender,
                    "email": email,
                    "plan_id_list": plan_id_list,
                    "experience": float(experience),
                    "salary": float(salary),
                    "isExpert":isExpert=='True',
                })
        file.close()

    except FileNotFoundError:
        print("Trainer File Not Found")




# ==== Get a valid argument input ====
"""
This function is very useful for avoiding TypeErrors in our program as it keeps 
running till user gives a valid input 

"""

def get_number(prompt, number_type=float):
    while True:
        value = input(prompt)
        try:
            if value=="":
                return None
            return number_type(value)

        except:
            print("Invalid input! Please enter a valid number")

"""
Another useful function which checks if the given ID is assigned somewhere in the database
so that no two members or no two plans will have the same ID 
"""

def get_ID(record):
    while True:
        _ID = input(" ID: ")
        for r in record:
            if r["ID"] == _ID:
                print("ID already taken please try again")
                break
        else:
            return _ID



# ==== Member Functions ====
"""
The members in this program are essentially dictionaries which are going to be stored
inside the list of members. Different keys are used to store the different kind of parameters.
ID will be stored as a string instead of a int or float as it allows combination of more
IDs using lesser digits and its unlikely we are to do any mathematics with the IDs so like in
real life IDs can have both numbers and Alphabets
"""

def add_member(members):
    member={}
    member['ID'] = get_ID(members)
    member['name'] = input("Name: ")
    member['age'] = get_number("Age",int)
    member['gender'] = input("Gender: ")
    member['email'] = input("Email: ")
    member['plan_id'] = input("Plan ID: ")
    member['attendance']=0
    member['weight']=get_number("Weight",float)
    member['isAdult']=False
    if member['age']>18:
        member['isAdult']=True
    members.append(member)
    print("✅ Member added successfully.")

"""
This is for viewing all the members in our database currently
Sorted According to the ID
"""
def view_members(members):
    print('''\n\n\n╔╦╗┌─┐┌┬┐┌┐ ┌─┐┬─┐  ╦  ┬┌─┐┌┬┐
║║║├┤ │││├┴┐├┤ ├┬┘  ║  │└─┐ │ 
╩ ╩└─┘┴ ┴└─┘└─┘┴└─  ╩═╝┴└─┘ ┴ \n''')
    members=sorted(members, key=lambda k: k["ID"])
    try:
        print("ID         Age       Gender       Name          Plan_ID     Attendance")
        for m in members:
         shortname=(m['name'])[0:12:]
         print(f'{"{:<5}".format(m['ID'])}      {"{:<3}".format(m['age'])}       {"{:<7}".format(m['gender'])}      {"{:<12}".format(shortname)}     {"{:<8}".format(m['plan_id'])}      {m['attendance']}')


    except IndexError:
        print("❌ No member found.")


"""
This function increments the attendance for given member by 1
"""
def record_attendance(members):
    member_id = input("Enter Member ID: ")
    for m in members:
        if m["ID"] == member_id:
            m["attendance"] = m["attendance"]+1
            print("✅ Attendance recorded! ")
            return
    print("❌ Member not found")

# ==== Plan & Trainer Functions ====
"""
Like the member functions, the add and view functions for the plans and trainers do the same
task, but with the different parameters in mind for plans and trainers
"""
def add_plan(plans):
    plan={}

    plan['ID'] = get_ID(plans)
    plan['name'] = input("Name: ")
    plan['price'] = get_number("Annual Price", float)
    plan['facilities'] = input("Facilities(seperated by commas): ")
    plan['isPremium'] = False
    if plan['price']>1000:
        plan['isPremium'] = True
    plan['members enrolled'] = get_number("Members Enrolled", int)
    plans.append(plan)
    print("✅ Plan added successfully.")


def view_plans(plans):
    print(plans)
    plans = sorted(plans, key=lambda k: k["ID"])
    print('''\n\n\n╔═╗┬  ┌─┐┌┐┌    ╦  ┬┌─┐┌┬┐
╠═╝│  ├─┤│││    ║  │└─┐ │ 
╩  ┴─┘┴ ┴┘└┘    ╩═╝┴└─┘ ┴ \n''')
    try:
        print("ID         Price         Type        Name          Members Enrolled")
        for p in plans:
            plan_type = "Basic"
            if p["isPremium"]:
                plan_type = "Premium"
            shortname = (p['name'])[0:12:]
            print(
                f'{"{:<5}".format(p['ID'])}      {"{:<3}".format(p['price'])}       {"{:<7}".format(plan_type)}      {"{:<12}".format(shortname)}        {p['members enrolled']}')



    except IndexError:
        print("❌ No plans found.")



def add_trainers(trainers):
    trainer={}

    trainer['ID'] = get_ID(trainers)
    trainer['name'] = input("Name: ")
    trainer['age'] = get_number("Age", int)
    trainer['gender'] = input("Gender: ")
    trainer['email'] = input("Email: ")
    trainer['plan_id_list'] = input("Plan ID list(seperated by commas): ")
    trainer['experience'] = get_number("Experience(years)", float)
    trainer['salary'] = get_number("Salary(yearly)", float)

    trainer['isExpert'] = False
    if trainer['experience'] > 10:
        trainer['isExpert'] = True
    trainers.append(trainer)
    print("✅ Trainer added successfully.")

def view_trainers(trainers):
    print('''\n\n\n╔╦╗┬─┐┌─┐┬┌┐┌┌─┐┬─┐    ╦  ┬┌─┐┌┬┐
 ║ ├┬┘├─┤││││├┤ ├┬┘    ║  │└─┐ │ 
 ╩ ┴└─┴ ┴┴┘└┘└─┘┴└─    ╩═╝┴└─┘ ┴ \n''')
    trainers=sorted(trainers, key=lambda k: k["ID"])
    try:
        print("ID         Age       Gender       Name          Salary       Plan List")
        for t in trainers:
         shortname=(t['name'])[0:12:]
         print(f'{"{:<5}".format(t['ID'])}      {"{:<3}".format(t['age'])}       {"{:<3}".format(t['gender'])}         {"{:<12}".format(shortname)}   {"{:<8}".format(t['salary'])}      {t['plan_id_list']}')


    except IndexError:
        print("❌ No trainers found.")





# Change Records
"""
This function is for changing the details of the records in our database 
without having to delete the record fully. Try except blocks are in place if user
enters an invalid argument as a number, in which case the parameter is not changed
"""
def change_records(members,plans,trainers):
    choice=input("Press 1 for Member Records, 2 for Plan Records, 3 for Trainer records ")
    if choice == '1':
        id = input(" ID: ")
        for m in members:
            if m['ID'] == id:
                print("Keep Blank for no change")
                new_id = get_ID(members)
                if new_id:
                    m['ID'] = new_id
                new_name = input("Enter new name: ")
                if new_name:
                    m["name"] = new_name
                new_gender = input("Enter new gender: ")
                if new_gender:
                    m["gender"] = new_gender
                new_email = input("Enter new email: ")
                if new_email:
                    m["email"] = new_email
                new_planID = input("Enter new plan_id: ")
                if new_planID:
                    m["plan_id"] = new_planID

                new_attendance = get_number("Enter new attendance: ", int)
                if new_attendance:
                    m["attendance"] = new_attendance
                new_weight = get_number("Enter new weight: ", float)
                if new_weight:
                    m["weight"] = new_weight
                new_age = get_number("Enter new age: ", int)
                if new_age:
                    m["age"] = new_age


                if m["age"] > 18:
                    m["isAdult"] = True
                else:
                    m["isAdult"] = False
                return
        else:
            print("Invalid ID please try again.")



    elif choice == '2':
        id = input(" ID: ")
        for p in plans:
            if id == p['ID']:
                print("Keep Blank for no change")

                new_id = get_ID(plans)
                if new_id:
                    p['ID'] = new_id
                new_name = input("Enter new name: ")
                if new_name:
                    p["name"] = new_name
                new_price = get_number("Enter new price: ", float)
                if new_price:
                    p["price"] = new_price

                new_facilities = input("Enter new facilities: ")
                if new_facilities:
                    p["facilities"] = new_facilities

                new_members = get_number("Enter new members: ", int)
                if new_members:
                    p['members enrolled'] = new_members

                if p['price'] > 1000:
                    p['isPremium'] = True
                return

        else:
            print("Invalid ID please try again")

    elif choice == '3':
        id = input(" ID: ")
        for t in trainers:
            if t['ID'] == id:
                print("Keep Blank for no change")
                new_id = get_ID(trainers)
                if new_id:
                    t['ID'] = new_id
                new_name = input("Enter new name: ")
                if new_name:
                    t["name"] = new_name
                new_age = get_number("Enter new age: ", int)
                if new_age:
                    t["age"] = new_age

                new_gender = input("Enter new gender: ")
                if new_gender:
                    t["gender"] = new_gender
                new_email = input("Enter new email: ")
                if new_email:
                    t["email"] = new_email
                new_planID_list = input("Enter new plan id list: ")
                if new_planID_list:
                    t["plan_id_list"] = new_planID_list
                new_salary = get_number("Enter new salary: ", float)
                if new_salary:
                    t["salary"] = new_salary
                new_exp = get_number("Enter new experience: ", float)
                if new_exp:
                    t["experience"] = new_exp

                if t["experience"] > 10:
                    t["isExpert"] = True
                else:
                    t["isExpert"] = False
                return
        else:
            print("Invalid ID please try again.")

    else:
        print("Invalid Choice Try Again")

"""
This function is for deleting the record of a member completely
"""

def delete_record(records):
    _id = input("Enter ID to delete: ")
    for record in records:
        if record["ID"] == _id:
            records.remove(record)
            print("Record deleted.")
            return
    print("No record with this ID found.")

#=== Search Function ====
"""
This function is for searching the individual members by their ID or name
"""

def search(members,plans,trainers):

    choice=input("Select 1 for Members, 2 for Plans, 3 for Trainers")

    if choice == '1':
        member_id = ""
        member_name = ""
        choice = input("Select 1 for search by ID and 2 for search by name:  ")
        if choice == '1':
            member_id = input("Enter Member ID: ")
        elif choice == '2':
            member_name = input("Enter Member Name: ")
        else:
            print("Invalid Choice, Select 1 or 2.")
            return

        for m in members:
            if m['ID'] == member_id or m['name'].lower() == member_name.lower():
                adult = "Junior"
                if m['isAdult']:
                    adult = "Senior"
                print("ID         Age       Gender       Name          Plan_ID    Attendance    ")
                firsthalf = (m['name'])[0:12:]
                secondhalf = (m['name'])[12::]
                print(
                    f'{"{:<5}".format(m['ID'])}      {"{:<3}".format(m['age'])}       {m['gender']}      {"{:<12}".format(firsthalf)}     {"{:<8}".format(m['plan_id'])}      {m['attendance']}')
                print(f"                               {secondhalf}  ")
                print("\n Additional Details:")
                print(f"email: {m['email']} , {adult} ,Weight: {m['weight']}kg ")
                return
        print("Member not found")
    elif choice == '2':
        plan_id = ""
        plan_name = ""
        choice = input("Select 1 for search by ID and 2 for search by name:  ")
        if choice == '1':
            plan_id = input("Enter Plan ID: ")
        elif choice == '2':
            plan_name = input("Enter Plan Name: ")
        else:
            print("Invalid Choice, Select 1 or 2.")
            return

        for p in plans:
            if p['ID'] == plan_id or p['name'].lower() == plan_name.lower():
                type = "Standard"
                if p['isPremium']:
                    type = "Premium"
                print("ID         Price        Type         Name       Members Enrolled    ")
                firsthalf = (p['name'])[0:12:]
                secondhalf = (p['name'])[12::]
                print(
                    f'{"{:<5}".format(p['ID'])}      {"{:<3}".format(p['price'])}       {type}      {"{:<12}".format(firsthalf)}      {p['members enrolled']}')
                print(f"                               {secondhalf}  ")
                print("\n Additional Details:")
                print(f" Facilities Used: {p['facilities']}  ")
                return
        print("Plan not found")
    elif choice == '3':
        trainer_id = ""
        trainer_name = ""
        choice = input("Select 1 for search by ID and 2 for search by name:  ")
        if choice == '1':
            trainer_id = input("Enter Member ID: ")
        elif choice == '2':
            trainer_name = input("Enter Member Name: ")
        else:
            print("Invalid Choice, Select 1 or 2.")
            return

        for t in trainers:
            if t['ID'] == trainer_id or t['name'].lower() == trainer_name.lower():
                expert = "Amateur"
                if t['isExpert']:
                    expert = "Expert"
                print("ID         Age       Gender       Name          Salary    Plan List    ")
                firsthalf = (t['name'])[0:12:]
                secondhalf = (t['name'])[12::]
                print(
                    f'{"{:<5}".format(t['ID'])}      {"{:<3}".format(t['age'])}       {t['gender']}      {"{:<12}".format(firsthalf)}     {t['salary']}      {t['plan_id_list']}')
                print(f"                               {secondhalf}  ")
                print("\n Additional Details:")
                print(f"email: {t['email']} , {expert} ,  Experience: {t['experience']} years ")
                return
        print("Member not found")






# ==== Main Menu ====
"""
This is the main function which has the menu for the options
Currently only member options are functional

"""
def main():
    try:
        m = open("mohammadMussaib_members.txt", "x")     #These 3 lines are for creating our txt files which we will use to store data
        t = open("mohammadMussaib_trainers.txt", "x")
        p = open("mohammadMussaib_plans.txt", "x")

    except FileExistsError:                  #Try,Except block to avoid error
        pass


    members = []      #Members is the list that contains the members
    plans = []        #Plan list contains the plans
    trainers = []     #Trainer list contains the trainers
    load(members, plans, trainers)

    while True:
        print('''\n\n\n·······················································
:╔═╗┬ ┬┌┬┐    ╔╦╗┌─┐┌┬┐┌─┐┌┐ ┌─┐┌─┐┌─┐    ╔╦╗┌─┐┌┐┌┬ ┬:
:║ ╦└┬┘│││     ║║├─┤ │ ├─┤├┴┐├─┤└─┐├┤     ║║║├┤ ││││ │:
:╚═╝ ┴ ┴ ┴    ═╩╝┴ ┴ ┴ ┴ ┴└─┘┴ ┴└─┘└─┘    ╩ ╩└─┘┘└┘└─┘:
·······················································''')


        print('''┏━━━━━━━━━━━━━━━━━━━━━━┓
┃0. Quit Without Saving┃
┃1. Add Member         ┃
┃2. View Members       ┃
┃3. Record Attendance  ┃
┃4. Add Plan           ┃
┃5. View Plans         ┃
┃6. Add Trainer        ┃
┃7. View Trainers      ┃
┃8. Search Member      ┃
┃9. Save & Exit        ┃
┃10. Delete Member     ┃
┃11. Make Changes      ┃
┗━━━━━━━━━━━━━━━━━━━━━━┛''')

        choice = input("Enter choice: ")

        if choice == '1':
            add_member(members)
        elif choice== '0':
            print(''' ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗
██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗  
██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  
╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗
 ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝''')
            break
        elif choice == '2':
            view_members(members)
        elif choice == '3':
            record_attendance(members)
        elif choice == '4':
            add_plan(plans)
        elif choice == '5':
            view_plans(plans)
        elif choice == '6':
            add_trainers(trainers)
        elif choice == '7':
            view_trainers(trainers)
        elif choice == '8':
            search(members,plans, trainers)
        elif choice == '9':
            save(members,plans,trainers)
            print("✅ Data saved. Goodbye!")
            print('''\n████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗        ██╗   ██╗ ██████╗ ██╗   ██╗
╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝        ╚██╗ ██╔╝██╔═══██╗██║   ██║
   ██║   ███████║███████║██╔██╗ ██║█████╔╝          ╚████╔╝ ██║   ██║██║   ██║
   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗           ╚██╔╝  ██║   ██║██║   ██║
   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗           ██║   ╚██████╔╝╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝           ╚═╝    ╚═════╝  ╚═════╝ ''')
            break
        elif choice == '10':
            choice2=input("Enter 1 for members, 2 for plans, 3 for trainers")
            if choice2 == '1':
                delete_record(members)
            elif choice2 == '2':
                delete_record(plans)
            elif choice2 == '3':
                delete_record(trainers)
            else:
                print(" Invalid choice ")
        elif choice == '11':
            change_records(members,plans,trainers)
        else:
            print("❌ Invalid choice.")

try:
    main()
except KeyboardInterrupt:
    print("\n\nProgram stopped by User")

