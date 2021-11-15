import java.util.Calendar;

public class Datas {

	private int dia;
	private int mes;
	private int ano;
	private String estacao;
		
	public void Data() {
		Calendar DataAtual = Calendar.getInstance();
	}
	
	
	
	//DIA:
	public void setDia(int dia) {
		this.dia = dia;
		
		if (this.dia>=1 && this.dia<=30) {
			System.out.println("Dia válido!");
		}
		else {
			System.out.println("Dia inválido!");
		}
	}
	
	public int getDia() {
		return this.dia;
	}
	
	
	//MES:	
	public void setMes(int mes) {
		this.mes = mes;
		
		if (this.mes>=1 && this.mes<=12) {
			System.out.println("Mês válido!");
		}
		else {
			System.out.println("Mês inválido!");
		}
	}
	
	public int getMes() {
		return this.mes;
	}
	
	
	//ANO:
	public void setAno(int ano) {
		this.ano = ano;
	}
	
	public int getAno() {
		return this.ano;
	}
	
	
	//Apresenta Data
	public void apresentaData(){
		System.out.println(Integer.toString(this.dia) + "/" + Integer.toString(this.mes) + "/" + Integer.toString(this.ano));
	}
	
	//Apresenta Data + Estação do ano
	public void apresentaData(boolean resposta){
		if(resposta = true) {
			System.out.println(Integer.toString(this.dia) + "/" + Integer.toString(this.mes) + "/" + Integer.toString(this.ano));
			
			if(this.mes == 12 || this.mes == 1 || this.mes == 2) {
				this.estacao = "Verão";
			}
			else if(this.mes>=3 && this.mes<=5) {
				this.estacao = "Outono";
			}
			else if(this.mes>=6 && this.mes<=8) {
				this.estacao = "Inverno";
			}
			else if(this.mes>=9 && this.mes<=11) {
				this.estacao = "Primavera";
			}			
			System.out.println("A estação do ano é: " + this.estacao);
		}
		else{
			System.out.println(Integer.toString(this.dia) + "/" + Integer.toString(this.mes) + "/" + Integer.toString(this.ano));
		}
	}
	
	
	//Avançar DATA para o dia seguinte
	public void avancarDia() {
		
		if(this.dia>30) {
			this.dia = 1;
			this.mes+=1;
		}
		if(this.mes>12) {
			this.mes = 1;
			this.ano+=1;
		}
		else {
			this.dia += 1;
		}		
	}
	
	
	//Avançar DATA para quantidade especifica de dias
	public void avancarQtdDias(int qtd) {
				
		if(this.dia+qtd > 30) {
			this.dia = (this.dia + qtd)%30;
			this.mes = (int)((this.dia+qtd)/30);
		} 
		if(this.mes==12) {
			this.dia = (this.dia + qtd)%30;
			this.mes = (int)((this.dia+qtd)/30);
			this.mes = 1;
			this.ano+=1;
		}
		else {
			this.dia += 1;
		}	
		
	}
	
}