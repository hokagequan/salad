import express from 'express';
import controller from './controllers'

let app = express();

app.use(express.static(__dirname + "/views"));
app.use(express.static(__dirname + "/public"));
app.use('/', controller);

app.listen('3000', function(){
	console.log("listening on port 3000!");
});