/*
 * 게임 개발
 */

import java.util.Scanner;

public class java_4 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int x = sc.nextInt();
        int y = sc.nextInt();
        int d = sc.nextInt();

        int[][] maps = new int[n][m];
        int[][] visited = new int[n][m];

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                maps[i][j] = sc.nextInt();
            }
        }

        visited[x][y] = 1;

        // n, e, s, w
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};

        int cnt = 0;
        int result = 1;
        while(true) {
            d -= 1;
            if(d < 0) {d = 3;}

            int nx = x + dx[d];
            int ny = y + dy[d];

            if(visited[nx][ny] == 0 && maps[nx][ny] == 0) {
                x = nx;
                y = ny;
                visited[nx][ny] = 1;
                cnt = 0;
                result++;
                continue;
            } else {
                cnt++;

                if(cnt == 4) {
                    nx = x - dx[d];
                    ny = y - dy[d];

                    if(maps[nx][ny] == 1) {break;}
                    else {
                        x = nx;
                        y = ny;
                        cnt = 0;
                    }
                }

                continue;
            }
        }

        System.out.println(result);

    }
}
