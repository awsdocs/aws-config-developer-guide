# redshift\-cluster\-maintenancesettings\-check<a name="redshift-cluster-maintenancesettings-check"></a>

Checks whether Amazon Redshift clusters have the specified maintenance settings\. 

**Identifier:** REDSHIFT\_CLUSTER\_MAINTENANCESETTINGS\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(Bahrain\) Region

**Parameters:**

allowVersionUpgradeType: booleanDefault: true  
Allow version upgrade is enabled\.

preferredMaintenanceWindow \(Optional\)Type: String  
Scheduled maintenance window for clusters \(for example, Mon:09:30\-Mon:10:00\)\.

automatedSnapshotRetentionPeriod \(Optional\)Type: intDefault: 1  
Number of days to retain automated snapshots\.

## AWS CloudFormation template<a name="w76aac11c31c17b7d407c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.