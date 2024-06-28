public abstract class VehiculoTerrestre extends Vehiculo{
    public int cantRuedas;

    public VehiculoTerrestre(char tipoDeCombustible, float cantCombustible, int cantRuedas) {
        super(tipoDeCombustible, cantCombustible);
        this.cantRuedas = cantRuedas;
    }

    public VehiculoTerrestre() {
    }

    @Override
    public void mostrarAtributos() {
        super.mostrarAtributos();
        System.out.println("Cantidad de ruedas: " + this.cantRuedas);
    }

}
