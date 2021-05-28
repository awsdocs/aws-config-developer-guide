# required\-tags<a name="required-tags"></a>

Checks if your resources have the tags that you specify\. For example, you can check whether your Amazon EC2 instances have the `CostCenter` tag\. Separate multiple values with commas\. You can check up to 6 tags at a time\.

**Important**  
The supported resource types for this rule are as follows:  
ACM::Certificate
AutoScaling::AutoScalingGroup
CloudFormation::Stack
CodeBuild::Project
DynamoDB::Table
EC2::CustomerGateway
EC2::Instance
EC2::InternetGateway
EC2::NetworkAcl
EC2::NetworkInterface
EC2::RouteTable
EC2::SecurityGroup
EC2::Subnet
EC2::Volume
EC2::VPC
EC2::VPNConnection
EC2::VPNGateway
ElasticLoadBalancing::LoadBalancer
ElasticLoadBalancingV2::LoadBalancer
RDS::DBInstance
RDS::DBSecurityGroup
RDS::DBSnapshot
RDS::DBSubnetGroup
RDS::EventSubscription
Redshift::Cluster
Redshift::ClusterParameterGroup
Redshift::ClusterSecurityGroup
Redshift::ClusterSnapshot
Redshift::ClusterSubnetGroup
S3::Bucket

**Identifier:** REQUIRED\_TAGS

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

tag1KeyType: StringDefault: CostCenter  
Key of the required tag\.

tag1Value \(Optional\)Type: CSV  
Optional value of the required tag\. Separate multiple values with commas\.

tag2Key \(Optional\)Type: String  
Key of a second required tag\.

tag2Value \(Optional\)Type: CSV  
Optional value of the second required tag\. Separate multiple values with commas\.

tag3Key \(Optional\)Type: String  
Key of a third required tag\.

tag3Value \(Optional\)Type: CSV  
Optional value of the third required tag\. Separate multiple values with commas\.

tag4Key \(Optional\)Type: String  
Key of a fourth required tag\.

tag4Value \(Optional\)Type: CSV  
Optional value of the fourth required tag\. Separate multiple values with commas\.

tag5Key \(Optional\)Type: String  
Key of a fifth required tag\.

tag5Value \(Optional\)Type: CSV  
Optional value of the fifth required tag\. Separate multiple values with commas\.

tag6Key \(Optional\)Type: String  
Key of a sixth required tag\.

tag6Value \(Optional\)Type: CSV  
Optional value of the sixth required tag\. Separate multiple values with commas\.

## AWS CloudFormation template<a name="w29aac11c33c17b7d287c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.