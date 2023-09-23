/*
 * 부품 찾기_계수 정렬
 */

import java.util.Scanner;

public class Java6 {

    public static void main(String[] args) {
        int[] arr = new int[1000001];

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        for(int i = 0; i < n; i++) {
            int idx = sc.nextInt();
            arr[idx]++;
        }

        int m = sc.nextInt();
        int[] targets = new int[m];
        for(int i = 0; i < m; i++) {
            targets[i] = sc.nextInt();
        }

        for(int i = 0; i < m; i++) {
            if(arr[targets[i]] != 0) {
                System.out.print("yes ");
            } else {
                System.out.print("no ");
            }
        }

        sc.close();

    }
    
}
