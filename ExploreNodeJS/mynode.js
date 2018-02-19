var http = require('http');
var dt = require('./myfirstmodule');
var url = require('url');

// The Node.js file system module allow you to work with the file system on your computer.
var fs = require('fs');

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    //res.write("The date and time are currently: " + dt.myDateTime());

// res.write(req.url);
// res.end();

//  var q = url.parse(req.url, true).query;
//  var txt = q.year + " " + q.month;
//  res.end(txt);

// Create a Node.js file that reads the HTML file, and return the content:
  fs.readFile('demofile1.html', function(err, data) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write(data);
    res.end();
  });

//The fs.appendFile() method appends specified content to a file. If the file does not exist, the file will be created:
fs.appendFile('mynewfile1.txt', 'Hello content!', function (err) {
  if (err) throw err;
  console.log('Saved!');
});

//The fs.open() method takes a "flag" as the second argument, if the flag is "w" for "writing", the specified file is opened for writing. If the file does not exist, an empty file is created:
fs.open('mynewfile2.txt', 'w', function (err, file) {
  if (err) throw err;
  console.log('Saved for writing!');
});

}).listen(8080);
