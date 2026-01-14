import { useNavigate } from "react-router-dom";
import { Button } from "../components/Button";
import { useVideojuegos } from "../hooks/usesVideojuegos";
import { useParams } from "react-router-dom";
import { useEffect } from "react";

export const DetallesVideojuego = () => {
    const idParam = useParams();
    const id = Number(idParam.id);
    const navigate = useNavigate();
    const { deleteVideojuego, getVideojuegoById, videojuegos } = useVideojuegos();
    

    const handleDelete = async () => {
        await deleteVideojuego(id);
        navigate('/'); // Redirect to home after deletion
    }

    const handleBack = () => {
        navigate('/'); // Redirect to home on back
    }

    useEffect(() => {
        getVideojuegoById(id);
    });

    if (!videojuegos) 
        return <div>Cargando...</div>;

    return (
        <div className="detalles-videojuego">
            <h1>{videojuegos[0]?.titulo}</h1>
            <p>Género: {videojuegos[0]?.genero}</p>
            <p>Precio: {videojuegos[0]?.precio}</p>
            <Button onClick={(handleBack)} value="Back" className="button" id="aceptar"/>
            <Button onClick={(handleDelete)} value="Delete" className="button" id="cancelar"/>
        </div>
    );
}