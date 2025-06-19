#include <iostream>               // For input/output functions
#include <cmath>                  // For mathematical functions like fabs, PI
#include <iomanip>                // For formatting output (e.g., setprecision)

// Define PI manually if not defined in cmath
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

// Define a struct to represent a 2D point
struct Point {
    float x, y;                  // x and y coordinates
};

// Abstract base class for all shapes
class Shape {
public:
    virtual float area() = 0;         // Pure virtual function to calculate area
    virtual void drawASCII() = 0;     // Pure virtual function to draw shape using ASCII
    virtual ~Shape() {}               // Virtual destructor
};

// Rectangle shape class derived from Shape
class Rectangle : public Shape {
private:
    float* width;                     // Pointer to width
    float* height;                    // Pointer to height

public:
    Rectangle(float w, float h) {     // Constructor: dynamically allocate width and height
        width = new float(w);
        height = new float(h);
    }

    ~Rectangle() {                    // Destructor: free memory
        delete width;
        delete height;
    }

    float area() override {           // Compute area using pointer dereferencing
        return (*width) * (*height);
    }

    void drawASCII() override {       // Draw rectangle using stars
        int w = static_cast<int>(*width);
        int h = static_cast<int>(*height);
        std::cout << "Rectangle:\n";
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++)
                std::cout << "* ";
            std::cout << "\n";
        }
    }
};

// Circle shape class derived from Shape
class Circle : public Shape {
private:
    float* radius;                    // Pointer to radius

public:
    Circle(float r) {                 // Constructor: allocate radius dynamically
        radius = new float(r);
    }

    ~Circle() {                       // Destructor: free memory
        delete radius;
    }

    float area() override {          // Compute area using pr²
        return M_PI * (*radius) * (*radius);
    }

    void drawASCII() override {      // Draw a simple ASCII circle (approximate)
        int r = static_cast<int>(*radius);
        std::cout << "Circle (approx):\n";
        for (int y = -r; y <= r; y++) {
            for (int x = -r; x <= r; x++) {
                if (x * x + y * y <= r * r)
                    std::cout << "*";
                else
                    std::cout << " ";
            }
            std::cout << "\n";
        }
    }
};

// Triangle shape class derived from Shape
class Triangle : public Shape {
private:
    Point* vertices;                 // Pointer to array of 3 vertices

public:
    Triangle(Point a, Point b, Point c) {  // Constructor: allocate and store vertices
        vertices = new Point[3];
        *(vertices + 0) = a;
        *(vertices + 1) = b;
        *(vertices + 2) = c;
    }

    ~Triangle() {                    // Destructor: free vertex array
        delete[] vertices;
    }

    float area() override {         // Compute area using determinant formula
        Point a = *(vertices + 0);
        Point b = *(vertices + 1);
        Point c = *(vertices + 2);
        return 0.5f * fabs(a.x * (b.y - c.y) +
                           b.x * (c.y - a.y) +
                           c.x * (a.y - b.y));
    }

    void drawASCII() override {     // Simple ASCII drawing of a triangle
        std::cout << "Triangle (simple):\n";
        std::cout << "   *\n";
        std::cout << "  * *\n";
        std::cout << " *   *\n";
        std::cout << "*******\n";
    }
};

// Class to manage a collection of shapes
class ShapeManager {
private:
    Shape** shapes;                  // Pointer to array of Shape pointers
    int count;                       // Number of shapes in the collection

public:
    ShapeManager() {                 // Constructor: initialize empty array
        shapes = nullptr;
        count = 0;
    }

    ~ShapeManager() {                // Destructor: free all shapes and array
        for (int i = 0; i < count; ++i)
            delete shapes[i];
        delete[] shapes;
    }

    void addShape(Shape* shape) {    // Add new shape by resizing array
        Shape** newShapes = new Shape*[count + 1];
        for (int i = 0; i < count; ++i)
            *(newShapes + i) = *(shapes + i);
        *(newShapes + count) = shape;
        delete[] shapes;             // Delete old array
        shapes = newShapes;          // Replace with new array
        count++;
    }

    void removeShape(int index) {    // Remove shape by index
        if (index < 0 || index >= count) return;

        delete shapes[index];        // Delete selected shape

        Shape** newShapes = new Shape*[count - 1]; // Allocate smaller array
        for (int i = 0, j = 0; i < count; ++i) {
            if (i != index)
                *(newShapes + (j++)) = *(shapes + i);
        }

        delete[] shapes;             // Free old array
        shapes = newShapes;          // Assign new array
        count--;
    }

    void displayShapes() {           // Loop through and display all shapes
        for (int i = 0; i < count; ++i) {
            std::cout << "Shape #" << (i + 1) << ":\n";
            std::cout << "Area: " << std::fixed << std::setprecision(2)
                      << shapes[i]->area() << "\n";
            shapes[i]->drawASCII();  // Call polymorphic draw function
            std::cout << "------------------------\n";
        }
    }
};

// Main function to demonstrate functionality
int main() {
    ShapeManager manager;            // Create shape manager object

    // Add a rectangle (6 units wide and 3 units tall)
    manager.addShape(new Rectangle(6, 3));

    // Add a circle with radius 4
    manager.addShape(new Circle(4));

    // Add a triangle with three points (A, B, C)
    Point A = {0, 0}, B = {5, 0}, C = {2.5, 5};
    manager.addShape(new Triangle(A, B, C));

    std::cout << "All Shapes:\n";
    manager.displayShapes();         // Display all added shapes

    // Remove the second shape (circle)
    manager.removeShape(1);

    std::cout << "\nAfter Removing Shape 2:\n";
    manager.displayShapes();         // Display remaining shapes

    return 0;                         // End of program
}

