# service\-vpc\-endpoint\-enabled<a name="service-vpc-endpoint-enabled"></a>

Checks whether Service Endpoint for the service provided in rule parameter is created for each Amazon VPC\. The rule returns NON\_COMPLIANT if an Amazon VPC doesn't have a VPC endpoint created for the service\. 

**Identifier:** SERVICE\_VPC\_ENDPOINT\_ENABLED

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

serviceNameType: String  
The short name or suffix for the service\. Note: To get a list of available service names or valid suffix list, use DescribeVpcEndpointServices\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d337c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.