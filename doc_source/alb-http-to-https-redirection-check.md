# alb\-http\-to\-https\-redirection\-check<a name="alb-http-to-https-redirection-check"></a>

Checks if HTTP to HTTPS redirection is configured on all HTTP listeners of Application Load Balancers\. The rule is NON\_COMPLIANT if one or more HTTP listeners of Application Load Balancer do not have HTTP to HTTPS redirection configured\. The rule is also NON\_COMPLIANT if one of more HTTP listeners have forwarding to an HTTP listener instead of redirection\.

**Identifier:** ALB\_HTTP\_TO\_HTTPS\_REDIRECTION\_CHECK

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Asia Pacific \(Osaka\), Europe \(Milan\), Africa \(Cape Town\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w79aac11c32c17b7c11c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.