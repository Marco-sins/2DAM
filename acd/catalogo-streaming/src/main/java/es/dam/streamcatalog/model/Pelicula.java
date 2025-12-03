package es.dam.streamcatalog.model;

import java.util.List;

public class Pelicula
{
    private int id;
    private String titulo;
    private String anioLanzamiento;
    private String genero;
    private Estudio estudio;
    private List<Critica> criticas;
}
