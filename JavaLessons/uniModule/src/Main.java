abstract class Shape{
    abstract double getArea();
}
class Rectangle extends Shape{
    int lenght;
    int width;

    Rectangle(int lenght,int width){
        this.lenght=lenght;
        this.width=width;
    }

    @Override
    double getArea() {
        return this.lenght*this.width;
    }

}


class Circle extends Shape{
    int radius;

    Circle(int radius){
        this.radius=radius;
    }

    @Override
    double getArea() {
        return Math.PI*this.radius*this.radius;
    }
}
class Triangle extends Shape{
    int base;
    int altitude;

    Triangle(int base,int altitude){
        this.base=base;
        this.altitude=altitude;
    }

    @Override
    double getArea() {
    return .5*this.altitude*this.base;
    }
}
public class Main {
    public static void main(String[] args) {
        Shape  s1 = new Rectangle(4,5);
        Shape s2 = new Circle(2);
        Shape s3 = new Triangle(3,4);

        System.out.println("Area of s1: "+s1.getArea());
        System.out.println("Area of s2: "+s2.getArea());
        System.out.println("Area of s3: "+s3.getArea());
        
        Shape[] arr1= new Shape[]{s1,s2,s3};
        for(Shape  o:arr1){
            System.out.println(o.getClass());
            System.out.println("Area : "+o.getArea());

        }

    }
}
