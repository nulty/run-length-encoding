# Your task is to implement the run-length encoding and decoding functions defined below.

# Some details about Run-length encoding:

# Run-length encoding (RLE) is a simple form of data compression, where runs (consecutive data elements) are replaced by just one data value and count.

# For example we can represent the original 53 characters with only 13.

# "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"  ->  "12WB12W3B24WB"

# RLE allows the original data to be perfectly reconstructed from the compressed data, which makes it a lossless data compression.

# "AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"

# For simplicity, you can assume that the unencoded string will only contain the letters A through Z (either lower or upper case) and whitespace. This way data to be encoded will never contain any numbers and numbers inside data to be decoded always represent the count for the following character.")


class RunLengthEncoding:
    def compress(self, string):
        if len(string) == 0:
            return string

        output = ""
        count = 1

        for i in range(1, len(string)):
            if string[i] == string[i - 1]:
                count += 1
            else:
                if count > 1:
                    output += str(count)
                output += string[i - 1]
                count = 1
        if count > 1:
            output += str(count)
        output += string[-1]
        return output

    def decompress(self, string):
        if len(string) == 0:
            return string
        count = ""
        output = ""
        inp = ""
        for i in range(0, len(string) - 1):
            if string[i].isdigit():
                count += string[i]
            else:
                if count.isdigit():
                    inp += string[i] * int(count)
                    count = ""
                else:
                    inp += string[i]
                output += inp
                inp = ""
        if count.isdigit():
            output += string[-1] * int(count)
        else:
            output += string[-1]
        return output


import unittest


class TestRunLengthEncoding(unittest.TestCase):
    def setUp(self):
        self.rle = RunLengthEncoding()

    def test_compress_empty_input(self):
        self.assertEqual(self.rle.compress(""), "")

    def test_compress_single_value(self):
        self.assertEqual(self.rle.compress("XYZ"), "XYZ")

    def test_compress_no_single_value(self):
        self.assertEqual(self.rle.compress("AABBBCCCC"), "2A3B4C")

    def test_compress_mixed_values(self):
        self.assertEqual(
            self.rle.compress("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"),
            "12WB12W3B24WB",
        )

    def test_compress_lower_case(self):
        self.assertEqual(self.rle.compress("aabbbcccc"), "2a3b4c")

    def test_compress_white_spaces(self):
        self.assertEqual(self.rle.compress("  hsqq qww  "), "2 hs2q q2w2 ")

    def test_decompress_empty_input(self):
        self.assertEqual(self.rle.decompress(""), "")

    def test_decompress_no_single_value(self):
        self.assertEqual(self.rle.decompress("2A3B4C"), "AABBBCCCC")

    def test_decompress_mixed_value(self):
        self.assertEqual(
            self.rle.decompress("10WB12W3B24WB"),
            "WWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB",
        )

    def test_decompress_lower_case(self):
        self.assertEqual(self.rle.decompress("2a3b4c"), "aabbbcccc")

    def test_decompress_white_spaces(self):
        self.assertEqual(self.rle.decompress("2 hs2q q2w2 "), "  hsqq qww  ")

    def test_input_equals_decompressed_compressed_string(self):
        inp = "zzz ZZ  zZ"
        compressed = self.rle.compress(inp)
        self.assertEqual(self.rle.decompress(compressed), inp)


if __name__ == "__main__":
    unittest.main()
