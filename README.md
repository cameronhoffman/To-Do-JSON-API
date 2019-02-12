Python Flask JSON API
===
By [Clevyr](https://clevyr.com)

Welcome to the Python Flask JSON API Challenge!

This project is a simple To-Do list JSON API, and we need your help to complete
it. We have added 2 initial routes:

* Get all lists (GET /lists)
* Create a list (POST /lists)

You need to add the ability to:

* Update a list (PUT /lists/<list_id>)
* Delete a list (DELETE /lists/<list_id>)
* Get a list's items (GET /lists/<list_id>/items)
* Create an item for a list (POST /items)
* Update an item (PUT /items/<item_id>)
* Delete an item (DELETE /items/<item_id>)

Also - the "Create a list" route is only functioning if valid data is passed in.
The server will error if invalid data is passed in - which is not okay. Please fix
this route.

All data is stored in a SQLite database, and we have also conveniently forgotten to
add a field that tracks whether an item is complete (which should default to
`false` if it is not set). You'll have to do that too!

The database is stored in `db/todo.db` (after you copy it, that is. See the
Installation notes for more details).

## Your Job

Fork the repo, and update your own fork.

Make that repo public.

Make all the tests pass!

This includes:
* Adding a new `is_complete` `BOOL` value to the database which defaults to
  `false`.
* Making sure all of the routes return valid responses and status codes.


## Installation

Must have **Python 3** installed

```
git clone <repo>
cd <repo>
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

# Lastly, make a copy of the DB.
cp db/todo.db.original db/todo.db
```

## Commands
```
make seed # seeds the database

make run # runs the flask app

make test # runs the tests
```


## Notes

You can and should feel free to edit anything EXCEPT for the `tests` directory.
You may comment out tests as needed to make them easier to debug - but please do
not commit any changes in the test files.
