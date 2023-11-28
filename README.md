

# FlaskApp

FlaskApp is a simple Flask web application that provides API endpoints for user management and a basic web page.

## Getting Started

1. **Clone the repository:**

   ```
   git clone https://github.com/vanisett1/flask-app
   cd flask-app
   ```

2. **Create a virtual environment and activate it:**

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install project dependencies:**

   ```
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the project root and set your `AUTH_TOKEN`:**

   ```
   AUTH_TOKEN=your_auth_token_here
   ```

5. **Start the Flask app:**

   ```
   python run.py
   ```

6. **Access the web page at [http://localhost:5000](http://localhost:5000).**

## Dockerfile

Alteratively use Dockerfile to build and run the container for local testing.

## API Endpoints

FlaskApp provides the following API endpoints for user management:

- **POST /v1/user**: Create a new user with a username and password.
- **GET /v1/user**: Retrieve user information. You can retrieve a specific user by providing a `user_id`, or retrieve all users.
- **PUT /v1/user**: Update an existing user's username and password.
- **DELETE /v1/user**: Delete an existing user based on `user_id`.

## Web Page

MyFlaskApp includes a simple web page accessible at [http://localhost:5000](http://localhost:5000).


## CLI Tool - client_api.py

The `client_api.py` script is a command-line tool for interacting with the FlaskApp's user management API. This tool allows you to create, update, retrieve, and delete users via the command line. It's designed to be interactive and user-friendly, utilizing the `inquirer` library for enhanced user experience.

### Features:

- **Interactive Menu**: Navigate through options using arrow keys.
- **CRUD Operations**: Easily create, read, update, and delete users.
- **Dynamic API Interaction**: Communicates with the API server for real-time data processing.

### Usage:

1. Ensure Python is installed on your system.
2. Run the script in your terminal:

   ```
   python client_api.py
   ```

3. Follow the interactive prompts to manage users. You will need the `AUTH_TOKEN` provided by the FlaskApp for authentication.

### Operations:

- **Create User**: Add a new user by providing a username and password.
- **Update User**: Modify details of an existing user.
- **Get User**: Retrieve information about one or all users.
- **Delete User**: Remove a user from the system.

This tool sends requests to the FlaskApp API server hosted at `https://ufoalien.azurewebsites.net`.

** Change BASE_URL to http://localhost:5000 for local testing**


---

# Continuous Deployment

Our FlaskApp is configured for Continuous Deployment using GitHub Actions, as defined in the `main_ufoalien.yaml` file. This setup automates the process of deploying our Flask application to Azure Web App whenever changes are pushed to the `main` branch.

## Deployment Workflow

The `main_ufoalien.yaml` workflow consists of two primary jobs: `build` and `deploy`. Here's an overview of each step in the workflow:

### Build Job

1. **Set up Docker Buildx**: Prepares Docker for building the container image.
2. **Log in to registry**: Authenticates with Azure Container Registry to store the Docker image.
3. **Build and push container image to registry**: Creates a Docker image from the Flask app and pushes it to the Azure Container Registry.

### Deploy Job

1. **Deploy to Azure Web App**: Takes the Docker image from the registry and deploys it to the specified Azure Web App. This step also sets the environment for deployment (`production`) and uses a publish profile for authentication.


## How to Trigger Deployment

The deployment process is triggered automatically whenever changes are pushed to the `main` branch. Additionally, you can manually trigger a deployment using the `workflow_dispatch` event in GitHub Actions.

## Monitoring Deployment

After each push to `main`, you can monitor the progress of your deployment in the Actions tab of your GitHub repository. Successful deployment will update your Flask application on the Azure Web App service.

Making this change to deploy flask-api to Azure webapps