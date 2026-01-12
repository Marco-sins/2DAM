package es.dam.streamingcatalog.repository;

import java.util.List;
import java.util.Optional;

import es.dam.streamingcatalog.model.Critica;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.EntityTransaction;
import jakarta.persistence.Persistence;

public class CriticaRepository 
{
    private final EntityManagerFactory emf = Persistence.createEntityManagerFactory("streaming-catalog-pu");

    public Critica save(Critica critica)
    {
        EntityManager em = emf.createEntityManager();
        EntityTransaction et = null;

        try
        {
            et = em.getTransaction();
            et.begin();

            Critica c;
            if (critica.getId() == null)
            {
                em.persist(critica);
                c = critica;
            }
            else
                c = em.merge(critica);
            et.commit();
            return c;
        }
        catch (Exception e) 
        {
            if (et != null && et.isActive())
                et.rollback();
            System.err.println(" Error al guardar Critica: " + e.getMessage());
            throw e;
        } 
        finally 
        {
            em.close();
        }
    }

    public Optional<Critica> findById(Long id)
    {
        EntityManager em = emf.createEntityManager();

        try
        {
            return Optional.ofNullable(em.find(Critica.class, id));
        }
        finally
        {
            em.close();
        }
    }

    public List<Critica> findAll() 
    {
        EntityManager em = emf.createEntityManager();
        try 
        {
            String jpql = "SELECT c FROM Critica c";
            return em.createQuery(jpql, Critica.class).getResultList();
        } 
        finally 
        {
            em.close();
        }
    }

    public void delete(Critica entity)
    {
        EntityManager em = emf.createEntityManager();
        EntityTransaction et = null;

        try
        {
            et = em.getTransaction();
            et.begin();

            Critica c = em.contains(entity) ? entity : em.merge(entity);
            em.remove(c);
            et.commit();
        }
        catch (Exception ex)
        {
            if (et != null && et.isActive())
            {
                et.rollback();
                System.err.println("Error al eliminar Critica: " + ex.getMessage());
            }
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
}
