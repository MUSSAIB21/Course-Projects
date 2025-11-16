import java.util.Scanner;
public class MohammadMussaibPortfolio1 {
    //The main method which calls our menu function
    public static void main(String[] args) {
        menu();

    }

    //The menu function gives the first choice and based on that it
    public static void menu(){
        //We can see several print statements and a switch statement block which acts as a replacement for if/else statements and makes code less repetitive

        Scanner input = new Scanner(System.in); //Creating Scanner Object to take input
        while (true){
            System.out.println();
            System.out.println("██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗\n" +
                    "██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝\n" +
                    "██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  \n" +
                    "██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  \n" +
                    "╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗\n" +
                    " ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝");
            System.out.println("This is the University Campus Help System");
            System.out.println("Opening Hours: 8am-5:15pm on weekdays");
            System.out.println("Select an option:");
            System.out.println("1. Student Services");
            System.out.println("2. Library Services");
            System.out.println("3. Sports Centre");
            System.out.println("4. Careers Team");
            System.out.println("5. Eating Places");
            System.out.println("6. Security");
            System.out.println("7. Exit");
            String choice=input.next();
            switch (choice){
                case "1":studentServices();break;
                case "2":libraryServices();break;
                case "3":sportsCentre();break;
                case "4":careers();break;
                case "5":eatingPlaces();break;
                case "6":security();break;
                case "7":System.out.print("\n\n████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗    ██╗   ██╗ ██████╗ ██╗   ██╗\n" +
                        "╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║\n" +
                        "   ██║   ███████║███████║██╔██╗ ██║█████╔╝      ╚████╔╝ ██║   ██║██║   ██║\n" +
                        "   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗       ╚██╔╝  ██║   ██║██║   ██║\n" +
                        "   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗       ██║   ╚██████╔╝╚██████╔╝\n" +
                        "   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ");return;
                case null, default:System.out.println("Please try again and select a valid option");
            }
        }
    // This part of the code contains several other functions which are called by the menu function based on the users choice
    }
    public static void studentServices(){
        //This function is for the first choice
        System.out.println("Student Services");
        System.out.println("1. Documents");
        System.out.println("2. Health Centre Services");
        System.out.println("3. Queries and Feedback");
        System.out.println("4. Contacting Tutors ");
        Scanner input = new Scanner(System.in);
        String choice=input.next();
        switch (choice){
            case "1":System.out.println("All documents are now available on MyHud to download");break;
            case "2":System.out.println("Make sure you are registered in the NHS system, after that you can book an appointment online or in person");
                System.out.println("The Health Centre is Located on the other side of the canal and can be accessed using the Schwann building bridge");break;
            case "3":System.out.println("You can email any feedback to us. iPoint is always open for any queries you may have at the 4th floor of the Student Union building.");break;
            case "4":System.out.println("Brightspace has the contact info of the module tutors and you can contact them through their university email");break;
            case null, default:System.out.println("Please try again and select a valid option");
        }
        System.out.println();

    }
    public static void libraryServices(){
        //Library Function
        System.out.println("Library Services");
        System.out.println("1. Borrow Book");
        System.out.println("2. Careers");
        System.out.println("3. Accessing Research Papers");
        Scanner input = new Scanner(System.in);
        String choice=input.next();
        switch (choice){
            case "1":System.out.println("The University does not allow students to borrow books");break;
            case "2":System.out.println("Please speak to the library staff to get information about careers in the library, located in floor 4 of Schwann building Good Luck! ");break;
            case "3":System.out.println("Log in to your browser using your University Email. This will give you access to most journals.");
            System.out.println("Additionally You may also speak to the librarians about getting access to specific books or research which may not be available.");break;
            case null, default:System.out.println("Please try again and select a valid option");
        }
        System.out.println();

    }
    //Sports centre function
    public static void sportsCentre(){
        System.out.println("Sports Centre is located in the 2nd and 3rd floor of the student union building");
        System.out.println("Sports Centre Services");
        System.out.println("1. Book Court");
        System.out.println("2. Sports Societies");
        System.out.println("3. Upcoming Events");
        Scanner input = new Scanner(System.in);
        String choice=input.next();
        switch (choice){
            case "1":System.out.println("Visit the student union office building to schedule a booking for yourself or your group");break;
            case "2":System.out.println("You can visit the student union website to join a society or to create your own");break;
            case "3":System.out.println("We will send you emails on your university email to inform you of any events, moreover the website will also have this information ");break;
            case null, default:System.out.println("Please try again and select a valid option");
        }
        System.out.println();
    }
    public static void careers(){
        System.out.println("The careers team is located on the 4th floor of the Student Union near iPoint building give them a visit if you require assistance");
    }
    public static void eatingPlaces(){
        System.out.println("The Student union building has a cafeteria, international kitchen pizza shop and shop. Be sure to check their social media to look up the menu. :) ");

    }
    public static void security(){
        System.out.println("The security team is located at the ground floor of he Harold Wilson building. Any lost property is to be declared or retrieved there");
    }
}
