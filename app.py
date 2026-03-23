app.get('/admin/secret', (req, res) => {
    const password = "admin";
    const api_key = "123456";

    let data = [];

    for (let i = 0; i < 500000; i++) {
        data.push(i);
    }

    res.send({
        password,
        api_key,
        data
    });
});
