# Authentication Service

## Table of Contents

## Introduction

The Authentication service is a backend microservice designed to handle user authentication and authorization. It uses PostgreSQL as its database and supports OAuth providers for login. This service is essential for managing user identities and securing access to other microservices in the system.

# Features

- User Registration and Login
- Password Hashing and Salting
- OAuth2.0 Integration
- JWT Token Generation and Validation
- Role-Based Access Control (RBAC)
- Multi-Factor Authentication (MFA)
- Account Lockout Mechanism
- Password Reset Functionality

## Installation

The microservice only needs the right packages installed and it's good for a simple authentication service.

## The requirements.txt

alembic==1.13.3
Authlib==1.0.0
blinker==1.8.2
certifi==2024.8.30
cffi==1.17.1
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
cryptography==43.0.1
Flask==2.2.5
Flask-Migrate==4.0.4
Flask-SQLAlchemy==3.0.3
greenlet==3.1.1
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.4
Mako==1.3.5
MarkupSafe==2.1.5
psycopg2-binary==2.9.6
pycparser==2.22
PyJWT==2.9.0
python-dotenv==1.0.0
requests==2.31.0
SQLAlchemy==2.0.35
typing_extensions==4.12.2
urllib3==2.2.3
Werkzeug==2.2.3

## Simply use the following commands to download all the requirements.txt in your root .venv file.

- python -m venv .venv // root folder

- .venv\Scripts\activate

- pip install -r backend/requirements.txt
