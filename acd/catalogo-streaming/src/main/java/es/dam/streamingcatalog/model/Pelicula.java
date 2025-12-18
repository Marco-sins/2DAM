package es.dam.streamingcatalog.model;

import java.util.ArrayList;
import java.util.List;
import jakarta.persistence.*;
import lombok.*;

@Entity
@AllArgsConstructor
@Getter
@Setter
@ToString
public class Pelicula 
{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String nombre;
    private String anioLanzamiento;
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
        this.anioLanzamiento = "01/01/2001";
        this.genero = "DefaultGenero";
        this.estudio = null;
        this.criticas = new ArrayList<>();
    }
}
