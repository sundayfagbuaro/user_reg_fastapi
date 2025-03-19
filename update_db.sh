#!/bin/bash
alembic revision --autogenerate -m "first commit"
alembic upgrade head
alembic revision --autogenerate -m "create user table"
alembic upgrade head

