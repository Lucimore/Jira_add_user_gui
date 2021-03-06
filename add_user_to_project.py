from ui import *
from jira import JIRA
import requests
import json


if not baseURL or not login or not password or not project:
    input("Не все данные были введены. Запустите заново!")
    exit()

jira = JIRA(
    basic_auth=(login, password),
    options={
        'server': baseURL
    }
)

with open('mail.txt') as f:
    email_list = [line.rstrip('\n') for line in f]

user_list = []
error_list = []


def ft_find_jira_name():
    for x in email_list:
        try:
            find_me = jira.search_users(x, startAt=0, maxResults=50, includeActive=True, includeInactive=False)
            user_list.append(find_me[0].name)
        except IndexError:
            error_list.append(x)
            continue
    return user_list, error_list


users, errors = ft_find_jira_name()


def ft_add_user_to_project():
    for i in users:
        body = json.dumps({
            "user": [str(i).lower()]
        })
        response = jiraSession.request(
            "POST",
            baseURL + 'rest/api/2/project/' + project + '/role/' + role,
            data=body,
            headers={'content-type': 'application/json; charset=UTF-8'}
        )
        if response.status_code != 200:
            print(i, response.status_code, sep=" -> ")


jiraSession = requests.Session()
jiraSession.post(baseURL + '/rest/auth/1/session', auth=(login, password))
ft_add_user_to_project()
if len(errors):
    print(errors)

input("Press any key to exit...")
exit()
