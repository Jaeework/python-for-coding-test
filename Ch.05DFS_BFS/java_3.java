/*
 * 재귀 함수
 */
public class java_3 {
    
    public static void recurciveFunc(){
        System.out.println("재귀 함수를 호출합니다.");
        recurciveFunc();
    }


    public static void main(String[] args) {
        recurciveFunc();
    }

}
