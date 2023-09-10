/*
*  stack
*/

import java.util.Stack;

public class java_1 {

    public static void main(String[] args) {
        Stack<Integer> st = new Stack<Integer>();

        st.push(5);
        st.push(2);
        st.push(3);
        st.push(7);
        st.pop();
        st.push(1);
        st.push(4);
        st.pop();

        while(!st.isEmpty()) {
            System.out.print(st.peek() + " ");
            st.pop();
        }

    }
    
}
