# internet\-gateway\-authorized\-vpc\-only<a name="internet-gateway-authorized-vpc-only"></a>

Checks that Internet gateways \(IGWs\) are only attached to an authorized Amazon Virtual Private Cloud \(VPCs\)\. The rule is NON\_COMPLIANT if IGWs are not attached to an authorized VPC\. 

**Identifier:** INTERNET\_GATEWAY\_AUTHORIZED\_VPC\_ONLY

**Trigger type:** Configuration changes 

**AWS Region:** All supported AWS Regions except Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

 AuthorizedVpcIds  
Comma\-separated list of the authorized VPC IDs with attached IGWs\. If parameter is not provided all attached IGWs will be NON\_COMPLIANT\. 

## AWS CloudFormation template<a name="w22aac11c29c17d219c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.