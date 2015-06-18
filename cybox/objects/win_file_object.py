# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox
import cybox.bindings.win_file_object as win_file_binding
from cybox.objects.file_object import File, FileAttribute, FilePermissions
from cybox.common import (DateTime, Hash, HashList, HexBinary,
        ObjectProperties, String, UnsignedLong)


class Stream(cybox.Entity):
    _binding = win_file_binding
    _binding_class = win_file_binding.StreamObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinFileObject-2'

    name = fields.TypedField("Name", String)
    size_in_bytes = fields.TypedField("Size_In_Bytes", UnsignedLong)
    hashes = fields.TypedField("Hash", Hash, key_name="hashes", multiple=True)


class StreamList(cybox.EntityList):
    _binding = win_file_binding
    _binding_class = win_file_binding.StreamListType
    _binding_var = "Stream"
    _contained_type = Stream
    _namespace = 'http://cybox.mitre.org/objects#WinFileObject-2'


class WindowsFileAttribute(String):
    _binding = win_file_binding
    _binding_class = win_file_binding.WindowsFileAttributeType
    _namespace = 'http://cybox.mitre.org/objects#WinFileObject-2'


class WindowsFileAttributes(FileAttribute, cybox.EntityList):
    _binding = win_file_binding
    _binding_class = win_file_binding.WindowsFileAttributesType
    _binding_var = "Attribute"
    _contained_type = WindowsFileAttribute
    _namespace = 'http://cybox.mitre.org/objects#WinFileObject-2'


class WindowsFilePermissions(FilePermissions, cybox.Entity):
    _binding = win_file_binding
    _binding_class = win_file_binding.WindowsFilePermissionsType
    _namespace = 'http://cybox.mitre.org/objects#WinFileObject-2'

    full_control = fields.TypedField("Full_Control")
    modify = fields.TypedField("Modify")
    read = fields.TypedField("Read")
    read_and_execute = fields.TypedField("Read_And_Execute")
    write = fields.TypedField("Write")


class WinFile(File):
    _binding = win_file_binding
    _binding_class = win_file_binding.WindowsFileObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinFileObject-2'
    _XSI_NS = "WinFileObj"
    _XSI_TYPE = "WindowsFileObjectType"

    filename_accessed_time = fields.TypedField("Filename_Accessed_Time",
                                              DateTime)
    filename_created_time = fields.TypedField("Filename_Created_Time", DateTime)
    filename_modified_time = fields.TypedField("Filename_Modified_Time",
                                              DateTime)
    drive = fields.TypedField("Drive", String)
    security_id = fields.TypedField("Security_ID", String)
    security_type = fields.TypedField("Security_Type", String)
    stream_list = fields.TypedField("Stream_List", StreamList)

    #Override abstract types
    file_attributes_list = fields.TypedField('File_Attributes_List',
                                            WindowsFileAttributes)
    privilege_list = fields.TypedField('Permissions', WindowsFilePermissions)
