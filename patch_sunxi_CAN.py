# file: patch_sunxi_CAN.py
# author: (c) Menschel 2017
# purpose: as SUNXI kernel repositories do not feature device tree overlays, 
#          this is a quick hack to activate CAN for the board
#          just call it in the make file before compiling dts


def patch(fpath):
    with open(fpath,"a") as f:
        f.write("""&can0 {
	pinctrl-names = "default";
	pinctrl-0 = <&can0_pins_a>;
	status = "okay";
};""")


if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-p", "--path", dest="path", default="linux/arch/arm/boot/dts/sun7i-a20-bananapi.dts",
                      help="PATH to the file which should be patched", metavar="PATH")

    (options, args) = parser.parse_args()
    patch(fpath=options.path)
