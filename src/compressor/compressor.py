import zlib


class MunixCompressor:
    def __init__(self, file: str, compressionLevel = "High"):
        self.file = file
        self.level = compressionLevel

    def compress(self):
        match self.level:
            case "Low":
                zlib.compress(self.file, level=1)
            case "Medium":
                zlib.compress(self.file, level=4)
            case "High":
                zlib.compress(self.file, level=9)

    def decompress(self):
        zlib.decompress(self.file)