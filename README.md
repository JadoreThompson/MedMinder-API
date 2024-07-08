## Introduction

API Documentation

Base URL

```
<https://chubby-guineafowl-zenzgroup-794982a0.koyeb.app/>

```

---

1. Get Prescription Details

Endpoint

```
GET /prescription/{prescription_id}

```

Description

Fetch the details of a prescription by its ID.

Parameters

- `prescription_id` (int): The ID of the prescription.

Response

```json
{
    "quantity": int,
    "mgs": int,
    "dosage": str,
    "name": str
}

```

---

1. Get User's Prescriptions

Endpoint

```
GET /prescriptions

```

Description

Fetch all prescriptions for a specific user.

Parameters

- `user_id` (int): The ID of the user.

Response

```json
[
    {
        "quantity": int,
        "mgs": int,
        "dosage": str,
        "name": str
    }
]

```

---

1. Find User

Endpoint

```
GET /find-user

```

Description

Find users based on the provided parameters.

Parameters (Optional)

- `user_id` (int): The ID of the user.
- `email` (str): The email of the user.
- `fname` (str): The first name of the user.
- `sname` (str): The surname of the user.

Response

```json
[
    {
        "id": int,
        "fname": str,
        "sname": str,
        "email": str,
        "phone": str,
        "password": str
    }
]

```

---

1. Login

Endpoint

```
POST /account/login

```

Description

Authenticate a user using their email and password.

Request Body

```json
{
    "email": str,
    "password": str
}

```

Response

```json
{
    "id": int
}

```

---

1. Register User

Endpoint

```
POST /accounts/register

```

Description

Register a new user.

Request Body

```json
{
    "fname": str,
    "sname": str,
    "email": str,
    "phone": str,
    "password": str
}

```

Response

```json
{
    "id": int
}

```

---

1. Update User

Endpoint

```
PUT /accounts/update/{user_id}

```

Description

Update user details.

Parameters

- `user_id` (int): The ID of the user to update.

Request Body

```json
{
    "fname": str (optional),
    "sname": str (optional),
    "email": str (optional),
    "phone": str (optional),
    "password": str (optional)
}

```

Response

```json
{
    "id": int,
    "fname": str,
    "sname": str,
    "email": str,
    "phone": str,
    "password": str
}

```

---

1. Delete User

Endpoint

```
DELETE /accounts/delete/{user_id}

```

Description

Delete a user by their ID.

Parameters

- `user_id` (int): The ID of the user to delete.

Response

```json
"Successfully Deleted"

```

---

1. Create Medicine

Endpoint

```
POST /create-medicine

```

Description

Create a new prescription for a user.

Parameters

- `user_id` (int): The ID of the user.

Request Body

```json
{
    "quantity": int,
    "mgs": int,
    "dosage": str,
    "name": str
}

```

Response

```json
{
    "id": int
}

```

---

1. Get Medicine Explanation

Endpoint

```
POST /get-explanation

```

Description

Get a short explanation of a medicine's use case.

Request Body

```json
{
    "medicine_name": str
}

```

Response

```json
"explanation": str

```

---

Running the API

To run the API, use the following command:

```bash
uvicorn api:app --host 0.0.0.0 --port 5000 --reload

```

Environment Variables

Ensure you have a `.env` file with the following content:

```
GEMINI_API_KEY=your_gemini_api_key_here

```

Database Connection

Configure your database connection parameters in `connection.py`:

```python
conn_params = {
    'dbname': 'your_db_name',
    'user': 'your_db_user',
    'password': 'your_db_password',
    'host': 'your_db_host',
    'port': 'your_db_port'
}

```

Note

Replace placeholders (e.g., `your_gemini_api_key_here`, `your_db_name`, etc.) with actual values.

This documentation provides an overview of all the available endpoints, their parameters, request bodies, and responses for the API.

## Introduction

### Overview:

This pill reminder aims to significantly improve medication adherence, a critical issue with the long-term conditions. Studies reveal a startling statistic: between 30 and 50% of prescribed medication for long-term illnesses aren’t taken as directed. This non-adherence translates to:

- **Missed doses:** People often forget medications, leading to missed days or incorrect time slots. This disrupts the treatment cycle and can reduce medication effectiveness.
- **Cramming:** To "catch up," patients might take multiple doses at once, which can be dangerous and lead to overdoses or adverse side effects.
- **Discontinuation:** Feeling overwhelmed or frustrated with complex medication schedules, some patients simply abandon their medication regimen altogether, putting their health at risk.

By using this pill reminder you can prevent these side-effects from occurring as the saying goes that prevention is better than cure. As a result:

- **Better health outcomes:** Consistent medication intake leads to better disease management and reduced risk of complications.
- **Reduced healthcare costs:** Proper medication use can prevent unnecessary hospital visits and emergency room admissions.
- **Improved quality of life:** Effective treatment can alleviate symptoms and allow you to live a more active and fulfilling life. As well as lift the smiles of your loved ones as they don’t enjoy seeing you in a harmful state.

### Features:

The pill reminder will host the necessary features for ensuring proper adherence to medication:

- **Automated Tracking**: The app automatically tracks your medication usage and calculates remaining doses

### Overview:

This pill reminder aims to significantly improve medication adherence, a critical issue with the long-term conditions. Studies reveal a startling statistic: between 30 and 50% of prescribed medication for long-term illnesses aren’t taken as directed. This non-adherence translates to:

- **Missed doses:** People often forget medications, leading to missed days or incorrect time slots. This disrupts the treatment cycle and can reduce medication effectiveness.
- **Cramming:** To "catch up," patients might take multiple doses at once, which can be dangerous and lead to overdoses or adverse side effects.
- **Discontinuation:** Feeling overwhelmed or frustrated with complex medication schedules, some patients simply abandon their medication regimen altogether, putting their health at risk.

By using this pill reminder you can prevent these side-effects from occurring as the saying goes that prevention is better than cure. As a result:

- **Better health outcomes:** Consistent medication intake leads to better disease management and reduced risk of complications.
- **Reduced healthcare costs:** Proper medication use can prevent unnecessary hospital visits and emergency room admissions.
- **Improved quality of life:** Effective treatment can alleviate symptoms and allow you to live a more active and fulfilling life. As well as lift the smiles of your loved ones as they don’t enjoy seeing you in a harmful state.

### Features

The pill reminder will host the necessary features for ensuring proper adherence to medication:

- **Automated Tracking**: The app automatically tracks your medication usage and calculates remaining doses

## Vision

**Why:**
I’m creating this project to help remind people to take their medication as it’s very easy to forget to do so especially in these modern lives of having to work pretty much all day then travel backa n hour or so. As well as this in my personal life I’ve been a victim of forgetting to take medication and having a notification can help. I t’ll also ensure people are taken the specified dosage.

**Whom**:
this product will be marketed towards anyone who has a prescription but if i could say anyone I’d say the younger generation as they live the busiest lives however the older generation shouldn’t be written off.

**How:**
I’ll be producing a mobile app as this is the easiest way to get the notifications in and it’s , for most people, the place they spend more time rather than a laptop or PC.

## Focus

- [ ]  Simple UI - Use Structured as a base
- [ ]  Calendar with the days and number on top with the items below in the main screen showing a fraction and a checklist if all completed

## Functionalities

- [ ]  Evenly spread periodic notifications
- [ ]  Short explanation of what the pill does. Use a Gemini Prompt
- [ ]  A page showing remaining number of pills within pack
- [ ]  Break through notifications in case user has Airplane Mode turned on
- [ ]  Manual Pill Adding
- [ ]  Reliability, many users complained app stopped working after a number of pills were added
- [ ]  Some users want a chime similar to TradingView as their notification
- [ ]  Add good size boundary for buttons to allow ease of use
- [ ]  Allow for repeating notifications in case the first one is missed ( this is normally the case)
- [ ]  Allow users to update checklist through the watch
- [ ]  Make it cheap

API Documentation

Base URL

```
<https://chubby-guineafowl-zenzgroup-794982a0.koyeb.app/>

```

---

1. Get Prescription Details

Endpoint

```
GET /prescription/{prescription_id}

```

Description

Fetch the details of a prescription by its ID.

Parameters

- `prescription_id` (int): The ID of the prescription.

Response

```json
{
    "quantity": int,
    "mgs": int,
    "dosage": str,
    "name": str
}

```

---

1. Get User's Prescriptions

Endpoint

```
GET /prescriptions

```

Description

Fetch all prescriptions for a specific user.

Parameters

- `user_id` (int): The ID of the user.

Response

```json
[
    {
        "quantity": int,
        "mgs": int,
        "dosage": str,
        "name": str
    }
]

```

---

1. Find User

Endpoint

```
GET /find-user

```

Description

Find users based on the provided parameters.

Parameters (Optional)

- `user_id` (int): The ID of the user.
- `email` (str): The email of the user.
- `fname` (str): The first name of the user.
- `sname` (str): The surname of the user.

Response

```json
[
    {
        "id": int,
        "fname": str,
        "sname": str,
        "email": str,
        "phone": str,
        "password": str
    }
]

```

---

1. Login

Endpoint

```
POST /account/login

```

Description

Authenticate a user using their email and password.

Request Body

```json
{
    "email": str,
    "password": str
}

```

Response

```json
{
    "id": int
}

```

---

1. Register User

Endpoint

```
POST /accounts/register

```

Description

Register a new user.

Request Body

```json
{
    "fname": str,
    "sname": str,
    "email": str,
    "phone": str,
    "password": str
}

```

Response

```json
{
    "id": int
}

```

---

1. Update User

Endpoint

```
PUT /accounts/update/{user_id}

```

Description

Update user details.

Parameters

- `user_id` (int): The ID of the user to update.

Request Body

```json
{
    "fname": str (optional),
    "sname": str (optional),
    "email": str (optional),
    "phone": str (optional),
    "password": str (optional)
}

```

Response

```json
{
    "id": int,
    "fname": str,
    "sname": str,
    "email": str,
    "phone": str,
    "password": str
}

```

---

1. Delete User

Endpoint

```
DELETE /accounts/delete/{user_id}

```

Description

Delete a user by their ID.

Parameters

- `user_id` (int): The ID of the user to delete.

Response

```json
"Successfully Deleted"

```

---

1. Create Medicine

Endpoint

```
POST /create-medicine

```

Description

Create a new prescription for a user.

Parameters

- `user_id` (int): The ID of the user.

Request Body

```json
{
    "quantity": int,
    "mgs": int,
    "dosage": str,
    "name": str
}

```

Response

```json
{
    "id": int
}

```

---

1. Get Medicine Explanation

Endpoint

```
POST /get-explanation

```

Description

Get a short explanation of a medicine's use case.

Request Body

```json
{
    "medicine_name": str
}

```

Response

```json
"explanation": str

```

---

Running the API

To run the API, use the following command:

```bash
uvicorn api:app --host 0.0.0.0 --port 5000 --reload

```

Environment Variables

Ensure you have a `.env` file with the following content:

```
GEMINI_API_KEY=your_gemini_api_key_here

```

Database Connection

Configure your database connection parameters in `connection.py`:

```python
conn_params = {
    'dbname': 'your_db_name',
    'user': 'your_db_user',
    'password': 'your_db_password',
    'host': 'your_db_host',
    'port': 'your_db_port'
}

```

Note

Replace placeholders (e.g., `your_gemini_api_key_here`, `your_db_name`, etc.) with actual values.

This documentation provides an overview of all the available endpoints, their parameters, request bodies, and responses for the API.

## Introduction

### Overview:

This pill reminder aims to significantly improve medication adherence, a critical issue with the long-term conditions. Studies reveal a startling statistic: between 30 and 50% of prescribed medication for long-term illnesses aren’t taken as directed. This non-adherence translates to:

- **Missed doses:** People often forget medications, leading to missed days or incorrect time slots. This disrupts the treatment cycle and can reduce medication effectiveness.
- **Cramming:** To "catch up," patients might take multiple doses at once, which can be dangerous and lead to overdoses or adverse side effects.
- **Discontinuation:** Feeling overwhelmed or frustrated with complex medication schedules, some patients simply abandon their medication regimen altogether, putting their health at risk.

By using this pill reminder you can prevent these side-effects from occurring as the saying goes that prevention is better than cure. As a result:

- **Better health outcomes:** Consistent medication intake leads to better disease management and reduced risk of complications.
- **Reduced healthcare costs:** Proper medication use can prevent unnecessary hospital visits and emergency room admissions.
- **Improved quality of life:** Effective treatment can alleviate symptoms and allow you to live a more active and fulfilling life. As well as lift the smiles of your loved ones as they don’t enjoy seeing you in a harmful state.

### Features:

The pill reminder will host the necessary features for ensuring proper adherence to medication:

- **Automated Tracking**: The app automatically tracks your medication usage and calculates remaining doses

API Documentation

Base URL

```
<https://chubby-guineafowl-zenzgroup-794982a0.koyeb.app/>

```

---

1. Get Prescription Details

Endpoint

```
GET /prescription/{prescription_id}

```

Description

Fetch the details of a prescription by its ID.

Parameters

- `prescription_id` (int): The ID of the prescription.

Response

```json
{
    "quantity": int,
    "mgs": int,
    "dosage": str,
    "name": str
}

```

---

1. Get User's Prescriptions

Endpoint

```
GET /prescriptions

```

Description

Fetch all prescriptions for a specific user.

Parameters

- `user_id` (int): The ID of the user.

Response

```json
[
    {
        "quantity": int,
        "mgs": int,
        "dosage": str,
        "name": str
    }
]

```

---

1. Find User

Endpoint

```
GET /find-user

```

Description

Find users based on the provided parameters.

Parameters (Optional)

- `user_id` (int): The ID of the user.
- `email` (str): The email of the user.
- `fname` (str): The first name of the user.
- `sname` (str): The surname of the user.

Response

```json
[
    {
        "id": int,
        "fname": str,
        "sname": str,
        "email": str,
        "phone": str,
        "password": str
    }
]

```

---

1. Login

Endpoint

```
POST /account/login

```

Description

Authenticate a user using their email and password.

Request Body

```json
{
    "email": str,
    "password": str
}

```

Response

```json
{
    "id": int
}

```

---

1. Register User

Endpoint

```
POST /accounts/register

```

Description

Register a new user.

Request Body

```json
{
    "fname": str,
    "sname": str,
    "email": str,
    "phone": str,
    "password": str
}

```

Response

```json
{
    "id": int
}

```

---

1. Update User

Endpoint

```
PUT /accounts/update/{user_id}

```

Description

Update user details.

Parameters

- `user_id` (int): The ID of the user to update.

Request Body

```json
{
    "fname": str (optional),
    "sname": str (optional),
    "email": str (optional),
    "phone": str (optional),
    "password": str (optional)
}

```

Response

```json
{
    "id": int,
    "fname": str,
    "sname": str,
    "email": str,
    "phone": str,
    "password": str
}

```

---

1. Delete User

Endpoint

```
DELETE /accounts/delete/{user_id}

```

Description

Delete a user by their ID.

Parameters

- `user_id` (int): The ID of the user to delete.

Response

```json
"Successfully Deleted"

```

---

1. Create Medicine

Endpoint

```
POST /create-medicine

```

Description

Create a new prescription for a user.

Parameters

- `user_id` (int): The ID of the user.

Request Body

```json
{
    "quantity": int,
    "mgs": int,
    "dosage": str,
    "name": str
}

```

Response

```json
{
    "id": int
}

```

---

1. Get Medicine Explanation

Endpoint

```
POST /get-explanation

```

Description

Get a short explanation of a medicine's use case.

Request Body

```json
{
    "medicine_name": str
}

```

Response

```json
"explanation": str

```

---

Running the API

To run the API, use the following command:

```bash
uvicorn api:app --host 0.0.0.0 --port 5000 --reload

```

Environment Variables

Ensure you have a `.env` file with the following content:

```
GEMINI_API_KEY=your_gemini_api_key_here

```

Database Connection

Configure your database connection parameters in `connection.py`:

```python
conn_params = {
    'dbname': 'your_db_name',
    'user': 'your_db_user',
    'password': 'your_db_password',
    'host': 'your_db_host',
    'port': 'your_db_port'
}

```

Note

Replace placeholders (e.g., `your_gemini_api_key_here`, `your_db_name`, etc.) with actual values.

This documentation provides an overview of all the available endpoints, their parameters, request bodies, and responses for the API.

## Introduction

### Overview:

This pill reminder aims to significantly improve medication adherence, a critical issue with the long-term conditions. Studies reveal a startling statistic: between 30 and 50% of prescribed medication for long-term illnesses aren’t taken as directed. This non-adherence translates to:

- **Missed doses:** People often forget medications, leading to missed days or incorrect time slots. This disrupts the treatment cycle and can reduce medication effectiveness.
- **Cramming:** To "catch up," patients might take multiple doses at once, which can be dangerous and lead to overdoses or adverse side effects.
- **Discontinuation:** Feeling overwhelmed or frustrated with complex medication schedules, some patients simply abandon their medication regimen altogether, putting their health at risk.

By using this pill reminder you can prevent these side-effects from occurring as the saying goes that prevention is better than cure. As a result:

- **Better health outcomes:** Consistent medication intake leads to better disease management and reduced risk of complications.
- **Reduced healthcare costs:** Proper medication use can prevent unnecessary hospital visits and emergency room admissions.
- **Improved quality of life:** Effective treatment can alleviate symptoms and allow you to live a more active and fulfilling life. As well as lift the smiles of your loved ones as they don’t enjoy seeing you in a harmful state.

### Features:

The pill reminder will host the necessary features for ensuring proper adherence to medication:

- **Automated Tracking**: The app automatically tracks your medication usage and calculates remaining doses