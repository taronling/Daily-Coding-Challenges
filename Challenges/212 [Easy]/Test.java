import java.util.ArrayList;
import java.util.Scanner;

public class Test {
    String[] letters = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
    final int colNum = 26;

    public void columnFinder() {
        int multiplier = ((colNum - 1) / 26) + 1;
        int letter = colNum % 26;
//        System.out.println(multiplier);
//        System.out.println(colNum);
//        System.out.println(colNum % 26);
        for(int i = 0; i < multiplier; i++) {
            if (letter == 0) {
                System.out.print("Z");
            }
            else {
                System.out.print(letters[letter - 1]);
            }
        }
    }
}