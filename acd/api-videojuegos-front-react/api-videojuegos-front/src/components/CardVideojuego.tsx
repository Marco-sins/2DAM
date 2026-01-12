import type { Videojuego } from "../models/Videojuego";
import '../styles/CardVideojuego.css';

interface CardVideojuegoProps {
    videojuego: Videojuego;
}

export const CardVideojuego = ({videojuego}: CardVideojuegoProps) => {
    return (
        <div className="card-videojuego">
            <h2>{videojuego.titulo}</h2>
            <p>Género: {videojuego.genero}</p>
            <p>Precio: ${videojuego.precio.toFixed(2)}</p>
        </div>
    );
}