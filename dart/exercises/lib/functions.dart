int add(int a, int b) {
  return a + b;
}

List<List<int>> halve(List<int> lst) {
  var l = lst.length;
  if (l % 2 != 0)
    throw ArgumentError('list should have even length');
  final m = l ~/ 2;
  return [lst.take(m).toList(), lst.skip(m).toList()];
}
