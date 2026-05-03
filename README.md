# GitHub User Activity CLI

A simple **Python CLI tool** that fetches and displays the most recent public activity of a GitHub user directly in the terminal.

This project was built using only the **Python standard library**, without external dependencies.

---

## 📌 Features

- Fetches recent public GitHub activity using the GitHub API
- Displays events in a readable format in the terminal
- Handles common errors such as:
  - User not found (404)
  - API rate limit exceeded (403)
  - No internet connection

---

## 🛠 Requirements

- Python 3.x
- Internet connection

No external libraries are required.

---

## 📂 Project Structure

.
├── github_activity.py
└── README.md


---

## 🚀 How to Run

Clone the repository and run the script using Python:

```bash
python github_activity.py <username>
```

Example:

```bash
python github_activity.py torvalds
```

## Example Output

Recent activity for GitHub user: torvalds

- Pushed 2 commit(s) to torvalds/linux
- Starred someuser/somerepo
- Forked torvalds/linux

## How It Works

The script sends a request to the GitHub public events endpoint:

https://api.github.com/users/<username>/events/public

Then it parses the JSON response and converts the events into readable messages such as:

- Push events
- Stars (watch events)
- Forks
- Issue updates
- Pull request actions

## Common Errors
User not found

If the username does not exist:

Error: User not found.

API rate limit exceeded

If you make too many requests in a short time:

Error: API rate limit exceeded. Try again later.

No internet / connection issues

If GitHub cannot be reached:

Error: Could not connect to GitHub.