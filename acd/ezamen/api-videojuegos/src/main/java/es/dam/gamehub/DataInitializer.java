package es.dam.gamehub;

import es.dam.gamehub.model.Videojuego;
import es.dam.gamehub.service.VideojuegoService;

import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class DataInitializer implements CommandLineRunner {

    private final VideojuegoService service;

    public DataInitializer(VideojuegoService service) {
        this.service = service;
    }

    @Override
    public void run(String... args) {
        // Solo insertamos si la tabla está vacía para evitar duplicados al reiniciar
        if (service.count() == 0) {
            service.save(new Videojuego(null, "The Legend of Zelda", "Aventura", 59.99, false));
            service.save(new Videojuego(null, "Elden Ring", "RPG", 69.99, true));
            service.save(new Videojuego(null, "FIFA 24", "Deportes", 49.99, true));
            service.save(new Videojuego(null, "Minecraft", "Sandbox", 29.99, true));
            service.save(new Videojuego(null, "Cyberpunk 2077", "RPG", 39.99, true));
            System.out.println("✅ Datos de prueba insertados correctamente");
        }
    }
}