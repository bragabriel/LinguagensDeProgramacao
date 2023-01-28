public class Fogao {
	
	private String marca;
	private Aquecedor aquecedor;
	private Tampa tampa;
	private Forno forno;
	private Painel painel;

	
	public Fogao(String marca, boolean aquecedor, String tampa, boolean forno, int painel) {
	
			this.marca = marca;
						
			this.aquecedor = new Aquecedor();
			this.aquecedor.setAquecedor(aquecedor);
			
			this.tampa = new Tampa();
			this.tampa.setMaterial(tampa);
			
			this.forno = new Forno();
			this.forno.setForno(forno);
			
			this.painel = new Painel();
			this.painel.setQtdBocas(painel);
			
			
		}		
		
	public String getMarca() {
		return marca;
	}
	public void setMarca(String marca) {
		this.marca = marca;
	}
	
	public void imprimir() {
		System.out.println("Marca do fogão: " + this.marca);
		System.out.println("Aquecedor: " + this.aquecedor.isAquecedor());
		System.out.println("Material da tampa: " + this.tampa.getMaterial());
		System.out.println("Tem forno embutido: " + this.forno.isForno());
		System.out.println("Quantidade de bocas do painel: " + this.painel.getQtdBocas());
		System.out.println("Tem botão: " + this.painel.getBotao().isBtnFaisca());
	}

}
