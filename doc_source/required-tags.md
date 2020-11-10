# required\-tags<a name="required-tags"></a>

Checks whether your resources have the tags that you specify\. For example, you can check whether your Amazon EC2 instances have the `CostCenter` tag\. Separate multiple values with commas\.

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

**AWS Region:** All supported AWS Regions

**Parameters:**

 tag1Key   
 Key of the required tag\. 

 tag1Value   
 Optional value of the required tag\. Separate multiple values with commas\. 

 tag2Key   
 Key of the required tag\. 

 tag2Value   
 Optional value of the required tag\. Separate multiple values with commas\. 

 tag3Key   
 Key of the required tag\. 

 tag3Value   
 Optional value of the required tag\. Separate multiple values with commas\. 

 tag4Key   
 Key of the required tag\. 

 tag4Value   
 Optional value of the required tag\. Separate multiple values with commas\. 

 tag5Key   
 Key of the required tag\. 

 tag5Value   
 Optional value of the required tag\. Separate multiple values with commas\. 

 tag6Key   
 Key of the required tag\. 

 tag6Value   
 Optional value of the required tag\. Separate multiple values with commas\. 

## AWS CloudFormation template<a name="w24aac11c29c17d269c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.