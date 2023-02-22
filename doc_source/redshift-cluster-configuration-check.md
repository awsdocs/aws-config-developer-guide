# redshift\-cluster\-configuration\-check<a name="redshift-cluster-configuration-check"></a>

Checks whether Amazon Redshift clusters have the specified settings\. 

**Identifier:** REDSHIFT\_CLUSTER\_CONFIGURATION\_CHECK

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(Bahrain\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

clusterDbEncryptedType: booleanDefault: true  
Database encryption is enabled\.

loggingEnabledType: booleanDefault: true  
Audit logging is enabled\.

nodeTypes \(Optional\)Type: CSVDefault: dc1\.large  
Specify node type\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d459c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.