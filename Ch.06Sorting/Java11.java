/*
 * 성적이 낮은 순서로 학생 출력하기
 */

import java.util.Arrays;
import java.util.Scanner;

class Student implements Comparable<Student>{

    private String name;
    private int score;

    public Student(String name, int score) {
        this.name = name;
        this.score = score;
    }

    public String getName(){
        return this.name;
    }

    public int getScore(){
        return this.score;
    }

    @Override
    public int compareTo(Student other) {
        // 성적 낮은 순서대로 출력
        if(other.score > this.score) {
            return -1;
        }

        return 1;
    }
}

public class Java11 {

    public static int n;
    public static Student[] students;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        students = new Student[n];

        for(int i = 0; i < n; i++) {
            students[i] = new Student(sc.next(), sc.nextInt());
        }
        sc.close();

        Arrays.sort(students);

        for(Student std : students) {
            System.out.print(std.getName() + " ");
        }
    }
}
