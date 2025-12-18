package es.dam.streamingcatalog.repository;

import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;

public class CriticaRepository 
{
    private final EntityManagerFactory emf = Persistence.createEntityManagerFactory("streaming-catalog-pu");
}
