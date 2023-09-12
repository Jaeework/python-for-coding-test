/*
 * bfs(Breadth First Search : 너비 우선 탐색)
 */

import java.util.*;

public class java_9 {
    
    public static boolean[] visited = new boolean[9];
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

    public static void bfs(int start) {
        Queue<Integer> q = new LinkedList<Integer>();

        visited[start] = true;
        q.offer(start);

        while(!q.isEmpty()) {
            int x = q.poll();
            System.out.print(x + " ");

            for(int i = 0; i < graph.get(x).size(); i++) {
                int y = graph.get(x).get(i);

                if(!visited[y]) {
                    visited[y] = true;
                    q.offer(y);
                }
            }
        }
    }

    public static void main(String[] args) {

        for(int i = 0; i < 9; i++) {
            graph.add(new ArrayList<Integer>());
        }

        // Node 1에 연결된 정보 저장
        graph.get(1).add(2);
        graph.get(1).add(3);
        graph.get(1).add(8);

        // Node 2에 연결된 정보 저장
        graph.get(2).add(1);
        graph.get(2).add(7);

        // Node 3에 연결된 정보 저장
        graph.get(3).add(4);
        graph.get(3).add(5);

        // Node 4에 연결된 정보 저장
        graph.get(4).add(3);
        graph.get(4).add(5);

        // Node 5에 연결된 정보 저장
        graph.get(5).add(3);
        graph.get(5).add(4);

        // Node 6에 연결된 정보 저장
        graph.get(6).add(7);
        
        // Node 7에 연결된 정보 저장
        graph.get(7).add(2);
        graph.get(7).add(6);
        graph.get(7).add(8);

        // Node 8에 연결된 정보 저장
        graph.get(8).add(1);
        graph.get(8).add(7);

        bfs(1);
    }
}
