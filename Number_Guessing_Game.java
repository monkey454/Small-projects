import java.util.Random;
import java.util.Scanner;
import java.util.InputMismatchException;

class Number_Guessing_Game {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        Random rand = new Random();
        int random_number = rand.nextInt(100) + 1; // Generate a random number once
        boolean PlayAgain = true;

        while(PlayAgain){
            int number = 0; // Store user's guess
            int attempts = 0; // Store user's attempts
    
            System.out.println("Guess a Number Between 1 to 100: ");
    
            // Loop until the user guesses correctly
            while (true) {
                try {
                    number = scan.nextInt(); // Take user input
                    attempts++;
    
                    if (number > random_number) {
                        System.out.println("Too high! Try again.");
                    } else if (number < random_number) {
                        System.out.println("Too low! Try again.");
                    } else {
                        System.out.println("Congratulations! You guessed it right.");
                        break; // Exit loop when guessed correctly
                    }
                } catch (InputMismatchException e) {
                    System.out.println("Invalid input! Please enter a valid number.");
                    scan.next(); // Clear invalid input
                }
            }
            System.out.println("You got the correct Guess in: "+attempts+" attempts");
           
            System.out.println("Do you want to play again? (yes/no)");
            String response = scan.next();

            while(true){
                response = scan.next();
                if(response.equalsIgnoreCase("yes")||response.equalsIgnoreCase("no")){
                    break;}
                else{
                    System.out.println("Invalid Input! Please enter valid Input");
                }
            }

            if (response.equalsIgnoreCase("no")) {
                PlayAgain = false; // Stop the loop if user doesn't want to play again
                System.out.println("Thanks for playing!");
            }
            // scan.close();
        }
       
    }
}
