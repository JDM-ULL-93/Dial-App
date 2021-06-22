import sys
import subprocess
from pathlib import Path
dial_modules = [
    Path("./dial-core"),
    Path("./dial-gui"),
    Path("./dial-basic-nodes"),
    Path("./dial-visualization"),
] 


def install_modules():
    for module in dial_modules:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", str(module)])


install_modules()