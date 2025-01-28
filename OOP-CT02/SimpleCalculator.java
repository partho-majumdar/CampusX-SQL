// 4

import javax.swing.*;
import java.awt.*;

public class SimpleCalculator extends JFrame {
    private JLabel outputLabel = new JLabel("10");
    private JTextField inputField = new JTextField(10);

    public SimpleCalculator() {
        setTitle("Calculator");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

        JButton performButton = new JButton("Perform");
        performButton.addActionListener(e -> calculate());

        add(outputLabel);
        add(inputField);
        add(performButton);

        pack();
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private void calculate() {
        try {
            String[] parts = inputField.getText().trim().split("\\s+");
            if (parts.length != 2)
                throw new IllegalArgumentException("Invalid format!");

            int outputValue = Integer.parseInt(outputLabel.getText());
            int number = Integer.parseInt(parts[1]);

            int result = switch (parts[0]) {
                case "+" -> outputValue + number;
                case "-" -> outputValue - number;
                case "*" -> outputValue * number;
                case "/" -> {
                    if (number == 0)
                        throw new ArithmeticException("Cannot divide by zero!");
                    yield outputValue / number;
                }
                default -> throw new IllegalArgumentException("Unknown operator!");
            };

            outputLabel.setText(String.valueOf(result));
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(this, "Invalid input! Use format: + 5", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(SimpleCalculator::new);
    }
}