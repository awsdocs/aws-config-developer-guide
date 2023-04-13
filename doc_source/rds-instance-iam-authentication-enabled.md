# rds\-instance\-iam\-authentication\-enabled<a name="rds-instance-iam-authentication-enabled"></a>

Checks if an Amazon Relational Database Service \(Amazon RDS\) instance has AWS Identity and Access Management \(IAM\) authentication enabled\. This rule is NON\_COMPLIANT if an Amazon RDS instance does not have AWS IAM authentication enabled\. 

**Note**  
The DB Engine should be one of 'mysql', 'postgres', 'aurora', 'aurora\-mysql', or 'aurora\-postgresql'\. The DB instance status should be one of 'available', 'backing\-up', 'storage\-optimization', or 'storage\-full'\.

**Identifier:** RDS\_INSTANCE\_IAM\_AUTHENTICATION\_ENABLED

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Africa \(Cape Town\), Asia Pacific \(Hong Kong\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d465c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.