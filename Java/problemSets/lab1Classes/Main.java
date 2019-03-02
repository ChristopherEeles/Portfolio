public class Main {
    public static void main(String[] args) {
        Student Chris = new Student("Chris", 136, (float) 4.0);

        // System.out.println(Chris.getName());
        // System.out.println(Chris.getId());
        // System.out.println(Chris.getGpa());
        // Chris.setGpa((float) 3.9);
        // System.out.println(Chris.getGpa());

        // Chris.printStudent(Chris);

        Matrix m1 = new Matrix(4, 4);

        int matSize = m1.getRows() * m1.getCols();

        int[] values = new int[matSize];

        for (int i = 0; i < matSize; i++) {
            int rand = (int) (Math.random() * matSize + 1);
            values[i] = rand;
        }

        m1.setRowWise(values);

        m1.printMatrix(m1);

    }
}