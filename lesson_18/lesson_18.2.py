import requests

BASE_URL = "http://127.0.0.1:8080"

image_path = "mars_photo1.jpg"
image_filename = "mars_photo1.jpg"



print(" Завантажуємо картинку на сервер...")

with open(image_path, "rb") as image_file:
    files = {"image": image_file}
    upload_response = requests.post(f"{BASE_URL}/upload", files=files)

print(f"Код відповіді: {upload_response.status_code}")
print(f"Відповідь сервера: {upload_response.json()}")

image_url = upload_response.json()["image_url"]
print(f"   URL картинки: {image_url}\n")



print(" Отримуємо URL картинки з сервера...")

headers = {"Content-Type": "text"}
get_response = requests.get(
    f"{BASE_URL}/image/{image_filename}",
    headers=headers
)

print(f"Код відповіді: {get_response.status_code}")
print(f"Відповідь сервера: {get_response.json()}\n")


print("Видаляємо картинку з сервера...")

delete_response = requests.delete(f"{BASE_URL}/delete/{image_filename}")

print(f"Код відповіді: {delete_response.status_code}")
print(f"Відповідь сервера: {delete_response.json()}\n")

print("запити виконані успішно!")