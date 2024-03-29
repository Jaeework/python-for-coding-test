/*
 * 선택 정렬 : 가장 작은 데이터를 앞으로 보내는 과정을 n - 1번 반복
 */

public class java_1 {

    public static void main(String[] args) {
        int[] array = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

        for(int i = 0; i < array.length; i++) {
            int min_idx = i;
            for(int j = i + 1; j < array.length; j++) {
                if(array[min_idx] > array[j]) {
                    min_idx = j;
                }
            }
            int temp = array[i];
            array[i] = array[min_idx];
            array[min_idx] = temp;
        }

        for(int i : array) {
            System.out.print(i + " ");
        }
    }
    
}
