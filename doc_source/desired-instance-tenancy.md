# desired\-instance\-tenancy<a name="desired-instance-tenancy"></a>

Checks instances for specified tenancy\. Specify AMI IDs to check instances that are launched from those AMIs or specify host IDs to check whether instances are launched on those Dedicated Hosts\. Separate multiple ID values with commas\.

**Identifier:** DESIRED\_INSTANCE\_TENANCY

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS Regions

**Parameters:**

 tenancy   
 The desired tenancy of the instances\. Valid values are `DEDICATED`, `HOST`, and `DEFAULT`\. 

 imageId   
 The rule evaluates instances launched only from the AMI with the specified ID\. Separate multiple AMI IDs with commas\. 

 hostId   
 The ID of the Amazon EC2 Dedicated Host on which the instances are meant to be launched\. Separate multiple host IDs with commas\. 

## AWS CloudFormation template<a name="w22aac11c29c17c87c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.