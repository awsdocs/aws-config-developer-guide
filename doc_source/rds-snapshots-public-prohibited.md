# rds\-snapshots\-public\-prohibited<a name="rds-snapshots-public-prohibited"></a>

Checks if Amazon Relational Database Service \(Amazon RDS\) snapshots are public\. The rule is NON\_COMPLIANT if any existing and new Amazon RDS snapshots are public\. 

**Note**  
It can take up to 12 hours for compliance results to be captured\.

**Identifier:** RDS\_SNAPSHOTS\_PUBLIC\_PROHIBITED

**Trigger type:** Configuration changes

**Evaluated resource types:** AWS::RDS::DBSnapshot and AWS::RDS::DBClusterSnapshot

**AWS Region:** All supported AWS Regions except Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

None  

## AWS CloudFormation template<a name="w22aac11c29c17d259c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.