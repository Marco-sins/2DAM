import { useState, useEffect } from "react";
import { getAll, getById, create, update, remove } from "../api/videojuegoApi";
import type { Videojuego } from "../models/Videojuego";

export const useVideojuegos = () => {
    const [videojuegos, setVideojuegos] = useState<Videojuego[]>([]);
    const [loading, setLoading] = useState(true);
    const [ error, setError] = useState<string | null>(null);

    // GET
    useEffect(() => {
        getAll()
        .then(data => setVideojuegos(data));
        setLoading(false);
    }, []);
   

    const getVideojuegoById = async (id: number) => {
        try {
            const videojuego = await getById(id);
            setVideojuegos([videojuego]);
        } catch (err) {
            setError("Error cargando el videojuego");
            setVideojuegos([]);
        } finally {
            setLoading(false);
        }
    }

    // POST
    const createVideojuego = async (videojuego: Videojuego) => {
        try {
            const newVideojuego = await create(videojuego);
            setVideojuegos([...videojuegos, newVideojuego]);
        }
        catch (err) {
            setError("Error creando el videojuego");
        } finally {
            setLoading(false);
        } 
    }

    // PUT
    const updateVideojuego = async (id: number, videojuego: Videojuego) => {
        try {
            const updated: Videojuego = await update(id, videojuego);
            setVideojuegos(prev => prev.map(vj => vj.id === id ? updated : vj));
        }
        catch (err) {
            setError("Error actualizando el videojuego");
        } finally {
            setLoading(false);
        }
    }
    
    // DELETE
    const deleteVideojuego = async (id: number) => {
        try {
            await remove(id);
            setVideojuegos(prev => prev.filter(vj => vj.id !== id));
        } catch (err) {
            setError("Error eliminando el videojuego");
        } finally {
            setLoading(false);
        }
    }

    return { getVideojuegoById, createVideojuego, updateVideojuego, deleteVideojuego, error, videojuegos, loading };
}
