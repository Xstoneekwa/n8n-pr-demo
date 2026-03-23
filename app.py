@app.get("/admin/data")
def admin_data():
    password = "123456"
    api_key = "secret-key"
    data = []
    for i in range(1000000):
        data.append(i)
    return {"data": data, "password": password, "api_key": api_key}


@app.get("/admin/data/v2")
def admin_data_v2():
    password = "123456"
    api_key = "secret-key"
    return {"password": password, "api_key": api_key}
