#!/bin/bash

val_normal=$(< normal.txt)

echo "Nombre de machines vendues: $val_normal" | mail -s "Historique des transactions machine" yashthevalil@gmail.com
