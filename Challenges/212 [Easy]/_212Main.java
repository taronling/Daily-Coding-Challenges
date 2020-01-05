import java.util.ArrayList;
import java.util.Scanner;

public class _212Main {
    String[] letters = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
    int colNum;

    public void columnFinder() {
        Scanner scanner = new Scanner(System.in);
        try {
            colNum = Integer.parseInt(scanner.nextLine());
            int multiplier = ((colNum - 1) / 26) + 1;
            int letter = colNum % 26;
            for(int i = 0; i < multiplier; i++) {
                if (letter == 0) {
                    System.out.print("Z");
                }
                else {
                    System.out.print(letters[letter - 1]);
                }
            }
        } catch (NumberFormatException e) {
            System.out.print("Please enter a valid integer");
        }
    }
}