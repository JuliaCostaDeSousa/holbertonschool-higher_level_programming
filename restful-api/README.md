# RESTful API Project

This project is part of Holberton School's curriculum "[C#26] Foundations v2.1 - Part 2" and demonstrates various ways to consume and build RESTful APIs in Python. It covers essential concepts of HTTP, API consumption, API creation with `http.server` and Flask, as well as authentication techniques using Basic Auth and JWT.

## 📚 Description

In today's interconnected digital environment, RESTful APIs are crucial for systems to communicate and exchange data efficiently. This project guides students through the fundamentals and best practices of consuming, developing, and securing RESTful APIs.

## 📚 Table of contents

- [Task 0 – HTTP vs HTTPS](#task-0)
- [Task 1 – Use curl to consume an API](#task-1--consume-data-from-an-api-using-curl)
- [Task 2 – Consume and process API data in Python](#task-2--consume-and-process-api-data-using-python)
- [Task 3 – Develop an API with http.server](#task-3--develop-a-simple-api-using-httpserver)
- [Task 4 – Develop a Flask API](#task-4--develop-a-simple-api-using-flask)
- [Task 5 – Secure API with Auth](#task-5--api-security-and-authentication-techniques)
- [📁 Files Overview](#-files-overview)
- [▶️ How to Use](#-how-to-use)

---

## Task 0
### 📡 HTTP vs HTTPS

- HTTP (HyperText Transfer Protocol)
HTTP (HyperText Transfer Protocol) is a client-server communication protocol where the client (typically a web browser) sends a request to a web server, which then returns a response (such as an HTML page, image, or data). HTTP operates over TCP, ensuring reliable data transmission between both ends.

- HTTPS (HyperText Transfer Protocol Secure)
HTTPS (HyperText Transfer Protocol Secure) is the secure version of HTTP. It uses TLS (Transport Layer Security) to encrypt the connection between the client and the server, ensuring that data exchanged remains confidential and cannot be intercepted or altered by unauthorized parties. This is essential for protecting sensitive information like passwords, credit card numbers, or personal data.

---

### 📨 Structure of an HTTP request

An HTTP request is composed of a series of text lines sent over the Internet to initiate communication with a server. It begins with the request line, which includes:
- the method (e.g., GET, POST, PUT, DELETE),
- the request target (typically a URI),
- and the HTTP version.

This is followed by a set of header fields, which are divided into:
- general headers (applicable to both request and response),
- request-specific headers (e.g., Host, User-Agent),
- and representation headers (e.g., Content-Type, Content-Length).

These headers provide metadata about the request. After the headers, an empty line indicates the end of the header section. If the method supports a payload (such as POST, PUT, or PATCH), the request body follows, containing the data to be processed by the server.

---

### 📨 Structure of an HTTP response

An HTTP response is structured similarly. It begins with the status line, which contains:
- the HTTP version,
- a status code (e.g., 200, 404, 500),
- and a reason phrase describing the status (e.g., "OK", "Not Found").

Next come the header fields, including:
- response headers (e.g., Server, Set-Cookie),
- and representation headers (describing the returned content).

As with the request, an empty line separates the headers from the optional response body, which contains the resource or data associated with the request—if the request was successful and the server returns content.

---

### 🔧 Common HTTP methods

| Method  | Description                                                                 | Use-case                                   |
|----------|-----------------------------------------------------------------------------|-----------------------------------------------|
| **POST** | Sends data to the server to create a new resource. The server processes the data and returns a response                     | Submitting a form, posting a comment, uploading a file |
| **PUT**  | Sends data to create or replace the entire representation of a resource at the target URI                                 | Updating a full user profile, replacing a document               |
| **DELETE** | Requests the server to delete the specified resource                                     | Deleting a user account, removing a file or record           |
| **CONNECT** | Establishes a tunnel to the server, typically used to relay encrypted traffic (e.g., HTTPS) through an HTTP proxy | Setting up an HTTPS connection via an HTTP proxy                  |

---

### 📊 Common HTTP status code

| Code | Description                        | Scenario                                    |
|------|--------------------------------------|-----------------------------------------------------------------|
| 200  | OK – The request was successful and the server returned the expected response                | Accessing a website URL and the homepage loads correctly                       |
| 201  | Created – The request was successful and a new resource was created   | Sending a POST request to create a new user, and the server confirms the creation                     |
| 400  | Bad Request – The server cannot process the request due to malformed syntax       | Sending a request with missing or invalid JSON data in the body         |
| 409  | Conflict – This occurs when a request conflicts with the current state of the server   | When two users try to update the same resource at the same time — say, editing a profile — and the system detects that the changes would overwrite each other without proper resolution |
| 500  | The server encountered an unexpected condition. | A bug in the backend code causes a crash during a request                        |

---

## Task 1 – Consume data from an API using curl

### 🧰 Tools Used
- `curl`: command-line HTTP client
- Tested API: [JSONPlaceholder](https://jsonplaceholder.typicode.com)

### 📦 Example Commands

- Display all posts:

```bash
curl https://jsonplaceholder.typicode.com/posts
```

- Display only HTTP headers:

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

- Send a simulated POST request:

```
bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```

## Task 2 – Consume and process API data using Python

Python script using the `requests` and `csv` modules to fetch and manipulate API data.

- `fetch_and_print_posts()`:
  - Fetches post data from JSONPlaceholder
  - Prints post titles
- `fetch_and_save_posts()`:
  - Writes `id`, `title`, `body` into `posts.csv`

---

## Task 3 – Develop a simple API using http.server

Custom API built using Python’s `http.server` module with multiple endpoints:

- `/` → Welcome text
- `/data` → Returns JSON: `{ "name": "John", "age": 30, "city": "New York" }`
- `/status` → Returns "OK"
- `/info` → Returns version info
- Other routes → 404 error message

---

## Task 4 – Develop a simple API using Flask

Lightweight API with user management using a Python dictionary:

- `/` → Welcome message
- `/data` → List of usernames
- `/status` → Returns "OK"
- `/users/<username>` → Returns user details or 404
- `/add_user` [POST] → Add user via JSON

Error handling included for missing username or invalid payloads.

---

## Task 5 – API Security and Authentication Techniques

### Basic Auth (`/basic-protected`)
- Uses `flask_httpauth`
- Requires valid credentials (e.g. `user1` / `password`)

### JWT Authentication
- `POST /login` → Returns JWT token
- `GET /jwt-protected` → Requires valid token
- `GET /admin-only` → Accessible only to users with `"role": "admin"`

Includes handlers for:
- Missing/invalid/expired tokens (returns 401)
- Unauthorized access (returns 403)

---

## 📁 Files Overview

| File                    | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `task_02_requests.py`   | Consume and process API data with Python.                                   |
| `task_03_http_server.py`| API using built-in `http.server`.                                           |
| `task_04_flask.py`      | Basic Flask API for user data handling.                                     |
| `task_05_basic_security.py` | Flask API secured with Basic Auth and JWT.                           |

---

## ▶️ How to Use

### Python API Consumption
```bash
python3 task_02_requests.py
```

### Run Basic API with `http.server`
```bash
python3 task_03_http_server.py
```

### Run Flask API
```bash
python3 task_04_flask.py
```

### Run Flask API with Authentication
```bash
python3 task_05_basic_security.py
```

Test routes with:
- `curl`
- Postman
- Python script

---

## Author

Julia Costa de Sousa
