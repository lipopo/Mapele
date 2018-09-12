#!/bin/bash
nohup mongod --logpath db.log --dbpath db --port 10291 & mapele_backend_mongo
