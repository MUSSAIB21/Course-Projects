import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        //printArray();
        //minMax();
        //reverseArray();
        ArrayList<String> lame = new ArrayList<>();
        lame.add("Apple");
        lame.add("Banana");
    }

    private static void reverseArray() {
        int[] nums = {1, 2, 3, 4, 5};
        int i = 0, r = nums.length - 1;
        while (i < r) {
            int temp = nums[i];
            nums[i] = nums[r];
            nums[r] = temp;

            i++;
            r--;
        }


        System.out.println("Reversed Array: " + Arrays.toString(nums));
    }

    private static void minMax() {
        int[] numbers = {22, 12, 60, 42, 6};

        int min = numbers[0];
        int max = numbers[0];

        for (int num : numbers) {
            if (num < min) {
                min = num;
            }
            if (num > max) {
                max = num;
            }
        }

        System.out.println("Minimum value: " + min);
        System.out.println("Maximum value: " + max);
    }

    private static void printArray() {
        int[] nums = {10, 20, 30, 40, 50};
        int sum = 0;

        System.out.println("Using for loop:");
        for (int i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
            sum += nums[i];
        }
        System.out.println("\nAverage is " + sum / nums.length);

        System.out.println("\nUsing for-each loop:");
        for (int num : nums) {
            System.out.println(num);
        }
    }


    private static void palindrome() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter String ");
        String s = sc.next();
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                System.out.println("Not a palindrome");
                return;
            }
            i++;
            j--;
        }
        System.out.println("Palindrome");
    }
}