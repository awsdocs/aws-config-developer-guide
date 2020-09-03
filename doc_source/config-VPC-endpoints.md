# Using AWS Config with Interface Amazon VPC Endpoints<a name="config-VPC-endpoints"></a>

If you use Amazon Virtual Private Cloud \(Amazon VPC\) to host your AWS resources, you can establish a private connection between your VPC and AWS Config\. You can use this connection to communicate with AWS Config from your VPC without going through the public internet\.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network that you define\. With a VPC, you have control over your network settings, such the IP address range, subnets, route tables, and network gateways\. Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that enables private communication between AWS services using an elastic network interface with private IP addresses\. To connect your VPC to AWS Config, you define an *interface VPC endpoint* for AWS Config\. This type of endpoint enables you to connect your VPC to AWS services\. The endpoint provides reliable, scalable connectivity to AWS Config without requiring an internet gateway, network address translation \(NAT\) instance, or VPN connection\. For more information, see [What is Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/) in the *Amazon VPC User Guide*\.

The following steps are for users of Amazon VPC\. For more information, see [Getting Started](https://docs.aws.amazon.com/vpc/latest/userguide/GetStarted.html) in the *Amazon VPC User Guide*\.

## Availability<a name="config-interface-VPC-availability"></a>

AWS Config currently supports VPC endpoints in the following Regions:
+ US East \(Ohio\)
+ US East \(N\. Virginia\)
+ US West \(N\. California\)
+ US West \(Oregon\)
+ Asia Pacific \(Mumbai\)
+ Asia Pacific \(Seoul\)
+ Asia Pacific \(Singapore\)
+ Asia Pacific \(Sydney\)
+ Asia Pacific \(Tokyo\)
+ Canada \(Central\)
+ Europe \(Frankfurt\)
+ Europe \(Ireland\)
+ Europe \(London\)
+ Europe \(Paris\)
+ South America \(São Paulo\)
+ Asia Pacific \(Hong Kong\)
+ Africa \(Cape Town\) 
+ Europe \(Milan\) 
+ Europe \(Stockholm\) 
+ Middle East \(Bahrain\) 
+ AWS GovCloud \(US\-East\) 
+ AWS GovCloud \(US\-West\) 

## Create a VPC Endpoint for AWS Config<a name="create-VPC-endpoint-for-Config"></a>

To start using AWS Config with your VPC, create an interface VPC endpoint for AWS Config\. You do not need to change the settings for AWS Config\. AWS Config calls other AWS services using their public endpoints\. For more information, see [Creating an Interface Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint.html) in the *Amazon VPC User Guide*\.