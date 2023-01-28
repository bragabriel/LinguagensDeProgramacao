import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		
		//Criando a lista de itens
		ArrayList<Itens> listaItens = new ArrayList<Itens>();
		Itens i1 = new Itens("Glock", "30/60", 0, "Pistola inicial", "TR"); 
		Itens i2 = new Itens("USP", "30/60", 0, "Pistola inicial", "CT"); 
		Itens i3 = new Itens("AK-47", "30/90", 2700, "Rifle principal", "TR"); 
		Itens i4 = new Itens("M4A4", "30/90", 3100, "Rifle principal", "CT"); 
		Itens i5 = new Itens("AWP", "10/30", 4750, "Sniper principal", "CT/TR"); 
		Itens i6 = new Itens("Desert Eagle", "10/30", 700, "Pistola forte, 'canhão de mão'", "CT/TR"); 
		Itens i7 = new Itens("AUG", "30/60", 3300, "Rifle com lente de aproximação", "CT"); 
		Itens i8 = new Itens("SIG SG552", "30/90", 3000, "Rifle com lente de aproximação", "TR"); 
				
		listaItens.add(i1);
		listaItens.add(i2);
		listaItens.add(i3);
		listaItens.add(i4);
		listaItens.add(i5);
		listaItens.add(i6);
		listaItens.add(i7);
		listaItens.add(i8);		

		
		//Criando a lista de Jogadores da FAZE
		ArrayList<Jogadores> listaJogadoresFaze = new ArrayList<Jogadores>();
				
		Jogadores j1 = new Jogadores(listaItens);
		j1.setNome("Finn Andersen");
		j1.setNick("karrigan");
		j1.setIdade(31);
		j1.setSalario(9000);
		
		Jogadores j2 = new Jogadores(listaItens);
		j2.setNome("Olof Kajbjer");
		j2.setNick("olofmeister");
		j2.setIdade(29);
		j2.setSalario(10000);
		
		Jogadores j3 = new Jogadores(listaItens);
		j3.setNome("Håvard Nygaard");
		j3.setNick("rain");
		j3.setIdade(27);
		j3.setSalario(9000);
		
		Jogadores j4 = new Jogadores(listaItens);
		j4.setNome("Russel Van Dulken");
		j4.setNick("Twistzz");
		j4.setIdade(21);
		j4.setSalario(6000);

		Jogadores j5 = new Jogadores(listaItens);
		j5.setNome("Helvijs Saukants");
		j5.setNick("broky");
		j5.setIdade(20);
		j5.setSalario(5000);
		
		listaJogadoresFaze.add(j1);
		listaJogadoresFaze.add(j2);
		listaJogadoresFaze.add(j3);
		listaJogadoresFaze.add(j4);
		listaJogadoresFaze.add(j5);
		
		
		//Criando a lista de Jogadores da FURIA
		ArrayList<Jogadores> listaJogadoresFuria = new ArrayList<Jogadores>();
						
		Jogadores j6 = new Jogadores(listaItens);
		j6.setNome("Andrei Piovezan");
		j6.setNick("arT");
		j6.setIdade(25);
		j6.setSalario(10000);
				
		Jogadores j7 = new Jogadores(listaItens);
		j7.setNome("Yuri Santos");
		j7.setNick("yuurih");
		j7.setIdade(21);
		j7.setSalario(9000);
				
		Jogadores j8 = new Jogadores(listaItens);
		j8.setNome("Vinicius Figueiredo");
		j8.setNick("VINI");
		j8.setIdade(22);
		j8.setSalario(9000);
				
		Jogadores j9 = new Jogadores(listaItens);
		j9.setNome("Kaike Cerato");
		j9.setNick("KSCERATO");
		j9.setIdade(22);
		j9.setSalario(10000);

		Jogadores j10 = new Jogadores(listaItens);
		j10.setNome("André Abreu");
		j10.setNick("drop");
		j10.setIdade(17);
		j10.setSalario(7000);
				
		listaJogadoresFuria.add(j6);
		listaJogadoresFuria.add(j7);
		listaJogadoresFuria.add(j8);
		listaJogadoresFuria.add(j9);
		listaJogadoresFuria.add(j10);
		
		
		//Criando a lista de Jogadores da Liquid
		ArrayList<Jogadores> listaJogadoresLiquid = new ArrayList<Jogadores>();
								
		Jogadores j11 = new Jogadores(listaItens);
		j11.setNome("Gabriel Toledo");
		j11.setNick("FalleN");
		j11.setIdade(30);
		j11.setSalario(10000);
						
		Jogadores j12 = new Jogadores(listaItens);
		j12.setNome("Keith Markovic");
		j12.setNick("NAF");
		j12.setIdade(23);
		j12.setSalario(9000);
						
		Jogadores j13 = new Jogadores(listaItens);
		j13.setNome("Jonathan Jablonowski");
		j13.setNick("EliGE");
		j13.setIdade(24);
		j13.setSalario(8000);
						
		Jogadores j14 = new Jogadores(listaItens);
		j14.setNome("Jake Yip");
		j14.setNick("Stewie2K");
		j14.setIdade(23);
		j14.setSalario(9500);

		Jogadores j15 = new Jogadores(listaItens);
		j15.setNome("Michael Wince");
		j15.setNick("Grim");
		j15.setIdade(20);
		j15.setSalario(7000);
						
		listaJogadoresLiquid.add(j11);
		listaJogadoresLiquid.add(j12);
		listaJogadoresLiquid.add(j13);
		listaJogadoresLiquid.add(j14);
		listaJogadoresLiquid.add(j15);
				
		
		//Criando uma lista com todos os Times:
		ArrayList<Times> listaTimes = new ArrayList<Times>();
		
		//Criando 3 times: Faze, Furia e Liquid
		Times t1 = new Times("FaZe", 6, "Robert 'RobbaN' Dahlstrom", listaJogadoresFaze);
		Times t2 = new Times("FURIA", 17, "Nicholas 'guerri' Nogueira", listaJogadoresFuria);
		Times t3 = new Times("Liquid", 11, "Eric 'adreN' Hoag", listaJogadoresLiquid);
		
		listaTimes.add(t1);
		listaTimes.add(t2);
		listaTimes.add(t3);
		
		
		//Criando uma lista com todas as Partidas:
		ArrayList<Partidas> listaPartidas = new ArrayList<Partidas>();
		
		Partidas p1 = new Partidas(1, "FURIA 16 x 12 FaZe", listaItens);
		
		Partidas p2 = new Partidas(2, "Liquid 9 x 16 FURIA", listaItens);
		
		Partidas p3 = new Partidas(3, "FaZe 16 x 10 Liquid", listaItens);
		
		Partidas p4 = new Partidas(4, "FURIA 16 x 10 FaZe", listaItens);

		listaPartidas.add(p1);
		listaPartidas.add(p2);
		listaPartidas.add(p3);
		listaPartidas.add(p4);
		
		
		//Criando o campeonato:
		Campeonatos campeonato1 = new Campeonatos("ESL Pro League", "Malta", 500000, listaTimes, listaPartidas);
		
		
		
		//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		//Métodos:
		//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		System.out.print("\nTime 1: ");
		System.out.println(t1.getNome()+"\n");
		System.out.print("Couch: ");
		System.out.println(t1.getCoach()+"\n");
		System.out.println("Jogadores: ");
		t1.imprimir_jogadores();
		
		
		System.out.print("\nTime 2: ");
		System.out.println(t2.getNome()+"\n");
		System.out.print("Couch: ");
		System.out.println(t2.getCoach()+"\n");
		System.out.println("Jogadores: ");
		t2.imprimir_jogadores();
		
		
		System.out.print("\nTime 3: ");
		System.out.println(t3.getNome()+"\n");
		System.out.print("Couch: ");
		System.out.println(t3.getCoach()+"\n");
		System.out.println("Jogadores: ");
		t3.imprimir_jogadores();
		
		
		System.out.print("\n");
		System.out.println("---------------------------");
		System.out.println("Campeonato: " + campeonato1.getNome() + "\n");
		System.out.println("Local da realização do campeonato: " + campeonato1.getCidade() + "\n");
		
		System.out.println("Os times participando desse campeonato são: ");
		campeonato1.imprimirTimesCampeonato();
		
		System.out.print("\n");
		
		System.out.println("Partidas jogadas nesse campeonato: ");
		campeonato1.imprimirPartidasCampeonato();
		
		System.out.print("\n");
		
		System.out.println("Os itens liberados nesse campeonato são: ");
		System.out.print("\n");
		p1.imprimirItens();
			
		
		System.out.print("\n");
		System.out.println("---------------------------");
		System.out.println("Feed de eliminações / Status da economia\n");
		
		j6.kill();		
		j6.kill();
		j11.kill();
		j14.kill();
		j6.kill();
		j6.kill();
		j6.kill();
		
		j6.comprarAWP();
		
		j14.comprarDeagle();

	}

}
