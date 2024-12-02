import streamlit
import pandas 
import streamlit.web.cli as stcli
import streamlit.runtime.scriptrunner.magic_funcs
import os, sys
from main import algo
import  gui
from  sql import func


def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path


if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("gui/__main__.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())

#cxfreeze --script main.py
#cx_freeze