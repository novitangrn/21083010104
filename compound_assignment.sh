#!/bin/bash

# deklarasi array
distroLinuxDesktop=('BlankOn' 'Ubuntu' 'Debian' 'ArchLinux' 'LinuxMint')
distroLinuxServer=('UbuntuServer' 'CentOS' 'FedoraServer')
distroLaptop=('Acer' 'HP' 'Macbook' 'Toshiba' 'Lenovo')

# mengambil nilai array
echo ${distroLinuxDesktop[*]}
echo ${distroLinuxServer[*]}
echo ${distroLaptop[*]}
