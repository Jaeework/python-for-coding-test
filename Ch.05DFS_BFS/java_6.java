/*
 *  DFS_인접 행렬
 *  2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
 */

import java.util.Arrays;

public class java_6 {

    public static final int INF = 999999999;

    public static void main(String[] args) {
        int[][] graph = {{0, 7, 5},
                        {7, 0, INF},
                        {5, INF, 0}};

        System.out.println(Arrays.deepToString(graph));
    }
}