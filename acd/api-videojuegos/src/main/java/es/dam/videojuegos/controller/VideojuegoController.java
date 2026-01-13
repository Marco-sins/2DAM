package es.dam.videojuegos.controller;

import es.dam.videojuegos.model.Videojuego;
import es.dam.videojuegos.repository.VideojuegoRepository;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * Controlador REST para gestionar la entidad Videojuego.
 * Define los endpoints para las operaciones CRUD completas.
 */
@RestController
@RequestMapping("/videojuegos")
@CrossOrigin(origins = "http://localhost:5173")
public class VideojuegoController {

    private final VideojuegoRepository repo;

    // Inyección de Dependencias por Constructor
    public VideojuegoController(VideojuegoRepository repo) {
        this.repo = repo;
    }

    // =======================================================
    // R (Read) - Métodos GET
    // =======================================================

    /**
     * Endpoint: GET /videojuegos
     * Lista todos los videojuegos disponibles.
     */
    @GetMapping
    public List<Videojuego> findAll() {
        return repo.findAll();
    }

    /**
     * Endpoint: GET /videojuegos/{id}
     * Busca un videojuego específico por su ID.
     */
    @GetMapping("/{id}")
    public Videojuego findById(@PathVariable Long id) {
        // Devuelve el objeto Videojuego si lo encuentra, o null si no existe.
        return repo.findById(id).orElse(null);
    }

    // =======================================================
    // C (Create) - Método POST
    // =======================================================

    /**
     * Endpoint: POST /videojuegos
     * Crea un nuevo videojuego a partir del JSON recibido en el cuerpo.
     */
    @PostMapping
    public Videojuego create(@RequestBody Videojuego videojuego) {
        // El método save() de JpaRepository inserta si el ID es null o no existe.
        return repo.save(videojuego);
    }

    // =======================================================
    // U (Update) - Método PUT
    // =======================================================

    /**
     * Endpoint: PUT /videojuegos/{id}
     * Actualiza un videojuego existente.
     */
    @PutMapping("/{id}")
    public Videojuego update(@PathVariable Long id, @RequestBody Videojuego videojuego) {
        // 1. Verificamos si el videojuego con ese ID existe en la base de datos
        if (repo.existsById(id)) {
            // 2. Asignamos el ID de la URL al objeto recibido para asegurar la actualización
            videojuego.setId(id);
            // 3. El método save() actualizará el registro existente
            return repo.save(videojuego);
        }
        // Si no existe, devolvemos null (se mejorará en el Taller 3 con 404 Not Found)
        return null; 
    }

    // =======================================================
    // D (Delete) - Método DELETE
    // =======================================================

    /**
     * Endpoint: DELETE /videojuegos/{id}
     * Elimina un videojuego por su ID.
     */
    @DeleteMapping("/{id}")
    public void delete(@PathVariable Long id) {
        // Elimina el registro por el ID.
        // Nota: JpaRepository no lanza error si el ID no existe (comportamiento a mejorar en Taller 3)
        repo.deleteById(id);
    }
}