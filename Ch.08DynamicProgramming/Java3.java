/*
 * 호출되는 함수 확인_탑다운(Top Down) 방식 : 재귀적 구현
 */
public class Java3 {

    public static long[] arr = new long[100];

    public static long fibo(int n) {

        System.out.print(n + " ");

        if(n == 1 || n == 2) {
            return 1;
        }

        if(arr[n] != 0){
            return arr[n];
        }

        arr[n] = fibo(n - 1) + fibo(n - 2);

        return arr[n];
    }

    public static void main(String[] args) {
        fibo(6);
    }
    
}
