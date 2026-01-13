import { useVideojuegos } from "../hooks/usesVideojuegos";
import { CardVideojuego } from "../components/CardVideojuego";
import { Button } from "../components/Button";
import { useNavigate } from 'react-router-dom';
import '../styles/pages/Home.css';

export const Home = () => {
    const { error, loading, videojuegos } = useVideojuegos();
    const navigate = useNavigate();

    if (error) 
        return <div>{error}</div>;
    if (loading) 
        return <div id="loading">Cargando...</div>;

    return (
        <div id="home">
            <h1>Lista de Videojuegos</h1>
            <div className="videojuegos-list">
                {videojuegos.map(videojuego => (
                    <CardVideojuego onClick={() => {navigate('/detalle-videojuego/' + videojuego.id)}} key={videojuego.id} videojuego={videojuego}/>
                ))}
            </div>
            <div className="button">
                {Button({ onClick: () => navigate('/crear-videojuego'), value: 'Añadir juego', className: "button-add" })}
            </div>
        </div>
    );
}