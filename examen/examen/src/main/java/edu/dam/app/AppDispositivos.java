package edu.dam.app;

import java.util.List;
import java.util.Scanner;

import edu.dam.dao.DispositivosDAO;
import edu.dam.model.Dispositivo;
import edu.dam.util.DatabaseConnector;

public class AppDispositivos 
{
    // El Scanner y el DAO para que todas las funciones puedan acceder
    private static final Scanner scan = new Scanner(System.in);
    private static final DispositivosDAO dao = new DispositivosDAO();

    // Funcion que gestiona el añadir dispositivos, recoge los datos y lo manda a la funcion del dao
    private static void addDispositivo()
    {
        System.out.print("Nombre: ");
        String nombre = scan.nextLine();
        System.out.print("\nCategoria: ");
        String categoria = scan.nextLine();
        System.out.print("\nPrecio: ");
        Double precio = scan.nextDouble();
        System.out.print("\nStock: ");
        int stock = scan.nextInt();

        try
        {
            dao.insertarDispositivo(new Dispositivo(nombre, categoria, precio, stock));
        }
        catch (Exception e)
        {
            System.err.println(e);
        }
    }

    // Funcion que gestiona la opcion de listarDispositivos, llama a la funcion del DAO y muestra el resultado
    private static void listDispositivos()
    {
        try
        {
            List<Dispositivo> list = dao.listarDisposivos();
            int i = 0;
            while (i < list.size())
            {
                System.out.println(list.get(i).toString());
                i++;
            }
        }
        catch (Exception e)
        {
            System.err.println(e);
        }
    }

    // Funcion que gestiona la opcion de buscarCategoria, recoge los datos y lo manda a la funcion del DAO
    private static void buscarCategoria()
    {
        System.out.print("Categoria: ");
        String categoria = scan.nextLine();
        System.out.print("\nPrecio minimo: ");
        Double minimo = scan.nextDouble();
        System.out.print("\nPrecio maximo: ");
        Double maximo = scan.nextDouble();

        try
        {
            List<Dispositivo> list = dao.buscarPorCategoriayRangoPrecio(categoria, minimo, maximo);
            int i = 0;
            while (i < list.size())
            {
                System.out.println(list.get(i).toString());
                i++;
            }
        }
        catch (Exception e)
        {
            System.err.println(e);
        }
    }

    // Funcion que gestiona la opcion de actualizar el Dispositivo, recoge los datos y lo manda a la funcion del DAO
    private static void actualizarPrecio()
    {
        System.out.print("ID: ");
        int id = scan.nextInt();
        scan.nextLine();
        System.out.print("Nombre: ");
        String nombre = scan.nextLine();
        System.out.print("\nCategoria: ");
        String categoria = scan.nextLine();
        System.out.print("\nPrecio: ");
        Double precio = scan.nextDouble();
        System.out.print("\nStock: ");
        int stock = scan.nextInt();

        try
        {
            dao.actualizarDispositivo(new Dispositivo(id, nombre, categoria, precio, stock));
        }
        catch (Exception e)
        {
            System.err.println(e);
        }
    }


    // Funcion que gestiona la opcion de eliminar un dispositivo, recoge los datos y lo manda a la funcion del DAO
    private static void eliminarDispositivo()
    {
        System.out.print("ID: ");
        int id = scan.nextInt();

        try
        {
            dao.eliminarDispositivo(id);
        }
        catch (Exception e)
        {
            System.err.println(e);
        }
    }


    // Funcion que echa a andar el menu y recoge las opciones
    private static void menu()
    {
        try
        {
            while (true)
            {
                System.out.println();
                System.out.println("1. Añadir Dispositivo");
                System.out.println("2. Listar Dispositivos");
                System.out.println("3. Buscar Categoria");
                System.out.println("4. Actualizar precio/stock");
                System.out.println("5. Elimnar Dispositivo");
                System.out.println("6. Salir");
                int input = scan.nextInt();
                scan.nextLine();
                switch (input) {
                    case 1:
                        addDispositivo();
                        break;
                    case 2:
                        listDispositivos();
                        break;
                    case 3:
                        buscarCategoria();
                        break;
                    case 4:
                        actualizarPrecio();
                        break;
                    case 5:
                        eliminarDispositivo();
                        break;
                    case 6:
                        return ;
                    default:
                        System.out.println("Bad Opction, try again");
                        break;
                }
            }
        }
        catch (Exception e)
        {
            System.err.println(e);
        }
    }

    // Main
    public static void main( String[] args )
    {
        System.out.println("Welcome to Manager \"Dispositivos\"");
        DatabaseConnector.inicializar();
        menu();

        System.out.println("Bye! Have a good day <3");
        scan.close();
    }
}
