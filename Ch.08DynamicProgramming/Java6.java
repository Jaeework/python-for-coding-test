/*
 * 개미 전사
 */

import java.util.Scanner;

public class Java6 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int[] arr = new int[n + 1];
        int[] d = new int[n + 1];

        for(int i = 1; i <= n; i++) {
            arr[i] = sc.nextInt();
        }

        d[1] = arr[1];
        d[2] = Math.max(arr[1], arr[2]);

        for(int i = 3; i < n + 1; i++) {
            d[i] = Math.max(d[i - 1], d[i - 2] + arr[i]);
        }

        System.out.println(d[n]);
        sc.close();
        
    }

}
