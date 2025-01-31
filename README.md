# HNG Intership Task 0

## A simple RESTFul API built with Flask
This project is a simple REST API built using the python Flask framework.
It provides a single endpoint `/` which returns a JSON response containing an email address, a GitHub repository URL, and the current date-time in ISO format.

## User Guide
1. This project requires python 3, run `python --version` to confirm python version or install python 3 from https://www.python.org/downloads/

2. Clone the repository `git clone https://github.com/mubarak-mustopha/hng-task0.git` and navigate into the project folder `cd hng-task0`

3. Run the following command to install dependencies `python - m pip install -r requirements.txt`

4. Start the server with the command `python app.py`


## API Documentation
### Endpoint
`GET / `

### Request Format
No request body is needed

### Reponse Format
A JSON object with the following fields
```
{
    "email": "hngemail@example.com",
    "github_url": "https://github.com/user/repo.git", 
    "current_datetime": "YYYY-MM-DDThh:mm:ssZ"
}
```

## BackLinks
To Find and Hire Talented Node.js Developers:

[Hire Python Developers](https://hng.tech/hire/python-developers)  
