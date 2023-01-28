package ex07_Prova_AgenciaBancaria;

public class Diretores {

	private String nome;
	private int cpf;
	private double salario;
	private boolean acessoGeracaoRelatorios;
	private int nrGerentes;
	private double salarioFinal;
	
	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public int getCpf() {
		return cpf;
	}
	
	public void setCpf(int cpf) {
		this.cpf = cpf;
	}
	
	public double getSalario() {
		return salario;
	}
	
	public void setSalario(int salario) {
		this.salario = salario;
	}
	
	public boolean isAcessoGeracaoRelatoriso() {
		return acessoGeracaoRelatorios;
	}
	
	public void setAcessoGeracaoRelatoriso(boolean acessoGeracaoRelatorios) {
		this.acessoGeracaoRelatorios = acessoGeracaoRelatorios;
	}
	
	public int getNrGerentes() {
		return nrGerentes;
	}
	
	public void setNrGerentes(int nrGerentes) {
		this.nrGerentes = nrGerentes;
	}
	
	public void imprimirInformacoes() {
		System.out.println("Cargo: Diretor");
		System.out.println("Nome: " + this.nome);
		System.out.println("Cpf: " + this.cpf);
		System.out.println("Tem acesso a geração de relátórios? " + this.acessoGeracaoRelatorios);
		System.out.println("Número de gerentes: " + this.nrGerentes);
		System.out.println("Salario inicial: $" + this.salario + "\n");
	}
	
	public void salarioFinal(){
		
		this.salarioFinal = this.salario + (this.salario * 0.2);
		System.out.println("O salário do(a) Diretor(a) " + this.nome + " antes da porcentagem era: $" + this.salario);
		System.out.println("20% do seu salário: " + (this.salario * 0.2));
		System.out.println("Seu novo salário com 20% incluso é de: $" + this.salarioFinal + "\n");		
	}	
}