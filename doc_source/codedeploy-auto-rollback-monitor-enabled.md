# codedeploy\-auto\-rollback\-monitor\-enabled<a name="codedeploy-auto-rollback-monitor-enabled"></a>

Checks if the deployment group is configured with automatic deployment rollback and deployment monitoring with alarms attached\. The rule is NON\_COMPLIANT if AutoRollbackConfiguration or AlarmConfiguration has not been configured or is not enabled\. 

**Identifier:** CODEDEPLOY\_AUTO\_ROLLBACK\_MONITOR\_ENABLED

**Resource Types:** AWS::CodeDeploy::DeploymentGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d143c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.