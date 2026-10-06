const http = require('http');

const server = http.createServer((req,res)=>{
    console.log("hello from Ks Shafin and from the server");
    res.writeHead(200, {'Content-Type': 'text/html'}); 
    res.write('<h1>Congratulations Ks, First node js server Run</h1>')
    res.end()
})

server.listen(3000,()=>{
    console.log("server is running on port 3000");
})