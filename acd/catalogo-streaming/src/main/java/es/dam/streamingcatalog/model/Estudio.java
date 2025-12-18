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
public class Estudio 
{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String nombre;
    private String fundacion;
    @OneToMany(mappedBy = "estudio",
        cascade = CascadeType.ALL,
        orphanRemoval = true,
        fetch = FetchType.LAZY)
    private List<Pelicula> peliculas;

    public Estudio()
    {
        this.nombre = "DefaultName";
        this.fundacion = "DefaultFundation";
        this.peliculas = new ArrayList<>();
    }
}
