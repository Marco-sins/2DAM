import 'dart:io';

void main(List<String> arguments) 
{
  print("¿Como te llamas?");
  String? name = stdin.readLineSync();
  if (name == null)
  {
    stderr.write("Escribe un nombre\n");
    return ;
  }
  print("¿Cuantos años tienes?");
  String ageInput = stdin.readLineSync() ?? '';
  int? age = int.tryParse(ageInput);
  if (age == null)
  {
    stderr.write("Eso no es un numero\n");
    return ;
  }
  print("Hola $name. Tienes $age años");
}
