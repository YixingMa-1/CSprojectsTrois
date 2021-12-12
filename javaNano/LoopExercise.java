package javaNano;

public class LoopExercise {

    public static void main(String[] args) {

        int[] numbers = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        // Add for Loop Here
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        // Add while Loop Here
        int index = 0;
        while (index < numbers.length) {
            System.out.println(numbers[index]);
            index++;
        }

        // Add Do while Loop Here
        int counter = 0;
        do {
            System.out.println(numbers[counter]);
            counter++;
        } while (counter < numbers.length);

    }

}