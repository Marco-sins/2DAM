import 'package:helloworld/calculo.dart';
import 'package:test/test.dart';

void main() {
  test('calculate', () {
    expect(multiplicar(6, 7), 42);
  });
}
