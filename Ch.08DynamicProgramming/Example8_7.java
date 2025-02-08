// 8-7.java

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Example8_7 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        br.close();

        int[] d = new int[n+1];

        d[1] = 1;
        d[2] = 3;

        for(int i = 3; i <= n; i++) {
            d[i] = (d[i-1] + 2 * d[i-2]) % 796796;
        }

        System.out.println(d[n]);

    }
    
}
