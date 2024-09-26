#!/bin/bash

# deklarasi array indirect declaration
distroLinuxDesktop[0]=BlankOn
distroLinuxDesktop[1]=Ubuntu
distroLinuxDesktop[2]=Debian
distroLinuxDesktop[3]=ArchLinux
distroLinuxDesktop[4]=LinuxMint

distroLinuxServer[0]=UbuntuServer
distroLinuxServer[1]=CentOS
distroLinuxServer[2]=FedoraServer

distroLaptop[0]=Acer
distroLaptop[1]=Lenovo
distroLaptop[3]=HP
distroLaptop[4]=Macbook
distroLaptop[5]=Toshiba

# mengambil nilai array
echo ${distroLinuxDesktop[*]}
echo ${distroLinuxServer[*]}
echo ${distroLaptop[*]}

