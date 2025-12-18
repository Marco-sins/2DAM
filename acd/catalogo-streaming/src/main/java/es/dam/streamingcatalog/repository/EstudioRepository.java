package es.dam.streamingcatalog.repository;

import java.util.List;
import java.util.Optional;

import es.dam.streamingcatalog.model.Estudio;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.EntityTransaction;
import jakarta.persistence.Persistence;

public class EstudioRepository 
{
    private final EntityManagerFactory emf = Persistence.createEntityManagerFactory("streaming-catalog-pu");

    public Estudio save(Estudio estudio)
    {
        EntityManager em = emf.createEntityManager();
        EntityTransaction et = null;

        try
        {
            et = em.getTransaction();
            et.begin();

            Estudio e;
            if (estudio.getId() == null)
            {
                em.persist(estudio);
                e = estudio;
            }
            else
                e = em.merge(estudio);
            et.commit();
            return e;
        }
        catch (Exception e)
        {
            if (et != null && et.isActive())
                et.rollback();
            System.err.println("Error al guardar Estudio: " + e.getMessage());
            throw e;
        }
        finally
        {
            em.close();
        }
    }

    public Optional<Estudio> findById(Long id)
    {
        EntityManager em = emf.createEntityManager();

        try
        {
            return Optional.ofNullable(em.find(Estudio.class, id));
        }
        finally
        {
            em.close();
        }
    }

    public List<Estudio> findAll()
    {
        EntityManager  em = emf.createEntityManager();

        try
        {
            String jpql = "Select e from Estudio e";
            return em.createQuery(jpql, Estudio.class).getResultList();
        }
        finally
        {
            em.close();
        }
    }

    public void delete(Estudio estudio)
    {
        EntityManager em = emf.createEntityManager();
        EntityTransaction et = null;

        try
        {
            et = em.getTransaction();
            et.begin();

            Estudio e = em.contains(estudio) ? estudio : em.merge(estudio);
            em.remove(e);
            et.commit();
        }
        catch (Exception ex)
        {
            if (et != null && et.isActive())
                et.rollback();
            System.err.println("Error al eliminar Estudio: " + ex.getMessage());
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
