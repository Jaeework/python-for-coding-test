/*
 * 재귀함수 종료 조건 주기
 */
public class java_4 {

    public static void recursiveFunc(int i) {
        if(i == 100) {
            return;
        }
        System.out.println(i + "번째 재귀함수에서 " + (i + 1)  + "번째 재귀함수를 호출합니다.");
        recursiveFunc(i + 1);
        System.out.println(i + "번째 재귀함수를 종료합니다.");
    }

    public static void main(String[] args) {
        recursiveFunc(1);
    }
    
}
