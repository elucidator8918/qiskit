# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2023.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Exception for errors raised by Opflow module."""

from qiskit.exceptions import QiskitError
from qiskit.utils.deprecation import deprecate_func


class OpflowError(QiskitError):
    """Deprecated: For Opflow specific errors."""

    @deprecate_func(
        removal_timeline="in the Qiskit 1.0 release",
        since="0.24.0",
        package_name="qiskit-terra",
        additional_msg="For code migration guidelines, visit https://qisk.it/opflow_migration.",
    )
    def __init__(self, *message):
        """Set the error message."""
        super().__init__(*message)