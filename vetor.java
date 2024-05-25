
import java.util.ArrayList;

public class vetor {

    public static void main(String[] args) {
    ArrayList<String> nomes = new ArrayList<>();
    nomes.add("Anderson");
    nomes.add("Bob");
    nomes.add("Carol");

    System.out.println("Primeiros nomes: "+nomes);
    System.out.println(nomes.get(0));

    for(String nome : nomes){
        System.out.println(nome);
    }
    nomes.remove("bob");
    System.out.println("Apos remoção a lista é"+nomes);
    }   
}
