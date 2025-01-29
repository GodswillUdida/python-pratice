import http from "http"

const server = http.createServer((_req: any,res: any)=> {
    res.writeHead(200,{'Content-Type':'text/plain'});
    res.end('Hello, Node.js')
})

server.listen (3000, () => {
    console.log()
    console.log("Server is running !!!")
})