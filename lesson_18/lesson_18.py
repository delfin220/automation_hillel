import requests

BASE_URL = "https://images-api.nasa.gov"


search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

response = requests.get(search_url, params=search_params)
print(f"Search status: {response.status_code}")

items = response.json()["collection"]["items"]
print(f"Знайдено items: {len(items)}")


nasa_ids = []
for item in items:
    nasa_id = item["data"][0]["nasa_id"]
    nasa_ids.append(nasa_id)

print(f"Зібрано nasa_id: {len(nasa_ids)}")
downloaded = 0

for nasa_id in nasa_ids:

    asset_url = f"{BASE_URL}/asset/{nasa_id}"
    asset_response = requests.get(asset_url)
    asset_items = asset_response.json()["collection"]["items"]


    jpg_url = None
    for asset_item in asset_items:
        href = asset_item["href"]
        if href.endswith(".jpg"):
            jpg_url = href


    img_response = requests.get(jpg_url)
    filename = f"mars_photo{downloaded + 1}.jpg"

    with open(filename, "wb") as f:
        f.write(img_response.content)

    downloaded += 1
    print(f"Збережено: {filename}")

    if downloaded == 2:
        break

print(f"\nГотово! Скачано файлів: {downloaded}")