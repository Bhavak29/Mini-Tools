#!/usr/bin/env python
import subprocess as sp #for executing commands
import optparse as op #for processing arguments passed by the user
def get_args():
    parser=op.OptionParser() #created an instance "parser" of the object "Optionparser" object
    parser.add_option("-i","--interface",dest="interface",help="Select the interface whose MAC has to be changed")
    parser.add_option("-m","--mac",dest="Updated_mac",help="New MAC address")
    (values,switch)=parser.parse_args()#parse_args will return a value switc pair
    if not values.interface:
        parser.error("[!] Please enter the name of the interface, choose --help for instructions")
    elif not values.Updated_mac:
        parser.error("[!] Please enter the new MAC, choose --help for instructions")
    return values

def change_mac(interface,Updated_mac):
    print("[*] Changing the MAC address for  " + interface + " to " + Updated_mac)
    sp.call(["ifconfig", interface, "down"])
    sp.call(["ifconfig", interface, "hw", "ether", Updated_mac])
    sp.call(["ifconfig", interface, "up"])

values=get_args()
change_mac(values.interface,values.Updated_mac)

