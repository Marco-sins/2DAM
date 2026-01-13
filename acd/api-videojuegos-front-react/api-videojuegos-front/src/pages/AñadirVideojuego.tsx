import React from 'react';
import '../styles/pages/AñadirVideojuego.css'; // Assuming you have a CSS file for styling
import { Button } from "../components/Button";
import { useNavigate } from 'react-router-dom';
import { useVideojuegos } from "../hooks/usesVideojuegos";

export const AñadirVideojuego = () => {
    const navigate = useNavigate();
    const { createVideojuego } = useVideojuegos();

    const handleAddVideojuego = async () => {
        await createVideojuego({
            titulo: (document.getElementById('titulo') as HTMLInputElement).value,
            genero: (document.getElementById('genero') as HTMLInputElement).value,
            precio: parseFloat((document.getElementById('precio') as HTMLInputElement).value)
        });
        navigate('/'); // Redirect to home after adding
    }

    const handleCancel = () => {
        navigate('/'); // Redirect to home on cancel
    }

    return (
        <div id="añadir-videojuego">
            <h1>Añadir Videojuego</h1>
            <form id='form'>
                <label htmlFor="titulo">Título:</label>
                <input type="text" id="titulo" name="titulo" required />

                <label htmlFor="genero">Género:</label>
                <input type="text" id="genero" name="genero" required />

                <label htmlFor="precio">Precio:</label>
                <input type="number" id="precio" name="precio" required />

                <Button onClick={handleCancel} value="Cancelar" className="button" id="cancelar" />
                <Button onClick={handleAddVideojuego} value="Añadir Videojuego" className="button" id="aceptar" />
            </form>
        </div>
    );
}