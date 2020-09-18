# redshift\-cluster\-maintenancesettings\-check<a name="redshift-cluster-maintenancesettings-check"></a>

Checks whether Amazon Redshift clusters have the specified maintenance settings\.

**Identifier:** REDSHIFT\_CLUSTER\_MAINTENANCESETTINGS\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions except Middle East \(Bahrain\)

**Parameters:**

 allowVersionUpgrade   
 Allow version upgrade is enabled\. 

 preferredMaintenanceWindow   
 Scheduled maintenance window for clusters \(for example, Mon:09:30\-Mon:10:00\)\. 

 automatedSnapshotRetentionPeriod   
 Number of days to retain automated snapshots\. 

## AWS CloudFormation template<a name="w22aac11c29c17d265c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.