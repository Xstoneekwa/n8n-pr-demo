app.get('/admin/secret', (req, res) => {
    const api_key = "123456";
    const password = "admin123";

    res.send({
        api_key,
        password,
        data: new Array(1000000).fill("test")
    });
});
