# ec2\-instance\-multiple\-eni\-check<a name="ec2-instance-multiple-eni-check"></a>

Checks if Amazon Elastic Compute Cloud \(Amazon EC2\) uses multiple ENIs \(Elastic Network Interfaces\) or Elastic Fabric Adapters \(EFAs\)\. This rule is NON\_COMPLIANT an Amazon EC2 instance use multiple network interfaces\. 

**Identifier:** EC2\_INSTANCE\_MULTIPLE\_ENI\_CHECK

**Resource Types:** AWS::EC2::Instance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Asia Pacific \(Melbourne\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\) Region

**Parameters:**

NetworkInterfaceIds \(Optional\)Type: CSV  
Comma\-separated list of network instance IDs

## Proactive Evaluation<a name="w2aac12c33c15b9d199c17"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive)\. For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
   "NetworkInterfaces": "[NetworkInterfaceId-1, NetworkInterfaceId-2, NetworkInterfaceId-3, ...]"
} 
...
```

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html)\. 

## AWS CloudFormation template<a name="w2aac12c33c15b9d199c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.