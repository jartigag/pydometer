#!/bin/bash

mkdir -p public/uploads
python -m pytest test/unit -v
#python -m pytest test/integration
