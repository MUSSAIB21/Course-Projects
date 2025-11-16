//Importing Classes from .util library
import java.util.ArrayList;
import java.util.Scanner;

// Importing Classes from .io library
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.BufferedReader;


// Data storing Classes
/*The contact class will store the email and phone number of patients and doctors
  Private access keywords have been used to prevent unauthorized access*/
class Contact {
    private String phone;
    private String email;

    public Contact(String phone, String email) {
        this.phone = phone;
        this.email = email;
    }

    //setters and getters
    public void setPhone(String phone) { this.phone = phone; }
    public void setEmail(String email) { this.email = email; }

    public String getPhone() { return phone; }
    public String getEmail() { return email; }

    //toString method will be used to print instances of that paticular class
    @Override
    public String toString() {
        return "Phone: " + phone + ", Email: " + email;
    }
}
// This class will store the medical records for patients
class MedicalRecord {
    private String diagnosis, bloodGroup, admissionDate, dischargeDate;

    public MedicalRecord(String diagnosis, String bloodGroup, String admissionDate, String dischargeDate) {
        this.diagnosis = diagnosis;
        this.bloodGroup = bloodGroup;
        this.admissionDate = admissionDate;
        this.dischargeDate = dischargeDate;
    }
    //setters and getters
    public void setDiagnosis(String diagnosis) { this.diagnosis = diagnosis; }
    public void setBloodGroup(String bg) { this.bloodGroup = bg; }
    public void setAdmissionDate(String date) { this.admissionDate = date; }
    public void setDischargeDate(String date) { this.dischargeDate = date; }

    public String getDiagnosis() { return diagnosis; }
    public String getBloodGroup() { return bloodGroup; }
    public String getAdmissionDate() { return admissionDate; }
    public String getDischargeDate() { return dischargeDate; }

    @Override
    public String toString() {
        return "Diagnosis: " + diagnosis + ", Blood Group: " + bloodGroup +
                ", Admitted: " + admissionDate + ", Discharged: " + dischargeDate;
    }
}

//Person Classes
/*These are the classes which will store most of the actual data for our doctors and patients
 * The person Class is an abstract class which will serve as the superclass for the other classes*/
abstract class Person {
    protected String id, name; //protected keyword is used so these fields can be inherited
    protected int age;

    public Person(String id, String name, int age) {
        this.id = id; this.name = name; this.age = age;
    }

    //Setters and Getters
    public String getId() { return id; }
    public String getName() { return name; }
    public int getAge() { return age; }

    public void setName(String name) { this.name = name; }
    public void setAge(int age) { this.age = age; }

    public abstract String getDetails();
}
// Doctor is subclass of person with fields about specialization and working hours
class Doctor extends Person {
    private String specialization;
    private String workingHours;
    private Contact contact;

    public Doctor(String id, String name, int age, String specialization, String hours, Contact contact) {
        super(id, name, age);
        this.specialization = specialization;
        this.workingHours = hours;
        this.contact = contact;
    }

    public String getWorkingHours() { return workingHours; }
    public void setWorkingHours(String hours) { this.workingHours = hours; }

    public String getSpecialization() { return specialization; }
    public void setSpecialization(String spec) { this.specialization = spec; }

    public Contact getContact() { return contact; }


    public String getSummary() {
        return String.format("%-10s %-20s %-20s", id, name, specialization);
    }
    // This method will be used to print each doctor object
    @Override
    public String getDetails() {
        return "Doctor [ID=" + id + ", Name=" + name + ", Age=" + age +
                ", Specialization=" + specialization + ", Hours=" + workingHours + ", " + contact + "]";
    }
}

//Patient is another subclass of Person, with additional fields of room number and medical record
class Patient extends Person {
    private String roomNumber;
    private MedicalRecord record;
    private Contact contact;

    public Patient(String id, String name, int age, String room, MedicalRecord record, Contact contact) {
        super(id, name, age);
        this.roomNumber = room;
        this.record = record;
        this.contact = contact;
    }
    //setters and getters
    public String getRoomNumber() { return roomNumber; }
    public void setRoomNumber(String roomNumber) { this.roomNumber = roomNumber; }

    public MedicalRecord getMedicalRecord() { return record; }


    public Contact getContact() { return contact; }



    public String getSummary() {
        return String.format("%-10s %-20s %-10s", id, name, roomNumber);
    }
    //This method is used to print details of each patient object
    @Override
    public String getDetails() {
        if (this.id.equals("007")){
            System.out.println("Congrats for discovering the easter egg \n");
            System.out.println("""
                         0000             0000        7777777777777777/========___________
                       00000000         00000000      7777^^^^^^^7777/ || ||   ___________
                      000    000       000    000     777       7777/=========//
                     000      000     000      000             7777// ((     //
                    0000      0000   0000      0000           7777//   \\\\   //
                    0000      0000   0000      0000          7777//========//
                    0000      0000   0000      0000         7777
                    0000      0000   0000      0000        7777
                     000      000     000      000        7777
                      000    000       000    000       77777
                       00000000         00000000       7777777
                         0000             0000        777777777""");
        }

        return "\nPatient [ID=" + id + ", Name=" + name + ", Age=" + age +
                ", Room=" + roomNumber + ", " + record + ", " + contact + "]";
    }
}


//Hospital Manager Class will contain all the methods used on the objects

class HospitalManager {
    private ArrayList<Person> records = new ArrayList<>();
    private final String filename = "mohammadMussaib_data.txt";


    //This method is used to add both doctors and patients to the records list
    public boolean addRecord(Person p) {
        for (Person existing : records) {
            //This checks for duplicate IDs, so no two objects with same ID exist
            if (existing.getId().equalsIgnoreCase(p.getId())) {
                System.out.println(" Duplicate ID detected. Record not added.");
                return false;
            }
        }
        records.add(p);
        return true;
    }

    public void viewAllDoctors() {
//This method prints details of all the doctor objects, using format strings
        System.out.println("\n    Doctors    ");
        System.out.printf("%-10s %-20s %-20s%n", "ID", "Name", "Specialization"); //using format string to format text cleanly
        for (Person p : records) {
            if (p instanceof Doctor) System.out.println(((Doctor)p).getSummary());
        }
    }

    public void viewAllPatients() {
        //Same as the previous function, except for patients
        System.out.println("\n    Patients    ");
        System.out.printf("%-10s %-20s %-10s%n", "ID", "Name", "Room");
        for (Person p : records) {
            if (p instanceof Patient&& !p.id.equals("007")) System.out.println(((Patient)p).getSummary());
        }
    }
    //This function is used to perform a search based on ID, it returns the doctor or person with that specific ID
    public Person searchById(String id) {
        for (Person p : records) {
            if (p.getId().equalsIgnoreCase(id)) return p;
        }
        return null;
    }
    //This function is used to modify records
    public void modifyRecord(String id, Scanner sc) {
        Person p = searchById(id);
        if (p == null) {
            System.out.println(" No record found for ID: " + id);
            return;
        }
        System.out.println("You can make changes to the record by entering new values");
        System.out.println("To keep the original value simply leave the field blank");

        System.out.println("\nEditing record for: " + p.getName());
        System.out.print("Update name (leave blank to skip): ");
        String name = sc.nextLine();
        if (!name.isEmpty()) p.setName(name);

        System.out.print("Update age (leave blank to skip): ");
        String ageStr = sc.nextLine();
        if (!ageStr.isEmpty()) {
            //try-catch block to avoid exception
            try {
                int age = Integer.parseInt(ageStr);
                p.setAge(age);
            } catch (NumberFormatException e) {
                System.out.println(" Invalid age. Skipped.");
            }
        }

        if (p instanceof Doctor d) {
            System.out.print("Update specialization (blank to skip): ");
            String s = sc.nextLine();
            if (!s.isEmpty()) d.setSpecialization(s);

            System.out.print("Update working hours (blank to skip): ");
            String h = sc.nextLine();
            if (!h.isEmpty()) d.setWorkingHours(h);

            System.out.print("Update phone (blank to skip): ");
            String phone = sc.nextLine();
            if (!phone.isEmpty()) d.getContact().setPhone(phone);

            System.out.print("Update email (blank to skip): ");
            String email = sc.nextLine();
            if (!email.isEmpty()) d.getContact().setEmail(email);

        } else if (p instanceof Patient pt) {
            System.out.print("Update room number (blank to skip): ");
            String room = sc.nextLine();
            if (!room.isEmpty()) pt.setRoomNumber(room);

            System.out.print("Update diagnosis (blank to skip): ");
            String diag = sc.nextLine();
            if (!diag.isEmpty()) pt.getMedicalRecord().setDiagnosis(diag);

            System.out.print("Update blood group (blank to skip): ");
            String bg = sc.nextLine();
            if (!bg.isEmpty()) pt.getMedicalRecord().setBloodGroup(bg);

            System.out.print("Update admission date (blank to skip): ");
            String adm = sc.nextLine();
            if (!adm.isEmpty()) pt.getMedicalRecord().setAdmissionDate(adm);

            System.out.print("Update discharge date (blank to skip): ");
            String dis = sc.nextLine();
            if (!dis.isEmpty()) pt.getMedicalRecord().setDischargeDate(dis);

            System.out.print("Update phone (blank to skip): ");
            String phone = sc.nextLine();
            if (!phone.isEmpty()) pt.getContact().setPhone(phone);

            System.out.print("Update email (blank to skip): ");
            String email = sc.nextLine();
            if (!email.isEmpty()) pt.getContact().setEmail(email);
        }

        System.out.println(" Record updated.");
    }
    //This function removes the record from the records list
    public boolean removeRecord(String id) {
        return records.removeIf(p -> p.getId().equalsIgnoreCase(id));
        /*This is a function which removes an element from a collection if
         the boolean condition is true  */
    }


    //IO methods
    //This method reads data from the text file and adds objects to the records list
    public void importData() {

        /*Easter Egg: A special patient whose record does not appear on the list
         * Even the data files don't store his information
         * Data about this patient can only be accessed by searching for his record
         */
        Contact ct=new Contact("999","not provided");
        MedicalRecord rc=new MedicalRecord("Digitalis Poisoning","A+","7.11.06","9.11.06");
        Patient jb= new Patient("007","James Bond",40,"7",rc,ct);
        addRecord(jb);

        try {
            File file = new File(filename);
            if (!file.exists()) {
                file.createNewFile();
                System.out.println("File created: " + filename);
                return;
            }
            //Creating buffer reader object to read file
            BufferedReader reader = new BufferedReader(new FileReader(file));
            String line;
            //creates appropriate object and adds to records
            while ((line = reader.readLine()) != null) {
                String[] obj = line.split(",");
                //if the first string in array is DOCTOR it creates a doctor object
                if (obj[0].equals("DOCTOR") && obj.length == 8) {
                    Doctor d = new Doctor(obj[1], obj[2], Integer.parseInt(obj[3]),
                            obj[4], obj[5], new Contact(obj[6], obj[7]));
                    addRecord(d);
                    //if the first string is PATIENT it creates a patient object
                } else if (obj[0].equals("PATIENT") && obj.length == 11) {
                    if (obj[1].equals("007") ) {continue;}// Easter egg: do not add this specific id from files

                    MedicalRecord mr = new MedicalRecord(obj[5], obj[6], obj[7], obj[8]);
                    Patient pt = new Patient(obj[1], obj[2], Integer.parseInt(obj[3]), obj[4], mr,
                            new Contact(obj[9], obj[10]));
                    addRecord(pt);
                }
            }
            reader.close();
            System.out.println(" Data imported.");
            //This try catch block handles exceptions caused by IO handling
        } catch (IOException e) {
            System.out.println(" Error importing data: " + e.getMessage());
        }
    }
    //This method writes data from the records list to the text file
    public void saveData() {
        //creating print writer object
        try (PrintWriter writer = new PrintWriter(new FileWriter(filename))) {
            for (Person p : records) {
                if (p instanceof Doctor d) {
                    writer.println("DOCTOR," + d.getId() + "," + d.getName() + "," + d.getAge() + "," +
                            d.getSpecialization() + "," + d.getWorkingHours() + "," + d.getContact().getPhone()+","+d.getContact().getEmail());
                } else if (p instanceof Patient pt) {
                    if (p.id.equals("007")) {continue;} //don't write this specific patient on files
                    writer.println("PATIENT," + pt.getId() + "," + pt.getName() + "," + pt.getAge() + "," +
                            pt.getRoomNumber() + "," + pt.getMedicalRecord().getDiagnosis() + "," + pt.getMedicalRecord().getBloodGroup() + "," +
                            pt.getMedicalRecord().getAdmissionDate()+","+pt.getMedicalRecord().getDischargeDate()+"," + pt.getContact().getPhone()+","+pt.getContact().getEmail());
                }
            }
            System.out.println("Data saved");
        } catch (IOException e) {
            System.out.println("Error saving: " + e.getMessage());
        }
    }
}

// Main method
// This method contains the main menu and switch block which navigates the program

public class SSD2FinalProject {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HospitalManager manager = new HospitalManager();
        boolean running = true;
        manager.importData();

        //Adding some sample records into our database
        Patient p11=new Patient("p44","Joe Biden",70,"7A",new MedicalRecord("Demantia","A+","12 Jan 2025","t.b.d"),new Contact("classified","sleepyjoe@democrats.com"));
        Doctor d44=new Doctor("d44","Dre",50,"Hip Hop","21-05",new Contact("07204102310","drdre@gmail.com"));
        manager.addRecord(d44);
        manager.addRecord(p11);

        /*Here we are making a new manager object
         * We are using boolean running to execute the code till it changes to false
         * Inside the while loop is switch cases which call functions inside the Hospital Manager Class
         * */
        System.out.println("Welcome to the hospital management system");
        while (running) {
            System.out.println("\n   Hospital Menu ");
            System.out.println("1. View Doctors");
            System.out.println("2. View Patients");
            System.out.println("3. Search by ID");
            System.out.println("4. Add Record");
            System.out.println("5. Remove Record");
            System.out.println("6. Save Records");
            System.out.println("7. Modify Record");
            System.out.println("8. Save and Quit");
            System.out.println("9. Quit without saving");
            System.out.println("Please select an option from menu and enter your choice");
            System.out.print("Your choice: ");

            try {
                String choice = sc.nextLine();
                switch (choice) {
                    case "1": manager.viewAllDoctors(); break;
                    case "2": manager.viewAllPatients(); break;
                    case "3":
                        System.out.println("To search the person, enter their ID");
                        System.out.print("Enter ID: ");
                        Person person = manager.searchById(sc.nextLine());
                        System.out.println(person != null ? person.getDetails() : "Not found.");
                        //This line prints the details if person exists, and prints not found if no person with that specific ID exists
                        break;
                    case "4":
                        System.out.print("ID: "); String id = sc.nextLine();
                        System.out.print("Name: "); String name = sc.nextLine();
                        System.out.print("Age: "); int age = Integer.parseInt(sc.nextLine());
                        System.out.print("Is this a Doctor or Patient: (enter doctor/patient)");
                        String type = sc.nextLine();


                        if (type.equalsIgnoreCase("Doctor")) {
                            System.out.print("Specialization: "); String spec = sc.nextLine();
                            System.out.print("Working Hours: "); String hours = sc.nextLine();
                            System.out.print("Phone: "); String phone = sc.nextLine();
                            System.out.print("Email: "); String email = sc.nextLine();

                            Contact c = new Contact(phone, email);
                            manager.addRecord(new Doctor(id, name, age, spec, hours, c));
                            System.out.println("Doctor "+name+" added successfully");
                            break;
                        } else if (type.equalsIgnoreCase("Patient")) {
                            System.out.print("Room Number: "); String room = sc.nextLine();
                            System.out.print("Diagnosis: "); String diagnosis = sc.nextLine();
                            System.out.print("Blood Group: "); String blood = sc.nextLine();
                            System.out.print("Admission Date: "); String admit = sc.nextLine();
                            System.out.print("Discharge Date: "); String discharge = sc.nextLine();
                            System.out.print("Phone: "); String phone = sc.nextLine();
                            System.out.print("Email: "); String email = sc.nextLine();

                            MedicalRecord med = new MedicalRecord(diagnosis, blood, admit, discharge);
                            Contact contact = new Contact(phone, email);
                            Patient patient = new Patient(id, name, age, room, med, contact);
                            manager.addRecord(patient);
                            System.out.println("Patient "+name+" added successfully");
                            break;
                        } else {
                            System.out.println("Invalid type. Please enter Doctor or Patient.");
                            break;
                        }

                    case "5":
                        System.out.print("Enter ID of record to remove: ");
                        String idToRemove = sc.nextLine();

                        if (manager.removeRecord(idToRemove)) {
                            System.out.println(" Record removed.");
                        } else {
                            System.out.println(" Record not found.");
                        }
                        break;

                    case "6":
                        manager.saveData();
                        break;

                    case "7":
                        System.out.print("Enter ID to modify: ");
                        String modId = sc.nextLine();
                        manager.modifyRecord(modId, sc);
                        break;

                    case "8":
                        System.out.println("Thank you for using the program");
                        manager.saveData();
                        running=false;
                        break;

                    case "9":
                        //Used to exit the program
                        //Asks users to confirm they want to exit
                        System.out.println("Are you sure? Unsaved data will be lost");
                        System.out.println("Enter y to confirm");
                        String confirm =sc.nextLine();
                        if (confirm.equalsIgnoreCase("y")) {
                            running = false;
                            System.out.println(" Exiting Hospital Management System.");
                        }
                        else{
                            System.out.println("Exit Aborted");
                        }
                        break;
                    default:
                        System.out.println(" Invalid choice. Please try again.");
                }
            } catch (Exception e) {
                System.out.println(" Error: " + e.getMessage());
            }
        }
        sc.close();
    }
}
