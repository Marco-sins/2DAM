package es.dam.gamehub.controller;

import org.springframework.web.bind.annotation.RestController;

import es.dam.gamehub.model.Videojuego;
import es.dam.gamehub.service.VideojuegoService;

import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;



@RestController
@RequestMapping("/videojuegos")
public class VideojuegoController 
{
    private final VideojuegoService videojuegoService;

    public VideojuegoController(VideojuegoService videojuegoService) 
    {
        this.videojuegoService = videojuegoService;
    }

    @GetMapping
    public List<Videojuego> getAllVideojuegos() 
    {
        return videojuegoService.findAll();
    }

    @GetMapping("/{id}")
    public Videojuego getVideojuegoById(@PathVariable Long id)
    {
        return videojuegoService.findById(id).orElse(null);
    }

    @PostMapping
    public Videojuego create(@RequestBody Videojuego videojuego)
    {
        return videojuegoService.save(videojuego);
    }

    @PutMapping
    public Videojuego update(@PathVariable Long id, @RequestBody Videojuego videojuego) 
    {
        if (videojuegoService.findById(id) != null) {
            videojuego.setId(id);
            return videojuegoService.save(videojuego);
        }
        return null; 
    }
    
    @DeleteMapping("/{id}")
    public boolean delete(@PathVariable Long id)
    {
        return videojuegoService.delete(id);
    }
}
