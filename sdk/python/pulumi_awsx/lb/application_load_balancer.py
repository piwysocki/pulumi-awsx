# coding=utf-8
# *** WARNING: this file was generated by pulumi-gen-awsx. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import awsx as _awsx
from ._inputs import *
import pulumi_aws

__all__ = ['ApplicationLoadBalancerArgs', 'ApplicationLoadBalancer']

@pulumi.input_type
class ApplicationLoadBalancerArgs:
    def __init__(__self__, *,
                 access_logs: Optional[pulumi.Input['pulumi_aws.lb.LoadBalancerAccessLogsArgs']] = None,
                 customer_owned_ipv4_pool: Optional[pulumi.Input[str]] = None,
                 default_security_group: Optional['_awsx.DefaultSecurityGroupArgs'] = None,
                 default_target_group: Optional['TargetGroupArgs'] = None,
                 default_target_group_port: Optional[pulumi.Input[int]] = None,
                 desync_mitigation_mode: Optional[pulumi.Input[str]] = None,
                 drop_invalid_header_fields: Optional[pulumi.Input[bool]] = None,
                 enable_deletion_protection: Optional[pulumi.Input[bool]] = None,
                 enable_http2: Optional[pulumi.Input[bool]] = None,
                 enable_waf_fail_open: Optional[pulumi.Input[bool]] = None,
                 idle_timeout: Optional[pulumi.Input[int]] = None,
                 internal: Optional[pulumi.Input[bool]] = None,
                 ip_address_type: Optional[pulumi.Input[str]] = None,
                 listener: Optional['ListenerArgs'] = None,
                 listeners: Optional[Sequence['ListenerArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 preserve_host_header: Optional[pulumi.Input[bool]] = None,
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_mappings: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.lb.LoadBalancerSubnetMappingArgs']]]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.ec2.Subnet']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ApplicationLoadBalancer resource.
        :param pulumi.Input['pulumi_aws.lb.LoadBalancerAccessLogsArgs'] access_logs: An Access Logs block. Access Logs documented below.
        :param pulumi.Input[str] customer_owned_ipv4_pool: The ID of the customer owned ipv4 pool to use for this load balancer.
        :param '_awsx.DefaultSecurityGroupArgs' default_security_group: Options for creating a default security group if [securityGroups] not specified.
        :param 'TargetGroupArgs' default_target_group: Options creating a default target group.
        :param pulumi.Input[int] default_target_group_port: Port to use to connect with the target. Valid values are ports 1-65535. Defaults to 80.
        :param pulumi.Input[str] desync_mitigation_mode: Determines how the load balancer handles requests that might pose a security risk to an application due to HTTP desync. Valid values are `monitor`, `defensive` (default), `strictest`.
        :param pulumi.Input[bool] drop_invalid_header_fields: Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type `application`.
        :param pulumi.Input[bool] enable_deletion_protection: If true, deletion of the load balancer will be disabled via
               the AWS API. This will prevent this provider from deleting the load balancer. Defaults to `false`.
        :param pulumi.Input[bool] enable_http2: Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.
        :param pulumi.Input[bool] enable_waf_fail_open: Indicates whether to allow a WAF-enabled load balancer to route requests to targets if it is unable to forward the request to AWS WAF. Defaults to `false`.
        :param pulumi.Input[int] idle_timeout: The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type `application`. Default: 60.
        :param pulumi.Input[bool] internal: If true, the LB will be internal.
        :param pulumi.Input[str] ip_address_type: The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` and `dualstack`
        :param 'ListenerArgs' listener: A listener to create. Only one of [listener] and [listeners] can be specified.
        :param Sequence['ListenerArgs'] listeners: List of listeners to create. Only one of [listener] and [listeners] can be specified.
        :param pulumi.Input[str] name: The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
               must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
               this provider will autogenerate a name beginning with `tf-lb`.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[bool] preserve_host_header: Indicates whether the Application Load Balancer should preserve the Host header in the HTTP request and send it to the target without any change. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_groups: A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `application`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: A list of subnet IDs to attach to the LB. Subnets
               cannot be updated for Load Balancers of type `network`. Changing this value
               for load balancers of type `network` will force a recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input['pulumi_aws.lb.LoadBalancerSubnetMappingArgs']]] subnet_mappings: A subnet mapping block as documented below.
        :param pulumi.Input[Sequence[pulumi.Input['pulumi_aws.ec2.Subnet']]] subnets: A list of subnets to attach to the LB. Only one of [subnets], [subnetIds] or [subnetMappings] can be specified
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        if access_logs is not None:
            pulumi.set(__self__, "access_logs", access_logs)
        if customer_owned_ipv4_pool is not None:
            pulumi.set(__self__, "customer_owned_ipv4_pool", customer_owned_ipv4_pool)
        if default_security_group is not None:
            pulumi.set(__self__, "default_security_group", default_security_group)
        if default_target_group is not None:
            pulumi.set(__self__, "default_target_group", default_target_group)
        if default_target_group_port is not None:
            pulumi.set(__self__, "default_target_group_port", default_target_group_port)
        if desync_mitigation_mode is not None:
            pulumi.set(__self__, "desync_mitigation_mode", desync_mitigation_mode)
        if drop_invalid_header_fields is not None:
            pulumi.set(__self__, "drop_invalid_header_fields", drop_invalid_header_fields)
        if enable_deletion_protection is not None:
            pulumi.set(__self__, "enable_deletion_protection", enable_deletion_protection)
        if enable_http2 is not None:
            pulumi.set(__self__, "enable_http2", enable_http2)
        if enable_waf_fail_open is not None:
            pulumi.set(__self__, "enable_waf_fail_open", enable_waf_fail_open)
        if idle_timeout is not None:
            pulumi.set(__self__, "idle_timeout", idle_timeout)
        if internal is not None:
            pulumi.set(__self__, "internal", internal)
        if ip_address_type is not None:
            pulumi.set(__self__, "ip_address_type", ip_address_type)
        if listener is not None:
            pulumi.set(__self__, "listener", listener)
        if listeners is not None:
            pulumi.set(__self__, "listeners", listeners)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if name_prefix is not None:
            pulumi.set(__self__, "name_prefix", name_prefix)
        if preserve_host_header is not None:
            pulumi.set(__self__, "preserve_host_header", preserve_host_header)
        if security_groups is not None:
            pulumi.set(__self__, "security_groups", security_groups)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)
        if subnet_mappings is not None:
            pulumi.set(__self__, "subnet_mappings", subnet_mappings)
        if subnets is not None:
            pulumi.set(__self__, "subnets", subnets)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accessLogs")
    def access_logs(self) -> Optional[pulumi.Input['pulumi_aws.lb.LoadBalancerAccessLogsArgs']]:
        """
        An Access Logs block. Access Logs documented below.
        """
        return pulumi.get(self, "access_logs")

    @access_logs.setter
    def access_logs(self, value: Optional[pulumi.Input['pulumi_aws.lb.LoadBalancerAccessLogsArgs']]):
        pulumi.set(self, "access_logs", value)

    @property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the customer owned ipv4 pool to use for this load balancer.
        """
        return pulumi.get(self, "customer_owned_ipv4_pool")

    @customer_owned_ipv4_pool.setter
    def customer_owned_ipv4_pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_owned_ipv4_pool", value)

    @property
    @pulumi.getter(name="defaultSecurityGroup")
    def default_security_group(self) -> Optional['_awsx.DefaultSecurityGroupArgs']:
        """
        Options for creating a default security group if [securityGroups] not specified.
        """
        return pulumi.get(self, "default_security_group")

    @default_security_group.setter
    def default_security_group(self, value: Optional['_awsx.DefaultSecurityGroupArgs']):
        pulumi.set(self, "default_security_group", value)

    @property
    @pulumi.getter(name="defaultTargetGroup")
    def default_target_group(self) -> Optional['TargetGroupArgs']:
        """
        Options creating a default target group.
        """
        return pulumi.get(self, "default_target_group")

    @default_target_group.setter
    def default_target_group(self, value: Optional['TargetGroupArgs']):
        pulumi.set(self, "default_target_group", value)

    @property
    @pulumi.getter(name="defaultTargetGroupPort")
    def default_target_group_port(self) -> Optional[pulumi.Input[int]]:
        """
        Port to use to connect with the target. Valid values are ports 1-65535. Defaults to 80.
        """
        return pulumi.get(self, "default_target_group_port")

    @default_target_group_port.setter
    def default_target_group_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "default_target_group_port", value)

    @property
    @pulumi.getter(name="desyncMitigationMode")
    def desync_mitigation_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Determines how the load balancer handles requests that might pose a security risk to an application due to HTTP desync. Valid values are `monitor`, `defensive` (default), `strictest`.
        """
        return pulumi.get(self, "desync_mitigation_mode")

    @desync_mitigation_mode.setter
    def desync_mitigation_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "desync_mitigation_mode", value)

    @property
    @pulumi.getter(name="dropInvalidHeaderFields")
    def drop_invalid_header_fields(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type `application`.
        """
        return pulumi.get(self, "drop_invalid_header_fields")

    @drop_invalid_header_fields.setter
    def drop_invalid_header_fields(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "drop_invalid_header_fields", value)

    @property
    @pulumi.getter(name="enableDeletionProtection")
    def enable_deletion_protection(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, deletion of the load balancer will be disabled via
        the AWS API. This will prevent this provider from deleting the load balancer. Defaults to `false`.
        """
        return pulumi.get(self, "enable_deletion_protection")

    @enable_deletion_protection.setter
    def enable_deletion_protection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_deletion_protection", value)

    @property
    @pulumi.getter(name="enableHttp2")
    def enable_http2(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.
        """
        return pulumi.get(self, "enable_http2")

    @enable_http2.setter
    def enable_http2(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_http2", value)

    @property
    @pulumi.getter(name="enableWafFailOpen")
    def enable_waf_fail_open(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether to allow a WAF-enabled load balancer to route requests to targets if it is unable to forward the request to AWS WAF. Defaults to `false`.
        """
        return pulumi.get(self, "enable_waf_fail_open")

    @enable_waf_fail_open.setter
    def enable_waf_fail_open(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_waf_fail_open", value)

    @property
    @pulumi.getter(name="idleTimeout")
    def idle_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type `application`. Default: 60.
        """
        return pulumi.get(self, "idle_timeout")

    @idle_timeout.setter
    def idle_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "idle_timeout", value)

    @property
    @pulumi.getter
    def internal(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, the LB will be internal.
        """
        return pulumi.get(self, "internal")

    @internal.setter
    def internal(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "internal", value)

    @property
    @pulumi.getter(name="ipAddressType")
    def ip_address_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` and `dualstack`
        """
        return pulumi.get(self, "ip_address_type")

    @ip_address_type.setter
    def ip_address_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address_type", value)

    @property
    @pulumi.getter
    def listener(self) -> Optional['ListenerArgs']:
        """
        A listener to create. Only one of [listener] and [listeners] can be specified.
        """
        return pulumi.get(self, "listener")

    @listener.setter
    def listener(self, value: Optional['ListenerArgs']):
        pulumi.set(self, "listener", value)

    @property
    @pulumi.getter
    def listeners(self) -> Optional[Sequence['ListenerArgs']]:
        """
        List of listeners to create. Only one of [listener] and [listeners] can be specified.
        """
        return pulumi.get(self, "listeners")

    @listeners.setter
    def listeners(self, value: Optional[Sequence['ListenerArgs']]):
        pulumi.set(self, "listeners", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
        must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
        this provider will autogenerate a name beginning with `tf-lb`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        """
        return pulumi.get(self, "name_prefix")

    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_prefix", value)

    @property
    @pulumi.getter(name="preserveHostHeader")
    def preserve_host_header(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the Application Load Balancer should preserve the Host header in the HTTP request and send it to the target without any change. Defaults to `false`.
        """
        return pulumi.get(self, "preserve_host_header")

    @preserve_host_header.setter
    def preserve_host_header(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "preserve_host_header", value)

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `application`.
        """
        return pulumi.get(self, "security_groups")

    @security_groups.setter
    def security_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_groups", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of subnet IDs to attach to the LB. Subnets
        cannot be updated for Load Balancers of type `network`. Changing this value
        for load balancers of type `network` will force a recreation of the resource.
        """
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="subnetMappings")
    def subnet_mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.lb.LoadBalancerSubnetMappingArgs']]]]:
        """
        A subnet mapping block as documented below.
        """
        return pulumi.get(self, "subnet_mappings")

    @subnet_mappings.setter
    def subnet_mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.lb.LoadBalancerSubnetMappingArgs']]]]):
        pulumi.set(self, "subnet_mappings", value)

    @property
    @pulumi.getter
    def subnets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.ec2.Subnet']]]]:
        """
        A list of subnets to attach to the LB. Only one of [subnets], [subnetIds] or [subnetMappings] can be specified
        """
        return pulumi.get(self, "subnets")

    @subnets.setter
    def subnets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.ec2.Subnet']]]]):
        pulumi.set(self, "subnets", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ApplicationLoadBalancer(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_logs: Optional[pulumi.Input[pulumi.InputType['pulumi_aws.lb.LoadBalancerAccessLogsArgs']]] = None,
                 customer_owned_ipv4_pool: Optional[pulumi.Input[str]] = None,
                 default_security_group: Optional[pulumi.InputType['_awsx.DefaultSecurityGroupArgs']] = None,
                 default_target_group: Optional[pulumi.InputType['TargetGroupArgs']] = None,
                 default_target_group_port: Optional[pulumi.Input[int]] = None,
                 desync_mitigation_mode: Optional[pulumi.Input[str]] = None,
                 drop_invalid_header_fields: Optional[pulumi.Input[bool]] = None,
                 enable_deletion_protection: Optional[pulumi.Input[bool]] = None,
                 enable_http2: Optional[pulumi.Input[bool]] = None,
                 enable_waf_fail_open: Optional[pulumi.Input[bool]] = None,
                 idle_timeout: Optional[pulumi.Input[int]] = None,
                 internal: Optional[pulumi.Input[bool]] = None,
                 ip_address_type: Optional[pulumi.Input[str]] = None,
                 listener: Optional[pulumi.InputType['ListenerArgs']] = None,
                 listeners: Optional[Sequence[pulumi.InputType['ListenerArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 preserve_host_header: Optional[pulumi.Input[bool]] = None,
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['pulumi_aws.lb.LoadBalancerSubnetMappingArgs']]]]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.ec2.Subnet']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides an Application Load Balancer resource with listeners, default target group and default security group.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['pulumi_aws.lb.LoadBalancerAccessLogsArgs']] access_logs: An Access Logs block. Access Logs documented below.
        :param pulumi.Input[str] customer_owned_ipv4_pool: The ID of the customer owned ipv4 pool to use for this load balancer.
        :param pulumi.InputType['_awsx.DefaultSecurityGroupArgs'] default_security_group: Options for creating a default security group if [securityGroups] not specified.
        :param pulumi.InputType['TargetGroupArgs'] default_target_group: Options creating a default target group.
        :param pulumi.Input[int] default_target_group_port: Port to use to connect with the target. Valid values are ports 1-65535. Defaults to 80.
        :param pulumi.Input[str] desync_mitigation_mode: Determines how the load balancer handles requests that might pose a security risk to an application due to HTTP desync. Valid values are `monitor`, `defensive` (default), `strictest`.
        :param pulumi.Input[bool] drop_invalid_header_fields: Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type `application`.
        :param pulumi.Input[bool] enable_deletion_protection: If true, deletion of the load balancer will be disabled via
               the AWS API. This will prevent this provider from deleting the load balancer. Defaults to `false`.
        :param pulumi.Input[bool] enable_http2: Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.
        :param pulumi.Input[bool] enable_waf_fail_open: Indicates whether to allow a WAF-enabled load balancer to route requests to targets if it is unable to forward the request to AWS WAF. Defaults to `false`.
        :param pulumi.Input[int] idle_timeout: The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type `application`. Default: 60.
        :param pulumi.Input[bool] internal: If true, the LB will be internal.
        :param pulumi.Input[str] ip_address_type: The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` and `dualstack`
        :param pulumi.InputType['ListenerArgs'] listener: A listener to create. Only one of [listener] and [listeners] can be specified.
        :param Sequence[pulumi.InputType['ListenerArgs']] listeners: List of listeners to create. Only one of [listener] and [listeners] can be specified.
        :param pulumi.Input[str] name: The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
               must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
               this provider will autogenerate a name beginning with `tf-lb`.
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with `name`.
        :param pulumi.Input[bool] preserve_host_header: Indicates whether the Application Load Balancer should preserve the Host header in the HTTP request and send it to the target without any change. Defaults to `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_groups: A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `application`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subnet_ids: A list of subnet IDs to attach to the LB. Subnets
               cannot be updated for Load Balancers of type `network`. Changing this value
               for load balancers of type `network` will force a recreation of the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['pulumi_aws.lb.LoadBalancerSubnetMappingArgs']]]] subnet_mappings: A subnet mapping block as documented below.
        :param pulumi.Input[Sequence[pulumi.Input['pulumi_aws.ec2.Subnet']]] subnets: A list of subnets to attach to the LB. Only one of [subnets], [subnetIds] or [subnetMappings] can be specified
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ApplicationLoadBalancerArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Application Load Balancer resource with listeners, default target group and default security group.

        :param str resource_name: The name of the resource.
        :param ApplicationLoadBalancerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationLoadBalancerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_logs: Optional[pulumi.Input[pulumi.InputType['pulumi_aws.lb.LoadBalancerAccessLogsArgs']]] = None,
                 customer_owned_ipv4_pool: Optional[pulumi.Input[str]] = None,
                 default_security_group: Optional[pulumi.InputType['_awsx.DefaultSecurityGroupArgs']] = None,
                 default_target_group: Optional[pulumi.InputType['TargetGroupArgs']] = None,
                 default_target_group_port: Optional[pulumi.Input[int]] = None,
                 desync_mitigation_mode: Optional[pulumi.Input[str]] = None,
                 drop_invalid_header_fields: Optional[pulumi.Input[bool]] = None,
                 enable_deletion_protection: Optional[pulumi.Input[bool]] = None,
                 enable_http2: Optional[pulumi.Input[bool]] = None,
                 enable_waf_fail_open: Optional[pulumi.Input[bool]] = None,
                 idle_timeout: Optional[pulumi.Input[int]] = None,
                 internal: Optional[pulumi.Input[bool]] = None,
                 ip_address_type: Optional[pulumi.Input[str]] = None,
                 listener: Optional[pulumi.InputType['ListenerArgs']] = None,
                 listeners: Optional[Sequence[pulumi.InputType['ListenerArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 preserve_host_header: Optional[pulumi.Input[bool]] = None,
                 security_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['pulumi_aws.lb.LoadBalancerSubnetMappingArgs']]]]] = None,
                 subnets: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_aws.ec2.Subnet']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationLoadBalancerArgs.__new__(ApplicationLoadBalancerArgs)

            __props__.__dict__["access_logs"] = access_logs
            __props__.__dict__["customer_owned_ipv4_pool"] = customer_owned_ipv4_pool
            __props__.__dict__["default_security_group"] = default_security_group
            __props__.__dict__["default_target_group"] = default_target_group
            __props__.__dict__["default_target_group_port"] = default_target_group_port
            __props__.__dict__["desync_mitigation_mode"] = desync_mitigation_mode
            __props__.__dict__["drop_invalid_header_fields"] = drop_invalid_header_fields
            __props__.__dict__["enable_deletion_protection"] = enable_deletion_protection
            __props__.__dict__["enable_http2"] = enable_http2
            __props__.__dict__["enable_waf_fail_open"] = enable_waf_fail_open
            __props__.__dict__["idle_timeout"] = idle_timeout
            __props__.__dict__["internal"] = internal
            __props__.__dict__["ip_address_type"] = ip_address_type
            __props__.__dict__["listener"] = listener
            __props__.__dict__["listeners"] = listeners
            __props__.__dict__["name"] = name
            __props__.__dict__["name_prefix"] = name_prefix
            __props__.__dict__["preserve_host_header"] = preserve_host_header
            __props__.__dict__["security_groups"] = security_groups
            __props__.__dict__["subnet_ids"] = subnet_ids
            __props__.__dict__["subnet_mappings"] = subnet_mappings
            __props__.__dict__["subnets"] = subnets
            __props__.__dict__["tags"] = tags
            __props__.__dict__["load_balancer"] = None
            __props__.__dict__["vpc_id"] = None
        super(ApplicationLoadBalancer, __self__).__init__(
            'awsx:lb:ApplicationLoadBalancer',
            resource_name,
            __props__,
            opts,
            remote=True)

    @property
    @pulumi.getter(name="defaultSecurityGroup")
    def default_security_group(self) -> pulumi.Output[Optional['pulumi_aws.ec2.SecurityGroup']]:
        """
        Default security group, if auto-created
        """
        return pulumi.get(self, "default_security_group")

    @property
    @pulumi.getter(name="defaultTargetGroup")
    def default_target_group(self) -> pulumi.Output['pulumi_aws.lb.TargetGroup']:
        """
        Default target group, if auto-created
        """
        return pulumi.get(self, "default_target_group")

    @property
    @pulumi.getter
    def listeners(self) -> pulumi.Output[Optional[Sequence['pulumi_aws.lb.Listener']]]:
        """
        Listeners created as part of this load balancer
        """
        return pulumi.get(self, "listeners")

    @property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> pulumi.Output['pulumi_aws.lb.LoadBalancer']:
        """
        Underlying Load Balancer resource
        """
        return pulumi.get(self, "load_balancer")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[Optional[str]]:
        """
        Id of the VPC in which this load balancer is operating
        """
        return pulumi.get(self, "vpc_id")

