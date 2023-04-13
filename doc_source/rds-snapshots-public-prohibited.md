# rds\-snapshots\-public\-prohibited<a name="rds-snapshots-public-prohibited"></a>

Checks if Amazon Relational Database Service \(Amazon RDS\) snapshots are public\. The rule is NON\_COMPLIANT if any existing and new Amazon RDS snapshots are public\. 

**Note**  
It can take up to 12 hours for compliance results to be captured\.

**Identifier:** RDS\_SNAPSHOTS\_PUBLIC\_PROHIBITED

**Resource Types:** AWS::RDS::DBSnapshot, AWS::RDS::DBClusterSnapshot

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d479c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.