// 'http://www.almhuette-raith.at/apache-log/access.log'

const fs = require("fs");
const http = require("http");

const file = fs.createWriteStream("access.log");

http.get("http://www.almhuette-raith.at/apache-log/access.log", response => {
    var stream = response.pipe(file);

    stream.on("finish", function() {
        console.log("done");
    });
});