# cloudwatch\-alarm\-action\-check<a name="cloudwatch-alarm-action-check"></a>

Checks whether CloudWatch alarms have at least one alarm action, one INSUFFICIENT\_DATA action, or one OK action enabled\. Optionally, checks whether any of the actions matches one of the specified ARNs\. 

**Identifier:** CLOUDWATCH\_ALARM\_ACTION\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

alarmActionRequiredType: StringDefault: true  
Alarms have at least one action\.

insufficientDataActionRequiredType: StringDefault: true  
Alarms have at least one action when the alarm transitions to the INSUFFICIENT\_DATA state from any other state\.

okActionRequiredType: StringDefault: false  
Alarms have at least one action when the alarm transitions to an OK state from any other state\.

action1 \(Optional\)Type: String  
The action to execute, specified as an ARN\.

action2 \(Optional\)Type: String  
The action to execute, specified as an ARN\.

action3 \(Optional\)Type: String  
The action to execute, specified as an ARN\.

action4 \(Optional\)Type: String  
The action to execute, specified as an ARN\.

action5 \(Optional\)Type: String  
The action to execute, specified as an ARN\.

## AWS CloudFormation template<a name="w29aac11c33c17b7c61c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.