ROOT=openapi_client
echo $ROOT
mkdir $ROOT
curl http://127.0.0.1:5000/openapi.json > $ROOT/openapi.json
docker run --rm -v "${PWD}:/local" \
    -u "$(id -u):$(id -g)" \
    openapitools/openapi-generator-cli generate \
    -i /local/$ROOT/openapi.json \
    -g python \
    -o /local/$ROOT \
    --additional-properties=library=urllib3,python_version=3.10
