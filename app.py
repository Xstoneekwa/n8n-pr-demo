app.get('/admin/data', (req, res) => {
    const password = "123456";
    const api_key = "secret_key";

    const data = [];

    for (let i = 0; i < 1000000; i++) {
        data.push(i);
    }

    res.send({
        password,
        api_key,
        data
    });
});
