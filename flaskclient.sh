#!/bin/bash
"exec" "$(poetry --directory $(realpath $(dirname ${BASH_SOURCE[0]})) env info --path )/bin/python" "$0" "$@"
import sys
import os
from exemplar_flask.client import main
main()
