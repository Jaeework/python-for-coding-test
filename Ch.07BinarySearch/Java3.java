/*
 * 이진 탐색_반복문
 */

import java.util.Arrays;
import java.util.Scanner;

public class Java3 {
    
    public static int binarySearch(int[] arr, int start, int end, int target) {
        while(start <= end) {
            int mid = (start + end) / 2;

            if(arr[mid] == target) {
                return mid;
            } else if(arr[mid] > target) {
                end = mid - 1;
            } else if(arr[mid] < target) {
                start = mid + 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int target = sc.nextInt();

        int[] arr = new int[n];
        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        
        sc.close();
        
        Arrays.sort(arr);

        int result = binarySearch(arr, 0, n - 1, target);

        if(result == -1) {
            System.out.println("원소가 존재하지 않습니다.");
        } else {
            System.out.println(result + 1);
        }
    }
}
