/*
 * 떡볶이 떡 만들기
 */

import java.util.Arrays;
import java.util.Scanner;

public class Java8 {

    public static int binarySearch(int[] arr, int start, int end, int target) {
        int result = 0;

        while(start <= end) {
            int mid = (start + end) / 2;
            int total = 0;

            for(int i = 0; i < arr.length; i++) {
                total += Math.max(0, arr[i] - mid);
            }

            if(total == target) {
                result = mid;
                break;
            } else if(total > target) {
                result = mid; // 적어도 m 이상의 떡을 손님이 가져가야 하기 때문에 result 값으로 임시로 넣어놓는다.
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] tteoks = new int[n];
        for(int i = 0; i < n; i++) {
            tteoks[i] = sc.nextInt();
        }

        Arrays.sort(tteoks);

        int h = binarySearch(tteoks, tteoks[0], tteoks[n - 1], m);

        System.out.println(h);

        sc.close();
    }
}
