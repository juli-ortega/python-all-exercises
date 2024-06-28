public class Coche extends VehiculoTerrestre{
    public String modelo;

    public Coche(char tipoDeCombustible, float cantCombustible, int cantRuedas, String modelo) {
        super(tipoDeCombustible, cantCombustible, cantRuedas);
        this.modelo = modelo;
    }

    @Override
    public float velocidadMaxima() {
        return 0;
    }

    @Override
    public float capacidadMaximaDeCarga() {
        return 500;
    }
}
