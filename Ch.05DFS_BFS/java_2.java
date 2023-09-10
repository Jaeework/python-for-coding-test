/*
 * queue
 */

import java.util.ArrayDeque;
import java.util.Queue;

public class java_2 {

    public static void main(String[] args) {
        Queue<Integer> q  = new ArrayDeque<Integer>();
        // Queue<Integer> q = new LinkedList<Integer>(); 사용 가능
        // 차이점 : ArrayDeque -> 스택과 큐를 합쳐 놓은 자료 구조. 앞과 뒤에서 삽입/삭제 가능
        //          LinkedList -> 반복 작업에서 현재 요소를 삭제할 때 더 유리.

        // offer : 실패 시 false 반환 , add : 실패 시 Exception 발생
        q.offer(5);
        q.offer(2);
        q.offer(3);
        q.offer(7);
        q.remove();
        // remove : 요소 제거, poll : 요소 제거 및 큐가 비었을 때 null 반환.
        q.offer(1);
        q.offer(4);
        q.remove();

        while(!q.isEmpty()) {
            System.out.print(q.poll() + " ");
        }
    }
    
}
