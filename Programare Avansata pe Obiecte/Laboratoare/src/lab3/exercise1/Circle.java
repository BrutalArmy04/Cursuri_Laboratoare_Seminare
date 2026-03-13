package lab3.exercise1;

/**
 * TODO: Implementează Circle extends Shape.
 * - Atribut: private double radius
 * - Constructor: super("Circle"), this.radius = radius
 * - area() = Math.PI * radius * radius
 * - perimeter() = 2 * Math.PI * radius
 */
public class Circle extends Shape {

    // TODO: private double radius
    private final double radius;

    public Circle(double radius) {
        super("Circle");
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius; // TODO: Math.PI * radius * radius
    }

    @Override
    public double perimeter() {
        return Math.PI * 2 * radius; // TODO: 2 * Math.PI * radius
    }
}
