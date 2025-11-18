import java.io.*;
import java.util.ArrayList;
import java.util.List;

import com.google.gson.Gson;

public class App 
{
    public static void main(String[] args) throws Exception 
    {
        // Inicialización de las variables.
        BufferedReader br = null;
        BufferedWriter bw = null;
        BufferedWriter errores = null;
        String line;
        List<Empleado> empleados = new ArrayList<Empleado>();
        Gson gson = new Gson();

        try
        {
            // Se crea el arhcivo donde se guardaran todos los errores
            errores = new BufferedWriter(new FileWriter("errores.log"));
            // Se abre el archivo de donde se leeran los datos de los empleados
            br = new BufferedReader(new FileReader("empleados.txt"));

            // Bucle donde se leen los datos y se meten en una lista
            int i = 0;
            while ((line = br.readLine()) != null)
            {
                if (i != 0)
                {
                    String[] data = line.split(";");
                    Empleado e = new Empleado(data[0], Integer.parseInt(data[1]), data[2]);
                    empleados.add(e);
                }
                i++;
                System.out.println(line);
            }
            // Creacion del archivo .json
            String json = gson.toJson(empleados);
            // Escritura de los datos en el json
            bw = new BufferedWriter(new FileWriter("empleados.json"));
            bw.write(json);
        }
        // Gestion de errores con mensaje por terminal y registrarlo en el archivo de errores
        catch (FileNotFoundException e)
        {
            errores.write(e.toString());
            System.out.println(e.toString());
            System.err.println("Archivo no encontrado");
        }
        catch (IOException e)
        {
            errores.write(e.toString());
            System.err.println(e);
        }
        catch (NumberFormatException e)
        {
            errores.write(e.toString());
            System.err.println(e);
        }
        catch (Exception e)
        {
            errores.write(e.toString());
            System.err.println(e);
        }
        finally
        {
            try
            {
                // Cierre de todos los archivos
                // Para que no haya error tengo que verificar esten abiertos.
                if (br != null)
                    br.close();
                if (errores != null)
                    errores.close();
                if (bw != null)
                    bw.close();
            }
            catch (Exception ex)
            {
                errores.write(ex.toString());
                System.err.println(ex);
            }
        }
    }
}
