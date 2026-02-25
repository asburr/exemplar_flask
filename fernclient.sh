#!/bin/bash
"exec" "$(poetry --directory $(realpath $(dirname ${BASH_SOURCE[0]})) env info --path )/bin/python" "$0" "$@"
from exemplar_flask.fernclient import main
main()
