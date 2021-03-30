# restricted\-ssh<a name="restricted-ssh"></a>

Checks if the incoming SSH traffic for the security groups is accessible\. The rule is COMPLIANT when IP addresses of the incoming SSH traffic in the security groups are restricted \(CIDR other than 0\.0\.0\.0/0\)\. This rule applies only to IPv4\.

**Identifier:** INCOMING\_SSH\_DISABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w26aac11c31c17b7d225c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.