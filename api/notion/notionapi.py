import requests

base_url = 'https://api.notion.com/v1'
token = 'secret_36REZ6tYNixmAVcndf3toygapV99NTtfzbDMjsYUHAJ'

# Retrieve a page
url = '/pages/b151b883e2234e139edebb74f1d4fc4e'
headers = {
    # "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "Authorization": "Bearer " + token
}
response = requests.get(url=base_url + url, headers=headers)
print(response.text)

# todo
# Create a page
url = '/pages'
headers = {
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "content-type": "application/json",
    "Authorization": "Bearer " + token
}
req = {
    "parent": {
        "database_id": "f446f4d4a5ae4fc79d4111d6ee26b220"
    },
    "properties": {
        "Type": {
            "select": {
                "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
                "name": "Article",
                "color": "default"
            }
        },
        # "Score /5": {
        #     "select": {
        #         "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
        #         "name": "⭐️⭐️⭐️⭐️⭐️",
        #         "color": "default"
        #     }
        # },
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "New Media Article"
                    }
                }
            ]
        },
        "Status": {
            "select": {
                "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                "name": "Ready to Start",
                "color": "yellow"
            }
        },
        "Publisher": {
            "select": {
                "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
                "name": "The Atlantic",
                "color": "red"
            }
        },
        "Publishing/Release Date": {
            "date": {
                "start": "2020-12-08T12:00:00Z",
                # "end": null
            }
        },
        "Link": {
            "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
        },
        "Summary": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                        # "link": null
                    },
                    "annotations": {
                        "bold": False,
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                        "code": False,
                        "color": "default"
                    },
                    "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                    # "href": null
                }
            ]
        },
        "Read": {
            "checkbox": False
        }
    }
}
response = requests.post(url=base_url + url, headers=headers, json=req)
print(response.text)

# Retrieve a block
url = '/blocks/68af9b80c6a54127bf2e991a140a0d0d'
headers = {
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "Authorization": "Bearer " + token
}
response = requests.get(url=base_url + url, headers=headers)
print(response.text)

# Create a database
url = '/databases'
headers = {
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "Authorization": "Bearer " + token
}
req = {
    "parent": {
        "type": "page_id",
        "page_id": "b151b883e2234e139edebb74f1d4fc4e"
    },
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List"
                # "link": null
            }
        }
    ],
    "properties": {
        "Name": {
            "title": {}
        },
        "Description": {
            "rich_text": {}
        },
        "In stock": {
            "checkbox": {}
        },
        "Food group": {
            "select": {
                "options": [
                    {
                        "name": "🥦Vegetable",
                        "color": "green"
                    },
                    {
                        "name": "🍎Fruit",
                        "color": "red"
                    },
                    {
                        "name": "💪Protein",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Price": {
            "number": {
                "format": "dollar"
            }
        },
        "Last ordered": {
            "date": {}
        },
        "Store availability": {
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "name": "Duc Loi Market",
                        "color": "blue"
                    },
                    {
                        "name": "Rainbow Grocery",
                        "color": "gray"
                    },
                    {
                        "name": "Nijiya Market",
                        "color": "purple"
                    },
                    {
                        "name": "Gus's Community Market",
                        "color": "yellow"
                    }
                ]
            }
        },
        "+1": {
            "people": {}
        },
        "Photo": {
            "files": {}
        }
    }
}
# response = requests.post(url=base_url + url, headers=headers, json=req)
# print(response.text)
