# rds\-cluster\-multi\-az\-enabled<a name="rds-cluster-multi-az-enabled"></a>

Checks if Multi\-AZ replication is enabled on Amazon Aurora and Hermes clusters managed by Amazon Relational Database Service \(Amazon RDS\)\. This rule is NON\_COMPLIANT if an Amazon RDS instance is not configured with Multi\-AZ\. 

**Identifier:** RDS\_CLUSTER\_MULTI\_AZ\_ENABLED

**Resource Types:** AWS::RDS::DBCluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(Bahrain\), China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), South America \(Sao Paulo\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d455c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.