if [ ! -d opc_venv ]
then
  python -m venv opc_venv
  opc_venv/bin/pip install openapi-python-client
  opc_venv/bin/pip install ruff
fi
mkdir -p openapi_python_client
source opc_venv/bin/activate && opc_venv/bin/openapi-python-client generate --url http://127.0.0.1:5000/openapi.json --overwrite --output-path openapi_python_client
