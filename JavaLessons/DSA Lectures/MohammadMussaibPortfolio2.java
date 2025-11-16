import java.util.ArrayList;
import java.util.Scanner;

public class MohammadMussaibPortfolio2 {
    /* This is our main ArrayList which stores the items
       It is a static object so it can be accessed throughout the class
    */
    static ArrayList<ArrayList<Object>> items = new ArrayList<>();
    //The elements of this arraylists are themselves arraylists
    public static void main(String[] args) {

        // Creating sample data for database
        ArrayList<Object> item1 = new ArrayList<>();
        item1.add("HP Laptop"); // itemName
        item1.add("OA4 10"); // place where item was found
        item1.add(new int[]{12, 6, 2025}); // date when item was found


        ArrayList<Object> item2 = new ArrayList<>();
        item2.add("Headphones");
        item2.add("Cafeteria in Student Union");
        item2.add(new int[]{20, 3, 2025});

        ArrayList<Object> item3 = new ArrayList<>();
        item3.add("Acer Laptop");
        item3.add("Library");
        item3.add(new int[]{7, 5, 2025});

        //adding them to the items arraylist
        items.add(item1);
        items.add(item2);
        items.add(item3);

        menu();
    }
    static void menu(){
        //Our menu function calls the other functions and shows the options to user
        Scanner input = new Scanner(System.in);
        while (true){             //while loop that runs menu till user exits
            System.out.println();

            System.out.println("Select an option:");
            System.out.println("1. Report lost items");
            System.out.println("2. View lost items");
            System.out.println("3. Search for lost items");
            System.out.println("4. Mark item as found");
            System.out.println("5. Exit");
            String choice=input.next();
            //Switch is used here as alternative to if statements
            switch (choice){
                case "1": report();break;
                case "2":viewAll();break;
                case "3":search();break;
                case "4":remove();break;
                case "5":
                    System.out.println("Thank you for using the program hope it helped you!");return;
                case null, default:System.out.println("Invalid choice please try again");break;
            }

        }
    }
    //The first function which adds items to the items arraylist
    static void report(){
        //The lost item objects are stored as arraylists containing 2 strings and an array storing their date
        Scanner input = new Scanner(System.in);
        //<Object> is used due to varying datatypes
        ArrayList<Object> item = new ArrayList<>();
        System.out.println("Name of lost item:");
        item.add(input.nextLine()); // itemName

        System.out.println("Place where lost item found:");
        String place=input.nextLine(); // place where item was found
        item.add(place);

        System.out.println("Date when lost item found:");
        System.out.println("Day: ");int day= input.nextInt();
        System.out.println("Month: ");int  month= input.nextInt();
        System.out.println("Year: ");int year= input.nextInt();
        item.add(new int[]{day,month,year}); // date when item was found

        items.add(item);
    }
    static void search(){
        /*The search function searches for items based on name or location found
        * It prints out the location, date and name of the items with a partial or full match*/
        Scanner input=new Scanner(System.in);
        System.out.println("Please enter the name of the lost item or location where it was lost");
        String name=input.next();
        boolean notFound=true;

        int itemsFound=0;
        System.out.println("\n\n   Name"+" (reported missing on)\n");
        for(ArrayList<Object> item:items){
            if((((item.get(0)).toString().toLowerCase()).contains(name.toLowerCase()))||((item.get(1)).toString().toLowerCase()).contains(name.toLowerCase())){
                int[] date=(int[])item.get(2);
                itemsFound+=1;
                System.out.println(itemsFound+". "+item.get(0)+"("+date[0]+"."+date[1]+"."+date[2]+")");
                System.out.println("Place it was found: "+item.get(1)+"\n");
                notFound=false;
            }
        }
        if (notFound){
            System.out.println("No item with that name found");
        }
    }
    static void viewAll(){
        /*This function prints out the names of all the lost items
          in the database along with the date they were reported*/
        System.out.println("\n\n   Name"+" (reported missing on)\n");
        int x=0;
        for(ArrayList<Object> item:items){
            int[] date=(int[])item.get(2);
            x+=1;
            System.out.println(x+". "+item.get(0)+"("+date[0]+"."+date[1]+"."+date[2]+")");
        }
        if (x==0){
            System.out.println("No items in database");
        }
    }
//This function searches object based on name and then confirms with user if they wish to remove it
    static void remove() {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the name of the object to be removed");
        String name = input.next();

        for (int i = 0; i < items.size(); i++) {
            ArrayList<Object> item = items.get(i);
            if (item.get(0).toString().toLowerCase().contains(name.toLowerCase())) {
                System.out.println("Do you wish to mark " + item.get(0) + " as found and remove it from our system?\nType Y to Confirm and any other key to cancel");
                String choice = input.next().toLowerCase();
                if (choice.equals("y")) {
                    System.out.println("Removed " + item.get(0) + "\n");
                    items.remove(i);
                    i--; // adjust index after removal to prevent skipping and avoid error
                }
            }
        }
    }


}

