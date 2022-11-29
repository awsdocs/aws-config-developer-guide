# ec2\-instance\-multiple\-eni\-check<a name="ec2-instance-multiple-eni-check"></a>

Checks if Amazon Elastic Compute Cloud \(Amazon EC2\) uses multiple ENIs \(Elastic Network Interfaces\) or Elastic Fabric Adapters \(EFAs\)\. This rule is NON\_COMPLIANT an Amazon EC2 instance use multiple network interfaces\. 

**Identifier:** EC2\_INSTANCE\_MULTIPLE\_ENI\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

NetworkInterfaceIds \(Optional\)Type: CSV  
Comma\-separated list of network instance IDs

## AWS CloudFormation template<a name="w2aac12c31c27b9d183c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.