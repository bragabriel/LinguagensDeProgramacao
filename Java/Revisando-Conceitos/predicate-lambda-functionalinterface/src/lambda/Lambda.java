package lambda;
import lambda.entity.*;
import lambda.*;

public class Lambda{
    public static void main(String[] args) {

        Cat myCat = new Cat();

//        Printable lambdaPrintable = () -> System.out.println("Meow");
//        printThing(lambdaPrintable);

        Printable lambdaPrintable = (s) -> System.out.println("Meow");
        printThing(lambdaPrintable);
    }
    static void printThing(Printable thing){
        thing.printWithEntry("@@");
    }
}


