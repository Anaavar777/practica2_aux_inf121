
package ejercicio2;
import java.util.ArrayList;
import java.util.List;
public class Main {


class Empleado {
    private String nombre;
    private String cargo;
    private double sueldo;

    public Empleado(String nombre, String cargo, double sueldo) {
        this.nombre = nombre;
        this.cargo = cargo;
        this.sueldo = sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString() {
        return nombre + " - " + cargo + " - $" + sueldo;
    }
}

class Departamento {
    private String nombre;
    private String area;
    private List<Empleado> empleados;

    public Departamento(String nombre, String area) {
        this.nombre = nombre;
        this.area = area;
        this.empleados = new ArrayList<>();
    }

    public Departamento(String nombre, String area, List<Empleado> empleados) {
        this.nombre = nombre;
        this.area = area;
        this.empleados = empleados;
    }

    public void mostrarEmpleados() {
        System.out.println("\nDepartamento: " + nombre + " (" + area + ")");
        if (empleados.isEmpty()) {
            System.out.println("   No tiene empleados.");
        } else {
            for (Empleado e : empleados) {
                System.out.println("  - " + e);
            }
        }
    }

    public void cambioSalario(double nuevoSalario) {
        for (Empleado e : empleados) {
            e.setSueldo(nuevoSalario);
        }
    }

    public boolean contieneEmpleado(Empleado e) {
        return empleados.contains(e);
    }

    public void moverEmpleadosA(Departamento otro) {
        otro.empleados.addAll(this.empleados);
        this.empleados.clear();
    }

public static void main(String[] args) {
        Main m = new Main();
        Empleado emp1 = m.new Empleado("Ana", "Desarrolladora", 5000);
        Empleado emp2 = m.new Empleado("Luis", "Diseñador", 4500);

        List<Empleado> empleadosDept1 = new ArrayList<>();
        empleadosDept1.add(emp1);
        empleadosDept1.add(emp2);

        Departamento dept1 = m.new Departamento("Tecnología", "IT", empleadosDept1);
        Departamento dept2 = m.new Departamento("Recursos Humanos", "HR");

        dept1.mostrarEmpleados();
        dept2.mostrarEmpleados();

        System.out.println("\nCambiando salario de todos los empleados del departamento de Tecnología a $6000...");
        dept1.cambioSalario(6000);
        dept1.mostrarEmpleados();

        System.out.println("\nMoviendo empleados del departamento de Tecnología al departamento de Recursos Humanos...");
        dept1.moverEmpleadosA(dept2);

        dept1.mostrarEmpleados();
        dept2.mostrarEmpleados();
    }
}
}