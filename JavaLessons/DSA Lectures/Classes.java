public class Classes {
/*
 CLasses are blueprints for creating a type for objects
 class ClassName {
 //Code
 }
 a public class is available outside the file while private means the thing isn't available outside the objects
 and only object can access it

 example: public class Taxi {
 // fields
 private int numPassengers;    (this is called leaving variable uninitialized as we didn't use = and value)
 private boolean isConvertable;  (uninitialized means no initial value)
 private String make; private string model;  (yes we can write code in 2 lines if there's ; in between because
 ; means new line)

 //methods
 public void addPassengers(int num) {(we used public so method is available to all obj and void as it dosent return)
 this.numPassengers += num; (this keyword refers to the object)
 }

 public int currentNumPassengers() {
 return this.numPassengers;
 }

 public void makeAndModel() {
 System.out.println(this.make+ "and" this.model);
 }

 //Constructors(must always have same name as class and it must be public because if we cant use it outside
 itself it will be completely useless)
 publc Taxi(int num, boolean conv, String mdl, String mke) {
 this.numPassengers= num;
 this.model= mdl;
 this.make= mke ;
 this.isConvertable= conv;


 }



 }
 //END OF CLASS

 java.lang (java initial package and .lang is subpackage)

 String CLass                                                      Math Class
 methods                                                       static methods
 .lenght(); returns the lenght of
 characters in main string                          .abs(num); returns absolute value of num

 .indexOf(string); returns index of                          .power(base,exponent); returns base^exponent
 the string inside our main string

 .substring(start,end); end is optional, it returns          .sqrt(num); returns square root of num
 string in original string
 based on the range.                  .random(); returns random number between 0 and 1

 .compareTo(String); returns value based on String
 comparison

 String indexes start from 0 For eg. In Hello,
 H has index 0 and o has 4

 Ex. String myString = "Hello";
 myString.lenght(); gives 5
 myString.indexOf("e"); gives 1
 myString.substring(2,3); gives l
 (substring does not include end index)
 myString.compareTo("Bye"); gives 6 as
 H is 6 letters ahead of B (including B)
 lowercase are greater so a>Z

 If we wish to use "" inside string "" we
 use escape sequences \" \"
 \" for quote \n for line \\ for backslash
 and \t for tab
*/

 }
