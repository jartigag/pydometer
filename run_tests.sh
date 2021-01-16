#!/bin/bash

mkdir -p public/uploads
#python -m pytest test/unit        #-v
#python -m pytest test/integration #-v

#pip install pytest-cov
#rm -r htmlcov/
python -m pytest --cov test/ #--cov-report html
