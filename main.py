import sys
import json
import urllib.request
import urllib.error

def main():
    if len(sys.argv)>1:
        username = sys.argv[1]
        url = (f'https://api.github.com/users/{username}/events/public')
        events = fetch_github_activity(url)
        if not events:
            sys.exit(1)
        print(f'========== Recent activity for the user: {username} =========\n\n')
        for event in events:
            print_event(event)
    else:
        print('you need to write a user')

def fetch_github_activity(url):
    headers = {
            "User-Agent": "Python-GitHub-Activity-CLI"
    }
    request = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(request) as response:
            data =  response.read().decode('utf-8')
            return json.loads(data)

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print('Error: User not found')
        elif e.code == 403:
            print('Error: API rate limit exceeded. Try again later.')
        else:
            print(f'HTTP Error: {e.code}')
        return None
    except urllib.error.URLError:
        print('Error: could not connect to GitHub.')
        return None

def print_event(event):
    event_type = event.get("type")
    username = sys.argv[1]
    repo = event.get("repo", {}).get("name", "Unknown repo")

    if event_type == "PushEvent":
        print(f'Pushed commit(s) to {repo}')

    elif event_type == "CreateEvent":
        print(f'create the repo: "{repo}"')
    elif event_type == "WatchEvent":
        print(f'starred the repo: {repo}')
    elif event_type == "ForkEvent":
        print(f'Forked {repo}')
    else:
        print(f'{event_type} in {repo}')
if __name__ == '__main__':
    main()
