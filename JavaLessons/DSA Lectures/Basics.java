public class Basics {/*

 Variables: Containers used to store data in RAM
 Syntax: type name = value;

 int is for Integers
 double is for floating point numbers
 boolean can be true or false
 String is used to store Texts (This is a refrence data type while the other 3 are primative data type )


 names of variables are in camelCase and name must have no spaces names of classes are to be in PascalCLass
 When typing value for string make sure its in "" or computer will think you are reffering to another variable


A constant is a variable whose value can't be changed
If we wish to create one we must add keyword final before variable initialization
example: final int pi = 3.14;

= is called the assignment operator it dosen't mean equals but rather becomes, like z becomes 7 is z = 7
equals is represented by ==

we can change values like so:
int myInteger = 7;
myInteger = 8;
if we use myInteger the value used will be of 8

ARITHMETIC OPERATORS
+             -        *        /       %
addition subtraction multiply divide modulus(remainder in division between two numbers)
 7.0-2.0 will be 5.0
 7*5.00 will be 35.00

 when we turn double to integer it just removes the part after the decimal
 when we do integer division, we get the decimal parts removed
 1%2 is remainder of one divided by two meaning one

 MODIFYING VALUES WITH Math
 example: int x=7;   x=x+3;  can also be done as x +=3
 here += is called compound operators  x
 if we only wish to change by one we can use increment or decrement operator ++ and --

 CASTING
 when we convert one type into another

 int d=(int)7.8; will give variable d value of 7
 double i=double(6); will givr 6.0 to i

 RANGE OF DATA TYPES
 The java data type int is stored as 4bytes of RAM while bit is one byte
 a byte is 8bits which can be 0 or 1 so bit can show max of 2^7 - 1 while for int its 2^31 -1 min in -2^31
 represented by Integer.MAX_VALUE and Integer.MIN_VALUE
 we can also use long for larger or lesser numbers

 Objects are singular entities which perform all the actual work
 Objects have properties called fields eg. colour, they have methods which actions they can perform they are made
 using constructors

 Methods: objectName.methodName(inputs);  , if a method returns no value its called a void method

 Constructos: className objectName = new className(inputs); this creates an object with name objectName
              (refrence) (name)
              Strings are objects(refrence type)
Methods can also be static or non static
Static are called on classes while non static are called on classes. Math has static while string has non static
*/
}
