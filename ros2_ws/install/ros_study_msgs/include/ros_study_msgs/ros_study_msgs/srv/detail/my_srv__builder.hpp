// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from ros_study_msgs:srv/MySrv.idl
// generated code does not contain a copyright notice

#ifndef ROS_STUDY_MSGS__SRV__DETAIL__MY_SRV__BUILDER_HPP_
#define ROS_STUDY_MSGS__SRV__DETAIL__MY_SRV__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "ros_study_msgs/srv/detail/my_srv__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace ros_study_msgs
{

namespace srv
{

namespace builder
{

class Init_MySrv_Request_req
{
public:
  Init_MySrv_Request_req()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ros_study_msgs::srv::MySrv_Request req(::ros_study_msgs::srv::MySrv_Request::_req_type arg)
  {
    msg_.req = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros_study_msgs::srv::MySrv_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros_study_msgs::srv::MySrv_Request>()
{
  return ros_study_msgs::srv::builder::Init_MySrv_Request_req();
}

}  // namespace ros_study_msgs


namespace ros_study_msgs
{

namespace srv
{

namespace builder
{

class Init_MySrv_Response_res
{
public:
  Init_MySrv_Response_res()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::ros_study_msgs::srv::MySrv_Response res(::ros_study_msgs::srv::MySrv_Response::_res_type arg)
  {
    msg_.res = std::move(arg);
    return std::move(msg_);
  }

private:
  ::ros_study_msgs::srv::MySrv_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::ros_study_msgs::srv::MySrv_Response>()
{
  return ros_study_msgs::srv::builder::Init_MySrv_Response_res();
}

}  // namespace ros_study_msgs

#endif  // ROS_STUDY_MSGS__SRV__DETAIL__MY_SRV__BUILDER_HPP_
