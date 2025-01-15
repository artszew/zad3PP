import requests

BASE_URL = "http://localhost:5000/api/data"


def test_get_all_data():
    new_data_1 = {
        "width": 1.5,
        "height": 2.5,
        "species": 1
    }
    new_data_2 = {
        "width": 3.5,
        "height": 4.5,
        "species": 2
    }

    response_1 = requests.post(BASE_URL, json=new_data_1)
    assert response_1.status_code == 201
    print("POST /api/data (first data point):", response_1.json())

    response_2 = requests.post(BASE_URL, json=new_data_2)
    assert response_2.status_code == 201
    print("POST /api/data (second data point):", response_2.json())

    response = requests.get(BASE_URL)
    assert response.status_code == 200

    data = response.json()
    assert len(data) == 2, f"Expected 2 data points, but got {len(data)}"
    print("GET /api/data: ", data)


def test_post_data():
    new_data = {
        "width": 1.5,
        "height": 2.5,
        "species": 1
    }
    # Send POST request to add new data
    response = requests.post(BASE_URL, json=new_data)
    assert response.status_code == 201
    response_data = response.json()
    print("POST /api/data:", response_data)
    return response_data.get("id")


def test_delete_data():
    new_data = {
        "width": 3.5,
        "height": 4.5,
        "species": 2
    }

    post_response = requests.post(BASE_URL, json=new_data)
    assert post_response.status_code == 201
    new_record_id = post_response.json().get("id")

    delete_response = requests.delete(f"{BASE_URL}/{new_record_id}")
    assert delete_response.status_code == 200
    print(f"DELETE /api/data/{new_record_id}: ", delete_response.json())


def test_post_invalid_data():
    invalid_data_width = {"width": -1, "height": 2, "species": 3}
    response = requests.post(BASE_URL, json=invalid_data_width)
    assert response.status_code == 400
    print("POST /api/data with invalid data:", response.json())

    invalid_data_height = {"width": 1, "height": "abc", "species": 3}
    response = requests.post(BASE_URL, json=invalid_data_height)
    assert response.status_code == 400
    print("POST /api/data with invalid data:", response.json())

    invalid_data_species = {"width": 1, "height": 2, "species": -3}
    response = requests.post(BASE_URL, json=invalid_data_species)
    assert response.status_code == 400
    print("POST /api/data with invalid data:", response.json())


def test_delete_nonexistent_record():
    invalid_id = 99999
    response = requests.delete(f"{BASE_URL}/{invalid_id}")
    assert response.status_code == 404
    print(f"DELETE /api/data/{invalid_id}:", response.json())


if __name__ == "__main__":
    test_get_all_data()
    test_post_data()
    test_delete_data()
    test_post_invalid_data()
    test_delete_nonexistent_record()
