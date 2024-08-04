#!/usr/bin/python3

## LINUX ONLY

## Build Flags
#
# --windows [default:linux] - compile target for windows
# --gdb [default:disabled] - enables cmd debugger
#
##

import os, sys, subprocess
from random import random, uniform

CC = "g++"
C = "gcc"

libs = []  # ex -lGL


def genmain():
    o = []

    HEADER = genheader()
    BPLATE = genbplate()

    o.extend(
        [
            HEADER,
            "int main() {",
            BPLATE,
        ]
    )

    o.append("}")
    o = "\n".join(o)
    return o


def genheader():
    CODE = r"""
    #include <stdio.h>
    """
    return CODE


def genbplate():
    CODE = r"""
    return 0;
    """

    return CODE


srcdir = os.path.abspath(".")


def build():
    cpps = []
    obfiles = []
    ffl = []

    open("/tmp/gen.tc.main.cpp", "wb").write(genmain().encode("utf-8"))
    file = "/tmp/gen.tc.main.cpp"
    print(file)
    ofile = "%s.o" % file
    obfiles.append(ofile)
    cpps.append(file)
    cmd = [
        #'gcc',
        CC,
        "-c",  ## do not call the linker
        "-fPIC",  ## position indepenent code
        "-o",
        ofile,
        os.path.join(file),
    ]
    print(cmd)
    subprocess.check_call(cmd)

    ctr = 1
    for ff in ffl:
        fn = "gen.tc." + ctr + ".cpp"
        open("/tmp/" + fn, "wb").write(ff().encode("utf-8"))
        file = "/tmp/" + fn
        print(file)
        ofile = "%s.o" % file
        obfiles.append(ofile)
        cpps.append(file)
        cmd = [
            #'gcc',
            CC,
            "-c",  ## do not call the linker
            "-fPIC",  ## position indepenent code
            "-o",
            ofile,
            os.path.join(file),
        ]
        print(cmd)
        subprocess.check_call(cmd)

    os.system("ls -lh /tmp/*.o")

    ## finally call the linker,
    ## note: there's better linkers we could use here, like gold and mold

    cmd = (
        [
            #'ld',
            CC,
            "-shared",
            "-o",
            "/tmp/thermo.so",
        ]
        + obfiles
        + libs
    )

    print(cmd)
    subprocess.check_call(cmd)

    exe = "/tmp/thermo"
    cmd = [
        CC,
        "-o",
        exe,
    ]
    cmd += obfiles + libs

    print(cmd)

    subprocess.check_call(cmd)


print("building...")
build()

if "--gdb" in sys.argv:
    cmd = ["gdb", "/tmp/thermo"]
else:
    cmd = ["/tmp/thermo"]

print(cmd)

subprocess.check_call(cmd, cwd=srcdir)
# sys.exit()

## TODO: get working from python for testing
import ctypes

os.chdir(srcdir)

thermo_so = "/tmp/thermo.so"

dll = ctypes.CDLL(thermo_so)
print(dll)

print(dll.main)
dll.main()

print("hello!")
