# subnet\-auto\-assign\-public\-ip\-disabled<a name="subnet-auto-assign-public-ip-disabled"></a>

Checks if Amazon Virtual Private Cloud \(Amazon VPC\) subnets are assigned a public IP address\. The rule is COMPLIANT if Amazon VPC does not have subnets that are assigned a public IP address\. The rule is NON\_COMPLIANT if Amazon VPC has subnets that are assigned a public IP address\. 

**Identifier:** SUBNET\_AUTO\_ASSIGN\_PUBLIC\_IP\_DISABLED

**Resource Types:** AWS::EC2::Subnet

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\) Region

**Parameters:**

None  

## Proactive Evaluation<a name="w2aac12c33c15b9d597c17"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive)\. For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
   "MapPublicIpOnLaunch": BOOLEAN
} 
...
```

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html)\. 

## AWS CloudFormation template<a name="w2aac12c33c15b9d597c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.