import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Moto moto = new Moto('N',12,2,"Honda");
        System.out.println("Clase: " + moto.getClass());
        System.out.println("Velocidad maxima: " + moto.velocidadMaxima());
        System.out.println("Capacidad maxima de carga: " + moto.capacidadMaximaDeCarga());
        /*
        while (true){
            System.out.println("Seleccione el combustible: (1 al 6)");
            int eleccion = sc.nextInt();
            if (eleccion<1 || eleccion>6){
                System.out.println("Error vuelva a intentarlo. Debe ser del 1 al 6");
            }else{
                System.out.println("Indique cuanto combustible posee: ");
                int capComb = sc.nextInt();
                moto.desdePotencia(eleccion, capComb);
                break;
            }
        }
         */
    }
}