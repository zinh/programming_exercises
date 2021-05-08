int add(int a, int b) {
  return a + b;
}

List<List<T>> halve<T>(List<T> lst) {
  var l = lst.length;
  if (l % 2 != 0)
    throw ArgumentError('list should have even length');
  final m = l ~/ 2;
  return [lst.take(m).toList(), lst.skip(m).toList()];
}

T third<T>(List<T> lst) {
  if (lst.length < 3)
    throw ArgumentError('list should have more than 3 elements');
  return lst[2];
}

bool luhn(String card) {
  return false;
}
