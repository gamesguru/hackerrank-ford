import java.util.*;

/* Write your class implementations here. Do not use access modifiers when declaring your classes. */
class Point2D {
    double x;
    double y;
    
    Point2D(double x, double y) {
        this.x = x;
        this.y = y;
    }
    
    double dist2D(Point2D p2) {
        double d = Math.pow(x - p2.x, 2) + Math.pow(y - p2.y, 2);
        return Math.sqrt(d);
    }
    
    void printDistance(double d) {
        String value = String.valueOf((int) Math.ceil((d)));
        System.out.println("2D distance = " + value);
    }
}

class Point3D extends Point2D {
    double x;
    double y;
    double z;
    
    Point3D(double x, double y, double z) {
        super(x, y);
        this.x = x;
        this.y = y;
        this.z = z;        
    }
    
    double dist3D(Point3D p2) {
        double d = Math.pow(x - p2.x, 2) + Math.pow(y - p2.y, 2) + Math.pow(z - p2.z, 2);
        return Math.sqrt(d);
    }
    
    void printDistance(double d) {
        String value = String.valueOf((int) Math.ceil((d)));
        System.out.println("3D distance = " + value);
    }
}

public class Solution {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int x1 = scanner.nextInt();
		int y1 = scanner.nextInt();
		int z1 = scanner.nextInt();
		int x2 = scanner.nextInt();
		int y2 = scanner.nextInt();
		int z2 = scanner.nextInt();
        scanner.close();
        
		Point3D p1 = new Point3D(x1, y1, z1);
		Point3D p2 = new Point3D(x2, y2, z2);
		double d2 = p1.dist2D(p2);
		double d3 = p1.dist3D(p2);
        // The code below uses runtime polymorphism to call the overridden printDistance method:
        Point2D p = new Point2D(0, 0);
		p.printDistance(d2);
		p = p1;
		p.printDistance(d3);
	}
}
