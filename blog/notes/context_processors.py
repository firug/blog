from .models import Partition
def add_variable_to_context(requests):
    return {
        "partitions": Partition.objects.all(),
    }