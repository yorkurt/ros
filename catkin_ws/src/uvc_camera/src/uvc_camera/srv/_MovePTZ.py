# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from uvc_camera/MovePTZRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MovePTZRequest(genpy.Message):
  _md5sum = "634cfef94ff2ed7578db5f7d396288a4"
  _type = "uvc_camera/MovePTZRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """

int16 pan
int16 tilt
int16 zoom
"""
  __slots__ = ['pan','tilt','zoom']
  _slot_types = ['int16','int16','int16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       pan,tilt,zoom

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MovePTZRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.pan is None:
        self.pan = 0
      if self.tilt is None:
        self.tilt = 0
      if self.zoom is None:
        self.zoom = 0
    else:
      self.pan = 0
      self.tilt = 0
      self.zoom = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3h().pack(_x.pan, _x.tilt, _x.zoom))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.pan, _x.tilt, _x.zoom,) = _get_struct_3h().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3h().pack(_x.pan, _x.tilt, _x.zoom))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.pan, _x.tilt, _x.zoom,) = _get_struct_3h().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3h = None
def _get_struct_3h():
    global _struct_3h
    if _struct_3h is None:
        _struct_3h = struct.Struct("<3h")
    return _struct_3h
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from uvc_camera/MovePTZResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MovePTZResponse(genpy.Message):
  _md5sum = "f5f93c0a2eb854a9067e042b93231a6f"
  _type = "uvc_camera/MovePTZResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int16 rpan
int16 rtilt
int16 rzoom
"""
  __slots__ = ['rpan','rtilt','rzoom']
  _slot_types = ['int16','int16','int16']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       rpan,rtilt,rzoom

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MovePTZResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.rpan is None:
        self.rpan = 0
      if self.rtilt is None:
        self.rtilt = 0
      if self.rzoom is None:
        self.rzoom = 0
    else:
      self.rpan = 0
      self.rtilt = 0
      self.rzoom = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3h().pack(_x.rpan, _x.rtilt, _x.rzoom))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.rpan, _x.rtilt, _x.rzoom,) = _get_struct_3h().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3h().pack(_x.rpan, _x.rtilt, _x.rzoom))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 6
      (_x.rpan, _x.rtilt, _x.rzoom,) = _get_struct_3h().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3h = None
def _get_struct_3h():
    global _struct_3h
    if _struct_3h is None:
        _struct_3h = struct.Struct("<3h")
    return _struct_3h
class MovePTZ(object):
  _type          = 'uvc_camera/MovePTZ'
  _md5sum = 'a964e82c0e0401a25741502592b56334'
  _request_class  = MovePTZRequest
  _response_class = MovePTZResponse