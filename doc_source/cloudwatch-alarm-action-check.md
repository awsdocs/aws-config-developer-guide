# cloudwatch\-alarm\-action\-check<a name="cloudwatch-alarm-action-check"></a>

Checks if Amazon CloudWatch alarms have at least one alarm action, one INSUFFICIENT\_DATA action, or one OK action configured\. Optionally, checks if any of the actions matches one of the specified Amazon Resource Names \(ARNs\)\. This rule is NON\_COMPLIANT if no action exists for the alarm or if there is no matching action for the optional parameter provided\.

**Identifier:** CLOUDWATCH\_ALARM\_ACTION\_CHECK

**Resource Types:** AWS::CloudWatch::Alarm

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

## AWS CloudFormation template<a name="w2aac12c33c15b9d101c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.