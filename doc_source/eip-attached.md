# eip\-attached<a name="eip-attached"></a>

Checks if all Elastic IP addresses that are allocated to an AWS account are attached to EC2 instances or in\-use elastic network interfaces \(ENIs\)\.

**Note**  
Results might take up to 6 hours to become available after an evaluation occurs\.

**Identifier:** EIP\_ATTACHED

**Resource Types:** AWS::EC2::EIP

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East \(UAE\) Region

**Parameters:**

None  

## Proactive Evaluation<a name="w2aac12c33c15b9d279c19"></a>

 For steps on how to run this rule in proactive mode, see [Evaluating Your Resources with AWS Config Rules](./evaluating-your-resources.html#evaluating-your-resources-proactive)\. For this rule to return COMPLIANT in proactive mode, the resource configuration schema for the [StartResourceEvaluation](https://docs.aws.amazon.com/config/latest/APIReference/API_StartResourceEvaluation.html) API needs to include the following inputs, encoded as a string: 

```
"ResourceConfiguration":
...
{
   "InstanceId": "my-instance-Id"
} 
...
```

 For more information on proactive evaluation, see [Evaluation Mode](./evaluate-config-rules.html)\. 

## AWS CloudFormation template<a name="w2aac12c33c15b9d279c21"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.