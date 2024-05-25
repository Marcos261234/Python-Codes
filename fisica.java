import java.util.Scanner;

public class fisica {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Qual sua altura? ");
        double altura = sc.nextDouble();
        System.out.println("Qual seu peso? ");
        double peso = sc.nextDouble();
        double IMC = altura/peso;

        System.out.println("IMC: " + IMC);
        sc.close();
    }       
}
