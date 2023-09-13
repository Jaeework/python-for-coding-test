/*
 * 계수 정렬 : 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용할 수 있는 매우 빠른 정렬 알고리즘
 * 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다. (각 데이터가 몇 번 등장했는지 그 횟수가 기록된다.)
 */
public class java_6 {
    
    public static void main(String[] args) {
        int[] arr = {7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};

        int[] cnt = new int[10];

        for(int i : arr) {
            cnt[i]++;
        }

        for(int i = 0; i < cnt.length; i++) {
            for(int j = 0; j < cnt[i]; j++) {
                System.out.print(i + " ");
            }
        }
    }
}
