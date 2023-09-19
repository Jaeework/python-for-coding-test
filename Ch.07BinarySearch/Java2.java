/*
 * 이진 탐색 : 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교.
 * 데이터가 이미 정렬되어 있는 상태에서 효율적.
 */

import java.util.Arrays;
import java.util.Scanner;

public class Java2 {

    public static int binarySearch(int[] arr, int start, int end, int target) {
        if(start > end) {
            return -1;
        }

        int mid = (start + end) / 2;

        if(arr[mid] == target) {
            return mid;
        } else if(arr[mid] > target) {
            return binarySearch(arr, 0, mid - 1, target);
        } else if(arr[mid] < target) {
            return binarySearch(arr, mid + 1, end, target);
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
        
        Arrays.sort(arr);

        int result = binarySearch(arr, 0, n - 1, target);

        if(result == -1) {
            System.out.println("원소가 존재하지 않습니다.");
        } else {
            System.out.println(result + 1);
        }
    }
    
}
