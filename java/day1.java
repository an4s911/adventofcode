import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * day1
 */
public class day1 {
    public static void main(String[] args) {
        Scanner sc = null;
        try {
            sc = new Scanner(new File("./input.txt"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        int sum = 0;
        int sum2 = 0;
        while (sc.hasNextLine()) {
            // Part 1
            String line = sc.nextLine();
            ArrayList<Character> numsInLine = new ArrayList<>();
            ArrayList<Integer> numsInLine2 = new ArrayList<>();
            for (char ch : line.toCharArray()) {
                if (Character.isDigit(ch)) {
                    numsInLine.add(ch);
                }
            }
            int num = Integer.parseInt(
                    String.valueOf(numsInLine.get(0)) + String.valueOf(numsInLine.get(numsInLine.size() - 1)));
            sum += num;

            // Part 2
            for (int i = 0; i < line.length(); i++) {
                int number = getNumFromString(line, i);
                if (number >= 0) {
                    numsInLine2.add(number);
                }
            }

            if (numsInLine2.isEmpty()) {
                System.out.println("helooooo -----".repeat(2));
                continue;
            }

            int num2 = Integer.parseInt(
                    String.valueOf(numsInLine2.get(0)) + String.valueOf(numsInLine2.get(numsInLine2.size() - 1)));
            sum2 += num2;
        }

        System.out.println("Part 1: " + sum);
        System.out.println("Part 2: " + sum2);

    }

    public static int getNumFromString(String str, int index) {
        if (Character.isDigit(str.charAt(index))) {
            return Integer.parseInt(String.valueOf(str.charAt(index)));
        }
        for (int i = index; i < str.length(); i++) {
            StringBuilder digitStr = new StringBuilder("");
            for (int j = i; j < str.length() && !Character.isDigit(str.charAt(j)); j++) {
                digitStr.append(str.charAt(j));
                if (isDigit(digitStr.toString())) {
                    break;
                }
            }
            switch (digitStr.toString()) {
                case "one":
                    return 1;
                case "two":
                    return 2;
                case "three":
                    return 3;
                case "four":
                    return 4;
                case "five":
                    return 5;
                case "six":
                    return 6;
                case "seven":
                    return 7;
                case "eight":
                    return 8;
                case "nine":
                    return 9;
            }
            if (!isDigit(digitStr.toString())) {
                return -1;
            }
        }
        return -1;
    }

    public static boolean isDigit(String digitStr) {
        ArrayList<String> numbersAsString = new ArrayList<>();
        numbersAsString.add("one");
        numbersAsString.add("two");
        numbersAsString.add("three");
        numbersAsString.add("four");
        numbersAsString.add("five");
        numbersAsString.add("six");
        numbersAsString.add("seven");
        numbersAsString.add("eight");
        numbersAsString.add("nine");

        return numbersAsString.indexOf(digitStr.toLowerCase()) >= 0;
    }
}