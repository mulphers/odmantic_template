#!/bin/bash

sleep 10

mongosh --host mongo_container_1:27017 <<EOF
  var cfg = {
    "_id": "mongo_replica_set",
    "members": [
      {
        "_id": 0,
        "host": "mongo_container_1:27017",
        "priority": 2
      },
      {
        "_id": 1,
        "host": "mongo_container_2:27017",
        "priority": 0
      }
    ]
  };
  rs.initiate(cfg);
EOF
