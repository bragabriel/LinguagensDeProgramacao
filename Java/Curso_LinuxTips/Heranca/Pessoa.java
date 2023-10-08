package Heranca;

public class Pessoa {

    public static void main(String[] args) {

        PessoaDesenvolvedoraBackend pessoaDesenvolderaBackend =
                new PessoaDesenvolvedoraBackend("gabrielbackend", "java e spring", 1000000.0);
        pessoaDesenvolderaBackend.codar();

        PessoaDesenvolvedoraFrontend pessoaDesenvolvedoraFrontend =
                new PessoaDesenvolvedoraFrontend("gabrielfrontend", "react e angular", 1000000.0);
        pessoaDesenvolvedoraFrontend.codar();
    }
}
