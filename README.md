# Backend-only College Enrolment System App

## Features

### - Easy to use containerization with docker

### - User System with Students, University Staff and Admins

### - JWT Authentication

### - System for creating university offers, applications and more

### - Easy to use system for students to add their exams scores

### - System for calculating students scores for each university offer

### - Asynchronous system for Accepting and Confirming Users for each Offer at Scheduled Date

## Tech Stack

### Backend
Python, Django, Django Rest Framework, Celery, Redis, Poetry

### Database
PostgreSQL

### CI/CD and DevOps
Docker, Docker Compose, Bash

## Install on Linux/WSL
### 1. Copy Repository
### 2. install docker and docker compose:
```curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh)```
### 3. get into main repository folder and type:
```make up-build```
### 4. If you wish you can load fixtures with users, universities, and offers with 
```make fixtures```
### 5. To test the repo its probably the best to use both admin panel and swagger documentation