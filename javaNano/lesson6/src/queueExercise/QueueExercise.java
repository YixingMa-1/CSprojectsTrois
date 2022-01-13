package queueExercise;

import java.util.Queue;
import java.util.LinkedList;
public class QueueExercise {
    public static void main(String[] args) {
        Queue<String> queuedCustomers = new LinkedList<>();
        queuedCustomers.add("1234");
        queuedCustomers.add("3412");
        queuedCustomers.add("0123");
        queuedCustomers.add("4321");

        while (!queuedCustomers.isEmpty()) {
            System.out.println("Customer " + queuedCustomers.poll() + " is getting helped");
        }
    }
}
