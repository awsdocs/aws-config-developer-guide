# alb\-http\-drop\-invalid\-header\-enabled<a name="alb-http-drop-invalid-header-enabled"></a>

Checks if rule evaluates AWS Application Load Balancers \(ALB\) to ensure they are configured to drop http headers\. The rule is NON\_COMPLIANT if the value of routing\.http\.drop\_invalid\_header\_fields\.enabled is set to false\. 

**Identifier:** ALB\_HTTP\_DROP\_INVALID\_HEADER\_ENABLED

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific \(Jakarta\), Africa \(Cape Town\), Asia Pacific \(Osaka\), Europe \(Milan\), Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

None  

## AWS CloudFormation template<a name="w2aac12c31c27b9b9c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.