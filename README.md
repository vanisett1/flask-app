

# FlaskApp

FlaskApp is a simple Flask web application that provides API endpoints for user management and a basic web page.

## Getting Started

1. Clone the repository:

  $$
   ```bash
   git clone <repository_url>
   cd myflaskapp
   ```
  $$

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and set your `AUTH_TOKEN`:

   ```
   AUTH_TOKEN=your_auth_token_here
   ```

5. Start the Flask app:

   ```bash
   python run.py
   ```

6. Access the web page at [http://localhost:5000](http://localhost:5000).

## API Endpoints

MyFlaskApp provides the following API endpoints for user management:

- **POST /v1/user**: Create a new user with a username and password.

- **GET /v1/user**: Retrieve user information. You can retrieve a specific user by providing a `user_id`, or retrieve all users.

- **PUT /v1/user**: Update an existing user's username and password.

- **DELETE /v1/user**: Delete an existing user based on `user_id`.

## Web Page

MyFlaskApp includes a simple web page accessible at [http://localhost:5000](http://localhost:5000).
