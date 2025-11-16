import java.util.Stack;
import java.util.Scanner;
import java.util.ArrayList;

 class isPalindrome {
    public static boolean isPal(String str) {
        Stack<Character> stack = new Stack<>();
        String cleaned = str.replaceAll("\\s+", "").toLowerCase();

        for (char ch : cleaned.toCharArray()) {
            stack.push(ch);
        }

        StringBuilder reversed = new StringBuilder();
        while (!stack.isEmpty()) {
            reversed.append(stack.pop());
        }

        return cleaned.equals(reversed.toString());
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        if(isPal(input.nextLine())){
            System.out.println("Palindrome");
        }
        else{
            System.out.println("Not a palindrome");
        }
    }
}


class BalancedParentheses {
    public static String isBalanced(String exp) {
        Stack<Character> stack = new Stack<>();
        for (char ch : exp.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            } else if (ch == ')' || ch == '}' || ch == ']') {
                if (stack.isEmpty() || "({[".indexOf(stack.pop()) != ")}]".indexOf(ch)) {
                    return "Not Balanced";
                }
            }
        }
        return "Balanced";
    }

    public static void main(String[] args) {
        Scanner input= new Scanner(System.in);
        System.out.println(isBalanced(input.next())); // true
    }
}

class InfixPostfix {
    public static String convert(String exp) {
        Stack<Character> stack = new Stack<>();
        StringBuilder result = new StringBuilder();

        for (char ch : exp.toCharArray()) {
            if (Character.isLetterOrDigit(ch)) {
                result.append(ch);
            } else if (ch == '(') {
                stack.push(ch);
            } else if (ch == ')') {
                while (!stack.isEmpty() && stack.peek() != '(') {
                    result.append(stack.pop());
                }
                stack.pop();
            } else {
                while (!stack.isEmpty()) {
                    result.append(stack.pop());
                }
                stack.push(ch);
            }
        }

        while (!stack.isEmpty()) {
            result.append(stack.pop());
        }

        return result.toString();
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println(convert(input.next())); // ABC*+
    }
}
class T2{
    public static void main(String[] args) {
        double[] array=new double[]{1,3,5,7,9};
        ArrayList<Double> list=new ArrayList<>(10);
        list.add(1.0);
        double sum=0;
        for(double num : array) {
            sum+=num;
        }

        System.out.println(sum/array.length);
    }
}

