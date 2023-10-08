package POO.abstracao.interfaces;

public class MainBank {

    public static void main(String[] args) {

        System.out.println("Seja bem vinde ao linux tips bank");
        ContaCorrente ccUsuario = new ContaCorrente();
        ccUsuario.consultarSaldo();
        ccUsuario.fazerPix();

        ContaPoupanca cpUsuario = new ContaPoupanca();
        cpUsuario.consultarSaldo();
        cpUsuario.fazerPix();

    }
}
