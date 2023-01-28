package ex07_Prova_AgenciaBancaria;

public class Gerentes {

	private String nome;
	private int cpf;
	private double salario;
	private int senha;
	private int nrFuncionarios;
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
	
	public int getSenha() {
		return senha;
	}
	
	public void setSenha(int senha) {
		this.senha = senha;
	}
	
	public int getNrFuncionarios() {
		return nrFuncionarios;
	}
	
	public void setNrFuncionarios(int nrFuncionarios) {
		this.nrFuncionarios = nrFuncionarios;
	}	
	
	public void imprimirInformacoes() {
		System.out.println("Cargo: Gerente");
		System.out.println("Nome: " + this.nome);
		System.out.println("Cpf: " + this.cpf);
		System.out.println("Senha: " + this.senha);
		System.out.println("Número de funcionários: " + this.nrFuncionarios);
		System.out.println("Salario inicial: $" + this.salario + "\n");
	}
	
	public void salarioFinal(){
		
		this.salarioFinal = this.salario + (this.salario * 0.15);
		System.out.println("O salário do(a) Gerente " + this.nome + " antes da porcentagem era: $" + this.salario);
		System.out.println("15% do seu salário: " + (this.salario * 0.15));
		System.out.println("Seu novo salário com 15% incluso é de: $" + this.salarioFinal + "\n");		
	}
}