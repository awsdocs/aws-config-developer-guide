# ec2\-token\-hop\-limit\-check<a name="ec2-token-hop-limit-check"></a>

Checks if an Amazon Elastic Compute Cloud \(EC2\) instance metadata has a specified token hop limit that is below the desired limit\. The rule is NON\_COMPLIANT for an instance if it has a hop limit value above the intended limit\. 

**Identifier:** EC2\_TOKEN\_HOP\_LIMIT\_CHECK

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

tokenHopLimit \(Optional\)Type: int  
The desired token hop limit\. Valid values are between 1 and 64, both inclusive\. Default value is 1 if parameter is not specified\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d233c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.