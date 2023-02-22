# rds\-instance\-public\-access\-check<a name="rds-instance-public-access-check"></a>

Checks whether the Amazon Relational Database Service \(RDS\) instances are not publicly accessible\. The rule is non\-compliant if the publiclyAccessible field is true in the instance configuration item\. 

**Identifier:** RDS\_INSTANCE\_PUBLIC\_ACCESS\_CHECK

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d437c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.