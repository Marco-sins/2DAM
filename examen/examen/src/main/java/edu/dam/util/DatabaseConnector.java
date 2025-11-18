package edu.dam.util;

import java.sql.*;


// El conector a la base de datos
public class DatabaseConnector
{
    // URL a la ubicacion de la base de datos
    private static final String sqlUrl = "jdbc:sqlite:examen/src/main/resources/dispositivos.db";

    // Devuelve la conexion a la base de datos
    public static Connection getConnection() throws SQLException
    {
        return DriverManager.getConnection(sqlUrl);
    }

    // Inicializa la base de datos y la crea si no ha sido creada antes
    public static void inicializar()
    {
        String sql =    "CREATE TABLE IF NOT EXISTS dispositivos (" + 
                        "id INTEGER PRIMARY KEY AUTOINCREMENT, " + 
                        "nombre TEXT NOT NULL, " + 
                        "categoria TEXT, " + 
                        "precio REAL, " + 
                        "stock INTEGER);";
        try (Connection c = getConnection();
        Statement st = c.createStatement())
        {
            st.execute(sql);
            System.out.println("Database creation was succesful");
        }
        catch (SQLException e)
        {
            System.err.println("Database creation failure: " + e.getMessage());
        }
    }

}