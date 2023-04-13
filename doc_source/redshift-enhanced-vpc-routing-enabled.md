# redshift\-enhanced\-vpc\-routing\-enabled<a name="redshift-enhanced-vpc-routing-enabled"></a>

Checks if Amazon Redshift cluster has 'enhancedVpcRouting' enabled\. The rule is NON\_COMPLIANT if 'enhancedVpcRouting' is not enabled or if the configuration\.enhancedVpcRouting field is 'false'\. 

**Identifier:** REDSHIFT\_ENHANCED\_VPC\_ROUTING\_ENABLED

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d501c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.