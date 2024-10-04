#!/bin/bash
#sudo ifconfig

#INTEGRANTES:
#ANDRÉS ESPINOZA 2120658
#JOSÉ SILVA GRIMALDO 2049762
#RAUL CARDENAS IBARRA 1992943

netstat -a -e | grep ESTABLISHED | more

echo

echo --------------------------------------------------------------

echo
#netstat -nr
#nmap 192.168.1.0/24
netstat tunap1 -e | grep CONNECTED
echo

echo --------------------------------------------------------------

echo

netstat -tunapl | grep ESTABLISHED || echo "No hay conexiones establecidas."
