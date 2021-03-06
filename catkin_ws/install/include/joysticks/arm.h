// Generated by gencpp from file joysticks/arm.msg
// DO NOT EDIT!


#ifndef JOYSTICKS_MESSAGE_ARM_H
#define JOYSTICKS_MESSAGE_ARM_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace joysticks
{
template <class ContainerAllocator>
struct arm_
{
  typedef arm_<ContainerAllocator> Type;

  arm_()
    : joint1(0)
    , joint2(0)
    , joint3(0)  {
    }
  arm_(const ContainerAllocator& _alloc)
    : joint1(0)
    , joint2(0)
    , joint3(0)  {
  (void)_alloc;
    }



   typedef int16_t _joint1_type;
  _joint1_type joint1;

   typedef int16_t _joint2_type;
  _joint2_type joint2;

   typedef int16_t _joint3_type;
  _joint3_type joint3;





  typedef boost::shared_ptr< ::joysticks::arm_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::joysticks::arm_<ContainerAllocator> const> ConstPtr;

}; // struct arm_

typedef ::joysticks::arm_<std::allocator<void> > arm;

typedef boost::shared_ptr< ::joysticks::arm > armPtr;
typedef boost::shared_ptr< ::joysticks::arm const> armConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::joysticks::arm_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::joysticks::arm_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace joysticks

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'joysticks': ['/home/adam/ros/catkin_ws/src/joysticks/msg', '/home/adam/ros/catkin_ws/src/joysticks/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::joysticks::arm_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::joysticks::arm_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::joysticks::arm_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::joysticks::arm_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::joysticks::arm_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::joysticks::arm_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::joysticks::arm_<ContainerAllocator> >
{
  static const char* value()
  {
    return "eb9863fcda7de6b24e4aac39823626c2";
  }

  static const char* value(const ::joysticks::arm_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xeb9863fcda7de6b2ULL;
  static const uint64_t static_value2 = 0x4e4aac39823626c2ULL;
};

template<class ContainerAllocator>
struct DataType< ::joysticks::arm_<ContainerAllocator> >
{
  static const char* value()
  {
    return "joysticks/arm";
  }

  static const char* value(const ::joysticks::arm_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::joysticks::arm_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int16 joint1\n\
int16 joint2\n\
int16 joint3\n\
";
  }

  static const char* value(const ::joysticks::arm_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::joysticks::arm_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.joint1);
      stream.next(m.joint2);
      stream.next(m.joint3);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct arm_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::joysticks::arm_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::joysticks::arm_<ContainerAllocator>& v)
  {
    s << indent << "joint1: ";
    Printer<int16_t>::stream(s, indent + "  ", v.joint1);
    s << indent << "joint2: ";
    Printer<int16_t>::stream(s, indent + "  ", v.joint2);
    s << indent << "joint3: ";
    Printer<int16_t>::stream(s, indent + "  ", v.joint3);
  }
};

} // namespace message_operations
} // namespace ros

#endif // JOYSTICKS_MESSAGE_ARM_H
