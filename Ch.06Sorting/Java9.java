/*
 * key를 활용한 소스코드
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Fruit implements Comparable<Object> {
    private String name;
    private int score;

    public Fruit(String name, int score) {
        this.name = name;
        this.score = score;
    }

    public String getName() {
        return this.name;
    }

    public int getScore() {
        return this.score;
    }

    @Override
    public int compareTo(Object other) {
        Fruit o = (Fruit) other;

        /*1이면 앞의 인자가 더 큰 값
		 * 0이면 값은값
		 * -1이면 뒤의 인자가 더 큰값
		 */
        if(this.score < o.score) {
            return -1;
        }

        return 1;
    }
}

public class Java9 {

    public static void main(String[] args) {
        List<Fruit> fruits = new ArrayList<Fruit>();
        fruits.add(new Fruit("바나나", 2));
        fruits.add(new Fruit("사과", 5));
        fruits.add(new Fruit("당근", 3));

        Collections.sort(fruits);
        for(int i = 0; i < fruits.size(); i++) {
            System.out.print("(" + fruits.get(i).getName() + ", " + fruits.get(i).getScore() + ") ");
        }
    }
    
}
