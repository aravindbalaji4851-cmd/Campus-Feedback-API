# Campus Feedback API

A RESTful API built with **Python, Django, and Django REST Framework** to manage student feedback and provide feedback analytics based on sentiment and category.

The API supports user registration, token-based authentication, feedback management, and summary reports. Each authenticated user can access and manage their own feedback records.

## Features

* **User Registration:** Register new users with username, email, and password.
* **Token Authentication:** Authenticate users using Django REST Framework's token authentication.
* **Create Feedback:** Submit feedback associated with a department.
* **List Feedback:** Retrieve feedback submitted by the authenticated user.
* **Retrieve Feedback:** View an individual feedback record.
* **Update Feedback:** Update existing feedback using PUT.
* **Delete Feedback:** Delete feedback records owned by the authenticated user.
* **Feedback Analytics:** Retrieve feedback counts grouped by sentiment and category.
* **Data Validation:** Validate required fields and predefined model choices.
* **Access Control:** Restrict feedback access and modifications to the record owner.

## Technologies Used

* Python
* Django
* Django REST Framework
* Django REST Framework Token Authentication
* SQLite
* Git and GitHub

## Project Structure

```text
Campus-Feedback-API/
│
├── campus_feedback/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   ├── urls.py
│   └── ...
│
├── voice_up/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── APIDOC.http
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/aravindbalaji4851-cmd/Campus-Feedback-API.git
```

### 2. Navigate to the Project Directory

```bash
cd Campus-Feedback-API
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root, alongside `manage.py`.

Add your Django secret key:

```env
SECRET_KEY=your-generated-secret-key
```

Ensure that `voice_up/settings.py` loads the environment variable and that the `.env` file is excluded from Git.

Do not commit your actual secret key or other sensitive credentials.

### 7. Apply Database Migrations

```bash
python manage.py migrate
```

### 8. Start the Development Server

```bash
python manage.py runserver
```

The development server will be available at:

`http://127.0.0.1:8000/`

## API Endpoints

The endpoints below use the URL configuration included in this project.

| Method | Endpoint                           | Description                            | Authentication |
| ------ | ---------------------------------- | -------------------------------------- | -------------- |
| POST   | `/campus_feedback/signup/`         | Register a new user                    | Not required   |
| POST   | `/campus_feedback/signin/`         | Obtain an authentication token         | Not required   |
| GET    | `/campus_feedback/feedbacks/`      | List the authenticated user's feedback | Required       |
| POST   | `/campus_feedback/feedbacks/`      | Create feedback                        | Required       |
| GET    | `/campus_feedback/feedbacks/<id>/` | Retrieve individual feedback           | Required       |
| PUT    | `/campus_feedback/feedbacks/<id>/` | Update feedback                        | Required       |
| DELETE | `/campus_feedback/feedbacks/<id>/` | Delete feedback                        | Required       |
| GET    | `/campus_feedback/summary/`        | Retrieve feedback analytics            | Required       |

**Note:** Replace `<id>` with the ID of the feedback record.

## Authentication

This project uses token-based authentication provided by Django REST Framework.

### 1. Register a User

**Request**

```http
POST /campus_feedback/signup/
Content-Type: application/json
```

**Request Body**

```json
{
    "username": "student01",
    "email": "student01@example.com",
    "password": "ExamplePassword123!"
}
```

### 2. Obtain an Authentication Token

**Request**

```http
POST /campus_feedback/signin/
Content-Type: application/json
```

**Request Body**

```json
{
    "username": "student01",
    "password": "ExamplePassword123!"
}
```

The response contains an authentication token.

### 3. Access Protected Endpoints

Include the token in the request header:

```http
Authorization: Token YOUR_TOKEN_HERE
```

Replace `YOUR_TOKEN_HERE` with the token returned by the signin endpoint.

## Feedback Management

### Create Feedback

**Request**

```http
POST /campus_feedback/feedbacks/
Content-Type: application/json
Authorization: Token YOUR_TOKEN_HERE
```

**Request Body**

```json
{
    "department": "cse",
    "feedback_text": "The college library should provide more technical books.",
    "sentiment": "neutral",
    "category": "facilities"
}
```

The feedback is associated with the authenticated user.

The department, sentiment, and category values must match the choices defined by the application.

### Retrieve Feedback

```http
GET /campus_feedback/feedbacks/1/
Authorization: Token YOUR_TOKEN_HERE
```

### Update Feedback

```http
PUT /campus_feedback/feedbacks/1/
Content-Type: application/json
Authorization: Token YOUR_TOKEN_HERE
```

**Request Body**

```json
{
    "department": "cse",
    "feedback_text": "The college library should provide more reference books and improve its facilities.",
    "sentiment": "positive",
    "category": "academics"
}
```

### Delete Feedback

```http
DELETE /campus_feedback/feedbacks/1/
Authorization: Token YOUR_TOKEN_HERE
```

Users can access or modify only feedback records they own.

## Feedback Analytics

The summary endpoint provides feedback counts grouped by sentiment and category for the authenticated user.

**Endpoint**

```http
GET /campus_feedback/summary/
Authorization: Token YOUR_TOKEN_HERE
```

**Example Response**

```json
{
    "total_feedback": 5,
    "sentiment_summary": [
        {
            "sentiment": "negative",
            "total": 2
        },
        {
            "sentiment": "neutral",
            "total": 1
        },
        {
            "sentiment": "positive",
            "total": 2
        }
    ],
    "category_summary": [
        {
            "category": "academics",
            "total": 2
        },
        {
            "category": "facilities",
            "total": 1
        },
        {
            "category": "faculty",
            "total": 2
        }
    ]
}
```

*The values above are illustrative. Actual results depend on the feedback records stored in the database.*

If the authenticated user has no feedback, the endpoint returns zero total feedback and empty summary lists.

## Testing the API

The repository includes `APIDOC.http`, which contains HTTP requests for testing the API endpoints.

You can use the HTTP Client in Visual Studio Code or another compatible REST client to execute the requests.

Before testing protected endpoints, register a user and obtain an authentication token.

Replace any token placeholders with your own token.

## Security Considerations

* Keep the Django secret key outside the source code.
* Exclude `.env` and other files containing secrets from version control.
* Do not publish real passwords or authentication tokens.
* Do not commit your local SQLite database if it contains private or development data.
* Use authentication and ownership checks to protect feedback records.
* Disable Django debug mode and configure allowed hosts appropriately before production deployment.

## Future Improvements

* Integrate automatic sentiment analysis.
* Implement backend-driven feedback categorization.
* Add PATCH support for partial feedback updates.
* Expand automated API tests.
* Deploy the API to a production environment.

## Author

**Aravind Balaji K J**

* GitHub: [aravindbalaji4851-cmd](https://github.com/aravindbalaji4851-cmd)

## License

This project was developed for learning and demonstrating Django REST Framework backend development.
