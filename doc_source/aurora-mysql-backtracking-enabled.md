# aurora\-mysql\-backtracking\-enabled<a name="aurora-mysql-backtracking-enabled"></a>

Checks if an Amazon Aurora MySQL cluster has backtracking enabled\. This rule is NON\_COMPLIANT if the Aurora cluster uses MySQL and it does not have backtracking enabled\. 

**Identifier:** AURORA\_MYSQL\_BACKTRACKING\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Hong Kong\), Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Europe \(Milan\), Europe \(Stockholm\), Middle East \(Bahrain\), Africa \(Cape Town\), South America \(Sao Paulo\) Region

**Parameters:**

BacktrackWindowInHours \(Optional\)Type: double  
Amount of time in hours \(up to 72\) to backtrack your Aurora MySQL cluster\.

## AWS CloudFormation template<a name="w76aac11c31c17b7c29c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.