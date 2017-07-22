# file: patch_sunxi_CAN.py
# author: (c) Menschel 2017
# purpose: as SUNXI kernel repositories do not feature device tree overlays, 
#          this is a quick hack to activate CAN for the board
#          just call it in the make file before compiling dts
import os

def patch(fpath):
    needpatch = False
    with open(fpath) as f:
        needpatch = not ("&can0" in f.read())
    if needpatch:
        print("patching {0}".format(os.path.split(fpath)[-1]))
        with open(fpath,"a") as f:
            f.write("""&can0 {
	pinctrl-names = "default";
	pinctrl-0 = <&can0_pins_a>;
	status = "okay";
};""")
        print("patched {0}".format(os.path.split(fpath)[-1]))
    else:
        print("no patch required")


if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-p", "--path", dest="path", default="linux/arch/arm/boot/dts/sun7i-a20-bananapi.dts",
                      help="PATH to the file which should be patched", metavar="PATH")

    (options, args) = parser.parse_args()
    patch(fpath=options.path)
