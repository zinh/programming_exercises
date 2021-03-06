import 'package:exercises/functions.dart';
import 'package:test/test.dart';

void main() {
  test('Always true', (){
    expect(add(1, 1), equals(2));
    expect(add(2, 1), equals(3));
  });

  test('halve', () {
    expect(halve([1,2,3,4]), equals([[1,2], [3,4]]));
    expect(() => halve([1,2,3]), throwsArgumentError);
  });

  test('third', () {
    expect(third([1,2,3]), equals(3));
    expect(() => third([1,2]), throwsArgumentError);
    expect(() => third([1]), throwsArgumentError);
    expect(() => third([]), throwsArgumentError);
  });

  test('luhn', () {
    expect(luhn("123"), equals(false));
    expect(luhn("4539027455502281"), equals(true));
    expect(() => luhn("0ab1"), throwsArgumentError);
  });

  test('replicate', () {
    expect(replicate(4, true), equals([true, true, true, true]));
    expect(replicate(0, true), equals([]));
    expect(() => replicate(-1, true), throwsArgumentError);
  });
}
