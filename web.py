import http.server
import socketserver

PORT = 880

# Your HTML structure stored correctly as a Python multi-line string
HTML_CONTENT = """
6<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Suite</title>
    <style>
        body {
            font-family: Arial;
            background: #eef2f7;
            margin: 30px;
        }
        h1 {
            text-align: center;
            color: #1e3a8a;
        }
        table {c
            width: 80%;
            margin: auto;
            border-collapse: collapse;
            background: white;
        }
        th, td {
            border: 1px solid #333;
            padding: 12px;
            text-align: center;
        }
        th {
            background: #2563eb;
            color: white;
        }
    </style>
</head>
<body>
    <h1>TCP/IP Protocol Suite</h1>
    <table>
        <tr>
            <th>Layer</th>
            <th>Protocols</th>
            <th>Purpose</th>
        </tr>
        <tr>
            <td>Application</td>
            <td>HTTP, HTTPS, FTP, SMTP, DNS, DHCP, SSH</td>
            <td>Provides network services to applications</td>
        </tr>
        <tr>
            <td>Transport</td>
            <td>TCP, UDP</td>
            <td>Provides end-to-end communication</td>
        </tr>
        <tr>
            <td>Internet</td>
            <td>IP, ICMP, ARP, IGMP</td>
            <td>Addressing and packet routing</td>
        </tr>
        <tr>
            <td>Network Access</td>
            <td>Ethernet, Wi-Fi, PPP</td>
            <td>Transfers data through physical networks</td>
        </tr>
    </table>
</body>
</html>"""

class CustomHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Respond with an HTTP 200 OK status
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Encode the HTML string text into bytes and transmit it
        self.wfile.write(bytes(HTML_CONTENT, "utf-8"))

print(f"my webserver is running...")

# Allow immediate reuse of the port to prevent address configurations locks
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", 8000), CustomHandler) as httpd:
    httpd.serve_forever()