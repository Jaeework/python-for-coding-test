/*
 * 순차 탐색 : 리스트 안에 있는 특정 데이터를 찾기 위해 앞에서부터 데이터를 차례대로 확인하는 방법
 */

import java.util.*;

public class Java1 {
    
    public static int sequentialSearch(List<String> arr, String target) {
        for(int i = 0; i < arr.size(); i++) {
            if(arr.get(i).equals(target)) {return i + 1;}
        }

        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.");
        int n = sc.nextInt();
        String target = sc.next();
        sc.nextLine();

        List<String> arr = new ArrayList<String>();

        System.out.println("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.");
        for(int i = 0; i < n; i++) {
            arr.add(sc.next());
        }
        
        sc.close();

        int result = sequentialSearch(arr, target);
        System.out.println(result);
    }
}
