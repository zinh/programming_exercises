int add(int a, int b) {
  return a + b;
}

List<List<T>> halve<T>(List<T> lst) {
  var l = lst.length;
  if (l % 2 != 0) throw ArgumentError('list should have even length');
  final m = l ~/ 2;
  return [lst.take(m).toList(), lst.skip(m).toList()];
}

T third<T>(List<T> lst) {
  if (lst.length < 3) {
    throw ArgumentError('list should have more than 3 elements');
  }
  return lst[2];
}

bool luhn(String card) {
  var chars = card.runes;
  var n = chars.length;
  var shouldDouble = false;
  var sum = 0;
  for (var i = n - 1; i >= 0; i--) {
    var c = chars.elementAt(i);
    if (c < 48 || c > 58) {
      throw ArgumentError('invalid card number');
    }
    var val = c - 48;
    if (shouldDouble) {
      sum += ((val * 2) % 9);
    } else {
      sum += val;
    }
    shouldDouble = !shouldDouble;
  }
  return (sum % 10 == 0);
}

int sumOfSquares(int limit) {
  var sum = 0;
  for (var i = 1; i <= limit; i++) {
    sum += i * i;
  }
  return sum;
}

List<T> replicate<T>(int t, T val) {
  if (t < 0) {
    throw ArgumentError('should have positive limit');
  }
  var lst = <T>[];
  for (var i = 0; i < t; i++) {
    lst.add(val);
  }
  return lst;
}
