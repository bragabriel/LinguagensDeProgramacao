
public class AlunoGrad extends Aluno{

	private double media;
	
	public AlunoGrad(int ra, String nome, boolean matriculado, double media) {
		super(ra, nome, matriculado);	
		this.media = media;
	}
	
	public void imprimir() {
		super.imprimir();
		System.out.println("Média = " + this.media);
	}
}
