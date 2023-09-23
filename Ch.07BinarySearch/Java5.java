/*
 * 부품 찾기
 */

import java.util.Arrays;
import java.util.Scanner;

public class Java5 {

    public static int n, m;
    public static int[] stock, targets;

    public static int binarySearch(int start, int end, int target, int[] arr) {
        if(start > end) { return -1; }
        int mid = (start + end) / 2;

        if(arr[mid] == target) {return mid;}
        else if(arr[mid] > target) {
            return binarySearch(0, mid - 1, target, arr);
        } else if(arr[mid] < target) {
            return binarySearch(mid + 1, end, target, arr);
        }

        return -1;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        
        stock = new int[n];
        for(int i = 0; i < n; i++) {
            stock[i] = sc.nextInt();
        }

        Arrays.sort(stock);

        m = sc.nextInt();
        targets = new int[m];
        for(int i = 0; i < m; i++) {
            targets[i] = sc.nextInt();
        }

        for(int i = 0; i < m; i++) {
            int result = binarySearch(0, n - 1, targets[i], stock);
            if(result != -1) {
                System.out.print("yes ");
            } else {
                System.out.print("no ");
            }
        }

        sc.close();

    }
}
