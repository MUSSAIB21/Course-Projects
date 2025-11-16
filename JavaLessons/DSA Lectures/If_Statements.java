public class If_Statements
{/*
Boolean is a data type evaluating to true or false

Relational Operators: == is equals, != is not equals, > and >= are greater and greater or equal(same for <)
ex. 2.0 == (4.0 -2.0) gives true

Control flow: We can disrupt our flow by running portions of code only when we want to

if statement runs code if boolean expression evaluates to true
   if(boolean expression)

   {//code to run if boolean expression is true}

   else

   {//code to run if boolean expression is false}


We can also use else if statements like this
   if(boolean expression) {//code}
   else if(another Boolean expression) {//code2}
   else {//code3



Nested If statements: if(expression){
    if(second expression)
    //code
    else {//code}
}
else{//some code}
   }


Logic Operators are used to join two conditions
 && is and Operator and || is or Operator
 if(condition1 && condition2)
 we can also use ! which is also Logic Operator it means not. ex. if!(A){//code} mean if not also


DeMorgan's Laws: !(A&&B) is same as !A||!B . != Becomes ==
ex. !(A<1 && B>2) = !(A<1) || !(B>2)= (A>=1) || (B<=2)

Short Circuit evaluation: IN if(A&&B) if computer evaluates A to be false it won't evaluate B.
and In if(A || B) if computer evaluates A to be true it won't evaluate B.

Comparing Objects: Lets take 3 String Objects
                   String a = new String("Hello");
                   String b = new String("Hello");
                   String c = a;
  The expression a==b will be false as even though a and b have same content they are stored in diffrent refrence
  or locations in ram. However, c==a will be true as both a and c reference same spot in ram

NOTE: We can also write if statements with only one item we can directly write it in the next line
 ex. if(expression)
     system.out.println("Hi"); will run the line if expression is true
*/
}
