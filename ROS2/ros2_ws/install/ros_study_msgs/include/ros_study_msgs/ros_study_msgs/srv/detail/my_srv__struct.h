// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ros_study_msgs:srv/MySrv.idl
// generated code does not contain a copyright notice

#ifndef ROS_STUDY_MSGS__SRV__DETAIL__MY_SRV__STRUCT_H_
#define ROS_STUDY_MSGS__SRV__DETAIL__MY_SRV__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/MySrv in the package ros_study_msgs.
typedef struct ros_study_msgs__srv__MySrv_Request
{
  float req;
} ros_study_msgs__srv__MySrv_Request;

// Struct for a sequence of ros_study_msgs__srv__MySrv_Request.
typedef struct ros_study_msgs__srv__MySrv_Request__Sequence
{
  ros_study_msgs__srv__MySrv_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ros_study_msgs__srv__MySrv_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/MySrv in the package ros_study_msgs.
typedef struct ros_study_msgs__srv__MySrv_Response
{
  float res;
} ros_study_msgs__srv__MySrv_Response;

// Struct for a sequence of ros_study_msgs__srv__MySrv_Response.
typedef struct ros_study_msgs__srv__MySrv_Response__Sequence
{
  ros_study_msgs__srv__MySrv_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ros_study_msgs__srv__MySrv_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROS_STUDY_MSGS__SRV__DETAIL__MY_SRV__STRUCT_H_
