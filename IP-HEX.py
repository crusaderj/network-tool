print("a python script to convert IP to HEX")
print("\n")
ip1 = input("please key in the first IP addrss: ")
ip2 = input("please key in the second IP address(enter to skip): ")
print("\n")

a, b, c, d = ip1.split(".")

if len(ip2) != 0:
    e, f, g, h = ip2.split(".")
    print("you have key in two IP: {} and {}".format(ip1, ip2))
    print("\n")
    print(
        "the HEX string is f108{:02x}{:02x}{:02x}\
{:02x}{:02x}{:02x}{:02x}{:02x}".format(
            int(a), int(b), int(c), int(d), int(e), int(g), int(g), int(h)
        )
    )
else:
    print("you have key in one IP: {}".format(ip1))
    print("\n")
    print(
        "the HEX string is f104{:02x}{:02x}{:02x}{:02x}".format(
            int(a), int(b), int(c), int(d)
        )
    )
