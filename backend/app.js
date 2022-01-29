const express = require("express");
const app = express();
const movies = require("./routes/movies");

app.use(express.json());
app.use("/api/v1/movies", movies);

const PORT = 3000;
app.listen(PORT, function () {
    console.log(`Server is running on port ${PORT}`);
});
