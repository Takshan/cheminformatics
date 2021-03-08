# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import interpolator_pb2 as interpolator__pb2


class InterpolatorStub(object):
    """python -m grpc_tools.protoc -I./grpc/ --python_out=generated --grpc_python_out=generated ./grpc/interpolator.proto
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Interpolate = channel.unary_unary(
                '/nvidia.cheminformatics.grpc.Interpolator/Interpolate',
                request_serializer=interpolator__pb2.InterpolationSpec.SerializeToString,
                response_deserializer=interpolator__pb2.SmilesList.FromString,
                )


class InterpolatorServicer(object):
    """python -m grpc_tools.protoc -I./grpc/ --python_out=generated --grpc_python_out=generated ./grpc/interpolator.proto
    """

    def Interpolate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InterpolatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Interpolate': grpc.unary_unary_rpc_method_handler(
                    servicer.Interpolate,
                    request_deserializer=interpolator__pb2.InterpolationSpec.FromString,
                    response_serializer=interpolator__pb2.SmilesList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nvidia.cheminformatics.grpc.Interpolator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Interpolator(object):
    """python -m grpc_tools.protoc -I./grpc/ --python_out=generated --grpc_python_out=generated ./grpc/interpolator.proto
    """

    @staticmethod
    def Interpolate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nvidia.cheminformatics.grpc.Interpolator/Interpolate',
            interpolator__pb2.InterpolationSpec.SerializeToString,
            interpolator__pb2.SmilesList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
