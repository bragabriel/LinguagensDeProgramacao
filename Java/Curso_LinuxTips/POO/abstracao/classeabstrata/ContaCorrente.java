package POO.abstracao.classeabstrata;

class ContaCorrente extends Conta{

    @Override
    public void consultarSaldo() {
        System.out.println("seu saldo é 1234");
    }

    @Override
    public void fazerPix() {
        System.out.println("digite o valor que voce deseja transferir");
    }
}