import sys
import json
import urllib.request
import urllib.error

def main():
    if len(sys.argv)>1:
        username = ' '.join(sys.argv[1:])
        url = (f'https://api.github.com/users/{username}/events/public')
        print(fetch_github_activity(url))
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


if __name__ == '__main__':
    main()
