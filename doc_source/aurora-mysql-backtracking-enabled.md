# aurora\-mysql\-backtracking\-enabled<a name="aurora-mysql-backtracking-enabled"></a>

Checks if an Amazon Aurora MySQL cluster has backtracking enabled\. This rule is NON\_COMPLIANT if the Aurora cluster uses MySQL and it does not have backtracking enabled\. 

**Identifier:** AURORA\_MYSQL\_BACKTRACKING\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific \(Mumbai\), Europe \(Paris\), US East \(Ohio\), Europe \(Ireland\), Europe \(Frankfurt\), US East \(N\. Virginia\), Asia Pacific \(Seoul\), Europe \(London\), Asia Pacific \(Tokyo\), US West \(Oregon\), US West \(N\. California\), Asia Pacific \(Singapore\), Asia Pacific \(Sydney\), Canada \(Central\), China \(Ningxia\) Region

**Parameters:**

BacktrackWindowInHours \(Optional\)Type: double  
Amount of time in hours \(up to 72\) to backtrack your Aurora MySQL cluster\.

## AWS CloudFormation template<a name="w2aac12c31c27b9c33c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.