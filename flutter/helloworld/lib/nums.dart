int getMax(List<String> list)
{
  int i = 1;
  int max = int.parse(list[0]);

  while (i < list.length)
  {
    if (max < int.parse(list[i]))
      max = int.parse(list[i]);
    i++;
  }
  return max;
}

int getMin(List<String> list)
{
  int i = 1;
  int min = int.parse(list[0]);

  while (i < list.length)
  {
    if (min > int.parse(list[i]))
      min = int.parse(list[i]);
    i++;
  }
  return min;
}

double getPro(List<String> list)
{
  int i = 1;
  double pro = double.parse(list[0]);

  while (i < list.length)
  {
    pro += double.parse(list[i]);
    i++;
  }
  return pro / list.length;
}