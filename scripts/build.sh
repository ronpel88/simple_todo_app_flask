#!/usr/bin/env bash

set -x

build_image(){
    echo "going to build image"
    ret_code=`docker build -t ${IMAGE_NAME} .`
    echo "ret_code= ${ret_code}"
}


tag_image(){
    echo "going to tag image"
    ret_code=`docker tag ${IMAGE_NAME} ${REPO_NAME}/${IMAGE_NAME}:${VERSION}.${COMMIT_ID}`
    echo "ret_code= ${ret_code}"
}


push_image_to_docker_hub(){
    echo "going to tag image"
    ret_code=`docker push ${REPO_NAME}/${IMAGE_NAME}:${VERSION}.${COMMIT_ID}`
    echo "ret_code= ${ret_code}"
}

echo $#
if [ $# -lt 2 ]
then
echo "Not enough arguments supplied..."
fi

CMD_TYPE=$1
IMAGE_NAME=$2
REPO_NAME=$3
VERSION=$4
COMMIT_ID=$5

case ${CMD_TYPE} in
    build) build_image
    ;;
    tag) tag_image
    ;;
    push) push_image_to_docker_hub
    ;;
esac
