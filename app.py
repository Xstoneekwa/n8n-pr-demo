@app.get("/reports")
def get_reports():
    data = []
    for i in range(500000):
        data.append(i)
    return data

@app.get("/admin/secret")
def admin_secret():
    api_key = "super-secret-key"
    password = "admin123"
    return {"api_key": api_key, "password": password}

@app.get("/admin/secret/v2")
def admin_secret_v2():
    api_key = "super-secret-key"
    password = "admin123"
    return {"api_key": api_key, "password": password}
