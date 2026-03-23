app.get('/admin', (req, res) => {
    const password = "123";
    const api_key = "abc";

    res.send({ password, api_key });
});
