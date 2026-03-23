app.get('/users', (req, res) => {
    const users = getUsers();

    res.send(users);
});
