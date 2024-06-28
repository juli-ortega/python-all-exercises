public class Avion extends VehiculoAereo{

    public int cantPasajeros;

    public Avion(char tipoDeCombustible, float cantCombustible, int cantPasajeros) {
        super(tipoDeCombustible, cantCombustible);
        this.cantPasajeros = cantPasajeros;
    }

    @Override
    public float velocidadMaxima() {
        return 0;
    }

    @Override
    public float capacidadMaximaDeCarga() {
        return 10000;
    }
}
