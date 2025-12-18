package es.dam.streamingcatalog;

import es.dam.streamingcatalog.model.Critica;
import es.dam.streamingcatalog.model.Estudio;
import es.dam.streamingcatalog.model.Pelicula;
import es.dam.streamingcatalog.repository.*;
import java.time.LocalDate;
import java.util.List;

public class Main 
{
    private static final EstudioRepository repositoryEstudio = new EstudioRepository();
    private static final PeliculaRepository repositoryPelicula = new PeliculaRepository();

    public static void main(String[] av)
    {
        Estudio e = new Estudio("Estudio", LocalDate.of(2001, 1, 1));
        Pelicula p1 = new Pelicula("Pelicula1", 2001, "Genero1", null);
        Pelicula p2 = new Pelicula("Pelicula2", 2002, "Genero2", null);

        e.addPelicula(p1);
        e.addPelicula(p2);

        p1.addCritica(new Critica("Autor1", 1.0, "Comentario1", null));
        p2.addCritica(new Critica("Autor2", 2.0, "Comentario2", null));

        e = repositoryEstudio.save(e);
        System.out.println("Estudio y sus peliculas guardadas");
        System.out.println("ID creado: " + e.getId());

        Pelicula p = e.getPeliculas().stream().filter(pe -> pe.getNombre().equals("Pelicula1")).findFirst().orElseThrow();
        System.out.println("ID de la Pelicula: \"" + p.getNombre() + " : " + p.getId() + "\"");

        System.out.println("Actualizando año de lanzamiento de la pelicula");
        p.setAnioLanzamiento(2002);
        repositoryPelicula.save(p);

        int anioActualizado = repositoryPelicula.findById(p.getId()).get().getAnioLanzamiento();
        System.out.println("La pelicula \"" + p.getNombre() + "\" ahora tiene año: " + anioActualizado);

        int anioFiltro = 2002;
        System.out.println("\n--- Peliculas estrenadas despues de " + anioFiltro + "---");
        
        List<Pelicula> peliculasRecientes = repositoryPelicula.findByAnioMayorQue(anioFiltro);
        peliculasRecientes.forEach(pel -> System.out.println("- " + pel.getNombre() + " (Año: " + pel.getAnioLanzamiento() + ")"));
        System.out.println("Todo ha sido realizado con exito");
    }
}