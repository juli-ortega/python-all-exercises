public class B  extends A {
    private char a, b, c;

    public B(String h, int j, char m )
    {
        super(h,j);
        a = m;
    }
    public void inicializaCarB(char b)
    {
        this.b = b;
    }
    public void muestraCars() {
        System.out.println( a );
        System.out.println( b );
        System.out.println( c );
    }
    public int sumar(int k) {
        int auxi = ((int)b+(int)c+ super.d+k);
        return auxi;
    }
}

