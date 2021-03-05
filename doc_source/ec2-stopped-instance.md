# ec2\-stopped\-instance<a name="ec2-stopped-instance"></a>

Checks whether there are instances stopped for more than the allowed number of days\. 

**Identifier:** EC2\_STOPPED\_INSTANCE

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

AllowedDays \(Optional\)Type: intDefault: 30  
Number of days the instance can be stopped for before it becomes non\-compliant\. The default number of days is 30\.

## AWS CloudFormation template<a name="w24aac11c29c17b7d135c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.