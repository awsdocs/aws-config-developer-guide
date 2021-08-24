# aurora\-resources\-protected\-by\-backup\-plan<a name="aurora-resources-protected-by-backup-plan"></a>

Checks if Amazon Aurora DB clusters are protected by a backup plan\. The rule is NON\_COMPLIANT if the Amazon Relational Database Service \(Amazon RDS\) Database Cluster is not protected by a backup plan\. 

**Identifier:** AURORA\_RESOURCES\_PROTECTED\_BY\_BACKUP\_PLAN

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except China \(Beijing\), Africa \(Cape Town\), Asia Pacific \(Osaka\), Europe \(Milan\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), US West \(Oregon\), and China \(Ningxia\) Region

**Parameters:**

resourceTags \(Optional\)Type: String  
Tags of Aurora DB clusters for the rule to check, in JSON format\.

resourceId \(Optional\)Type: String  
ID of Aurora DB cluster for the rule to check\.

## AWS CloudFormation template<a name="w29aac11c33c17b7c31c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.