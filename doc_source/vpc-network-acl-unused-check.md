# vpc\-network\-acl\-unused\-check<a name="vpc-network-acl-unused-check"></a>

Checks if there are unused network access control lists \(network ACLs\)\. The rule is COMPLIANT if each network ACL is associated with a subnet\. The rule is NON\_COMPLIANT if a network ACL is not associated with a subnet\.

**Identifier:** VPC\_NETWORK\_ACL\_UNUSED\_CHECK

**Resource Types:** AWS::EC2::NetworkAcl

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d607c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.