# desired\-instance\-tenancy<a name="desired-instance-tenancy"></a>

Checks instances for specified tenancy\. Specify AMI IDs to check instances that are launched from those AMIs or specify host IDs to check whether instances are launched on those Dedicated Hosts\. Separate multiple ID values with commas\.

**Identifier:** DESIRED\_INSTANCE\_TENANCY

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

tenancyType: String  
Desired tenancy of the instances\. Valid values are DEDICATED, HOST and DEFAULT\.

imageId \(Optional\)Type: CSV  
The rule evaluates instances launched only from AMIs with the specified IDs\. Separate multiple AMI IDs with commas\.

hostId \(Optional\)Type: CSV  
The IDs of the EC2 Dedicated Hosts on which the instances are meant to be launched\. Separate multiple Host IDs with commas\.

## AWS CloudFormation template<a name="w2aac12c33c15b9d149c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.