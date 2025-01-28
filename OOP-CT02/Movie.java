// 2(a)

class MovieTheater {
    int availableSeats;

    MovieTheater(int s) {
        availableSeats = s;
    }

    public synchronized int bookTickets(int numOFseats) {
        int numOfTicketsBooked = 0;
        for (int i = 1; i <= numOFseats; i++) {
            if (availableSeats > 0) {
                availableSeats--;
                numOfTicketsBooked++;
            }
        }
        return numOfTicketsBooked;
    }
}

class User extends Thread {
    MovieTheater m;
    int numOfTickets;

    User(MovieTheater m, int numOfTickets, String name) {
        super(name);
        this.m = m;
        this.numOfTickets = numOfTickets;
    }

    public void run() {
        int booked = m.bookTickets(numOfTickets);
        System.out.println(getName() + " has booked " + booked + " tickets");
    }
}

public class Movie {
    public static void main(String[] args) {
        MovieTheater theater = new MovieTheater(15);

        User mina = new User(theater, 6, "Mina");
        User nabil = new User(theater, 5, "Nabil");
        User farhan = new User(theater, 4, "Farhan");

        mina.start();
        nabil.start();
        farhan.start();

        try {
            mina.join();
            nabil.join();
            farhan.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Available tickets: " + theater.availableSeats);
    }
}
