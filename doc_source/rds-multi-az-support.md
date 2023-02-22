# rds\-multi\-az\-support<a name="rds-multi-az-support"></a>

Checks whether high availability is enabled for your RDS DB instances\.

In a Multi\-AZ deployment, Amazon RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone\. For more information, see [High Availability \(Multi\-AZ\)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) in the *Amazon RDS User Guide*\.

**Note**  
This rule does not evaluate Amazon Aurora DB, Amazon DocumentDB, and Amazon Neptune DB instances\.

**Identifier:** RDS\_MULTI\_AZ\_SUPPORT

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d445c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.