/*
 * 두 배열의 원소 교체
 */

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Java12 {

    public static int n, k;
    public static Integer[] A;
    public static Integer[] B;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        k = sc.nextInt();

        A = new Integer[n];
        B = new Integer[n];

        for(int i = 0; i < n; i++) {
            A[i] = sc.nextInt();
        }

        for(int i = 0; i < n; i++) {
            B[i] = sc.nextInt();
        }

        sc.close();

        Arrays.sort(A);
        Arrays.sort(B, Collections.reverseOrder());

        for(int i = 0, cnt = 0; i < n; i++) {
            if(A[i] < B[i] && cnt < k) {
                int temp = A[i];
                A[i] = B[i];
                B[i] = temp;
                cnt++;
            }
        }

        int result = 0;
        for(int i : A) {
            result += i;
        }

        System.out.println(result);

    }
}
