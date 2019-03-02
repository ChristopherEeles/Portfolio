import java.util.*;

public class Student {
    // Variables
    private String name;
    private int id;
    private float gpa;

    // Constructors
    public Student(String name) {
        this.name = name;
    }

    public Student(String name, int id) {
        this.name = name;
        this.id = id;
    }

    public Student(float gpa) {
        this.gpa = gpa;
    }

    public Student(String name, int id, float gpa) {
        this(name, id);
        this.gpa = gpa; // Need to use this.var to affect private variables.
    }

    // Methods

    public void printStudent(Student std) {
        System.out.printf("%s%n%s%n%s%n", std.getName(), std.getId(), std.getGpa());

    }

    public void setGpa(float num) {
        this.gpa = num;
    }

    public String getName() {
        return name;
    }

    public Integer getId() {
        return id;
    }

    public Float getGpa() {
        return gpa;
    }

}