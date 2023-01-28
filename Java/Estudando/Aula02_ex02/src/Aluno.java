
public class Aluno {

	private String nome;
	private int ra;
	private float notaA1;
	private float notaA2;
	private float media;
	private float frequencia;
	
	//Métodos:
	public void setNome(String n) {
		this.nome = n;
	} 
	
	public void setRa(int ra) {
		this.ra = ra;
	} 
	
	public void setNotaA1(float n1) {
		this.notaA1 = n1;
	} 
	
	public void setNotaA2(float n2) {
		this.notaA2 = n2;
	} 
	
	public void CalcularMedia() {
		this.media = (this.notaA1 + (2*this.notaA2)) / 3;
	}
	
	public void setFrequencia(float freq) {
		this.frequencia = freq;
	}
	
	public float getFrequencia() {
		return frequencia;
	}
		
	public void getMedia() {
		System.out.println("A média do aluno " + this.nome + " é: " + String.format("%.2f", this.media));
	}
	
	public void situacaoAluno() {
		if(this.frequencia < 75) {
			System.out.println("Aluno está reprovado por faltas!");
		}
		else if(this.media >= 5) {
			System.out.println("Aluno está aprovado!");
		}
		else if(this.media >= 3) {
			System.out.println("Aluno está de RE!");
		}
		else {
			System.out.println("Aluno está reprovado por nota!");
		}
	}
	
	public void getDadosAluno() {
		System.out.println("\n");
		System.out.println("Aluno: " + this.nome);
		System.out.println("R.A: " + this.ra);
		System.out.println("Frequencia: " + this.frequencia);
		System.out.println("Nota A1: " + this.notaA1);
		System.out.println("Nota A2: " + this.notaA2);
		System.out.println("Média: " + String.format("%.2f", this.media));
	}
	
	
}
