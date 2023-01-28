package ex07_Prova_AgenciaBancaria;

public class Main {

	public static void main(String[] args) {
		
	Funcionarios f1 = new Funcionarios();

	Gerentes g1 = new Gerentes();
	
	Diretores d1 = new Diretores();
	
	f1.setNome("Douglas");
	f1.setCpf(484798904);
	f1.setSalario(4000);
	
	g1.setNome("Giovana");
	g1.setCpf(987283882);
	g1.setSalario(7000);
	g1.setSenha(123);
	g1.setNrFuncionarios(1);
	
	d1.setNome("Gabriel");
	d1.setCpf(468343089);
	d1.setSalario(10000);
	d1.setAcessoGeracaoRelatoriso(true);
	d1.setNrGerentes(1);
	
	f1.imprimirInformacoes();
	f1.salarioFinal();
	
	g1.imprimirInformacoes();
	g1.salarioFinal();
	
	d1.imprimirInformacoes();
	d1.salarioFinal();
	}
}