/*
 * 위에서 아래로
 */

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class java10 {
    
    public static int n;
    public static Integer[] arr;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        arr = new Integer[n];

        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        sc.close();

        Arrays.sort(arr,Collections.reverseOrder());
        
        for(int i : arr) {
            System.out.print(i + " ");
        }
    }
}