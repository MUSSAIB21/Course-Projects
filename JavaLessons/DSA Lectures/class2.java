public class class2{
    public static void main(String[] args) {
        Shape s = new Shape();
        Circle c = new Circle();
        Shape s2 = new Circle();

        s.draw();
        c.draw();
        s2.draw();
    }
}
class Shape{
    Shape(){}
    public void draw(){
        System.out.println("I am a shape");
    }
}
class Circle extends Shape{
    Circle(){}
    public void draw(){
        System.out.println("I am a new Circle");
    }
}