# rds\-instance\-iam\-authentication\-enabled<a name="rds-instance-iam-authentication-enabled"></a>

Checks if an Amazon Relational Database Service \(Amazon RDS\) instance has AWS Identity and Access Management \(IAM\) authentication enabled\. This rule is NON\_COMPLIANT if an Amazon RDS instance does not have AWS IAM authentication enabled i\.e `configuration.iAMDatabaseAuthenticationEnabled` is set to false\.

**Identifier:** RDS\_INSTANCE\_IAM\_AUTHENTICATION\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), Asia Pacific \(Hong Kong\), Asia Pacific \(Osaka\), Africa \(Cape Town\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w29aac11c33c17b7d265c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.