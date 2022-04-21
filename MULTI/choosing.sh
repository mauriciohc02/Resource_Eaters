#!/bin/sh

echo "Running $EATER program"

if [ $EATER == "cpu" ]
then
    python3 cpu.py
elif [ $EATER == "disk" ]
then
    python3 disk.py
elif [ $EATER == "mem" ]
then
    python3 mem.py
elif [ $EATER == "net" ]
then
    python3 net.py
else
    echo "You didn't choose any option"
fi
