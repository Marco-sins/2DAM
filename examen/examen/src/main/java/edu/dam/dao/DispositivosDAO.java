package edu.dam.dao;

import java.util.List;
import java.util.ArrayList;

import java.sql.*;

import edu.dam.model.Dispositivo;
import edu.dam.util.*;

public class DispositivosDAO 
{

    // Inserta el dispositivo en la base de datos
    public void insertarDispositivo(Dispositivo d) throws SQLException
    {
        String sql = "INSERT INTO dispositivos(nombre, categoria, precio, stock) VALUES (?, ?, ?, ?)";
        try (Connection c = DatabaseConnector.getConnection(); 
            PreparedStatement ps = c.prepareStatement(sql))
        {
            ps.setString(1, d.getNombre());
            ps.setString(2, d.getCategoria());
            ps.setDouble(3, d.getPrecio());
            ps.setInt(4, d.getStock());
            ps.executeUpdate();
        }
    }

    // Actualiza un dispositivo en la base de datos
    public void actualizarDispositivo(Dispositivo d) throws SQLException
    {
        String sql = "UPDATE dispositivos SET nombre = ?, categoria = ?, precio = ?, stock = ? WHERE id = ?";
        try (Connection c = DatabaseConnector.getConnection(); 
            PreparedStatement ps = c.prepareStatement(sql))
        {
            ps.setString(1, d.getNombre());
            ps.setString(2, d.getCategoria());
            ps.setDouble(3, d.getPrecio());
            ps.setInt(4, d.getStock());
            ps.setInt(5, d.getId());
            ps.executeUpdate();
        }
    }

    // Elimina a traves de la id del dispositivo el dispositivo de la base de datos
    public void eliminarDispositivo(int id) throws SQLException
    {
        String sql = "DELETE FROM dispositivos WHERE id = ?";
        try (Connection c = DatabaseConnector.getConnection();
            PreparedStatement ps = c.prepareStatement(sql))
        {
            ps.setInt(1, id);
            ps.executeUpdate();
        }
    }

    // Lista los dispositivos que hay en la base de datos
    public List<Dispositivo> listarDisposivos() throws SQLException
    {
        String sql = "SELECT * FROM dispositivos";
        List<Dispositivo> list = new ArrayList<>();
        try (Connection c = DatabaseConnector.getConnection();
            PreparedStatement ps = c.prepareStatement(sql);
            ResultSet r = ps.executeQuery())
        {
            while (r.next())
            {
                Dispositivo d = new Dispositivo(
                    r.getInt("id"),
                    r.getString("nombre"),
                    r.getString("categoria"),
                    r.getDouble("precio"),
                    r.getInt("stock")
                );
                list.add(d);
            }
        }
        return list;
    }

    // Busca por categoria  y un rango de precio los dispositivos de la base de datos
    public List<Dispositivo> buscarPorCategoriayRangoPrecio(String categoria, double precioMinimo, double precioMaximo) throws SQLException
    {
        String sql = "SELECT * FROM dispositivos WHERE categoria = ? AND precio BETWEEN ? AND ?";
        List<Dispositivo> list = new ArrayList<>();
        try (Connection c = DatabaseConnector.getConnection();
            PreparedStatement ps = c.prepareStatement(sql);)
        {
            ps.setString(1, categoria);
            ps.setDouble(2, precioMinimo);
            ps.setDouble(3, precioMaximo);
            ResultSet r = ps.executeQuery();
            while (r.next())
            {
                list.add(new Dispositivo(
                    r.getInt("id"),
                    r.getString("nombre"),
                    r.getString("categoria"),
                    r.getDouble("precio"),
                    r.getInt("stock")
                    ));
            }
        }
        return list;
    }

}
