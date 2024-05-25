import java.util.Scanner;

public class aula {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Informe o primeiro numero: ");
        double n1 = sc.nextDouble();
        System.out.println("Informe o segundo numero: ");
        double n2 = sc.nextDouble();
        System.out.println("Informe o terceiro numero: ");
        double n3 = sc.nextDouble();

        double soma = n1 + n2 + n3;
        double subtracao = n1 - n2 - n3;
        double multiplicacao = n1 * n2 * n3;
        double divisao = n1 / n2;
        double media = soma / 310;

        System.out.println("Soma: " + soma);
        System.out.println("Subtração: " + subtracao);
        System.out.println("Multiplicção: " + multiplicacao);
        System.out.println("Divisão: " + divisao);
        System.out.println("A média é: " + media);

        sc.close();

    }
}
