# API Documentation

## Overview

This API provides a set of endpoints to manage users, prescriptions, and provide explanations for medicines using a generative model. It uses FastAPI as the framework and PostgreSQL as the database.

## Base URL

The base URL for all endpoints is `/`.

## Authentication

No authentication is required for these endpoints.

## Endpoints

### General Endpoints

### Root Endpoint

**GET /**

**Response:**

```json
{
  "status": 200,
  "message": ""
}

```

### Prescription Endpoints

### Get Prescription by ID

**GET /prescription/{prescription_id}**

Fetch a prescription by its ID.

**Path Parameters:**

- `prescription_id` (int): The ID of the prescription to fetch.

**Response:**

- `200 OK` with a JSON object containing prescription details.
- `404 Not Found` if no ID was passed.
- `401 Unauthorized` if the prescription is not found.

**Response Model:**

```json
{
  "quantity": int,
  "mgs": int,
  "dosage": string,
  "name": string
}

```

### Get User's Prescriptions

**GET /prescriptions**

Fetch all prescriptions for a specific user.

**Query Parameters:**

- `user_id` (int): The ID of the user whose prescriptions to fetch.

**Response:**

- `200 OK` with a JSON array of prescription details.
- `420 Missing user id` if user_id is not provided.
- `401 Unauthorized` if the user is not found.
- `404 Not Found` if no prescriptions are found for the user.

**Response Model:**

```json
[
  {
    "name": string,
    "quantity": int,
    "dosage": string,
    "mgs": int
  }
]

```

### Create a Prescription

**POST /create-medicine**

Create a new prescription for a user.

**Body Parameters:**

- `prescription` (Prescription Details): Details of the prescription to be created.
- `user_id` (int): The ID of the user to whom the prescription belongs.

**Response:**

- `200 OK` with a JSON object containing the prescription ID.
- `404 Not Found` if the user is not found.

**Response Model:**

```json
{
  "id": int
}

```

### User Endpoints

### Find User

**GET /find-user**

Find a user by various parameters.

**Query Parameters:**

- `user_id` (Optional[int]): The ID of the user to find.
- `email` (Optional[string]): The email of the user to find.
- `fname` (Optional[string]): The first name of the user to find.
- `sname` (Optional[string]): The surname of the user to find.

**Response:**

- `200 OK` with a JSON array of user details.
- `404 Not Found` if no parameters are entered or the user is not found.

**Response Model:**

```json
[
  {
    "id": int,
    "fname": string,
    "sname": string,
    "email": string,
    "phone": string,
    "password": string
  }
]

```

### Login User

**POST /account/login**

Login a user with email and password.

**Body Parameters:**

- `user` (LoginUser): The login credentials.

**Response:**

- `200 OK` with a JSON object containing the user ID.
- `404 Not Found` if the user is not found.
- `401 Unauthorized` if the password is incorrect.

**Response Model:**

```json
{
  "id": int
}

```

### Register User

**POST /accounts/register**

Register a new user.

**Body Parameters:**

- `user` (RegisterUser): The user registration details.

**Response:**

- `200 OK` with a JSON object containing the user ID.
- `401 Unauthorized` if the user already exists.

**Response Model:**

```json
{
  "id": int
}

```

### Update User

**PUT /accounts/update/{user_id}**

Update user details.

**Path Parameters:**

- `user_id` (int): The ID of the user to update.

**Body Parameters:**

- `update_data` (UpdateUser): The user details to update.

**Response:**

- `200 OK` with a JSON object containing the updated user details.
- `404 Not Found` if the user is not found.
- `401 Unauthorized` if the update fails.
- `400 Bad Request` if no valid fields are provided for update.

**Response Model:**

```json
{
  "id": int,
  "fname": string,
  "sname": string,
  "email": string,
  "phone": string,
  "password": string
}

```

### Delete User

**DELETE /accounts/delete/{user_id}**

Delete a user.

**Path Parameters:**

- `user_id` (int): The ID of the user to delete.

**Response:**

- `200 OK` with a message "Successfully Deleted".
- `404 Not Found` if the user is not found.

**Response:**

```json
"Successfully Deleted"

```

### Medicine Explanation Endpoint

### Get Medicine Explanation

**POST /get-explanation**

Get a brief explanation of the use case of a medicine using a generative model.

**Body Parameters:**

- `medicine_name` (str): The name of the medicine.

**Response:**

- `200 OK` with a string explanation of the medicine's use case.
- `401 Unauthorized` if there is an error with the generative model.

**Response:**

```json
"explanation of the medicine's use case"

```

## Data Models

### Prescription Details

```json
{
  "quantity": int,
  "mgs": int,
  "dosage": string,
  "name": string
}

```

### Patient Details

```json
{
  "id": int,
  "fname": string,
  "sname": string,
  "email": string,
  "phone": string,
  "password": string
}

```

### LoginUser

```json
{
  "email": string,
  "password": string
}

```

### RegisterUser

```json
{
  "fname": string,
  "sname": string,
  "email": string,
  "phone": string,
  "password": string
}

```

### UpdateUser

```json
{
  "fname": string,
  "sname": string,
  "email": string,
  "phone": string,
  "password": string
}

```

## Improvements

### Caching

At first, making calls to the API had some latency issues whether or not that was because of the hosting provider I wasn’t sure however I wanted to prevent it being from something I could control. The backend.

And so I decided to make the first step be caching.

Caching is the temporary storage of values / data such that instead of making a new connection to the DB, increasing costs, latency and delay, we can grab said data from the cache which is a drastically quicker alternative.

The response time from the /login route was:

```python
Duration: 1.4123912391239 
```

After performing a simple cache:

```python
Duration: 0.920147180557251
```

To achieve this i used the cahce_tools module, utilising the cached decorator to get it below 

### SQL Queries

Unnecessary loading of columns can slow down an API response due to the redundancy. to fix this, when checking for existing users I did

```python
SELECT id FROM table_name
WHERE email=%s
```

By doing this, we load only one column and one item drastically improving response time, bringing us into the sub 1s
