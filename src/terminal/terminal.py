import os
import zlib


class MunixCMD:
    def __init__(self, compressionLevel = "High") -> None:
        self.compressLevel = compressionLevel

    def getCMD(self):
        userIn = input("MUNIX >> ")
        return userIn

    def run(self):
        _in = input("MUNIX >> ")
        self.CMD(_in)

    def CMD(self, cmd: str):
        breakDown = cmd.split(" ")
        
        if breakDown[0] in "r":
            print(os.system(f"cat {breakDown[1]}\n"))
        elif breakDown[0] in "w":
            print(os.system(f"nano {breakDown[1]}\n"))
        elif breakDown[0] in "print":
            print(os.system(f"echo {breakDown[1:]}\n"))
        elif breakDown[0] in "get":
            print(os.system(f"sudo apt install {breakDown[1:]}\n"))
        elif breakDown[0] in "update":
            print(os.system(f"sudo apt update {breakDown[1:]}\n"))
        elif breakDown[0] in "remove":
            print(os.system(f"sudo apt uninstall {breakDown[1:]}\n"))
        elif breakDown[0] in "f":
            print(os.system(f"locate -b {breakDown[1:]}\n"))
        elif cmd == "get -py":
            print(os.system("sudo apt install python3-pip\n"))
        elif cmd == "get -rs":
            print(os.system("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh\n"))
        elif cmd in "get -py [":
                libs = cmd.split("[")[-1].strip("]")
                print(os.system(f"pip install {libs}\n"))
        elif breakDown[0] in "py":
            print(os.system(f"python {breakDown[1]}"))
        elif breakDown[0] in "compile-c":
            print(os.system(f"gcc {breakDown[1]} -o {breakDown[2]}\n"))
        elif breakDown[0] in "compress":
            self.compress(breakDown[1:])
            print(f"{breakDown[1:]} Compressed\n")
        elif breakDown[0] in "decompress":
            self.decompress(breakDown[1:])
            print(f"{breakDown[1:]} Decompressed\n")
        elif breakDown[0] in "user":
            if breakDown[1] in "-a":
                print(os.system(f"sudo useradd {breakDown[2]}\n"))
            elif breakDown[1] in "-r":
                print(os.system(f"userdel {breakDown[2]}\n"))
            elif breakDown[1] in "-l":
                print(os.system("awk -F: '{print $1}' /etc/passwd\n"))
            elif breakDown[1] in "-f":
                print(os.system(f"sudo passwd --expire {breakDown[2]}\n"))
            else:
                print("CMD ERROR :: User Command Does Not Exist\nCan Only Use [-r][-a][-l][-f]\n")
        elif breakDown[0] in "help" or breakDown[0] in "-h":
            print("Command Name\tFunction\tCommand\nr\tRead\tr [FILE]\nw\tWrite\tw [FILE]\nf\tFind\tf [FILE]\ncompile\tGCC Compiler\tcompile [FILE] [EXE NAME]\nprint\tEcho\tprint [MESSAGE]\nget\tInstaller\tget [-py, -rs *OPTIONAL] | [LIBRARIES *OPTIONAL]\nupdate\tUpdater\tupdate [NAME]\nremove\tUninstaller\tremove [NAME]\ncompress\tCompressor\tcompress [FILE]\ndecompress\tDecompressor\tdecompress [FILE]\npy\tPython Runner\tpy [FILE]\n")
        else:
            os.system(f"{breakDown[0:]}")
            
    def compress(self, file):
        match self.level:
            case "Low":
                zlib.compress(file, level=1)
            case "Medium":
                zlib.compress(file, level=4)
            case "High":
                zlib.compress(file, level=9)

    def decompress(self, file):
        zlib.decompress(file)

    def __count__(self, x: list):
        count = 0
        for x2 in x:
            count += 1

        return count
    