# elb\-deletion\-protection\-enabled<a name="elb-deletion-protection-enabled"></a>

Checks whether an Elastic Load Balancer has deletion protection enabled\. The rule is NON\_COMPLIANT if deletion\_protection\.enabled is false\. 

**Identifier:** ELB\_DELETION\_PROTECTION\_ENABLED

**Resource Types:** AWS::ElasticLoadBalancingV2::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Hyderabad\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d329c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.