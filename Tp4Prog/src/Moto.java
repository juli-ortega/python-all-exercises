public class Moto extends VehiculoTerrestre{
    public String marca;

    public Moto(char tipoDeCombustible, float cantCombustible, int cantRuedas, String marca) {
        super(tipoDeCombustible, cantCombustible, cantRuedas);
        this.marca = marca;
    }
    public Moto(){

    }

    @Override
    public float velocidadMaxima() {
        System.out.println("Estoy en la clase Moto");
        return 130;
    }

    @Override
    public float capacidadMaximaDeCarga() {
        System.out.println("Estoy en la clase Moto");
        return 200;
    }
}
