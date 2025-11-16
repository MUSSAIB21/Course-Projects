import jdk.jfr.Timestamp;

import java.util.Scanner;
class Person{
    Scanner input=new Scanner(System.in);
    private String name;
    private int age;
    private double weight;
    private double height;

    public double getWeight() {
        return weight;
    }
    public void setWeight(double weight) {
        this.weight = weight;
    }
    public double getHeight() {
        return height;
    }
    public void setHeight(double height) {
        this.height = height;
    }
    public String getName() {
        return name;
    }
    public void setName() {
        this.name = input.next();
    }
    public int getAge() {
        return age;
    }
    public void setAge() {
        this.age = input.nextInt();
    }


    Person(String n,int a,double w,double h){
        this.name=n;
        this.age=a;
        this.weight=w;
        this.height=h;
    }
    Person(){}

    public static void main(String[] args) {
        Person p1 =new Person("as",20,75,180);
        System.out.println(p1.name);
        System.out.println(p1.age);
    }
}
