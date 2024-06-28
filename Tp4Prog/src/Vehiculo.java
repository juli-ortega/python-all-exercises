public abstract class Vehiculo implements Potencia{
    public char tipoDeCombustible;
    public float cantCombustible;

    public abstract float velocidadMaxima();

    public void mostrarAtributos(){
        System.out.println("Tipo de combustible: " + this.tipoDeCombustible);
        System.out.println("Cantidad de combustible: " + this.cantCombustible + "L");
    }

    public Vehiculo() {
    }

    public Vehiculo(char tipoDeCombustible, float cantCombustible) {
        this.tipoDeCombustible = tipoDeCombustible;
        this.cantCombustible = cantCombustible;
    }

    public void desdePotencia(int pos, int cant){
        System.out.println("Combustible elegido es: " + Potencia.tipoCombustible[pos]);
        System.out.println("Cantidad de combustible: " + cant);

    }
}
