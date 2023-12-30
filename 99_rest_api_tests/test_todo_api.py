import requests

ENDPOINT = 'HTTPS://TODO.PIXEGAMI.IO'

response=requests.get(ENDPOINT)

print(response)

data = response.json()
print(data)

status_code = response.status_code
print(status_code)

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    pass


def test_can_create_task():
    payload = {
      "content": "tutorial on pytest and rest",
      "user_id": "tony_b",
      "task_id": "001",
      "is_done": False,
    }
    c_response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert c_response.status_code == 200
    data = c_response.json()
    print(data)
    task_id = data["task"]["task_id"]
    print(task_id)
    cmd = f'/get-task/{task_id}'
    print(cmd)
    t_response = requests.get(ENDPOINT + cmd)
    assert t_response.status_code == 200
    get_task_data = t_response.json()
    assert get_task_data['content'] == payload['content']
    assert get_task_data['user_id'] == payload['user_id']