# rds\-resources\-protected\-by\-backup\-plan<a name="rds-resources-protected-by-backup-plan"></a>

Checks if Amazon Relational Database Service \(Amazon RDS\) instances are protected by a backup plan\. The rule is NON\_COMPLIANT if the Amazon RDS Database instance is not covered by a backup plan\. 

**Identifier:** RDS\_RESOURCES\_PROTECTED\_BY\_BACKUP\_PLAN

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Africa \(Cape Town\), Asia Pacific \(Osaka\), Europe \(Milan\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), US West \(Oregon\), and China \(Ningxia\) Region

**Parameters:**

resourceTags \(Optional\)Type: String  
Tags for Amazon RDS instances for the rule to check, in JSON format\.

resourceId \(Optional\)Type: String  
ID of Amazon RDS instance for the rule to check\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d301c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.