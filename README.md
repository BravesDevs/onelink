# Onelink

Onelink helps the people by keeping all the updated urls of the professional 
sites at one place so whenever you update your linkedin or your portfolio site url, you don't have to remember and update anywhere else instead in Onelink


## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See installation
for notes on installing the project on a system.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- [Python](https://www.contributor-covenant.org/)
## Installation

- Clone the repository into your local machine.
- Make sure you have python installed in your machine.
- Create a virtual environment using following command.
```bash
python -m venv <env_name>
```
- Install the packages by running the following command.
```bash
pip install -r requirement.txt
```
- Migrate the models.
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
- Run the project.

```bash
python manage.py runserver
```
