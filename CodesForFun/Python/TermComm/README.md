# TermComm

Two terminal apps that talk to a MongoDB database.

| App | File | What it does |
| --- | --- | --- |
| Public Messaging | `MM.py` | A shared chat room: sign up, log in, send messages and refresh to see everyone else's |
| Blogger | `MessagingBlogger/MB.py` | A small blog: admins create and delete posts, users read them |

## Running it

Both apps read the database connection string from the `MONGODB_URI`
environment variable, so no login details are stored in the code.

```bash
pip install -r requirements.txt
export MONGODB_URI="mongodb+srv://<user>:<password>@<cluster>/?retryWrites=true&w=majority"

python MM.py
python MessagingBlogger/MB.py
```

## Notes

- Passwords are stored as salted PBKDF2 hashes, not plain text.
- Blogger post and user IDs (`P0001`, `U0000`, `A0000`) are always one more
  than the highest ID in use, so an ID is never reused after a post is deleted.

## Built with

Python, pymongo, MongoDB Atlas
