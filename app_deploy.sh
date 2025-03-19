#!/bin/bash

docker-compose up -d
sleep "5"
docker exec -it fastapi ./update_db.sh
