app.get('/users', (req, res) => {
    const users = getUsers();

    // pas de pagination
    res.send(users);
});
