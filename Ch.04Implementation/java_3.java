/*
 * 왕실의 나이트
 */

import java.util.Scanner;

public class java_3 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] d = sc.nextLine().split("");

        String sy = "abcdefgh";

        int x = Integer.valueOf(d[1]);
        int y = sy.indexOf(d[0]) + 1;

        int[][] moves = {{-1, 2}, {1, 2}, {-1, -2}, {1, -2}, {2, 1}, {2, -1}, {-2, 1}, {-2, -1}};

        int cnt = 0;

        for(int[] move : moves) {
            int nx = x + move[0];
            int ny = y + move[1];

            if(nx < 1 || nx > 8 || ny < 1 || ny > 8) {continue;}
            cnt++;
        }

        System.out.println(cnt);

    }
}
