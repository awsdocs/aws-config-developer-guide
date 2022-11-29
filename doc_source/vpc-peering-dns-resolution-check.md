# vpc\-peering\-dns\-resolution\-check<a name="vpc-peering-dns-resolution-check"></a>

Checks if DNS resolution from accepter/requester VPC to private IP is enabled\. The rule is NON\_COMPLIANT if DNS resolution from accepter/requester VPC to private IP is not enabled\. 

**Identifier:** VPC\_PEERING\_DNS\_RESOLUTION\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

vpcIds \(Optional\)Type: CSV  
Comma\-separated list of VPC IDs to be checked\.

## AWS CloudFormation template<a name="w2aac12c31c27b9d559c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.