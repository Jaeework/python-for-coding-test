/*
 * 보텀업(Bottom Up) 방식 : 단순 반복문 사용
 */
public class Java4 {

    public static long[] arr = new long[100];

    public static void main(String[] args) {
        
        int n = 50;

        arr[1] = 1;
        arr[2] = 2;

        for(int i = 3 ; i <= n; i++) {
            arr[i] = arr[i - 1] + arr[i - 2];
        }

        System.out.println(arr[50]);
    }
    
}
