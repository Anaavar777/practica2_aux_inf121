package ejercicio4;

class Ropa {
    private String tipo;
    private String material;

    public Ropa(String tipo, String material) {
        this.tipo = tipo;
        this.material = material;
    }

    public String getTipo() {
        return tipo;
    }

    public String getMaterial() {
        return material;
    }

    @Override
    public String toString() {
        return "Ropa{" + "tipo='" + tipo + "', material='" + material + "'}";
    }
}


class Ropero {
    private String material;
    private Ropa[] ropas;
    private int nroRopas;

    public Ropero(String material) {
        this.material = material;
        this.ropas = new Ropa[20];
        this.nroRopas = 0;
    }

    public boolean agregarRopa(Ropa r) {
        if (nroRopas < 20) {
            ropas[nroRopas] = r;
            nroRopas++;
            return true;
        }
        return false;
    }

    public void eliminarPorMaterial(String mat) {
        for (int i = 0; i < nroRopas; i++) {
            if (ropas[i].getMaterial().equalsIgnoreCase(mat)) {
                ropas[i] = ropas[nroRopas - 1]; 
                nroRopas--;
                i--;
            }
        }
    }

    public void eliminarPorTipo(String tipo) {
        for (int i = 0; i < nroRopas; i++) {
            if (ropas[i].getTipo().equalsIgnoreCase(tipo)) {
                ropas[i] = ropas[nroRopas - 1];
                nroRopas--;
                i--;
            }
        }
    }

    // d1) Mostrar prendas de material X
    public void mostrarPorMaterial(String mat) {
        System.out.println("\nPrendas de material " + mat + ":");
        for (int i = 0; i < nroRopas; i++) {
            if (ropas[i].getMaterial().equalsIgnoreCase(mat)) {
                System.out.println(ropas[i]);
            }
        }
    }

    // d2) Mostrar prendas de tipo X
    public void mostrarPorTipo(String tipo) {
        System.out.println("\nPrendas de tipo " + tipo + ":");
        for (int i = 0; i < nroRopas; i++) {
            if (ropas[i].getTipo().equalsIgnoreCase(tipo)) {
                System.out.println(ropas[i]);
            }
        }
    }

    public void mostrar() {
        System.out.println("\nContenido del ropero:");
        for (int i = 0; i < nroRopas; i++) {
            System.out.println(ropas[i]);
        }
    }
}


public class Main {
    public static void main(String[] args) {

        Ropero ropero = new Ropero("Madera");

        ropero.agregarRopa(new Ropa("Camisa", "Algodón"));
        ropero.agregarRopa(new Ropa("Pantalón", "Jean"));
        ropero.agregarRopa(new Ropa("Chaqueta", "Cuero"));
        ropero.agregarRopa(new Ropa("Remera", "Algodón"));
        ropero.agregarRopa(new Ropa("Pollera", "Seda"));
        ropero.mostrar();
        ropero.mostrarPorMaterial("Algodón");
        ropero.mostrarPorTipo("Chaqueta");
        System.out.println("\nEliminando prendas de material 'Algodón'...");
        ropero.eliminarPorMaterial("Algodón");
        ropero.mostrar();

        System.out.println("\nEliminando prendas de tipo 'Jean'...");
        ropero.eliminarPorTipo("Jean");

        ropero.mostrar();
    }
}

