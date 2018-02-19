var http = require('http');
// There is a very good module for working with file uploads, called "Formidable".
var formidable = require('formidable');

// When a file is successfully uploaded to the server, it is placed on a temporary folder.
// The path to this directory can be found in the "files" object, passed as the third argument in the parse() method's callback function.

// To move the file to the folder of your choice, use the File System module, and rename the file:
var fs = require('fs');


http.createServer(function (req, res) {
  if (req.url == '/fileupload') {
    var form = new formidable.IncomingForm();
    form.parse(req, function (err, fields, files) {
      var oldpath = files.filetoupload.path;
		console.log("name: ",files.filetoupload.name)
      var newpath = '/home/zemoso/Desktop/Sample-apps/RecommenderIMDB/ExploreNodeJS/FilesUploaded/' + files.filetoupload.name;
      fs.rename(oldpath, newpath, function (err) {
        if (err) throw err;
        res.write('File uploaded and moved!');
        res.end();
      });
    });
  } else {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
    res.write('<input type="file" name="filetoupload"><br>');
    res.write('<input type="submit">');
    res.write('</form>');
    return res.end();
  }
}).listen(8080);
