# codedeploy\-auto\-rollback\-monitor\-enabled<a name="codedeploy-auto-rollback-monitor-enabled"></a>

Checks if the deployment group is configured with automatic deployment rollback and deployment monitoring with alarms attached\. The rule is NON\_COMPLIANT if AutoRollbackConfiguration or AlarmConfiguration has not been configured or is not enabled\. 

**Identifier:** CODEDEPLOY\_AUTO\_ROLLBACK\_MONITOR\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w79aac11c32c17b9d127c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.