// 2(b)

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Appliance {
    String name, category;
    double powerConsumption;

    Appliance(String n, String c, double d) {
        name = n;
        category = c;
        powerConsumption = d;
    }

    public String toString() {
        return name + " " + category + " " + powerConsumption;
    }
}

class ApplianceTest {
    public static void main(String[] args) {
        ArrayList<Appliance> appliances = new ArrayList<>();

        appliances.add(new Appliance("Television", "Entertainment", 150));
        appliances.add(new Appliance("Washing machine", "Laundry", 2000));
        appliances.add(new Appliance("Refrigerator", "Kitchen", 100));

        System.out.println("Kitchen Appliances:");
        for (Appliance appliance : appliances) {
            if (appliance.category.equalsIgnoreCase("Kitchen")) {
                System.out.println(appliance);
            }
        }

        Collections.sort(appliances, new Comparator<Appliance>() {
            @Override
            public int compare(Appliance a1, Appliance a2) {
                return Double.compare(a2.powerConsumption, a1.powerConsumption);
            }
        });

        if (!appliances.isEmpty()) {
            Appliance highestPowerAppliance = appliances.get(0);
            Appliance lowestPowerAppliance = appliances.get(appliances.size() - 1);

            System.out.println("Appliance with highest power consumption: " + highestPowerAppliance);
            System.out.println("Appliance with lowest power consumption: " + lowestPowerAppliance);
        }
    }
}