; Auto-generated. Do not edit!


(cl:in-package joysticks-msg)


;//! \htmlinclude drive.msg.html

(cl:defclass <drive> (roslisp-msg-protocol:ros-message)
  ((left
    :reader left
    :initarg :left
    :type cl:fixnum
    :initform 0)
   (right
    :reader right
    :initarg :right
    :type cl:fixnum
    :initform 0))
)

(cl:defclass drive (<drive>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <drive>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'drive)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name joysticks-msg:<drive> is deprecated: use joysticks-msg:drive instead.")))

(cl:ensure-generic-function 'left-val :lambda-list '(m))
(cl:defmethod left-val ((m <drive>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joysticks-msg:left-val is deprecated.  Use joysticks-msg:left instead.")
  (left m))

(cl:ensure-generic-function 'right-val :lambda-list '(m))
(cl:defmethod right-val ((m <drive>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joysticks-msg:right-val is deprecated.  Use joysticks-msg:right instead.")
  (right m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <drive>) ostream)
  "Serializes a message object of type '<drive>"
  (cl:let* ((signed (cl:slot-value msg 'left)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'right)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <drive>) istream)
  "Deserializes a message object of type '<drive>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'left) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'right) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<drive>)))
  "Returns string type for a message object of type '<drive>"
  "joysticks/drive")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'drive)))
  "Returns string type for a message object of type 'drive"
  "joysticks/drive")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<drive>)))
  "Returns md5sum for a message object of type '<drive>"
  "09d1b2323a1aeae9343e81809a820b60")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'drive)))
  "Returns md5sum for a message object of type 'drive"
  "09d1b2323a1aeae9343e81809a820b60")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<drive>)))
  "Returns full string definition for message of type '<drive>"
  (cl:format cl:nil "int16 left~%int16 right~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'drive)))
  "Returns full string definition for message of type 'drive"
  (cl:format cl:nil "int16 left~%int16 right~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <drive>))
  (cl:+ 0
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <drive>))
  "Converts a ROS message object to a list"
  (cl:list 'drive
    (cl:cons ':left (left msg))
    (cl:cons ':right (right msg))
))
