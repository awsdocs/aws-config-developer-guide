# codedeploy\-ec2\-minimum\-healthy\-hosts\-configured<a name="codedeploy-ec2-minimum-healthy-hosts-configured"></a>

Checks if the deployment group for EC2/On\-Premises Compute Platform is configured with a minimum healthy hosts fleet percentage or host count greater than or equal to the input threshold\. The rule is NON\_COMPLIANT if either is below the threshold\. 

**Identifier:** CODEDEPLOY\_EC2\_MINIMUM\_HEALTHY\_HOSTS\_CONFIGURED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

minimumHealthyHostsFleetPercent \(Optional\)Type: intDefault: 66  
Minimum percentage of healthy hosts fleet during deployment\. Default value is set to 66 percent\.

minimumHealthyHostsHostCount \(Optional\)Type: intDefault: 1  
Minimum number of healthy hosts in fleet during deployment\. Default value is set to 1\.

## AWS CloudFormation template<a name="w76aac11c31c17b7d113c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.