# rds\-db\-security\-group\-not\-allowed<a name="rds-db-security-group-not-allowed"></a>

Checks if there are any Amazon Relational Database Service \(RDS\) DB security groups that are not the default DB security group\. The rule is NON\_COMPLIANT is there are any DB security groups that are not the default DB security group\. 

**Identifier:** RDS\_DB\_SECURITY\_GROUP\_NOT\_ALLOWED

**Resource Types:** AWS::RDS::DBSecurityGroup

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe \(Ireland\), South America \(Sao Paulo\), US East \(N\. Virginia\), Asia Pacific \(Tokyo\), US West \(Oregon\), US West \(N\. California\), Asia Pacific \(Singapore\), Asia Pacific \(Sydney\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d457c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.