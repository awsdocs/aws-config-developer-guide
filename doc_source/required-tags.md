# required\-tags<a name="required-tags"></a>

Checks if your resources have the tags that you specify\. For example, you can check whether your Amazon EC2 instances have the `CostCenter` tag\. Separate multiple values with commas\. You can check up to 6 tags at a time\.

The AWS\-managed AWS Systems Manager automation document `AWS-SetRequiredTags` does not work as a remediation with this rule\. You will need to create your own custom Systems Manager automation documentation for remediation\.

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

**Resource Types:** AWS::ACM::Certificate, AWS::AutoScaling::AutoScalingGroup, AWS::CloudFormation::Stack, AWS::CodeBuild::Project, AWS::DynamoDB::Table, AWS::EC2::CustomerGateway, AWS::EC2::Instance, AWS::EC2::InternetGateway, AWS::EC2::NetworkAcl, AWS::EC2::NetworkInterface, AWS::EC2::RouteTable, AWS::EC2::SecurityGroup, AWS::EC2::Subnet, AWS::EC2::Volume, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::RDS::DBInstance, AWS::RDS::DBSecurityGroup, AWS::RDS::DBSnapshot, AWS::RDS::DBSubnetGroup, AWS::RDS::EventSubscription, AWS::Redshift::Cluster, AWS::Redshift::ClusterParameterGroup, AWS::Redshift::ClusterSecurityGroup, AWS::Redshift::ClusterSnapshot, AWS::Redshift::ClusterSubnetGroup, AWS::S3::Bucket

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

## AWS CloudFormation template<a name="w2aac12c33c15b9d475c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.