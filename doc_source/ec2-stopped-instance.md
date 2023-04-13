# ec2\-stopped\-instance<a name="ec2-stopped-instance"></a>

Checks if there are Amazon Elastic Compute Cloud \(Amazon EC2\) instances stopped for more than the allowed number of days\. The rule is NON\_COMPLIANT if the state of an Amazon EC2 instance has been stopped for longer than the allowed number of days, or if the amount of time cannot be determined\.

**Identifier:** EC2\_STOPPED\_INSTANCE

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Middle East \(UAE\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Milan\) Region

**Parameters:**

AllowedDays \(Optional\)Type: intDefault: 30  
The number of days an Amazon EC2 instance can be stopped before the rule is NON\_COMPLIANT\. The default number of days is 30\.  
The number of days selected needs to be less than the configured retention period since this rule relies on the historical data collected\. For more information about historical data retention, see [Deleting AWS Config Data](https://docs.aws.amazon.com/config/latest/developerguide/delete-config-data-with-retention-period.html)\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d231c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.