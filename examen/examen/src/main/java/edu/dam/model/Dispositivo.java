package edu.dam.model;


// Clase Dispositivo
public class Dispositivo
{
    // Atributos
    private int id;
    private String nombre;
    private String categoria;
    private Double precio;
    private int stock;

    // Constructores, vacio, con todos los parametros, sin el id
    public Dispositivo() {}

    public Dispositivo(int id, String nombre, String categoria, Double precio, int stock)
    {
        this.id = id;
        this.nombre = nombre;
        this.categoria = categoria;
        this.precio = precio;
        this.stock = stock;
    }

    public Dispositivo(String nombre, String categoria, Double precio, int stock)
    {
        this(0, nombre, categoria, precio, stock);
    }


    // Getters y toString
    public int getId() { return id; }
    public String getNombre() { return nombre; }
    public String getCategoria() { return categoria; }
    public Double getPrecio() { return precio; }
    public int getStock() { return stock; }

    @Override
    public String toString()
    {
        return String.format(
            "ID: %d, Nombre: %s, Categoria: %s, Precio : %f, Stock: %d",
            this.id,
            this.nombre,
            this.categoria,
            this.precio,
            this.stock);
    }
}
