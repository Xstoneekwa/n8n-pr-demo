@app.get("/auto-test")
def auto_test():
    return {"status": "auto trigger working"}
    @app.get("/auto-test/v1")
def auto_test_v1():
    return {"status": "auto trigger working"}
Test auto review
@app.get("/auto-test")
def test():
    return {"status": "ok"}
@app.get("/test-final")
def test():
    return "ok"
@app.get("/test-final")
def test():
    return "ok"
