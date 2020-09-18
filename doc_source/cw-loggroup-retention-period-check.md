# cw\-loggroup\-retention\-period\-check<a name="cw-loggroup-retention-period-check"></a>

Checks whether Amazon CloudWatch LogGroup retention period is set to specific number of days\. The rule is NON\_COMPLIANT if the retention period is not set or is less than the configured retention period\. 

**Identifier:** CW\_LOGGROUP\_RETENTION\_PERIOD\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions

**Parameters:**

LogGroupNames \(Optional\)Type: CSV  
A comma\-separated list of Log Group names to check the retention period\.

MinRetentionTime \(Optional\)Type: int  
Specify the retention time\. Valid values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653\. The default retention period is 365 days\.

## AWS CloudFormation template<a name="w22aac11c29c17c81c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.