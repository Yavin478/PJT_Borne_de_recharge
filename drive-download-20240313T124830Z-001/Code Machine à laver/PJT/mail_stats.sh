#!/bin/bash

val_normal=$(< normal.txt)

#echo "Nombre de machines vendues: $val_normal" | mail -s "Historique des transactions machine" a.libereau@residam.com
#echo "Nombre de machines vendues: $val_normal" | mail -s "Historique des transactions machine" tresors.kin@gadz.org
#echo "Nombre de machines vendues: $val_normal" | mail -s "Historique des transactions machine" info.kin@gadz.org


wget -q --tries=1 --timeout=5 --spider http://google.com
if [[ $? -eq 0 ]]; then
        echo "Online" > network_status.txt
	echo "Nombre de machines vendues: $val_normal" | mail -s "Historique des transactions machine" a.libereau@residam.com
	echo "Nombre de machines vendues: $val_normal" | mail -s "Historique des transactions machine" tresors.kin@gadz.org
	echo "Nombre de machines vendues: $val_normal" | mail -s "Historique des transactions machine" info.kin@gadz.org
	rm normal.txt
else
        echo "Offline" > network_status.txt
fi
