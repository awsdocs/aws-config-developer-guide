# autoscaling\-group\-elb\-healthcheck\-required<a name="autoscaling-group-elb-healthcheck-required"></a>

Checks if your Auto Scaling groups that are associated with a Classic Load Balancer are using Elastic Load Balancing health checks\. The rule is NON\_COMPLIANT if the Auto Scaling groups are not using Elastic Load Balancing health checks\. 

**Identifier:** AUTOSCALING\_GROUP\_ELB\_HEALTHCHECK\_REQUIRED

**Resource Types:** AWS::AutoScaling::AutoScalingGroup

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(UAE\), Asia Pacific \(Melbourne\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c33c15b9c51c17"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.