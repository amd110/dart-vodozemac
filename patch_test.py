import sys

file_path = "dart/test/vodozemac_test.dart"
with open(file_path, "r") as f:
    content = f.read()

test_to_insert = """
    test('Aes256Ctr streaming API', () {
      final iv = Uint8List.fromList(secureRandomBytes(16));
      iv[8] &= 0x7f;
      final key = Uint8List.fromList(secureRandomBytes(32));
      final input = Uint8List.fromList('streaming test data'.codeUnits);
      
      final cipher = Aes256Ctr(key: key, iv: iv);
      // Process in two chunks
      final encryptedChunk1 = cipher.update(input.sublist(0, 10));
      final encryptedChunk2 = cipher.update(input.sublist(10));
      cipher.finalize();
      
      final encrypted = Uint8List.fromList([...encryptedChunk1, ...encryptedChunk2]);
      
      // Decrypt
      final decCipher = Aes256Ctr(key: key, iv: iv);
      final decryptedChunk1 = decCipher.update(encrypted.sublist(0, 5));
      final decryptedChunk2 = decCipher.update(encrypted.sublist(5));
      decCipher.finalize();
      
      final decrypted = Uint8List.fromList([...decryptedChunk1, ...decryptedChunk2]);
      
      expect(decrypted, input);
      
      // Compare with CryptoUtils.aesCtr
      final oneshot = CryptoUtils.aesCtr(input: input, key: key, iv: iv);
      expect(encrypted, oneshot);
    });
"""

insert_pos = content.find("expect(decrypted, Uint8List.fromList('test'.codeUnits));\n    });")
if insert_pos == -1:
    print("Could not find insertion point!")
    sys.exit(1)

# Find the end of the block
end_pos = content.find("});", insert_pos) + 3
new_content = content[:end_pos] + "\n" + test_to_insert + content[end_pos:]

with open(file_path, "w") as f:
    f.write(new_content)
print("Success")
