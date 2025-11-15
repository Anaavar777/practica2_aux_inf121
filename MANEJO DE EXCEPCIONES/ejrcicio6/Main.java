class FondosInsuficientesException extends Exception {
    public FondosInsuficientesException(String mensaje) {
        super(mensaje);
    }
}

class CuentaBancaria {
    private String numeroCuenta;
    private String titular;
    private double saldo;

    public CuentaBancaria(String numeroCuenta, String titular, double saldoInicial) {
        this.numeroCuenta = numeroCuenta;
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    public void depositar(double monto) {
        if (monto <= 0) {
            throw new IllegalArgumentException("El monto a depositar debe ser positivo.");
        }
        saldo += monto;
    }

    public void retirar(double monto) throws FondosInsuficientesException {
        if (monto > saldo) {
            throw new FondosInsuficientesException("Fondos insuficientes. Saldo disponible: " + saldo);
        }
        saldo -= monto;
    }

    public void mostrarInfo() {
        System.out.println("Número de Cuenta: " + numeroCuenta);
        System.out.println("Titular: " + titular);
        System.out.println("Saldo: " + saldo);
    }
}
public class Main {
    public static void main(String[] args) {
        
        CuentaBancaria cuenta = new CuentaBancaria("12345", "Juan Pérez", 1000);

        cuenta.mostrarInfo();
        System.out.println();

        try {
            cuenta.depositar(500);
            System.out.println("Depósito exitoso.");
        } catch (IllegalArgumentException e) {
            System.out.println("Error en depósito: " + e.getMessage());
        }

        try {
            cuenta.depositar(-200);
        } catch (IllegalArgumentException e) {
            System.out.println("Error en depósito: " + e.getMessage());
        }

        try {
            cuenta.retirar(300);
            System.out.println("Retiro exitoso.");
        } catch (FondosInsuficientesException e) {
            System.out.println("Error en retiro: " + e.getMessage());
        }

        try {
            cuenta.retirar(2000);
        } catch (FondosInsuficientesException e) {
            System.out.println("Error en retiro: " + e.getMessage());
        }

        System.out.println();
        cuenta.mostrarInfo();
    }
}
