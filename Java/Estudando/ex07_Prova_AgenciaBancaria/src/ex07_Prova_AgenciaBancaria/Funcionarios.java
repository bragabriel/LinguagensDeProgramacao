package ex07_Prova_AgenciaBancaria;

public class Funcionarios {

	private String nome;
	private int cpf;
	private double salario;
	private double salarioFinal=0.0;
	
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
	
	public void imprimirInformacoes() {
		System.out.println("Cargo: Funcionário");
		System.out.println("Nome: " + this.nome);
		System.out.println("Cpf: " + this.cpf);
		System.out.println("Salario inicial: $" + this.salario + "\n");
	}
	
	public void salarioFinal(){
		
		this.salarioFinal = this.salario + (this.salario * 0.1);
		System.out.println("O salário do(a) funcionário(a) " + this.nome + " antes da porcentagem era: $" + this.salario);
		System.out.println("10% do seu salário: " + (this.salario * 0.1));
		System.out.println("Seu novo salário com 10% incluso é de: $" + this.salarioFinal + "\n");		
	}
		
}