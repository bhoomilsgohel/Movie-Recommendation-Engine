const express = require("express");
const router = express.Router();
const movies = require("../modelFormat");

router.route("/").get(function (req, res) {
    res.status(200).json({
        movies,
    });
});

module.exports = router;
