# Your task is to implement the run-length encoding and decoding functions defined below.

# Some details about Run-length encoding:

# Run-length encoding (RLE) is a simple form of data compression, where runs (consecutive data elements) are replaced by just one data value and count.

# For example we can represent the original 53 characters with only 13.

# "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"  ->  "12WB12W3B24WB"

# RLE allows the original data to be perfectly reconstructed from the compressed data, which makes it a lossless data compression.

# "AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"

# For simplicity, you can assume that the unencoded string will only contain the letters A through Z (either lower or upper case) and whitespace. This way data to be encoded will never contain any numbers and numbers inside data to be decoded always represent the count for the following character.")


require 'rspec/autorun'

class RunLengthEncoding
  def compress(str)
    str
  end

  def decompress(str)
    str
  end
end

RSpec.describe RunLengthEncoding do
  subject(:rle) { described_class.new }

  it 'Returns empty string if input is empty' do
    expect(rle.compress('')).to eq('')
  end

  it 'compresses with only single value' do
    expect(rle.compress('XYZ')).to eq('XYZ')
  end

  it 'compresses with no single value' do
    expect(rle.compress('AABBBCCCC')).to eq('2A3B4C')
  end

  it 'compresses with mixed values' do
    expect(rle.compress('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB')).to eq('12WB12W3B24WB')
  end

  it 'compresses with lower case' do
    expect(rle.compress('aabbbcccc')).to eq('2a3b4c')
  end

  it 'compresses with white spaces' do
    expect(rle.compress('  hsqq qww  ')).to eq('2 hs2q q2w2 ')
  end

  it 'decompress returns empty string if input is empty' do
    expect(rle.decompress('')).to eq('')
  end

  it 'decompresses with no single value' do
    expect(rle.decompress('2A3B4C')).to eq('AABBBCCCC')
  end

  it 'decompresses with mixed value' do
    expect(rle.decompress('10WB12W3B24WB')).to eq('WWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB')
  end

  it 'decompresses with lower case' do
    expect(rle.decompress('2a3b4c')).to eq('aabbbcccc')
  end

  it 'decompresses with white spaces' do
    expect(rle.decompress('2 hs2q q2w2 ')).to eq('  hsqq qww  ')
  end

  it 'returns input when decompressing a compressed string' do
    inp = 'zzz ZZ  zZ'
    compressed = rle.compress(inp)
    expect(rle.decompress(compressed)).to eq(inp)
  end
end
