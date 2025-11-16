//break is used to manually break a while loop
import java.util.Scanner;
public class Calculator {
    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

        while(true){     int ans=0;
            System.out.print("Enter operator");
            char op=input.next().trim().charAt(0);
            if(op=='+' ||op=='-' ||op=='*' ||op=='/' ||op=='%')
            {
                int num1 =input.nextInt();
                int num2 =input.nextInt();

                if (op=='+'){ans=num1+num2;}
                if (op=='-'){ans=num1-num2;}
                if (op=='*'){ans=num1*num2;}
                if (op=='/'){if(num2!=0)
                {ans=num1/num2;}
                else {System.out.print("cant divide by zero");

                }
                }


                if (op=='%'){ans=num1%num2;}
            }
            else if(op=='x'||op=='X')
            {break;}
            else {System.out.println("Invalid Operation");}
            System.out.println(ans);

        }

    }

}
