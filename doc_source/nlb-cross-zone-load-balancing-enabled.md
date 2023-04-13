# nlb\-cross\-zone\-load\-balancing\-enabled<a name="nlb-cross-zone-load-balancing-enabled"></a>

Checks if cross\-zone load balancing is enabled on Network Load Balancers \(NLBs\)\. The rule is NON\_COMPLIANT if cross\-zone load balancing is not enabled for an NLB\. 

**Identifier:** NLB\_CROSS\_ZONE\_LOAD\_BALANCING\_ENABLED

**Resource Types:** AWS::ElasticLoadBalancingV2::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), Asia Pacific \(Jakarta\), Middle East \(UAE\), Asia Pacific \(Hyderabad\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Europe \(Spain\), China \(Ningxia\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9d427c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.