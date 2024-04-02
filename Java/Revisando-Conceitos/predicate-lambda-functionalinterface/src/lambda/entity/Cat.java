package lambda.entity;

import lambda.Printable;

public class Cat implements Printable {
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    private String name;

//    @Override
//    public void print() {
//        System.out.println("Meow 1");
//    }

    @Override
    public void printWithEntry(String suffix) {
        System.out.println("Meow 2 + " + suffix);
    }
}


