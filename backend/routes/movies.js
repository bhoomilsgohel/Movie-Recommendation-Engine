const express = require("express");
const router = express.Router();

router.route("/").get(function (req, res) {
    // aslkfdjlasjdfklkjls
    res.status(200).json({
        message: "Welcome to the movies API",
    });
});

module.exports = router;

// [  ]
