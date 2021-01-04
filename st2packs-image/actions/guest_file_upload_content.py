# Copyright 2021 Carnegie Mellon University. All Rights Reserved.
# Released under a MIT (SEI)-style license. See LICENSE.md in the project root for license information.

from vmwarelib.guest import GuestAction
from pyVmomi import vim  # pylint: disable-msg=E0611
import os
import requests


class InitiateFileTransferToGuest(GuestAction):

    def run(self, vm_id, username, password, guest_file_path,
            file_content='', vsphere=None):
        """
        Upload a file to a directory inside a guest.

        Args:
        - vm_id: MOID of the Virtual Machine
        - username: username to perform the operation
        - password: password of that user
        - guest_file_path: Full file path in the guest to store the file
        - file_content: The content of the file to be uploaded
        - vsphere: Pre-configured vsphere connection details (config.yaml)
        """
        self.prepare_guest_operation(vsphere, vm_id, username, password)

        file_attribute = vim.vm.guest.FileManager.FileAttributes()
        url = self.guest_file_manager.InitiateFileTransferToGuest(
            self.vm, self.guest_credentials, guest_file_path, file_attribute,
            len(file_content), True)

        response = requests.put(url, data=file_content, verify=False)
        response.raise_for_status()  # raise if status_code is not 200
        return guest_file_path
