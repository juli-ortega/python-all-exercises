public class Helicoptero extends VehiculoAereo{
    public float autonomia;

    public Helicoptero(char tipoDeCombustible, float cantCombustible, float autonomia) {
        super(tipoDeCombustible, cantCombustible);
        this.autonomia = autonomia;
    }

    @Override
    public float velocidadMaxima() {
        return 0;
    }

    @Override
    public float capacidadMaximaDeCarga() {
        return 2000;
    }
}
