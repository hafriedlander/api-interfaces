# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: engines.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='engines.proto',
  package='gooseai',
  syntax='proto3',
  serialized_options=b'Z\n./;engines',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rengines.proto\x12\x07gooseai\"Y\n\nEngineInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t\x12\r\n\x05ready\x18\x03 \x01(\x08\x12!\n\x04type\x18\x04 \x01(\x0e\x32\x13.gooseai.EngineType\"\x14\n\x12ListEnginesRequest\".\n\x07\x45ngines\x12#\n\x06\x65ngine\x18\x01 \x03(\x0b\x32\x13.gooseai.EngineInfo*9\n\nEngineType\x12\x08\n\x04TEXT\x10\x00\x12\x0b\n\x07PICTURE\x10\x01\x12\t\n\x05\x41UDIO\x10\x02\x12\t\n\x05VIDEO\x10\x03\x32P\n\x0e\x45nginesService\x12>\n\x0bListEngines\x12\x1b.gooseai.ListEnginesRequest\x1a\x10.gooseai.Engines\"\x00\x42\x0cZ\n./;enginesb\x06proto3'
)

_ENGINETYPE = _descriptor.EnumDescriptor(
  name='EngineType',
  full_name='gooseai.EngineType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PICTURE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUDIO', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VIDEO', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=187,
  serialized_end=244,
)
_sym_db.RegisterEnumDescriptor(_ENGINETYPE)

EngineType = enum_type_wrapper.EnumTypeWrapper(_ENGINETYPE)
TEXT = 0
PICTURE = 1
AUDIO = 2
VIDEO = 3



_ENGINEINFO = _descriptor.Descriptor(
  name='EngineInfo',
  full_name='gooseai.EngineInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gooseai.EngineInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='gooseai.EngineInfo.owner', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ready', full_name='gooseai.EngineInfo.ready', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='gooseai.EngineInfo.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=115,
)


_LISTENGINESREQUEST = _descriptor.Descriptor(
  name='ListEnginesRequest',
  full_name='gooseai.ListEnginesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=137,
)


_ENGINES = _descriptor.Descriptor(
  name='Engines',
  full_name='gooseai.Engines',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='engine', full_name='gooseai.Engines.engine', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=185,
)

_ENGINEINFO.fields_by_name['type'].enum_type = _ENGINETYPE
_ENGINES.fields_by_name['engine'].message_type = _ENGINEINFO
DESCRIPTOR.message_types_by_name['EngineInfo'] = _ENGINEINFO
DESCRIPTOR.message_types_by_name['ListEnginesRequest'] = _LISTENGINESREQUEST
DESCRIPTOR.message_types_by_name['Engines'] = _ENGINES
DESCRIPTOR.enum_types_by_name['EngineType'] = _ENGINETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EngineInfo = _reflection.GeneratedProtocolMessageType('EngineInfo', (_message.Message,), {
  'DESCRIPTOR' : _ENGINEINFO,
  '__module__' : 'engines_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.EngineInfo)
  })
_sym_db.RegisterMessage(EngineInfo)

ListEnginesRequest = _reflection.GeneratedProtocolMessageType('ListEnginesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTENGINESREQUEST,
  '__module__' : 'engines_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.ListEnginesRequest)
  })
_sym_db.RegisterMessage(ListEnginesRequest)

Engines = _reflection.GeneratedProtocolMessageType('Engines', (_message.Message,), {
  'DESCRIPTOR' : _ENGINES,
  '__module__' : 'engines_pb2'
  # @@protoc_insertion_point(class_scope:gooseai.Engines)
  })
_sym_db.RegisterMessage(Engines)


DESCRIPTOR._options = None

_ENGINESSERVICE = _descriptor.ServiceDescriptor(
  name='EnginesService',
  full_name='gooseai.EnginesService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=246,
  serialized_end=326,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListEngines',
    full_name='gooseai.EnginesService.ListEngines',
    index=0,
    containing_service=None,
    input_type=_LISTENGINESREQUEST,
    output_type=_ENGINES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENGINESSERVICE)

DESCRIPTOR.services_by_name['EnginesService'] = _ENGINESSERVICE

# @@protoc_insertion_point(module_scope)