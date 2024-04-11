import json
import os
import requests
from bs4 import BeautifulSoup

ORG_ID = os.environ["ORG_ID"]
ORG_URL = f"https://qiita.com/organizations/{ORG_ID}/items"

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def main():
    params = {"page": 1}
    while True:
        items = get_items_of_organization(ORG_URL, params)
        if not items:
            break
        for item in items:
            item_id = item["uuid"]
            print(item_id)
            like_items(item_id, HEADERS)
        params["page"] += 1


def get_items_of_organization(url, params):
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find(
        "script",
        {"type": "application/json", "data-component-name": "OrganizationsItemsPage"},
    ).get_text()
    data = json.loads(items)
    items = data["organization"]["paginatedOrganizationArticles"]["items"]
    return items


def like_items(item_id, headers):
    like_endpoint = f"https://qiita.com/api/v2/items/{item_id}/like"
    response = requests.put(like_endpoint, headers=headers)
    if response.text:
        print(response.text)


if __name__ == "__main__":
    main()
