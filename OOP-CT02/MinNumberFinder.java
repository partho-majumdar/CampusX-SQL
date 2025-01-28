// 3 

import java.io.*;
import java.util.*;

public class MinNumberFinder {
    public static void findMinNumber(String inputPath, String outputPath) {
        List<Double> numbers = new ArrayList<>();

        try {
            BufferedReader reader = new BufferedReader(new FileReader(inputPath));
            String line;

            while ((line = reader.readLine()) != null) {
                String[] words = line.trim().split("\\s+");

                for (String word : words) {
                    try {
                        double number = Double.parseDouble(word);
                        numbers.add(number);
                    } catch (NumberFormatException e) {
                        continue;
                    }
                }
            }
            reader.close();

            BufferedWriter writer = new BufferedWriter(new FileWriter(outputPath));
            if (!numbers.isEmpty()) {
                double minNumber = Collections.min(numbers);
                writer.write(String.valueOf(minNumber));
            } else {
                writer.write("No numbers found in input file");
            }
            writer.close();

        } catch (IOException e) {
            System.err.println("Error processing files: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        findMinNumber("input.txt", "output.txt");
    }
}