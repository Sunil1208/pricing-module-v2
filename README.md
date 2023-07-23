
# Pricing Module V2

Pricing Module V2 is a Django-based web application that allows users to manage pricing configurations for a ride-hailing service. It provides an easy-to-use interface for creating, updating, and managing pricing configurations, and also calculates the pricing for a ride based on the provided parameters.

## Features

User-friendly interface for managing pricing configurations.
Calculation of ride pricing based on distance, ride time, and waiting time.
Logging of pricing configurations changes and HTTP requests.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

## Prerequisites

Make sure you have the following software installed:

Python (version 3.6 or higher)
Django (version 4.2.3)
Virtual environment tool (e.g., virtualenv, conda)



## Installation

Install my-project with npm

```bash
git clone https://github.com/your_username/pricing_module_v2.git
cd pricing_module_v2
```

Create and active a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```
    
Install the project dependencies

```bash
pip install -r requirements.txt
```


## Database Setup

The project uses a SQLite database by default. You can create and apply the database migrations using the following commands:

```bash
python manage.py migrate
```
## Usage

To start the development server, run the following command:

```bash
python manage.py runserver
```

You can now access the application at http://127.0.0.1:8000/

## Logging
The application logs two types of events:

HTTP requests log: Logs all incoming HTTP requests to `http_requests.log`.

Pricing module log: Logs pricing configurations changes and creations to `pricing_module.log`.
## Administration

The Django admin panel provides an interface for managing pricing configurations. To access the admin panel, create a superuser with the following command:

```bash
python manage.py createsuperuser
```

Then, go to http://127.0.0.1:8000/admin/, log in with the superuser credentials, and you can manage pricing configurations from there.