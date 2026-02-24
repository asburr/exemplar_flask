if ! which fren
then
  sudo apt update
  sudo apt-get remove --purge nodejs npm node-cacache libnode72 libnode-dev
  sudo apt-get autoremove
  sudo apt-get clean
  sudo rm -rf /var/lib/apt/lists/*
  sudo apt-get update
  curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
  sudo apt-get install -y nodejs
  sudo apt install nodejs npm -y
  sudo npm install -g fern-api
  hash -r
fi
if [  ! -d fern ]
then
  fern init --openapi openapi.json
  fern add fern-python-sdk
fi
mkdir -p fernclient
curl http://127.0.0.1:5000/openapi.json > fernclient/openapi.json
fern generate --local --group local
