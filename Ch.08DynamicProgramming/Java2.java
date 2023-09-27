/*
 * 피보나치_메모이제이션(Memoization) 활용
 * 한 번 호출한 결과는 리스트에 저장했다가 다음 번 호출 때 활용하는 기법
 */
public class Java2 {

    public static long[] arr = new long[101];

    public static long fibo(int n) {
        if(n == 1 || n == 2) {
            return 1;
        }

        if(arr[n] != 0) {
            return arr[n];
        }

        arr[n] = fibo(n - 1) + fibo(n - 2);

        return arr[n];
    }

    public static void main(String[] args) {
        System.out.println(fibo(50));
    }
}
