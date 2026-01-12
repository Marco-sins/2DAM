package es.dam.streamingcatalog.model;

import jakarta.persistence.*;

@Entity
public class Critica 
{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String autor;
    private Double puntuacion;
    private String comentario;
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "pelicula_id")
    private Pelicula pelicula;

    public Critica() {}

    public Critica(String autor, Double puntuacion, String comentario, Pelicula pelicula)
    {
        this.autor = autor;
        this.puntuacion = puntuacion;
        this.comentario = comentario;
        this.pelicula = pelicula;
    }

    public Long getId()
    {
        return id;
    }

    public Pelicula getPelicula() {
        return pelicula;
    }

    public void setPelicula(Pelicula pelicula) {
        this.pelicula = pelicula;
    }

    public String getComentario() {
        return comentario;
    }

    public void setComentario(String comentario) {
        this.comentario = comentario;
    }

    public Double getPuntuacion() {
        return puntuacion;
    }

    public void setPuntuacion(Double puntuacion) {
        this.puntuacion = puntuacion;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    @Override
    public String toString() {
        return "Critica{" +
                "id=" + id +
                ", autor='" + autor + '\'' +
                ", puntuacion=" + puntuacion +
                ", comentario='" + comentario + '\'' +
                ", pelicula=" + pelicula +
                '}';
    }


}
