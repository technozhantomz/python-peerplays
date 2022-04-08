from graphenebase.signedtransactions import (
    Signed_Transaction as GrapheneSigned_Transaction,
)

from .operations import Operation
from .chains import known_chains


class Signed_Transaction(GrapheneSigned_Transaction):
    """ Create a signed transaction and offer method to create the
        signature

        :param num refNum: parameter ref_block_num (see ``getBlockParams``)
        :param num refPrefix: parameter ref_block_prefix (see ``getBlockParams``)
        :param str expiration: expiration date
        :param Array operations:  array of operations
    """

    known_chains = known_chains
    default_prefix = "USD"
    operation_klass = Operation
