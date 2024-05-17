#!/usr/bin/env sh

echo 'Running a containers...'
docker-compose up -d

sleep 10

echo 'Replica initializations...'
docker exec -d mongo_container_1 mongosh --eval 'rs.initiate({_id: "mongo_replica_set",
                                                 members: [
                                                   { _id: 0, host: "mongo_container_1:27017" },
                                                   { _id: 1, host: "mongo_container_2:27017" }
                                                 ]})'

sleep 10

echo 'Prioritizing replicas...'

sleep 10

docker exec -d mongo_container_1 mongosh --eval 'cfg = rs.conf()
                                                 cfg.members[0].priority = 1
                                                 cfg.members[1].priority = 0.5
                                                 rs.reconfig(cfg)'

sleep 10

docker exec -d mongo_container_2 mongosh --eval 'cfg = rs.conf()
                                                 cfg.members[0].priority = 1
                                                 cfg.members[1].priority = 0.5
                                                 rs.reconfig(cfg)'

sleep 10

echo 'Application is running'
