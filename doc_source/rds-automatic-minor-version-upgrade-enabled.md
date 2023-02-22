# rds\-automatic\-minor\-version\-upgrade\-enabled<a name="rds-automatic-minor-version-upgrade-enabled"></a>

Checks if Amazon Relational Database Service \(RDS\) database instances are configured for automatic minor version upgrades\. The rule is NON\_COMPLIANT if the value of 'autoMinorVersionUpgrade' is false\. 

**Identifier:** RDS\_AUTOMATIC\_MINOR\_VERSION\_UPGRADE\_ENABLED

**Resource Types:** AWS::RDS::DBInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d417c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.