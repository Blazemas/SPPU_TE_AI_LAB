import java.util.Scanner;

public class NQueens {

    public static boolean isSafe(int n, char[][] chessboard, int row, int column) {
        // Check upwards
        for (int i = row - 1; i >= 0; i--) {
            if (chessboard[i][column] == 'Q') {
                return false;
            }
        }

        // Check upper left diagonal
        for (int i = row, j = column; i >= 0 && j >= 0; i--, j--) {
            if (chessboard[i][j] == 'Q') {
                return false;
            }
        }

        // Check upper right diagonal
        for (int i = row, j = column; i >= 0 && j < n; i--, j++) {
            if (chessboard[i][j] == 'Q') {
                return false;
            }
        }

        return true;
    }

    public static void printBoard(int n, char[][] chessboard) {
        System.out.println("----------chess Board----------");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(chessboard[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void placeNQueens(int n, int row, char[][] chessboard) {
        // Base condition
        if (row == n) {
            printBoard(n, chessboard);
            return;
        }

        // Placing queen
        for (int j = 0; j < n; j++) {
            if (isSafe(n, chessboard, row, j)) {
                chessboard[row][j] = 'Q';
                placeNQueens(n, row + 1, chessboard);
                // Backtracking
                chessboard[row][j] = 'X';
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the chessboard: ");
        int n = scanner.nextInt();

        // Dynamically allocate memory for the chessboard
        char[][] chessboard = new char[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                chessboard[i][j] = 'X'; // initialize the chess board
            }
        }

        placeNQueens(n, 0, chessboard);

        scanner.close();
    }
}
