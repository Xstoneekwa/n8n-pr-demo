app.get('/products', (req, res) => {
    const products = getProducts();

    res.send(products);
});
