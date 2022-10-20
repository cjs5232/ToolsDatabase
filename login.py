"""
filename: login.py
Author: Brett Lubberts
Description: File containing and functions that query the database to log
a user in, or create a new user
"""

from typing import Optional
from psycopg2.errors import IntegrityError
from psycopg2.extensions import cursor

"""
log in a user if that user exists
@param cur: the cursor to the database
@param username: the users username
@param password: the users password
@return True if logging in was successful, False if credentials were incorrect, None if error
"""


def login_user(cur: cursor, username: str, password: str) -> Optional[bool]:
    try:
        cur.execute(
            f"update users set last_access = now() where username = '{username}' and password = '{password}'")
    except:
        return None

    return cur.rowcount > 0


"""
create a new user and add them to the database
@param cur: the cursor to the database
@param username: the new users username
@param password: the new users password
@param fname: the new users first name
@param lname: the new users last name
@param email: the new users email
@return None if an error occurred, otherwise whether the new user was created
"""


def create_user(cur: cursor, username: str, password: str, fname: str, lname: str, email: str) -> Optional[bool]:
    try:
        cur.execute(
            f"insert into users values ('{username}', '{password}', '{fname}', '{lname}', '{email}')")
    except IntegrityError:
        return False
    except:
        return None

    return True
