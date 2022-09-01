# vpc\-network\-acl\-unused\-check<a name="vpc-network-acl-unused-check"></a>

Checks if there are unused network access control lists \(network ACLs\)\. The rule is COMPLIANT if each network ACL is associated with a subnet\. The rule is NON\_COMPLIANT if a network ACL is not associated with a subnet\.

**Identifier:** VPC\_NETWORK\_ACL\_UNUSED\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w85aac12c32c17b9d557c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.