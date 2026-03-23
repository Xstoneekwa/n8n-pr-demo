app.get('/users', (req, res) => {
    try {
        const page = parseInt(req.query.page) || 1;
        const limit = 10;

        if (page < 1) {
            return res.status(400).json({ error: "Invalid page" });
        }

        const users = getUsersPaginated(page, limit);

        res.status(200).json({
            success: true,
            data: users
        });

    } catch (error) {
        res.status(500).json({
            error: "Internal server error"
        });
    }
});
