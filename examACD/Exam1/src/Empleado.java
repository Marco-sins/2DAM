public class Empleado
{
    /***---------- Clase Empleado ----------***/
    private String nombre;
    private int edad;
    private String departamento;

    Empleado() {}

    Empleado(String nombre, int edad, String departamento) 
    {
        this.nombre = nombre;
        this.edad = edad;
        this.departamento = departamento;
    }

    @Override
    public String toString() 
    {
        return "Nombre: " + this.nombre + ", Edad: " + this.edad + ", Departamento: " + this.departamento;
    }
}