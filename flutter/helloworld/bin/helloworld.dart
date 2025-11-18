// import 'package:helloworld/calculo.dart' as calc;
import 'package:helloworld/checkin.dart' as check;
import 'package:helloworld/nums.dart' as nums;

import 'dart:io';

void ex01()
{
  print("Escribe una frase");
  String? input = stdin.readLineSync();
  if (input == null)
    return ;
  int i = 0;
  int vocal = 0;
  int cons = 0;
  int space = 0;

  while (i < input.length)
  {
    if (input[i] == ' ')
      space++;
    else if (check.isVocal(input[i]))
      vocal++;
    else if (check.isCons(input[i]))
      cons++;
    i++;  
  }

  print("Vocales: $vocal");
  print("Espacios: $space");
  print("Consonantes: $cons");
}

void ex02()
{
  print("Escriba una lista de numeros separado por espacios");
  String? input = stdin.readLineSync();
  if (input == null)
    return;
  List<String> list = input.split(' ');
  int max = nums.getMax(list);
  int min = nums.getMin(list);
  double pro = nums.getPro(list);

  print("Maximo: ${max}");
  print("Minimo: ${min}");
  print("Promedio: ${pro}");
}

void main(List<String> av)
{
  ex02();
}
