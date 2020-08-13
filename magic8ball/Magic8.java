import java.util.Random;
import java.util.Scanner;

public class Magic8 {
    static String[] responses = { "As I see it, yes.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "It is certain.",
            "It is decidedly so.",
            "Most likely.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Outlook good.",
            "Reply hazy, try again.",
            "Signs point to yes.",
            "Very doubtful.",
            "Without a doubt.",
            "Yes.",
            "Yes – definitely.",
            "You may rely on it."
    };

    static String askAgain = "yes";

    public static void main(String[] args) {
        while (askAgain == "yes") {
            askQuestion();
        }
    }

    public static void askQuestion() {
        System.out.println("What would you like to know?");
        Scanner sc = new Scanner(System.in);
        sc.nextLine();
        Random rand = new Random();
        int randInt = rand.nextInt(20);
        String answer = responses[randInt];
        System.out.println(answer);
        System.out.println("Would you like to ask something else? yes/no");
        String yOrn = sc.nextLine();
        if (!yOrn.equals("yes")) {
            askAgain = "no";
        }
    }
}
