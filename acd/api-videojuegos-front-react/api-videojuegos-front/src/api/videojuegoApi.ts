/**
 * Videojuego API
 * Módulo para interactuar con la API de videojuegos.
 * Proporciona funciones para obtener, crear, actualizar y eliminar videojuegos.
 * @module videojuegoApi
 * 
 */

import type { Videojuego } from "../models/Videojuego";

// GET 
export const getAll = async () => {
    const response = await fetch('http://localhost:8080/videojuegos');
    return response.json();
}

export const getById = async (id: number) => {
    const response = await fetch(`http://localhost:8080/videojuegos/${id}`);
    return response.json();
}

// POST
export const create = async (videojuego: Videojuego) => {
    const response = await fetch('http://localhost:8080/videojuegos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(videojuego)
    });
    return response.json();
}

// PUT
export const update = async (id: number, videojuego: any) => {
    const response = await fetch(`http://localhost:8080/videojuegos/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(videojuego)
    });
    return response.json();
}

// DELETE
export const remove = async (id: number) => {
    await fetch(`http://localhost:8080/videojuegos/${id}`, {
        method: 'DELETE'
    });
}