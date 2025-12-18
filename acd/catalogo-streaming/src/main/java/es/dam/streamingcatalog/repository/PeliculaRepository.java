package es.dam.streamingcatalog.repository;

import java.util.List;
import java.util.Optional;

import es.dam.streamingcatalog.model.Pelicula;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.EntityTransaction;
import jakarta.persistence.Persistence;

public class PeliculaRepository 
{
    private final EntityManagerFactory emf = Persistence.createEntityManagerFactory("streaming-catalog-pu");

    public Pelicula save(Pelicula pelicula)
    {
        EntityManager em = emf.createEntityManager();
        EntityTransaction et = null;

        try
        {
            et = em.getTransaction();
            et.begin();

            Pelicula p;
            if (pelicula.getId() == null)
            {
                em.persist(pelicula);
                p = pelicula;
            }
            else
                p = em.merge(pelicula);
            et.commit();
            return p;
        }
        catch (Exception ex)
        {
            if (et != null && et.isActive())
                et.rollback();
            System.err.println("Error al guardar Pelicula: " + ex.getMessage());
            throw ex;
        }
    }

    public Optional<Pelicula> findById(Long id)
    {
        EntityManager em = emf.createEntityManager();

        try
        {
            return Optional.ofNullable(em.find(Pelicula.class, id));
        }
        finally
        {
            em.close();
        }
    }

    public List<Pelicula> findAll()
    {
        EntityManager em = emf.createEntityManager();

        try
        {
            String jpql = "Select p from Pelicula p";
            return em.createQuery(jpql, Pelicula.class).getResultList();
        }
        finally
        {
            em.close();
        }
    }

    public void delete(Pelicula pelicula)
    {
        EntityManager em = emf.createEntityManager();
        EntityTransaction et = null;

        try
        {
            et = em.getTransaction();
            et.begin();

            Pelicula p = em.contains(pelicula) ? pelicula : em.merge(pelicula);
            em.remove(p);
            et.commit();
        }
        catch (Exception ex)
        {
            if (et != null && et.isActive())
                et.rollback();
            System.err.println("Error al eliminar Pelicula: " + ex.getMessage());
            throw ex;
        }
        finally
        {
            em.close();
        }
    }

    public void deleteById(Long id)
    {
        findById(id).ifPresent(this::delete);
    }

    public List<Pelicula> findByAnioMayorQue(int anio)
    {
        EntityManager em = emf.createEntityManager();

        try
        {
            String jpql = "Select p from Pelicula p Where p.anioLanzamiento > :anio";
            return em.createQuery(jpql, Pelicula.class).setParameter("anio", anio).getResultList();
        }
        finally
        {
            em.close();
        }
    }
}
