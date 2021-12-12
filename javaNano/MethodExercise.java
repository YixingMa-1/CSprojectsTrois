package javaNano;

public class MethodExercise{

    public static void main(String[] args){
        System.out.println("The first product is: " + MethodExercise.multiplyNumbers(7,7));
        System.out.println("The second product is: " + MethodExercise.multiplyNumbers(2,3));
    }

    public static int multiplyNumbers(int num1, int num2) {
        return num1 * num2;
    }

}
