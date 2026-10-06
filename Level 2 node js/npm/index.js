const http = require('http');
const fs = require("fs");
const path = require("path");

function renderPage(){
    const filePath = path.join(__dirname, "random.html");
    const data =fs.readFileSync(filePath, "utf-8");
    return data 
}


const server = http.createServer((req,res)=>{
    // console.log("hello from Ks Shafin and from the server");
    res.writeHead(200, {'Content-Type': 'text/html'}); 
    // res.write('<h1>Congratulations Ks, First node js server Run</h1>')
    res.end(renderPage())
})

server.listen(3000,()=>{
    console.log("server is running on port 3000");
})