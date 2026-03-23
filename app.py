@app.get("/users")
def get_users():
    data = []
    for i in range(1000000):  # mauvaise perf
        data.append(i)
    return data


@app.get("/login")
def login():
    password = "admin123"  # hardcoded password ❌
    token = "secret-token"  # fuite sensible ❌
    return {"password": password, "token": token}


@app.get("/login/v2")
def login_v2():
    password = "admin123"  # duplication ❌
    token = "secret-token"
    return {"password": password, "token": token}
