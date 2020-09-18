# cloudwatch\-alarm\-settings\-check<a name="cloudwatch-alarm-settings-check"></a>

Checks whether CloudWatch alarms with the given metric name have the specified settings\.

**Identifier:** CLOUDWATCH\_ALARM\_SETTINGS\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

metricName  
The name for the metric associated with the alarm\.

threshold  
The value against which the specified statistic is compared\.

evaluationPeriod  
The number of periods in which data is compared to the specified threshold\.

period   
The period, in seconds, during which the specified statistic is applied\.  
The default value is 300 seconds\.

comparisonOperator  
The operation for comparing the specified statistic and threshold \(for example, "GreaterThanThreshold"\)\.

statistic  
The statistic for the metric associated with the alarm \(for example, "Average" or "Sum"\)\.

## AWS CloudFormation template<a name="w22aac11c29c17c67c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.