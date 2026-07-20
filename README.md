# gRPC Microservice with Python

A simple Python gRPC microservice demonstrating service-to-service communication.

## Features
- Protocol Buffers
- Unary RPC
- Client-server communication
- HTTP/2 transport

## Technologies Used
- Python
- gRPC
- Protocol Buffers

## Installation
```bash
pip install -r requirements.txt
```

Generate gRPC files:
python -m grpc_tools.protoc --proto_path=proto --python_out=. --grpc_python_out=. proto/hello.proto

Run the server:
python server.py

Run the client:
python client.py
