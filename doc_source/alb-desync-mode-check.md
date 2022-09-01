# alb\-desync\-mode\-check<a name="alb-desync-mode-check"></a>

Checks if an Application Load Balancer \(ALB\) is configured with a user defined desync mitigation mode\. The rule is NON\_COMPLIANT if ALB desync mitigation mode does not match with the user defined desync mitigation mode\. 

**Identifier:** ALB\_DESYNC\_MODE\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China \(Beijing\), China \(Ningxia\), AWS GovCloud \(US\-East\), AWS GovCloud \(US\-West\), Asia Pacific \(Jakarta\) Region

**Parameters:**

desyncModeType: CSV  
Comma\-separated list, in which customers can choose max 2 values among \- 'defensive', 'strictest', and 'monitor'\.

## AWS CloudFormation template<a name="w85aac12c32c17b9b7c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.