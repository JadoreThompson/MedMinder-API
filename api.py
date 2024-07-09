import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from typing import List

import psycopg2
from psycopg2 import sql, IntegrityError, OperationalError
from connection import conn_params

import os
from dotenv import load_dotenv

import google.generativeai as genai
import textwrap
from IPython.display import Markdown

import hashlib


app = FastAPI()

load_dotenv('.env')

gemini_ak = os.getenv('GEMINI_API_KEY')
header = {
    'x-goog-api-key': gemini_ak
}
genai.configure(api_key=gemini_ak)
model = genai.GenerativeModel('gemini-1.5-flash')


def encrypt_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


def compare_password(password, encrypted_password):
    if encrypt_password(password) == encrypted_password:
        return True
    else:
        return False


def to_markdown(text):
    text = text.replace('.', '*')

    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


def get_explanation(medicine_name):
    prompt = f"shortly explain the use case of {medicine_name}"
    quote = model.generate_content(prompt)
    quote = quote.candidates[0].content.parts[0].text
    # quote = quote.splitlines()[0]
    quote = quote.replace('*', '')

    return quote



# all classes

class Prescription(BaseModel):
    id: int


class PrescriptionDetails(BaseModel):
    quantity: int
    mgs: int
    dosage: str
    name: str


class Patient(BaseModel):
    id: int


class PatientDetails(Patient):
    fname: str
    sname: str
    email: str
    phone: str
    password: str


class LoginUser(BaseModel):
    email: str
    password: str


class RegisterUser(BaseModel):
    fname: str
    sname: str
    email: str
    phone: str
    password: str


class UpdateUser(BaseModel):
    fname: Optional[str] = None
    sname: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None


@app.get('/')
def read_root():
    return {'status': 200, 'message': ''}


@app.get('/prescription/{prescription_id}', response_model=PrescriptionDetails)
def get_prescription(prescription_id: int):
    if not prescription_id:
        raise HTTPException(status_code=404, detail='No ID was passed"!')

    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            db_query = sql.SQL("""
                SELECT * FROM prescriptions
                WHERE id = %s;
            """)
            cur.execute(db_query, (prescription_id,))
            rows = cur.fetchone()

            if rows is None:
                raise HTTPException(status_code=401, detail='No Such Prescription')

            else:
                prescription = PrescriptionDetails(quantity=rows[3], mgs=rows[5], dosage=rows[4], name=rows[2])
                return prescription


@app.get('/prescriptions', response_model=List[PrescriptionDetails])
def get_users_prescriptions(user_id: int):
    if user_id is None:
        raise HTTPException(status_code=420, detail="Missing user id")
    else:
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                db_query = sql.SQL("""
                    SELECT * FROM users
                    WHERE id = %s;
                """)
                cur.execute(db_query, (user_id,))
                rows = cur.fetchone()

                if rows is None:
                    raise HTTPException(status_code=401, detail='No such user')
                else:
                    db_query = sql.SQL("""
                        SELECT * FROM prescriptions
                        WHERE user_id=%s;
                    """)
                    cur.execute(db_query, (user_id, ))
                    rows = cur.fetchall()

                    if rows is None:
                        raise HTTPException(status_code=404, detail="No prescriptions")
                    else:
                        users_prescriptions =[
                            PrescriptionDetails(
                                name=row[2], quantity=row[3], dosage=row[4], mgs=row[5]
                            ) for row in rows
                        ]

                        return users_prescriptions


@app.get('/find-user', response_model=List[PatientDetails])
def get_user(user_id: Optional[int] = None, email: Optional[str] = None, fname: Optional[str] = None, sname: Optional[str] = None):
    if user_id is None and email is None and fname is None and sname is None:
        raise HTTPException(status_code=404, detail="No parameters entered")
    else:
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                query_conditions = []
                query_values = []

                if user_id is not None:
                    query_conditions.append("id=%s")
                    query_values.append(user_id)
                if email is not None:
                    query_conditions.append("email=%s")
                    query_values.append(email)
                if fname is not None:
                    query_conditions.append("fname=%s")
                    query_values.append(fname)
                if sname is not None:
                    query_conditions.append("sname=%s")
                    query_values.append(sname)

                query_conditions_str = " AND ".join(query_conditions)
                db_query = sql.SQL(f"SELECT * FROM users WHERE {query_conditions_str};")
                cur.execute(db_query, query_values)
                rows = cur.fetchall()

                if rows is None:
                    raise HTTPException(status_code=404, detail="User not found")
                else:
                    list_of_patients = [
                        PatientDetails(
                            id=row[0],
                            fname=row[2],
                            sname=row[3],
                            email=row[3],
                            phone=row[4],
                            password=row[5]
                        )
                        for row in rows
                    ]

                    return list_of_patients


@app.post('/account/login', response_model=Patient)
def login(user: LoginUser):
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            db_query = sql.SQL("""
                SELECT * FROM users
                WHERE email=%s;
            """)
            cur.execute(db_query, (user.email,))
            rows = cur.fetchone()

            if rows is None:
                raise HTTPException(status_code=404, detail='User not found')

            if compare_password(user.password, rows[5]):
                return Patient(id=rows[0])
            else:
                raise HTTPException(status_code=401, detail='incorrect')


@app.post('/accounts/register', response_model=Patient)
def register_user(user: RegisterUser):
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            db_query = sql.SQL("""
                SELECT * FROM users
                WHERE email=%s;
            """)
            cur.execute(db_query, (user.email, ))
            rows = cur.fetchone()
            if rows:
                raise HTTPException(status_code=401, detail='User already exists')
            else:
                insert_script = sql.SQL("""
                    INSERT INTO users(fname,sname,email,phone,password)
                    VALUES (%s,%s,%s,%s,%s)
                    RETURNING id;
                """)
                hashed_password = encrypt_password(user.password)
                cur.execute(insert_script, (user.fname, user.sname, user.email, user.phone, hashed_password, ))
                user_id = cur.fetchone()[0]

                return Patient(id=user_id)


@app.put('/accounts/update/{user_id}', response_model=PatientDetails)
def update_user(user_id: int, update_data: UpdateUser):
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            db_query = sql.SQL("""
                SELECT * FROM users
                WHERE id=%s;
            """)
            cur.execute(db_query, (user_id, ))
            row = cur.fetchone()

            if row is None:
                raise HTTPException(status_code=404, detail="User not found")

            update_fields = []
            update_values = []

            if update_data.fname:
                update_fields.append(sql.SQL("fname = %s"))
                update_values.append(update_data.fname)
            if update_data.sname:
                update_fields.append(sql.SQL("sname = %s"))
                update_values.append(update_data.sname)
            if update_data.email:
                update_fields.append(sql.SQL("email = %s"))
                update_values.append(update_data.email)
            if update_data.phone:
                update_fields.append(sql.SQL("phone = %s"))
                update_values.append(update_data.phone)
            if update_data.password:
                update_fields.append(sql.SQL("password = %s"))
                update_values.append(update_data.password)

            # If no valid fields provided for update
            if not update_fields:
                raise HTTPException(status_code=400, detail="No valid fields provided for update")

            # Add user_id as the last value in update_values
            update_values.append(user_id)

            # Construct and execute the update query
            update_query = sql.SQL("""
                UPDATE users
                SET {}
                WHERE id = %s
                RETURNING *;
            """).format(sql.SQL(', ').join(update_fields))

            cur.execute(update_query, update_values)
            updated_user = cur.fetchone()

            if updated_user is None:
                raise HTTPException(status_code=401, detail="Failed to update user")

            return PatientDetails(
                id=updated_user[0],
                fname=updated_user[1],
                sname=updated_user[2],
                email=updated_user[3],
                phone=updated_user[4],
                password=updated_user[5]
            )


@app.delete('/accounts/delete/{user_id}')
def delete_user(user_id: int):
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            db_query = sql.SQL("""
                SELECT * FROM users
                WHERE id=%s;
            """)
            cur.execute(db_query, (user_id, ))
            row = cur.fetchone()

            if row is None:
                raise HTTPException(status_code=404, detail="User not found")
            else:
                delete_query = sql.SQL("""
                    DELETE FROM users
                    WHERE id=%s;
                """)
                cur.execute(delete_query, (user_id, ))
                conn.commit()

                return "Successfully Deleted"


@app.post('/create-medicine')
def create_medicine(prescription: PrescriptionDetails, user_id: int):
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            insert_script = sql.SQL("""
                INSERT INTO prescriptions (user_id, name, quantity, dosage, mgs)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
            """)
            cur.execute(insert_script, (user_id, prescription.name, prescription.quantity, prescription.dosage, prescription.mgs, ))
            prescription_id = cur.fetchone()[0]

            return Prescription(id=prescription_id)


@app.post('/get-explanation')
def explain(medicine_name: str):
    print("Medicine Name: ", medicine_name)
    try:
        explanation = get_explanation(medicine_name)
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Error: {e}")

    return explanation


if __name__ == '__main__':
    uvicorn.run('api:app', host='0.0.0.0', port=80, reload=True)

