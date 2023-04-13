# elb\-cross\-zone\-load\-balancing\-enabled<a name="elb-cross-zone-load-balancing-enabled"></a>

Checks if cross\-zone load balancing is enabled for the Classic Load Balancers \(CLBs\)\. This rule is NON\_COMPLIANT if cross\-zone load balancing is not enabled for a CLB\. 

**Identifier:** ELB\_CROSS\_ZONE\_LOAD\_BALANCING\_ENABLED

**Resource Types:** AWS::ElasticLoadBalancing::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d325c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.