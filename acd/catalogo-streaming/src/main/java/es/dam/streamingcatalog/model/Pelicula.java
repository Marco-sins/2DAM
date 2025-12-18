package es.dam.streamingcatalog.model;

import java.util.ArrayList;
import java.util.List;
import jakarta.persistence.*;

@Entity
public class Pelicula 
{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String nombre;
    private int anioLanzamiento;
    private String genero;
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "estudio_id")
    private Estudio estudio;
    @OneToMany(
        mappedBy = "pelicula",
        cascade = CascadeType.ALL,
        orphanRemoval = true,
        fetch = FetchType.LAZY)
    private List<Critica> criticas;

    public Pelicula()
    {
        this.nombre = "DefaultName";
        this.anioLanzamiento = 2001;
        this.genero = "DefaultGenero";
        this.estudio = null;
        this.criticas = new ArrayList<>();
    }

    public Pelicula(String nombre, int anioLanzamiento, String genero, Estudio e)
    {
        this.nombre = nombre;
        this.anioLanzamiento = anioLanzamiento;
        this.genero = genero;
        this.estudio = e;
        this.criticas = new ArrayList<>();
    }

    public void addCritica(Critica critica)
    {
        this.criticas.add(critica);
        critica.setPelicula(this);
    }

    public List<Critica> getCriticas() {
        return criticas;
    }

    public void setCriticas(List<Critica> criticas) {
        this.criticas = criticas;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public int getAnioLanzamiento() {
        return anioLanzamiento;
    }

    public void setAnioLanzamiento(int anioLanzamiento) {
        this.anioLanzamiento = anioLanzamiento;
    }

    public Estudio getEstudio() {
        return estudio;
    }

    public void setEstudio(Estudio estudio) {
        this.estudio = estudio;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return "Pelicula{" +
                "id=" + id +
                ", nombre='" + nombre + '\'' +
                ", anioLanzamiento=" + anioLanzamiento +
                ", genero='" + genero + '\'' +
                ", estudio=" + estudio +
                ", criticas=" + criticas +
                '}';
    }
}
