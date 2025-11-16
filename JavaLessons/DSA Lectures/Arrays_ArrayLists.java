public class Arrays_ArrayLists {

    /*
    Array: Collection of Values
we may refer to each element by its index starting at 0

Creating Arrays:
 First specify type of array

 dataType[] varName = new dataType[n]; will create array of n elements of given dataType

 n is called the arraylenght and can be accessed using arrayName.lenght
 once we set this lenght we cannot change its

 when we create array all elements are set to default values:
 int,double is 0, boolean is false and null for String


Accessing Elements:arrayName[indexOfElement]
  System.out.println(varName[4]); prints the 5th element(AT INDEX 4)
We may also edit like this: arrayName[4] = 2; makes index 4 equal to 2


Creating Arrays using literals:
  int[] arrayName = {1,2,3,4,5}; this also subsequently put our arraylenght at 5

Traversing Arrays using loops:
 for(int i=0;i<array.lenght;i++){

     System.out.println(array[i]);

 }

for(int i = array.lenght-1;i>=0;i--){     //array.lenght - 1 is index of last item of array

    System.out.println(array[i]);
}

for each loops: for(int num : array){          // int is datatype and array is name of array
    System.out.println(num);                   //num is temporary variable
}


ArrayLists: Objects that store a collection of reference data types or Objects

            Primitive                               Reference
        int                                     Integer
        double                                  Double
        boolean                                 Boolean
                                                String
                                                Objects

Arraylists are more flexible , their lenght can be modified

 Creating: ArrayList<String> listName = new ArrayList<String>();
           (type)  (reference type)         (arraylist constructor)
  list starts out empty

 Arraylist Methods:
   list.get(i); returns value of element at index index
   list.add(v); adds v at the end
   list.add(i,v); adds v at i index,previous element at i is moved forward
   list.set(i,v); it replaces the element at index i with v
   list.size(); returns the number of elements in list

 Traversing Arraylists:
    for (int i=0,i<list.size();i++) {

        System.out.println(list.get(i));


    }

2D Arrays: Array with 2 dimentions
we refer to rows with indexes starting with 0 so we start with 0th row and 0th column             ROWS   C
                                                                                                         O
                                                                                                         L
Creating: int[][] varname = new int[3][4];
                                (rows)(columns)
   2D arrays are in row major order meaning column are stored in rows

Accessing the elements of 2D array:System.out.println(arrayName[r][c]); arrayName[r] accesses the entire r row array

Editing Element: arrayName[r][c] =3;

Traversing 2D arrays:   for(int r=o;r<array.lenght;r++){                  //array.lenght means no. of rows
                              for(int c=0;c<array[0].lenght;c++)      //array[0].lenght means no. of columns
    {System.out.println(array[r][c]);  }                  //this code traverses from top left to bottom right
}

    for (int[] row:array){
        for(int val:row)
{System.out.println(val)}
    }


    Good Question from inheritance: public X extends Y
            ArrayList<Y> myYList = new ArrayList<Y>;  //Arraylist containing all Y Objects
            ArrayList<X> myXList = new Arraylist<X>;  //Arraylist containing all X Objects

             Y yObj = new Y();
             X xObj = new X();

    Which code wont't be executed:
    a)myYList.add(xObj);
    b)myYList.add(yObj);
    c)myXList.add(xObj);
    d)myXList.add(yObj);   //this line won't be executed because we cannot add y object in x object ArrayList
                             because even though X objects belong in Y list, Y objects don't in X lists



     */
}
