print('a python script to convert IP to HEX for WLC DHCP option 43')
print('\n')
ip1 = input('please key in the first IP addrss: ')
ip2 = input('please key in the second IP address(enter to skip): ')
print('\n')


def ip_to_hex(ip1, ip2=''):
    ''' convert the IP to INT, then convert to HEX '''
    address1 = ip1.split(".")
    num1 = 0
    for (i, value) in enumerate(address1):
        part = 8 * (i+1)
        value = int(value) << (32 - part)
        num1 = value + num1
    hex_string = '{:x}'.format(num1)
    if len(ip2) != 0:
        print('you have key in two IP: {} and {}'.format(ip1, ip2))
        address2 = ip2.split(".")
        num2 = 0
        for (i, value) in enumerate(address2):
            part = 8 * (i+1)
            value = int(value) << (32 - part)
            num2 = value + num2
        print('\n')
        hex_string = hex_string + '{:x}'.format(num2)
        return(hex_string)
    else:
        print('you have key in one IP: {}'.format(ip1))
        return(hex_string)


def main():
    hex_string = ip_to_hex(ip1, ip2)
    print('-'*40)
    if len(hex_string) == 8:
        print('the hex string is \033[01m\033[31mf104{}\033[0m'.format(hex_string.upper()))
    else:
        print('the hex string is \033[01m\033[31mf108{}\033[0m'.format(hex_string.upper()))


if __name__ == "__main__":
    main()
