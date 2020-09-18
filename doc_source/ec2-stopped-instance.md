# ec2\-stopped\-instance<a name="ec2-stopped-instance"></a>

Checks whether there are instances stopped for more than the allowed number of days\. The instance is NON\_COMPLIANT if the state of the ec2 instance has been stopped for longer than the allowed number of days\.

**Identifier:** EC2\_STOPPED\_INSTANCE

**Trigger type:** Periodic

**AWS Region:** All supported AWS Regions except Africa \(Cape Town\) and Europe \(Milan\)

**Parameters:**

AllowedDays  
\(Optional\) The number of days an ec2 instance can be stopped before it is NON\_COMPLIANT\. The default number of days is 30\.

## AWS CloudFormation template<a name="w22aac11c29c17d137c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.