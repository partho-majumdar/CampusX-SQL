// 1(b)

import java.util.InputMismatchException;
import java.util.Scanner;

public class ExceptionHandling {
    private int[] myArray;

    public ExceptionHandling(int size) {
        myArray = new int[size];
    }

    public void insertValue(int index, int value) {
        try {
            myArray[index] = value;
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Type A Exception occurred!");
        } catch (InputMismatchException e) {
            System.out.println("Type B Exception occurred!");
        } catch (Exception e) {
            System.out.println("Some other exception occurred!");
        } finally {
            System.out.println("Exception handling is amazing");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter Array Size: ");
        int size = scanner.nextInt();

        ExceptionHandling exceptionHandling = new ExceptionHandling(size);

        System.out.print("Enter index position: ");
        int index = scanner.nextInt();

        System.out.print("Enter value to insert: ");
        try {
            int value = scanner.nextInt();
            exceptionHandling.insertValue(index, value);
        } catch (InputMismatchException e) {
            System.out.println("Type B Exception occurred!");
            System.out.println("Exception handling is amazing");
        } finally {
            scanner.close();
        }
    }
}