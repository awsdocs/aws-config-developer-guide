# cloudwatch\-alarm\-action\-check<a name="cloudwatch-alarm-action-check"></a>

Checks whether CloudWatch alarms have at least one alarm action, one `INSUFFICIENT_DATA` action, or one `OK` action enabled\. Optionally, checks whether any of the actions matches one of the specified ARNs\.

**Identifier:** CLOUDWATCH\_ALARM\_ACTION\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

alarmActionRequired  
 Alarms have at least one action\.   
The default value is `true`\.

insufficientDataActionRequired  
Alarms have at least one action when the alarm transitions to the `INSUFFICIENT_DATA` state from any other state\.  
The default value is `true`\.

okActionRequired  
Alarms have at least one action when the alarm transitions to an `OK` state from any other state\.  
The default value is `false`\.

 action1   
The action to execute, specified as an ARN\.

 action2   
The action to execute, specified as an ARN\.

action3   
 The action to execute, specified as an ARN\.

action4   
The action to execute, specified as an ARN\.

action5   
The action to execute, specified as an ARN\.

## AWS CloudFormation template<a name="w22aac11c29c17c63c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.