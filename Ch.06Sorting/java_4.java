/*
 * 퀵 정렬 : 기준 데이터(피벗)를 설정하고 그 기준보다 큰 데이터와 작은 데이터를 교환
 */
public class java_4 {

    public static int[] arr = {5, 7, 9, 0, 3, 1, 6, 2, 4, 8};

    public static void quickSort(int start, int end) {
        if(start >= end) {return;}

        int pivot = start;
        int left = start + 1;
        int right = end;

        while(left <= right) {
            while(left <= end && arr[left] <= arr[pivot]) {
                left++;
            }
            while(right > start && arr[right] >= arr[pivot]) {
                right--;
            }

            if(left > right) {
                int temp = arr[pivot];
                arr[pivot] = arr[right];
                arr[right] = temp;
            } else {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
            }
        }

        quickSort(start, right - 1);
        quickSort(right + 1, end);

    }

    public static void main(String[] args) {
        quickSort(0, arr.length - 1);

        for(int i : arr) {
            System.out.print(i + " ");
        }
    }
    
}
