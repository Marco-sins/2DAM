/**
 * 
 * Interface que representa un videojuego.
 * Contiene las propiedades id, titulo, genero y precio.
 * @interface Videojuego
 * @property {number} id - Identificador único del videojuego.
 * @property {string} titulo - Título del videojuego.
 * @property {string} genero - Género del videojuego.
 * @property {number} precio - Precio del videojuego.
 * 
 * Se pone como interface y no como class porque no se van a crear objetos de este tipo,
 * solo se va a usar para tipar los datos que vienen de la API.
 */

export interface Videojuego {
    id?: number;
    titulo: string;
    genero: string;
    precio: number;
}
