package es.dam.gamehub.service;

import es.dam.gamehub.repository.VideojuegoRepository;
import es.dam.gamehub.model.Videojuego;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

@Service
public class VideojuegoService 
{
    private final VideojuegoRepository videojuegoRepository;

    public VideojuegoService(VideojuegoRepository videojuegoRepository) 
    {
        this.videojuegoRepository = videojuegoRepository;
    }

    public long count() 
    {
        return videojuegoRepository.count();
    }

    public List<Videojuego> findAll() 
    {
        return videojuegoRepository.findAll();
    }

    public Optional<Videojuego> findById(Long id) 
    {
        return Optional.ofNullable(videojuegoRepository.findById(id).orElse(null));
    }

    public Videojuego save(Videojuego videojuego) 
    {
        return videojuegoRepository.save(videojuego);
    }

    public Videojuego update(Long id, Videojuego videojuegoDetails) 
    {
        return videojuegoRepository.findById(id).map(videojuego -> {
            videojuego.setTitulo(videojuegoDetails.getTitulo());
            videojuego.setGenero(videojuegoDetails.getGenero());
            videojuego.setPrecio(videojuegoDetails.getPrecio());
            videojuego.setMultiplayer(videojuegoDetails.getMultiplayer());
            return videojuegoRepository.save(videojuego);
        }).orElse(null);
    }

    public boolean delete(Long id) 
    {
        return videojuegoRepository.findById(id).map(videojuego -> {
            videojuegoRepository.delete(videojuego);
            return true;
        }).orElse(false);
    }
}
