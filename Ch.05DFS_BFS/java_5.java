/*
 * factorial
 */
public class java_5 {
    
    public static int factorialInterative(int n) {
        int result = 1;

        for(int i = 1; i <= n; i++) {
            result *= i;
        }

        return result;
    }

    public static int factorialRecursive(int n) {
        if(n <= 1) {return 1;}

        return n * factorialInterative(n - 1);
    }

    public static void main(String[] args) {
        System.out.println("반복적으로 구현 : " + factorialInterative(5));
        System.out.println("재귀적으로 구현 : " + factorialRecursive(5));
    }
}
