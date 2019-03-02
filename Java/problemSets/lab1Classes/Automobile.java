import java.util.*;

public class Automobile {
    // Variables
    private String carName;
    private Wheel frontWheel;
    private Wheel rearWheel;
    private Wheel extra;

    // Constructors
    public Automobile(String carName) {
        this.carName = carName;
    }

    // Methods
    public Wheel thirdWheel(Automobile car) {

    }

    // Subclasses
    private class Wheel {
        // Variables
        private String hubcapType;
        private Float radius;

        // Constructors

        // Methods
    }

}