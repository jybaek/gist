#!/bin/sh
SETUP()
{
	LINE=$(grep -an "exit 0$" $0  | awk -F':' '{print $1}')
    sed "1,${LINE}d" DoxygenToolkit.sh > img.tgz
}

DOIT()
{
	# add code
	# e.g. tar xzf ...; cp -rf ...; echo ...
}

FREE()
{
	# add code (e.g. rm -rf ...)
}

SETUP
DOIT
FREE

exit 0
