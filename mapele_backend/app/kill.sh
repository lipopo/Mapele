#!/bin/bash

ps -aux | grep mapele_backend_app | grep -r grep | awk '{print $2}' | xargs kill -9