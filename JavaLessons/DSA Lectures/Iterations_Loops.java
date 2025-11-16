public class Iterations_Loops {
    /*
Iterations mean repetition of a process and we use them to repeat code to make it more concise and less repetitive

Loops are code structures which allow us to repeat code they are of 2 main Types:
1. While Loops: they run code till the condition holds. while(condition){//code to repeat}
example: boolean hasInternet = false;
     while(hasInternet==false){
    boolean flag = checkInternet();
    if(flag==true){
    hasInternet=true;
    System.out.println("Has Internet");
    }
    else {
    System.out.println("Checking Again");
    }

     }

We can limit the number of repetitions using counter variables
 int i=0;  (initialisation of counter variable)
 while(i<5){   (condition for counter variable)
 //code blocks
i ++;     (increment for counter variable)
 }
 this repeats our code 5 times


 2. for loop: repeats code for a certain number if time. for(int i=0;i<5;i++)
 this will repeat code 5 times

ex. for(int i=10;i>0;i-=2)
{System.out.print("*");}  will print *****                      NOTE: System.out.print doesn't add a line break
                                                                      everytime it repeats at ends

// do while loop: We use it when we want the code to run at least once regardless if condition is false


Nested loops
 for(int i=0;i<3;i++){
     for(int i=0;i<4;i++){
         System.out.print("*");
     }
     System.out.println();
 }

 this code will print ****
                      ****
                      ****
 */
}
/*
Question: Largest of 4 Number
   import java.util.Scanner;
        public class Exec{
            public static void main(String[] args){
                Scanner input = new Scanner(System.in);

                double a=input.nextDouble();
                double b=input.nextDouble();
                double c=input.nextDouble();

                double max=a;
                if(b>max){ max=b;}
                if(c>max){ max=c;}
                System.out.print("The Largest is "+max);

             Alternatively,
                            int max= Math.max(c,Math.max(a,b));

            }

        }

*/