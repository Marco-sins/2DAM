package es.dam.streamingcatalog.model;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import jakarta.persistence.*;

@Entity
public class Estudio 
{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String nombre;
    private LocalDate fundacion;
    @OneToMany(mappedBy = "estudio",
        cascade = CascadeType.ALL,
        orphanRemoval = true,
        fetch = FetchType.LAZY)
    private List<Pelicula> peliculas;

    public Estudio()
    {
        this.nombre = "DefaultName";
        this.fundacion = LocalDate.of(2001, 1, 1);
        this.peliculas = new ArrayList<>();
    }

    public Estudio(String nombre, LocalDate date)
    {
        this.nombre = nombre;
        this.fundacion = date;
        this.peliculas = new ArrayList<>();
    }

    public void addPelicula(Pelicula pelicula)
    {
        this.peliculas.add(pelicula);
        pelicula.setEstudio(this);
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public LocalDate getFundacion() {
        return fundacion;
    }

    public void setFundacion(LocalDate fundacion) {
        this.fundacion = fundacion;
    }

    public List<Pelicula> getPeliculas() {
        return peliculas;
    }

    public void setPeliculas(List<Pelicula> peliculas) {
        this.peliculas = peliculas;
    }

    @Override
    public String toString() {
        return "Estudio{" +
                "id=" + id +
                ", nombre='" + nombre + '\'' +
                ", fundacion=" + fundacion +
                ", peliculas=" + peliculas +
                '}';
    }
}
