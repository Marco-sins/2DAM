import type { Videojuego } from "../models/Videojuego";
import '../styles/components/CardVideojuegos.css';

export const CardVideojuego = ({videojuego, onClick}: {videojuego: Videojuego, onClick: () => void}) => {
    return (
        <div className="card-videojuego" onClick={onClick}>
            <h2>{videojuego.titulo}</h2>
            <p>Género: {videojuego.genero}</p>
            <p>Precio: {videojuego.precio} €</p>
        </div>
    );
}