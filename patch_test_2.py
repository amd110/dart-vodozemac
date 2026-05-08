import sys

file_path = "dart/test/vodozemac_test.dart"
with open(file_path, "r") as f:
    content = f.read()

# Replace the beginning of my test to include secureRandomBytes
old_start = """    test('Aes256Ctr streaming API', () {
      final iv = Uint8List.fromList(secureRandomBytes(16));"""

new_start = """    test('Aes256Ctr streaming API', () {
      Uint8List secureRandomBytes(int len) {
        final rng = Random.secure();
        final list = Uint8List(len);
        list.setAll(0, Iterable.generate(list.length, (i) => rng.nextInt(256)));
        return list;
      }
      final iv = Uint8List.fromList(secureRandomBytes(16));"""

if old_start in content:
    content = content.replace(old_start, new_start)
    with open(file_path, "w") as f:
        f.write(content)
    print("Patched successfully")
else:
    print("Could not find the test start")
