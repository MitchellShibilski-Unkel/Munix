import os


class MunixCMD:
    def __init__(self) -> None:
        pass

    def run(self, cmd: str):
        breakDown = cmd.split(" ")
        
        if breakDown[0] in "r":
            print(os.system(f"cat {breakDown[1]}"))
        elif breakDown[0] in "w":
            print(os.system(f"nano {breakDown[1]}"))
        elif breakDown[0] in "print":
            print(os.system(f"echo {breakDown[1:]}"))
        elif breakDown[0] in "get":
            print(os.system(f"sudo apt install {breakDown[1:]}"))
        elif breakDown[0] in "update":
            print(os.system(f"sudo apt update {breakDown[1:]}"))
        elif breakDown[0] in "uninstall":
            print(os.system(f"sudo apt uninstall {breakDown[1:]}"))
        elif breakDown[0] in "f":
            print(os.system(f"locate -b {breakDown[1:]}"))
        elif breakDown[0] in "install -py":
            count = self.__count__(breakDown)
            if count <= 2:
                print(os.system(f"sudo apt install python3-pip"))
            else:
                print(os.system(f"pip install {breakDown[1]}"))
        elif breakDown[0] in "py":
            print(os.system(f"python {breakDown[1]}"))
        else:
            print("CMD ERROR (1) :: Command Does Not Exist")

    def __count__(self, x: list):
        count = 0
        for x2 in x:
            count += 1

        return count