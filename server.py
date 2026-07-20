from concurrent import futures
import grpc

import hello_pb2
import hello_pb2_grpc


class GreetingService(
    hello_pb2_grpc.GreetingServiceServicer
):

    def SayHello(self, request, context):

        return hello_pb2.HelloResponse(
            message=f"Hello {request.name}"
        )


server = grpc.server(
    futures.ThreadPoolExecutor(max_workers=10)
)

hello_pb2_grpc.add_GreetingServiceServicer_to_server(
    GreetingService(),
    server
)

server.add_insecure_port("[::]:50051")

server.start()

print("gRPC Server Running...")

server.wait_for_termination()
