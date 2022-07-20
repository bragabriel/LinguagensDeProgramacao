package teste;

import java.util.ArrayList;
import java.util.List;

public class teste {

	public static void main(String[] args) {
		

		substring("strawberrie");
		qtdHello();
		
	}
	
	public static void substring(String st) {
		
		st = "strawberries";
		
		System.out.println(st.substring(2,5));
	}
	
	public static void qtdHello() {
		for(int i=0; i<10; i=i++) {
			i+=1;
			System.out.println("Hello World!");
		}
		
		int j = 0;
		j = j++;
		System.out.println(j); 
	}

	
	
}
