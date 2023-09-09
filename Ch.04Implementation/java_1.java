/*
 * 상하좌우
 */

import java.util.Scanner;

public class java_1 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        sc.nextLine();
        String[] moves = sc.nextLine().split(" ");

        int x = 1;
        int y = 1;

        for(String move : moves) {
            int nx = x;
            int ny = y;

            switch(move) {
                case "L" :
                    ny -= 1;
                    break;
                case "R" :
                    ny += 1;
                    break;
                case "U" :
                    nx -= 1;
                    break;
                case "D" :
                    nx += 1;
                    break;
            }
            if(nx < 1 || nx > N || ny < 1 || ny > N) {
                continue;
            } else {
                x = nx;
                y = ny; 
            }
        }

        System.out.println(x + " " + y);

    }
}
