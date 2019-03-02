import java.util.*;

public class Matrix {
    // Variables
    // matrix is an array of arrays
    private int nrows;
    private int ncols;
    private int[][] cells;

    // Constructors
    // constructor that takes another matrix
    public Matrix(int[][] cells) {
        this.cells = cells;
        this.nrows = cells.length;
        this.ncols = cells[0].length;
    }

    public Matrix(int nrows, int ncols) {
        this.nrows = nrows;
        this.ncols = ncols;
        cells = new int[nrows][ncols];
    }

    // Methods
    public void setRowWise(int[] rowVals) {
        if (rowVals.length % ncols != 0) {
            return;
        }

        int idx = 0;
        for (int r = 0; r < (rowVals.length / ncols); r++) {
            for (int c = 0; c < ncols; c++) {
                cells[r][c] = rowVals[idx];
                idx++;
            }
        }
    }

    public void setColWise(int[] colVals) {
        if (colVals.length % nrows != 0) {
            return;
        }
        int idx = 0;
        for (int c = 0; c < (colVals.length / nrows); c++) {
            for (int r = 0; r < nrows; r++) {
                cells[r][c] = colVals[idx];
                idx++;
            }
        }
    }

    public int getRows() {
        return nrows;
    }

    public int getCols() {
        return ncols;
    }

    public int[][] getCells() {
        return cells;
    }

    public void printMatrix(Matrix mat) {
        int rows = mat.getRows();
        int cols = mat.getCols();
        int[][] matrix = mat.getCells();

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print(matrix[i][j]);
            }
            System.out.printf("%n");
        }
    }

}