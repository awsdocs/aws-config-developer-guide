# required\-tags<a name="required-tags"></a>

Checks whether your resources have the tags that you specify\. For example, you can check whether your EC2 instances have the 'CostCenter' tag\. Separate multiple values with commas\.

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

**Parameters:**

 tag1Key   
 Key of the required tag\. 

 tag1Value   
 Optional value of the required tag\. Separate multiple values with commas\. 

## AWS CloudFormation template<a name="w4aac13c29c17d227c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.