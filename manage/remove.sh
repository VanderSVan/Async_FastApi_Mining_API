#!/usr/bin/env bash

set -e

cd ..

set -a
source $PWD/.env
set +a

case "$1" in
--dev)
  export COMPOSE_PROJECT_NAME=ore_concentrate_dev
  echo "The development containers data are removing ..."
  docker rmi ore_concentrate-dev-flower
  docker rmi ore_concentrate-dev-celery_worker
  docker rmi ore_concentrate-dev-backend
  docker volume rm ore_concentrate-dev_ore_concentrate-db
  ;;
*)
  export COMPOSE_PROJECT_NAME=ore_concentrate
  echo "The production containers data are removing ..."
  docker rmi ore_concentrate-flower
  docker rmi ore_concentrate-celery_worker
  docker rmi ore_concentrate-backend
  docker volume rm ore_concentrate_ore_concentrate-backend ore_concentrate_ore_concentrate-db
  ;;
esac