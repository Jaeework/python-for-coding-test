/*
 * 삽입 정렬 : 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한 후 적절한 위치에 삽입하는 정렬
 * 자신보다 작은 데이터를 만나기 전까지 왼쪽으로 한 칸 씩 이동
 */
public class java_3 {

    public static void main(String[] args) {
        int[] array = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

        for(int i = 1; i < array.length; i++) {
            for(int j = i; j > 0; j--) {
                if(array[j - 1] > array[j]) {
                    int temp = array[j-1];
                    array[j-1] = array[j];
                    array[j] = temp;
                } else {
                    break;
                }
            }
        }

        for(int i : array) {
            System.out.print(i + " ");
        }
    }
    
}
