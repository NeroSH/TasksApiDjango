# TasksApiDjango
Back-end app with basic usage of API.

## Basic usage

note represents JSON 
`
{
  "id": int,
  "title": "string",
  "content": "string"
}
`

Method | URL | Response
------------ | ------------ | -------------
GET | http://127.0.0.1:8000/notes | List of all notes
GET | http://127.0.0.1:8000/notes?query=string | Get note that contains query in title ot content
GET | http://127.0.0.1:8000/notes/{id} | Get a note by id
POST | http://127.0.0.1:8000/notes/ | Create a note with `title` and `content` [JSON should look like `{ "title": "string", "content": "string" }`] Returns json with object with `id`, `title`, `content`
PUT | http://127.0.0.1:8000/notes/{id} | Updates a note with `title` and `content` [JSON should look like `{ "title": "string", "content": "string" }`]
DELETE | http://127.0.0.1:8000/notes/{id} | Deletes a note by id

## How to run project
1 - Clone repository via command 
`git clone  https://github.com/NeroSH/TasksApiDjango`
, then navigate to the project root

2 - Activate virtual environment `/venv/Scrips/activate`

3 - fire a command `./manage.py migrate`

4 - now you can run sever by `./manage.py runserver`

## Examples
If you have no problems when running server, open 
http://127.0.0.1:8000/docs . Youll see available options for project

