public class Questions {

    /*
    Question:Alphabet Case Check
//.trim() removes the additional spaces in strings in .in
// System.out.println(input.next().trim()); all spaces around string will be removed
// so, "   Hello   " will be trimmed to "Hello"


    //.charAt(index) gives the character at given index starting from 0. 0 means first character
//ex word = "Hello"; word.charAt(0) will return H
    Scanner input = new Scanner(System.in);
    char ch = input.next().trim().charAt(0);
    if(ch >='a' && ch <='z'){System.out.print("Lowercase")}
    else {System.out.print("Uppercase");}

    Question: Fibbonachi Numner n
    Scanner input= new Scanner(System.in);
    int a = 0;
    int b = 1;
    int n=input.nextInt();
    int p=1;
    while(p!=n){

        int sum=a+b;
        a=b;
        b=sum;
        p++;

    }
    Alternatively: int n =input.nextInt();
    int c=1;
    int p=0;
    int count=2;
               while(count<=n){
        int temp=c;
        c=c+p;
        p=temp;
        count++;
    }
             System.out.print(b);


    Question: Find number of occurences of a digit in number
    int n= input.nextInt();
    int count=0;
               while(n>0){
        int rem=n%10;
        n=n/10;
        if(rem==3)
        { count++;}
    }
             System.out.print(count);

    Question: Give reverse of a number
    int n=input.nextInt();
    int d=0;
               while(n>0){

        int t=n%10;
        n=n/10;
        d=10*d+t;

    }
             System.out.print(d);


     */
}
