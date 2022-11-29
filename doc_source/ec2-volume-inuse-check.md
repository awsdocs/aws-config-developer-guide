# ec2\-volume\-inuse\-check<a name="ec2-volume-inuse-check"></a>

Checks if EBS volumes are attached to EC2 instances\. Optionally checks if EBS volumes are marked for deletion when an instance is terminated\.

**Identifier:** EC2\_VOLUME\_INUSE\_CHECK

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Europe \(Spain\), Europe \(Zurich\) Region

**Parameters:**

deleteOnTermination \(Optional\)Type: boolean  
EBS volumes are marked for deletion when an instance is terminated\. Possible values: True or False \(other input values are marked as non\-compliant\)\.

## AWS CloudFormation template<a name="w2aac12c31c27b9d219c15"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md)\.