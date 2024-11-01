$base64Encoded = "dY9RS8MwFIX/ynUIyWDKZNkYTjdSW/DFKe3Ux0ttbligpjVtGTL2311a58bA+xIO37nnntwtynUJirSxxFkYYBLFb1HMBsDUB+vPTtHrni3lU9RBbCpyZ44XmSTvz3HoHY+rYKuHE1Q3Y1GWI+FGCoVVqHMxwY2oUA8bqy52ZxGhXMlAJu2RdBwsU6W9Ay4/v6uv3MA9WNpAJ/hf3wGc9GvFoUorDqE+yGjgv2FX86ywlrIaybnC9WELfpQh3nvoiCks6NTkpG6hB9fwz+YMdnBkFdWYrVO3fzlraj31P1jMfwA="

$compressedBytes = [Convert]::FromBase64String($base64Encoded)

$compressedStream = [System.IO.MemoryStream]::new($compressedBytes)

$decompressedStream = [System.IO.MemoryStream]::new()
$decompressor = [System.IO.Compression.DeflateStream]::new($compressedStream, [System.IO.Compression.CompressionMode]::Decompress)
$decompressor.CopyTo($decompressedStream)
$decompressor.Close()

$decompressedBytes = $decompressedStream.ToArray()

$output = [Text.Encoding]::UTF8.GetString($decompressedBytes)

$output
