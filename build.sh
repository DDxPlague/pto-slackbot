#!/bin/bash
unset VERSION_NUMBER

CORRECT_USAGE_STRING="script usage: build.sh [-v some_version_number_here i.e 0.0.1-SNAPSHOT]"

while getopts 'v:' OPTION; do
  case "$OPTION" in
    v)
      echo "VERSION_NUMBER = $OPTARG"
      VERSION_NUMBER=$OPTARG
      ;;
    *)
      echo "$CORRECT_USAGE_STRING" >&2
      exit 1
      ;;
  esac
done

#Veryf the version number has been passed in. If not, spit out the correct usage string to the user.
if [ -z "$VERSION_NUMBER" ]
then
  echo "$CORRECT_USAGE_STRING" >&2
  exit 1
fi

build_docker_image(){
  echo "Running docker build -t ddxplague/pto-slackbot:$VERSION_NUMBER ."
  /usr/local/bin/docker build -t ddxplague/pto-slackbot:$VERSION_NUMBER .
}

build_docker_image
