import java.util.Scanner;
public class Inputs{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);   //we created a Scanner Object callled input which stores System.in
        System.out.println("Please Enter ROLL NUMBER");
        int rollno = input.nextInt();           //created integer variable which takes next int from input object
        System.out.print("Your roll number is ");
        System.out.print(rollno);
    }

}
//ctrl+/ while selecting line/lines turns them into comments

/*
    when we assign variables there are default data types for them and if we want something different we
    have to cast them while assigning

    for example: int is the default for integers and if we wish to store a number as long,
    we must cast it as long while initializing ex:  long largeInteger = 3201983091839083L;
*/


