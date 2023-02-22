# internet\-gateway\-authorized\-vpc\-only<a name="internet-gateway-authorized-vpc-only"></a>

Checks that Internet gateways \(IGWs\) are only attached to an authorized Amazon Virtual Private Cloud \(VPCs\)\. The rule is NON\_COMPLIANT if IGWs are not attached to an authorized VPC\. 

**Identifier:** INTERNET\_GATEWAY\_AUTHORIZED\_VPC\_ONLY

**Resource Types:** AWS::EC2::InternetGateway

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

AuthorizedVpcIds \(Optional\)Type: String  
Comma\-separated list of the authorized VPC IDs with attached IGWs\. If parameter is not provided all attached IGWs will be NON\_COMPLIANT\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d365c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.