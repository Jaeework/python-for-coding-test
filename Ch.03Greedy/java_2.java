import java.util.Arrays;
import java.util.Scanner;

public class java_2 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int k = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);
        int first = arr[n - 1];
        int scnd = arr[n - 2];

        int first_cnt = m / (k + 1) * k + m % (k + 1);
        
        int result = first * first_cnt + scnd * (m - first_cnt);

        System.out.println(result);

    }

}
