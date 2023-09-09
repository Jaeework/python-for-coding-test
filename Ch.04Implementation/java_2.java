/*
 * 시각
 */

import java.util.Scanner;

public class java_2 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int cnt = 0;

        for(int i = 0; i <= n; i++) {
            for(int j = 0; j < 60; j++) {
                for(int h = 0; h < 60; h++) {
                    if((""+ i + j + h).contains("3")) {
                        cnt++;
                    }
                }
            }
        }

        System.out.println(cnt);
    }
}
