/*
 * 부품 찾기_Set 이용
 */

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Java7 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        Set<Integer> stockSet = new HashSet<Integer>();
        
        for(int i = 0; i < n; i++) {
            stockSet.add(sc.nextInt());
        }

        int m = sc.nextInt();
        int[] targets = new int[m];
        for(int i = 0; i < m; i++) {
            targets[i] = sc.nextInt();
        }

        for(int i = 0; i < m; i++) {
            if(stockSet.contains(targets[i])) {
                System.out.print("yes ");
            } else {
                System.out.print("no ");
            }
        }

        sc.close();
    }
    
}
