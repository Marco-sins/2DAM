import 'dart:ffi';

bool isVocal(String c)
{
  return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ? true : false);
}

bool isCons(String c)
{
  return (RegExp(r'[a-zA-Z]').hasMatch(c));
}